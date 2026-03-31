"""
THEMIS Full-Archive Cache Builder v2 — 32-thread, 96GB RAM optimized

STATE already downloaded (1135 files). This script:
  Phase 1: SKIP (STATE already cached)
  Phase 2: Parallel geometry screening (32 threads, load all STATE into RAM)
  Phase 3: Parallel encounter processing (32 threads)
  Phase 4: Build indexes

Geometry: X_GSM > 5 Re, SZA < 30°, 8 < r < 25 Re
"""
import json, os, sys, csv, time, calendar, traceback
import datetime as dt_module
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from cdasws import CdasWs
from pdl_pilot.mapping.s_mapper import compute_s_with_uncertainty, compute_bin_occupancy
from pdl_pilot.config.schema import BinConfig, UncertaintyConfig

BINS = BinConfig()
UNC = UncertaintyConfig()
RE_KM = 6371.2
WORKERS = 32

X_MIN = 5.0; SZA_MAX = 30.0; R_MIN = 8.0; R_MAX = 25.0
ENC_HOURS = 6
MAX_RETRIES = 4

BASE = "data_cache/themis_archive"
STATE_DIR = os.path.join(BASE, "raw_state")
ENC_DIR = os.path.join(BASE, "encounters")
os.makedirs(ENC_DIR, exist_ok=True)

_tls = threading.local()
def get_cdas():
    if not hasattr(_tls, 'cdas'):
        _tls.cdas = CdasWs()
    return _tls.cdas

_lock = threading.Lock()
def tprint(msg):
    with _lock:
        print(msg, flush=True)

def _e2u(a):
    if hasattr(a,'dtype') and np.issubdtype(a.dtype, np.datetime64):
        return (a.astype('datetime64[ns]') - np.datetime64('1970-01-01T00:00:00','ns')).astype(np.float64)/1e9
    return np.asarray(a, dtype=np.float64)

def _interp(st, sd, tt, mg=60.0):
    if len(st)==0 or len(sd)==0: return np.full_like(tt, np.nan)
    r = np.interp(tt, st, sd.astype(np.float64))
    if mg>0 and len(st)>1:
        i=np.clip(np.searchsorted(st,tt),0,len(st)-1)
        ip=np.clip(i-1,0,len(st)-1)
        d=np.minimum(np.abs(tt-st[i]),np.abs(tt-st[ip]))
        r[d>mg]=np.nan
    return r

def _fetch(ds, vs, t0, t1):
    for a in range(MAX_RETRIES+1):
        try:
            _,d = get_cdas().get_data(ds, vs, t0, t1)
            return d
        except:
            if a < MAX_RETRIES: time.sleep(1+a*2)
    return None

# =====================================================================
# PHASE 2: Parallel geometry screening
# =====================================================================
print("="*70)
print("PHASE 2: GEOMETRY SCREENING (32 threads)")
print(f"  X>{X_MIN} SZA<{SZA_MAX} {R_MIN}<r<{R_MAX}")
print("="*70)

state_files = sorted([f for f in os.listdir(STATE_DIR) if f.endswith('.npz')])
print(f"STATE files: {len(state_files)}")

def screen_one_state(fname):
    """Screen one STATE file. Returns list of qualifying (date, probe, center_t, sza)."""
    parts = fname.replace('.npz','').split('_')
    if len(parts)!=3: return []
    probe, ys, ms = parts
    year, month = int(ys), int(ms)
    try:
        d = np.load(os.path.join(STATE_DIR, fname), allow_pickle=True)
        t=d["times"]; x=d["x_re"]; y=d["y_re"]; z=d["z_re"]
    except:
        return []
    if len(t)==0: return []
    r = np.sqrt(x**2+y**2+z**2)
    sza = np.degrees(np.arctan2(np.sqrt(y**2+z**2), x))
    good = (x>X_MIN)&(sza<SZA_MAX)&(r>R_MIN)&(r<R_MAX)&np.isfinite(x)
    if not np.any(good): return []
    # Group by day
    wins = {}
    for i in range(len(t)):
        if not good[i]: continue
        dt = dt_module.datetime.fromtimestamp(t[i], tz=dt_module.timezone.utc)
        dk = dt.date()
        if dk not in wins or sza[i] < wins[dk][1]:
            wins[dk] = (float(t[i]), float(sza[i]))
    return [(str(dk), probe, ct, sz, year, month) for dk,(ct,sz) in wins.items()]

results = []
with ThreadPoolExecutor(max_workers=WORKERS) as ex:
    futs = {ex.submit(screen_one_state, f): f for f in state_files}
    done = 0
    for fut in as_completed(futs):
        done += 1
        try:
            results.extend(fut.result())
        except: pass
        if done % 200 == 0:
            tprint(f"  Screened {done}/{len(state_files)} files, {len(results)} qualifying so far")

# Dedup by (date, probe)
seen = {}
for date_s, probe, ct, sz, y, m in results:
    k = (date_s, probe)
    if k not in seen or sz < seen[k][2]:
        seen[k] = (date_s, probe, sz, ct, y, m)

qualifying = [{"date":v[0],"probe":v[1],"sza_deg":round(v[2],1),"center_unix":v[3],"year":v[4],"month":v[5]}
              for v in sorted(seen.values())]

print(f"\nGeometry screening complete: {len(qualifying)} qualifying days")
by_y = Counter(q["year"] for q in qualifying)
by_p = Counter(q["probe"] for q in qualifying)
print(f"  By year: {dict(sorted(by_y.items()))}")
print(f"  By probe: {dict(sorted(by_p.items()))}")

# Save screened index
with open(os.path.join(BASE, "screened_index.json"), 'w') as f:
    json.dump({"generated": dt_module.datetime.now().isoformat(),
               "criteria": {"x_min":X_MIN,"sza_max":SZA_MAX,"r_min":R_MIN,"r_max":R_MAX},
               "total": len(qualifying),
               "by_year": dict(sorted(by_y.items())),
               "by_probe": dict(sorted(by_p.items())),
               "qualifying_days": qualifying}, f, indent=2)

# =====================================================================
# PHASE 3: Parallel encounter processing (32 threads)
# =====================================================================
print(f"\n{'='*70}")
print(f"PHASE 3: ENCOUNTER PROCESSING ({WORKERS} workers, {len(qualifying)} encounters)")
print("="*70)

def process_enc(q):
    ds = q["date"]; probe = q["probe"]; ct = q["center_unix"]
    year = q["year"]; month = q["month"]; pl = probe[-1]
    eid = f"{ds}_{probe}"
    ep = os.path.join(ENC_DIR, f"{eid}.json")
    if os.path.exists(ep):
        try:
            with open(ep) as f: return json.load(f)
        except: os.remove(ep)

    half = ENC_HOURS*3600/2
    ts = dt_module.datetime.fromtimestamp(ct-half, tz=dt_module.timezone.utc)
    te = dt_module.datetime.fromtimestamp(ct+half, tz=dt_module.timezone.utc)
    t0s = ts.strftime("%Y-%m-%dT%H:%M:%SZ"); t1s = te.strftime("%Y-%m-%dT%H:%M:%SZ")
    base = {"encounter_id":eid,"spacecraft":"themis","probe":probe,
            "date":ds,"year":year,"month":month,"sza_deg":q["sza_deg"],
            "evaluable":False,"retained":False,"cone_bin":"unknown"}
    try:
        # STATE
        sp = os.path.join(STATE_DIR, f"{probe}_{year}_{month:02d}.npz")
        if not os.path.exists(sp): base["exclude_reason"]="no STATE"; return base
        sd = np.load(sp, allow_pickle=True)
        st=sd["times"]; t0=ct-half-600; t1=ct+half+600
        m=(st>=t0)&(st<=t1)
        stt=st[m]; stx=sd["x_re"][m]; sty=sd["y_re"][m]; stz=sd["z_re"][m]

        # MOM
        mom = _fetch(f"TH{pl.upper()}_L2_MOM",[f"th{pl}_peim_density"],t0s,t1s)
        if mom is None or f"th{pl}_peim_density" not in mom.data_vars:
            base["exclude_reason"]="no MOM"; return base
        mc=[c for c in mom.coords if "epoch" in c.lower() or "time" in c.lower()]
        if not mc: base["exclude_reason"]="no MOM time"; return base
        mt=_e2u(mom.coords[mc[0]].values)
        den=mom[f"th{pl}_peim_density"].values.astype(np.float64)
        if len(mt)<10: base["exclude_reason"]="insufficient MOM"; return base
        tt=mt

        # FGM
        fgm=_fetch(f"TH{pl.upper()}_L2_FGM",[f"th{pl}_fgs_gsm"],t0s,t1s)
        if fgm is None or f"th{pl}_fgs_gsm" not in fgm.data_vars:
            base["exclude_reason"]="no FGM"; return base
        bv=fgm[f"th{pl}_fgs_gsm"].values.astype(np.float64)
        if bv.ndim<2: base["exclude_reason"]="FGM not 3c"; return base
        bmr=np.sqrt(np.sum(bv**2,axis=-1))
        fc=[c for c in fgm.coords if "epoch" in c.lower() or "time" in c.lower()]
        ft=None
        if fc: ft=_e2u(fgm.coords[fc[0]].values)
        if ft is None or len(ft)!=len(bmr):
            for d in fgm[f"th{pl}_fgs_gsm"].dims:
                if d in fgm.coords and len(fgm.coords[d].values)==len(bmr):
                    ft=_e2u(fgm.coords[d].values); break
        if ft is None or len(ft)!=len(bmr):
            if len(bmr)>0: ft=np.linspace(tt[0],tt[-1],len(bmr))
            else: base["exclude_reason"]="FGM time fail"; return base
        bm=_interp(ft,bmr,tt,30.0)

        xr=_interp(stt,stx,tt,600.0); yr=_interp(stt,sty,tt,600.0); zr=_interp(stt,stz,tt,600.0)
        xm=float(np.nanmean(xr)); ym=float(np.nanmean(yr)); zm=float(np.nanmean(zr))
        sza=float(np.degrees(np.arctan2(np.sqrt(ym**2+zm**2),xm))) if np.isfinite(xm) else 999.
        if sza>SZA_MAX: base["sza_deg"]=round(sza,1); base["exclude_reason"]=f"SZA={sza:.0f}"; return base

        # OMNI
        os0=(ts-dt_module.timedelta(minutes=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
        oe0=(te+dt_module.timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%SZ")
        om=_fetch("OMNI_HRO_1MIN",["BX_GSE","BY_GSM","BZ_GSM","F","Pressure","Mach_num"],os0,oe0)
        dp=bz=bt=bx=by=ma=None
        if om is not None:
            def _o(k):
                if k not in om.data_vars: return None
                a=om[k].values.astype(np.float64); v=a[np.isfinite(a)]
                v=v[(v>-1e30)&(v<1e30)&(np.abs(v)<9990)]
                return float(np.nanmedian(v)) if len(v)>0 else None
            dp=_o("Pressure"); bz=_o("BZ_GSM"); bt=_o("F")
            ma=_o("Mach_num"); bx=_o("BX_GSE"); by=_o("BY_GSM")
        if dp is None or dp<=0: base["sza_deg"]=round(sza,1); base["exclude_reason"]="no OMNI Dp"; return base

        cd=float(np.degrees(np.arccos(min(abs(bx)/bt,1.0)))) if bx is not None and bt and bt>0 else None
        ck=(float(np.degrees(np.arctan2(by,bz)))%360.0) if by is not None and bz is not None else None

        den[den<=0]=np.nan; den[den>1000]=np.nan; bm[bm<=0]=np.nan; bm[bm>500]=np.nan
        s,_,_,mp,bs=compute_s_with_uncertainty(xr,dp_nPa=dp,bz_nT=bz or 0.,mach_alfven=ma or 8.,unc=UNC)
        occ=compute_bin_occupancy(s,BINS); no=occ["near"]; bo=occ["background"]
        nm=(s>=.2)&(s<.4); bgm=(s>=.6)&(s<=1.)
        def _sm(a,m):
            v=a[m]; v=v[np.isfinite(v)]
            return float(np.nanmedian(v)) if len(v)>0 else None
        nn=_sm(den,nm); nb=_sm(den,bgm); bn=_sm(bm,nm); bb=_sm(bm,bgm)
        Dn=(nn/nb) if (nn and nb and nb>0) else None
        EB=(bn/bb) if (bn and bb and bb>0) else None
        ev=no>=.05 and bo>=.01 and Dn is not None and EB is not None
        ml=float((12.+np.degrees(np.arctan2(ym,xm))/15.)%24.) if np.isfinite(xm) and np.isfinite(ym) else None
        rm=float(np.sqrt(xm**2+ym**2+zm**2))

        cb="unknown"
        if cd is not None:
            if cd<30: cb="quasi-radial"
            elif cd<=45: cb="low-cone"
            elif cd<=60: cb="intermediate"
            else: cb="perpendicular"

        e={"encounter_id":eid,"spacecraft":"themis","probe":probe,"date":ds,"year":year,"month":month,
           "sza_deg":round(sza,1),"mlt":round(ml,1) if ml else None,"x_gsm_re":round(xm,2),"r_re":round(rm,2),
           "dp_nPa":round(dp,2),"bz_nT":round(bz,2) if bz else None,"ma":round(ma,1) if ma else None,
           "cone_deg":round(cd,1) if cd is not None else None,"clock_deg":round(ck,1) if ck is not None else None,
           "mp_standoff_re":round(mp,2),"bs_standoff_re":round(bs,2),
           "near_occ":round(no,4),"bg_occ":round(bo,4),
           "Dn":round(Dn,4) if Dn else None,"EB":round(EB,4) if EB else None,
           "evaluable":ev,"retained":ev,"cone_bin":cb,"n_points":len(tt),
           "exclude_reason":None if ev else (f"bg<1%({bo:.3f})" if bo<.01 else f"near<5%({no:.3f})" if no<.05 else "Dn/EB null")}
        if ev and Dn and EB:
            if Dn<1 and EB>1: e["qc_transition_cleanliness"]="clean"
            elif Dn<1 or EB>1: e["qc_transition_cleanliness"]="mixed"
            else: e["qc_transition_cleanliness"]="unclear"
        else: e["qc_transition_cleanliness"]="not_assessed"
        e["qc_disturbance"]="undisturbed" if no>.1 and bo>.05 else "uncertain"
        e["qc_boundary_motion"]="stable" if 2<=dp<=6 else "uncertain"
        e["omni_context_quality_note"]="good" if bz is not None and cd is not None else "partial"
        e["boundary_uncertainty_note"]="plausible" if 2<=dp<=6 else "uncertain"
        with open(ep,'w') as f: json.dump(e,f,indent=2,default=str)
        return e
    except Exception as ex:
        base["exclude_reason"]=f"err:{ex}"; return base

cat = []
done = [0]; ret = [0]; total = len(qualifying)
tprint(f"Processing {total} encounters with {WORKERS} threads...")

with ThreadPoolExecutor(max_workers=WORKERS) as ex:
    futs = {ex.submit(process_enc, q): q for q in qualifying}
    for fut in as_completed(futs):
        done[0] += 1
        try:
            e = fut.result(); cat.append(e)
            if e.get("retained"):
                ret[0] += 1
                tprint(f"  [{done[0]}/{total}] RETAINED {e['date']} {e['probe']} "
                       f"cone={e.get('cone_deg')} Dp={e.get('dp_nPa')} Dn={e.get('Dn')} EB={e.get('EB')} [{e['cone_bin']}]")
            elif done[0] % 500 == 0:
                tprint(f"  [{done[0]}/{total}] progress... ({ret[0]} retained)")
        except Exception as ex2:
            q = futs[fut]
            cat.append({"encounter_id":f"{q['date']}_{q['probe']}","date":q["date"],"probe":q["probe"],
                "year":q["year"],"month":q["month"],"evaluable":False,"retained":False,
                "exclude_reason":str(ex2),"cone_bin":"unknown"})

tprint(f"\nAll {total} processed. {ret[0]} retained.")

# =====================================================================
# PHASE 4: Build indexes
# =====================================================================
print(f"\n{'='*70}")
print("PHASE 4: BUILD INDEXES")
print("="*70)

# Dedup retained
seen={}
for e in cat:
    if e.get("retained"):
        k=(e["date"],e["probe"])
        if k not in seen: seen[k]=e
ur=sorted(seen.values(), key=lambda x:(x.get("cone_deg") or 999))

cg={}
for e in ur: cg.setdefault(e.get("cone_bin","unknown"),[]).append(e)
cc={k:len(v) for k,v in cg.items()}
by_y=Counter(e.get("year") for e in ur)
by_p=Counter(e.get("probe") for e in ur)

# encounter_index.json
with open(os.path.join(BASE,"encounter_index.json"),'w') as f:
    json.dump({"generated":dt_module.datetime.now().isoformat(),"total":len(cat),
               "retained":len(ur),"encounters":cat},f,indent=2,default=str)

# retained_index.json
with open(os.path.join(BASE,"retained_index.json"),'w') as f:
    json.dump({"generated":dt_module.datetime.now().isoformat(),"unique_retained":len(ur),
               "cone_counts":cc,"by_year":dict(sorted(by_y.items())),"by_probe":dict(sorted(by_p.items())),
               "by_cone_bin":cg},f,indent=2,default=str)

# summary.json
sf=len([f for f in os.listdir(STATE_DIR) if f.endswith('.npz')])
summary={"generated":dt_module.datetime.now().isoformat(),
    "archive_scope":"THEMIS 2007-2025, all 5 probes, all months",
    "geometry":{"x_min":X_MIN,"sza_max":SZA_MAX,"r_min":R_MIN,"r_max":R_MAX},
    "state_files":sf,"qualifying_days":len(qualifying),"processed":len(cat),
    "unique_retained":len(ur),"cone_counts":cc,
    "by_year":dict(sorted(by_y.items())),"by_probe":dict(sorted(by_p.items()))}
with open(os.path.join(BASE,"summary.json"),'w') as f:
    json.dump(summary,f,indent=2)

# CSV
cf=['encounter_id','date','year','month','probe','sza_deg','mlt','cone_deg','clock_deg',
    'dp_nPa','bz_nT','near_occ','bg_occ','Dn','EB','cone_bin','retained','exclude_reason',
    'qc_transition_cleanliness','qc_disturbance','qc_boundary_motion',
    'omni_context_quality_note','boundary_uncertainty_note','r_re','x_gsm_re']
with open(os.path.join(BASE,"encounter_catalogue.csv"),'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cf,extrasaction='ignore'); w.writeheader()
    for e in cat: w.writerow(e)

print(f"STATE files: {sf}")
print(f"Qualifying days: {len(qualifying)}")
print(f"Processed: {len(cat)}")
print(f"Unique retained: {len(ur)}")
print(f"Cone counts: {cc}")
print(f"By year: {dict(sorted(by_y.items()))}")
print(f"By probe: {dict(sorted(by_p.items()))}")
print(f"\nDONE. Time: {(time.time()-__import__('time').time())/60:.1f}min" if False else "")
print("DONE.")
