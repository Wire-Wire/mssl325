## RESEARCH ARTICLE

10.1029/2019JA026507

## Key Points:

- Solar wind plasma may be processed between L1 and the magnetopause
- Statistical uncertainties are identified in connections between L1 and the magnetopause
- The foreshock is a primary source of variability in propagating data from L1 to the magnetopause

## Correspondence to:

B. Walsh bwalsh@bu.edu

## Citation:

Walsh, B. M., Bhakyapaibul, T., &amp; Zou, Y. (2019). Quantifying the uncertainty of using solar wind measurements for geospace inputs. Journal of Geophysical Research: Space Physics , 124 , 3291-3302. https://doi. org/10.1029/2019JA026507

Received 15 JAN 2019 Accepted 17 APR 2019 Accepted article online 1 MAY 2019 Published online 21 MAY 2019

©2019. The Authors This is an open access article under the terms of the Creative Commons Attribution-NonCommercial-NoDerivs License, which permits use and distribution in any medium, provided the original work is properly cited, the use is non-commercial and no modifications or adaptations are made.

## Quantifying the Uncertainty of Using Solar Wind Measurements for Geospace Inputs

B. M. Walsh 1,2 , T. Bhakyapaibul 1,2 , and Y. Zou 2

1 Department of Mechanical Engineering, Boston University, Boston, MA, USA, 2 Center for Space Physics, Boston University, Boston, MA, USA

Abstract Predictive models for the Earth's space environment routinely use parameters from the solar wind as inputs. Measurements from spacecraft orbiting the first Lagrange point serve as convenient values for these inputs. The mass, momentum, and energy input into the Earth's space environment, however, are a function of the shocked and processed plasma within the magnetosheath, which can vary significantly from the pristine solar wind at the first Lagrange point. Here statistical measurements from the OMNI data set are combined with measurements by the THEMIS mission within the magnetosheath to generate uncertainty values for pressure and magnetic clock angle. These uncertainties are generated to account for known physical processes in the foreshock and magnetosheath as well as the position of the spacecraft being used to generate the OMNI data set.

## 1. Introduction

For decades the space community has recognized that the majority of the energy that drives disturbances in the Earth's space environment is extracted from the flowing solar wind. This is visible in models designed to predict the conditions in different regions of space such as solar wind magnetosphere coupling (Borovsky, 2008; Newell et al., 2007), radiation belt dynamics (Barker et al., 2005; Li, 2004), and global magnetohydrodynamic (MHD) models (Janhunen et al., 2012; Lyon et al., 2004; Raeder et al., 1998; Tóth et al., 2005), which all rely on inputs from the solar wind.

Since the launch of the ACE mission in 1997 (Stone et al., 1998), measurements from a spacecraft orbiting the first Lagrange point (L1) have been a convenient platform for these solar wind inputs. Data in the solar wind are readily accessible with a steady time cadence for operational models. Further convenience was created with the generation of the OMNI database (King &amp; Papitashvili, 2005), which combines measurements primarily from multiple spacecraft orbiting L1 shifted into the Earth's Sun-orbiting reference frame and propagated to the nose of the bow shock. The convenience and availability has enabled a wide range of studies that have illuminated connections between the Sun and the Earth's magnetosphere, ionosphere, and thermosphere.

Solar wind measured near L1, however, is not what contacts the magnetopause and drives these systems. The shocked and processed magnetosheath plasma is what contacts the magnetopause and subsequently drives the geospace system. Although there is a connection between the solar wind and magnetosheath, the use of data from L1 as drivers of the geospace system has several limitations. First, upstream monitors orbit L1 and do not sit at the L1 point. This means spacecraft can be up to 100 RE off the Earth-Sun line. Since the solar wind is composed of parcels of plasma with varying parameters, a spacecraft orbiting L1 could be probing a block of plasma that does not contact the Earth (Borovsky, 2017; Wang et al., 2016). Figure 1 presents an example of two spacecraft orbiting L1 and sitting within different parcels of plasma or flux tubes. Wind (Acuña et al., 1995) measures a steady positive interplanetary magnetic field (IMF) Bz for almost an hour, while ACE measures an equally steady but negative IMF Bz value. Since the Bz component of the IMF is critical in predicting the efficiency of magnetic reconnection, this is a particularly misleading period for using L1 measurements to predict energy input to the geospace system.

A second limitation is that plasma can be processed significantly between L1 and the Earth. Even if the L1 monitor measures a parcel of plasma that is moving on a trajectory to strike the Earth, the plasma can be significantly processed and changed through the foreshock, structured bow shock, and within the magnetosheath. Variations in plasma and magnetic field measured at L1 may or may not actually strike the

<!-- image -->

<!-- image -->

<!-- image -->

Figure 1. Discrepancy in the interplanetary magnetic field between two L1 monitors. The B z component was measured with a steady yet opposite sign between the Wind and ACE spacecraft for close to a full hour period on 25 April 2010 .

<!-- image -->

<!-- image -->

magnetosphere. A variety of dynamic and time-variable kinetic effects and structures in the region just upstream of the Earth's magnetosphere have been modeled as well as observed to dominate the state of the plasma (Eastwood et al., 2005; Schwartz &amp; Burgess, 1991). These structures include foreshock bubbles (Omidi et al., 2010; Turner et al., 2013), Hot Flow Anomalies (Facskó et al., 2008; Thomsen et al., 1986; Zhang et al., 2010, 2013), mirror mode waves, cavitons (Blanco-Cano et al., 2011), andhigh-speed jets (Nˇ emeˇ cek et al., 1998). A steady solar wind monitored at L1 can result in a highly variable plasma striking the Earth's magnetosphere (Dimmock et al., 2014; Hartinger et al., 2013; Osmane et al., 2015; Sibeck &amp; Gosling, 1996; Turner et al., 2011).

An example of vastly different conditions between the solar wind and the subsolar magnetosheath is presented in Figure 2. The DSCOVR spacecraft (Burt &amp; Smith, 2012) was positioned near L1 and measured relatively steady conditions, while a spacecraft from the THEMIS mission (Angelopoulos, 2008) measured highly turbulent conditions downstream in the magnetosheath. Looking at specific parameters, the magnetic field contacting the magnetopause was highly variable in time compared with that in the solar wind. The dynamic pressure impinging on the magnetopause was also highly variable and even included several magnetosheath high-speed jets, increasing the dynamic pressure significantly. It should be noted that the time sampling period was 4 s for the two spacecraft during this period, so both had the ability to measure similar rates of variability. The dynamic structures observed can occur under all solar wind conditions, but statistically are most common behind the foreshock when the solar wind has a magnetic field vector close to aligned with the Earth-Sun line (Archer &amp; Horbury, 2013; Hietala &amp; Plaschke, 2013). These structures have been shown to have significant impacts on the geospace system and, importantly for the current study, can significantly alter solar wind parameters from L1 to the region just upstream of the magnetopause.

The work presented here uses measurements from the OMNI database and THEMIS spacecraft to provide uncertainties on commonly used solar wind parameters. These uncertainties are obtained as a function of solar wind cone angle and distance of the L1 monitors from the Earth-Sun line. Although the community has developed an understanding for a number of dynamic kinetic processes, prediction of a particular structure, and its evolution as a function of time is beyond our current ability. With this in mind, the uncertainties derived here are based on statistical variation. The uncertainties derived also do not include uncertainty produced from the spacecraft instruments or through calculation of plasma moments from particle measurements.

## 2. Data Set

Measurements from the THEMIS mission provided in situ measurements within the magnetosheath. During the period of interest, THEMIS A (ThA) had an apogee of 12 RE and was close to equatorial with an inclination of 16 ◦ and a perigee of 470 km. Since a nominal subsolar magnetopause position is ∼ 10.5 RE , this provided a probe in the dayside magnetosheath.

Data from ThA were visually inspected from April 2016 to October 2016 to identify periods when the spacecraft was in the magnetosheath. To identify the magnetosheath, the electron spectra, bulk flow, density, and temperature from the electrostatic analyzer instrument (ESA) (McFadden et al., 2008) were used as well as the magnetic field vector measured from the fluxgate magnetometer (FGM) (Auster et al., 2008). Only periods of time when the spacecraft was clearly within the magnetosheath for more than 20 min were included in the study to eliminate possible contamination near the magnetopause or bow shock boundary.

This survey produced 355 magnetosheath intervals and more than 68,000 min ( ∼ 48 days) of data within the magnetosheath. A spatial distribution of the spacecraft position during the time intervals is presented in Figure 3. The coverage spans all local times in the dayside magnetosheath.

In the solar wind, the OMNI data set were used. OMNI combines measurements from spacecraft upstream of the Earth into a single data product time propagated to the nose of the bow shock. During the time period

Figure 2. Processing of solar wind plasma from the foreshock. DSCOVR measurements (left) are in the pristine solar wind while the THEMIS measurements (middle) are from the magnetosheath. Spacecraft positions are shown in the right.

<!-- image -->

<!-- image -->

used, the ACE and Wind spacecraft are the primary contributors to the OMNI product. As part of the creation of the OMNI data set, measurements are normalized to account for systematic variations between spacecraft. One-minute time cadence OMNI and 1-min time-averaged THEMIS measurements were used. The OMNI data set also includes 5-min and hour-long average data products. As many of the variations magnetosheath are temporally variable, longer time averages may have better agreement with averaged measurements in the magnetosheath.

The paper will first focus on total pressure and magnetic clock angle between OMNI and THEMIS. Next these parameters will be monitored in the context of uncertainty resulting from plasma processing at the foreshock and spacecraft placement of the L1 monitors. These parameters have been chosen as they are often assumed to remain constant through the bow shock.

Figure 3. (a) Relative positions of THEMIS, ACE, and Wind during the study. (b) Cutout of THEMIS positions during magnetosheath encounters from April to October 2016. All coordinates are in geocentric solar equatorial (GSE).

<!-- image -->

<!-- image -->

Figure 4. Comparison of total pressure (magnetic, thermal, and dynamic) from corresponding (a) OMNI and (b) THEMIS measurements in the solar wind and magnetosheath respectively.

<!-- image -->

## 3. Pressure

As the supersonic flowing solar wind passes through the bow shock, flow speed and dynamic pressure decrease while the thermal pressure increases. Although the pressure components change, the total pressure (thermal + dynamic + magnetic) is conserved through the boundary. As such it can be used for comparison upstream at L1 and within the magnetosheath.

Figure 4 presents a comparison of the total pressure in both the solar wind and magnetosheath at corresponding times. Here 'corresponding times' means the same time step from OMNI and THEMIS. Since the OMNIdatabase is time propagated to the nose of the bow shock, and not necessarily the position within the magnetosheath where THEMIS is sitting, this adds another source of error. Since all of the THEMIS spacecraft measurements were on the dayside in the magnetosheath, the anticipated propagation time from the bow shock to the spacecraft would be several minutes (Walsh et al., 2012).

The comparison of pressure shows several features. If the upstream data were a perfect representation of the parameters in the magnetosheath striking the magnetosphere, all points would fall along the red line in Figure 4a. Deviation from this line represents the combination of errors from instrumentation, propagation, and missing physics. Quantitatively, the P OMNI P THEMIS distribution had a standard deviation of 0.67 nPa. Another notable feature is an offset in total pressure (shown in Figure 4b). The mean of the distribution is 0.45 nPa indicating the OMNI data set measures slightly larger pressures than THEMIS.

Several possible culprits exist for this pressure discrepancy. The first is cross calibration between the two missions. The second explanation is the ram pressure calculation. Here, the ram pressure is calculated using only the Vx component. In the solar wind the ram pressure is almost entirely in the X direction; however,

Figure 5. Comparison of magnetic clock angle ( /u1D703 ) from corresponding (a) OMNI and (b) THEMIS measurements in the solar wind and magnetosheath. In the right, the difference between the two angles is presented.

<!-- image -->

Figure 6. (a) Number of counts in each cone angle bin. (b) Probability distribution function of P OMNI -P THEMIS . (c) Standard deviations of the P OMNI -P THEMIS distribution as a function of cone angle ( /u1D719 ). The width of the horizontal blue lines indicates the size of the cone angle bin. When the foreshock is upstream of the Earth (small clock angle), OMNI measurements do a poorer job representing pressure measurements in the magnetosheath.

<!-- image -->

<!-- image -->

in the magnetosheath the flow can be turbulant and diverted with velocity in other directions. Since other components are not included in the calculation here, the THEMIS measurements may be underpredicting the total pressure in the magnetosheath as shown in Figure 4.

## 4. Clock Angle

Clock angle of the IMF is a second parameter often assumed to be conserved through the bow shock. Clock angle is defined as

<!-- formula-not-decoded -->

A clock angle of 0 ◦ corresponds to pure northward IMF ( + Bz ), 90 ◦ corresponds to pure + By while 180 ◦ corresponds to pure southward IMF ( -Bz ). For a front that is coplanar with the shock, the clock angle should be conserved, however, for locations off the nose of the bow shock, or on a rippled or structured bow shock where the boundary normal direction is not aligned with the Earth-Sun line, this condition is not strictly conserved. However, since the clock angle is often used as an input for geospace models, the relationship between the value in the dayside magnetosheath near the magnetopause and L1 is studied here.

Measurements of clock angle from OMNI and THEMIS are compared in Figure 5. A large-scale trend in Figure 5a shows a good correlation between the values from the two measurement platforms; however, there are many points with significant deviation (Figure 5b). A more subtle 'Z' shape is also seen in the plot. When the clock angle is slightly above or below 180 ◦ or 0 ◦ , there is a shift in the OMNI/THEMIS

Figure 7. (a) Number of counts in each cone angle bin. (b) Probability distribution function of clock angle differences ( /u1D703 OMNI -/u1D703 THEMIS ). (c) Standard deviations of the /u1D703 OMNI -/u1D703 THEMIS distribution as a function of cone angle ( /u1D719 ). The width of the horizontal green lines indicates the size of the cone angle bin. When the foreshock is upstream of the Earth (small clock angle), OMNI measurements do a poorer job representing pressure measurements in the magnetosheath.

<!-- image -->

<!-- image -->

trend. This shift illustrates the magnetic field lines being bent toward the z axis, either 180 ◦ or 0 ◦ , within the magnetosheath as compared to corresponding measurements in the solar wind. This is likely an effect of magnetic field line draping. As magnetic field lines drape within the magnetosheath, they bend to conform to the shape of the local magnetopause. Since the THEMIS spacecraft are primarily in the equatorial plane, this would mean the observed field lines would bend toward a clock angles of 180 ◦ or 0 ◦ (roughly aligned with the magnetopause for an observer in the XY plane). Similar rotations have been seen through a number of spacecraft measurements (Coleman, 2005; Crooker et al., 1985; Kaymaz et al., 1992).

In a more binary view of the magnetic field propagation, the sign of the Bz component is compared between OMNI and the THEMIS probe. Since some predictive models ingest the Bz component alone, successful prediction is important. Using the full data set, the Bz component matches sign between OMNI and the magnetosheath probe just 65.4% of the time. We note since the sign can only have two values, two random distributions would agree 50% of the time. Šafránková et al. (2009) focused more closely on the ability to predict the sign of Bz from upstream monitors and found similar results but noted the prediction success rate increases as the magnitude of the magnetic field increases.

## 5. Foreshock Impact

When the magnetic field vector in the solar wind is close to normal with the Earth's bow shock, a foreshock forms upstream. This region is highly turbulent with dynamic kinetic features forming. These structures subsequently propagate downstream into the magnetosheath and contact the magnetosphere.

Figure 8. Distance of ACE and Wind from the Earth-Sun line. The time period corresponds the data presented in Figure 3. The black trace presents the closest position between the two spacecraft.

<!-- image -->

<!-- image -->

Such structures are not present in the upstream solar wind and would not be predicted from an L1 monitor alone. Although accurately predicting the physics in the foreshock as a function of time and space is beyond the ability of our current models, we do have a basic understanding of when a foreshock will form at the dayside bow shock based on the magnetic field orientation in the solar wind.

When the cone angle is small (near 0 ◦ ), the foreshock is typically present upstream of the Earth. Conversely, if the cone angle is large (near 90 ◦ ), a a foreshock is not likely to be upstream of the Earth and the parameters in the solar wind will do a better job in predicting parameters within the magnetosheath. The magnetic cone angle is defined as

<!-- formula-not-decoded -->

To evaluate the impact of the foreshock on solar wind propagating from L1 to the magnetosheath and magnetopause, parameters typically assumed to be conserved through the Earth's bow shock are evaluated in both regions. The first parameter assessed is total pressure.

## 5.1. Pressure

Since total pressure is conserved through the bow shock, the value can be used to test processing between L1 and the magnotosheath. Figure 6

quantifies the variability in pressure. The data are sorted by cone angle as a proxy for the position of the foreshock. For each cone angle bin in Figure 6a P OMNI -P THEMIS distribution, similar to that in Figure 4b, is created. Figure 6b displays a probability distribution function for data in each cone angle bin. The probability distribution function is generated from the data through a kernel density estimate. Figure 6c presents the standard deviations of the raw data. The general trend in the plot is clear. When the cone angle is small, the OMNI measurements do a poorer job representing pressure measurements in the magnetosheath. This is consistent with our understanding of the upstream system. When the foreshock is upstream of the Earth, parameters in the magnetosheath are disturbed due to a variety of physical mechanisms introduced above. Each bin has more than 1,700 points, and many have more then 10,000 points. The trend is fit linearly to provide a functional form describing how the uncertainty varies.

## 5.2. Clock Angle

The variability of the magnetic clock angle between L1 and the magnetosheath is also tested as a function of cone angle. Figure 7 quantifies this trend. Figure 7 and the subsequent two figures follow the same structure as Figure 6. Figure 7b presents a probability distribution function generated through a kernel density estimate, and Figure 7c presents standard deviations of the actual data. Once again, a clear relationship is visible. For lower cone angles, when the foreshock is on the dayside, the clock angles measured at L1 do a worse job predicting the values in the magnetosheath than for large cone angles. The trend is fit linearly to provide a functional form describing how this standard deviation or uncertainty varies.

## 6. Position of Upstream Monitors

An additional source of error between the parameters measured at L1 and in the magnetosheath is the position of the upstream monitors. In most cases, rather than sitting at L1, upstream monitors are in halo orbits around the Lagrange point. The left side of Figure 3 presents the orbits of ACE and Wind around the L1point. The positions as a function of distance from the Earth-Sun line are presented in Figure 8. The orbits can bring the spacecraft more than 100 RE from the Earth-Sun line. At times when the upstream monitors are further from the Earth-Sun line they may have larger uncertainty in predicting material that will strike the Earth's magnetosphere.

In a similar fashion as with the cone angle, total pressure and magnetic clock angle are assessed from the OMNI database and in the magnetosheath as a function of distance of ACE and Wind from the Earth-Sun line.

Figure 9. (a) Number of counts in each distance bin. (b) Probability distribution function of P OMNI -P THEMIS . (c) Standard deviations of the P OMNI -P THEMIS distribution as a function of position of the ACE and Wind spacecraft. The width of the horizontal blue lines indicates the size of the distance bin. When the minimum distance from the Earth-Sun line to ACE or Wind is large, OMNI measurements do a poorer job representing pressure measurements in the magnetosheath.

<!-- image -->

<!-- image -->

## 6.1. Pressure

Once again the total pressure near L1 is compared with that measured in the dayside magnetosheath. Here, the comparison is made as a function of the position of the upstream monitors. Using Wind and ACE, the minimum distance from the Earth-Sun line to the spacecraft ranges from 11 to 41 RE . Figure 9 presents a standard deviation of the difference distribution as a function of the minimum distance of either ACE or Wind and the Earth-Sun line. This is similar to Figure 6, but here we bin by spatial position rather than cone angle. Each positional bin has more than 3,000 data points. A slight positive trend is observed. As the minimumdistance from a spacecraft to the Earth-Sun line increases, the uncertainty in pressure between L1 and the magnetosheath increases. As the spacecraft are further from the Earth-Sun line, ACE and Wind may not provide a measurement of the block of plasma that actually strikes the Earth's magnetopause or dayside magnetosheath. Although one may expect this trend, it is not significant in these data. One reason for this may be the correlation lengths in the solar wind. Borovsky (2017) found the magnetic field correlation to be on the order of 100 RE . Due to the smaller apoapsis of ACE, the spacecraft are never more than roughly 40 RE from the Earth-Sun line, smaller than a typical spatial scale.

In terms of application, these results have implications for design of future L1 monitoring missions. For orbits around L1 with a small apoapsis, it is likely the block of plasma being observed by the L1 monitor is the same as the one striking the magnetopause. For distances up to 40 RE from the Earth-Sun line, the pressure in the magnetosheath is similar to that monitored by a solar wind monitor. Stating this differently, these results imply that increasing an orbit from an apoapsis of 10 RE to 40 RE does not make a significant difference in the probe's ability to predict pressure in the magnetosheath.

Figure 10. (a) Number of counts in each distance bin. (b) Probability distribution function of clock angle difference ( /u1D703 OMNI -/u1D703 THEMIS ) as a function of distance from the Earth-Sun line. (c) Standard deviations of the /u1D703 OMNI -/u1D703 THEMIS distribution as a function of ACE and Wind positions. The width of the horizontal green lines indicates the size of the distance bin. When the minimum distance from the Earth-Sun line to ACE or Wind is large, OMNI measurements do a poorer job representing clock angle measurements in the magnetosheath.

<!-- image -->

<!-- image -->

## 6.2. Clock Angle

The magnetic clock angle measured at L1 is also compared with that in the magnetosheath as a function of the position of L1 monitors. Figure 10 presents this comparison, similar to the analysis above for pressure. As the minimum distance between the L1 monitor and the Earth-Sun line increases, the L1 monitor does a worse job predicting the parameters in the magnetosheath. This is a consistent trend to that seen comparing the total pressure. The points have been fit with a linear trend to quantify the relationship.

## 7. Discussion

The community has long understood values from an upstream monitor do not always represent what propagates downstream to contact the Earth's space environment (Crooker et al., 1982). Without a steady magnetosheath monitor just upstream of the magnetopause, measurements from L1 provide a convenient platform for case studies as well as operational models despite the caveat of uncertainty during propagation. An effect of this intrinsic uncertainty can be seen in the prediction of geomagnetic indices based on solar wind parameters. Models predicting geomagnetic indices based on solar wind parameters have improved significantly since the first attempts (Kan &amp; Lee, 1979; Newell et al., 2007; McPherron et al., 2015), but no matter how many variables are used, or tools engaged, the models have not been able to generate a prediction with a correlation coefficient greater than ∼ 0.8 (Borovsky, 2008). A simple explanation could be the solar wind model inputs are not directly driving the system. There is an uncertainty on the inputs that is not taken into account.

<!-- image -->

## Table 1

Relationship Between the Uncertainty in Solar Wind Parameters and Properties of the Solar Wind and Location of Solar Wind Monitors

Linear Dependencies of Standard Deviations

Cone angle ( /u1D719 ) dependencies

Stdev( /u1D703 OMNI -/u1D703 Thm )[ deg ] = -0 . 22 /u1D719 +54.01 ◦

Stdev(P OMNI -P Thm ) [nPa] = -0.01 /u1D719 +1.39 nPa

Distance from Earth-Sun line ( d ) dependencies

Stdev( /u1D703 OMNI -/u1D703 Thm )[ deg ] = 0 . 35 d +27.57 ◦

Stdev(P OMNI -P Thm ) [nPa] = 0.002 d +0.58 nPa

Note . All angles are in degrees. /u1D703 represents interplanetary magnetic field clock angle.

The uncertainty trends measured here are anticipated based on our understanding of the system. During times of low cone angle, values from L1 do a poorer job in predicting values in the magnetosheath. During times when the L1 monitors are far from the Earth-Sun line, values from L1 do a poorer job in predicting values in the magnetosheath. Here the average uncertainties and standard deviations of values between L1 and the magnetosheath are quantified. A summary of these values and their relationships to the position of L1 monitors and magnetic cone angle are presented in Table 1.

Through quantifying these uncertainties as a function of driver, a user can run ensembles of models with different inputs spanning the standard uncertainties. The use of ensemble runs incorporating anticipated uncertainties is a common practice in many fields such as weather and climate study (Kay et al., 2015; Owen &amp;Palmer, 1987) and is growing in use in space weather prediction (Cash et al., 2015; Morley et al., 2018; Riley et al., 2013). One application of this use could be running a global MHD simulation of the magnetosphere. Instead of running a single MHD simulation with an input of a single time-varying clock angle based on an L1solar wind monitor, a researcher could run a series of MHD simulations. One could be run with the OMNI data input, but two more could be run with the OMNI clock angle plus or minus the standard deviation in clock angle. These ensemble of simulations outputs would then provide a full range of the possible outputs given standard deviations in solar wind propagation.

One example of such an experiment was conducted by Morley et al. (2018). Morley et al. (2018) found variation of solar wind parameters between L1 and a probe (geotail) just upstream of the bow shock then used those uncertainties to run ensemble predictions of Sym -H as well as magnetic perturbations on the surface of the Earth while incorporating uncertainties in the solar wind inputs. In the present study we have further evolved the uncertainty measurements by incorporating variations resulting from a plasma passing through the bow shock.

Onevariable not explicitly tested for here is timing. The study directly compares a time step from OMNI with the corresponding time step from THEMIS. One could imagine a scenario where a solar wind parameter oscillated as a periodic signal. If the time propagation was such that the resulting signal was transmitted to the magnetosheath perfectly but time-delayed such that the signal was out of phase by 180 ◦ , the analysis method used here would find a maximum error. One solution to eliminate this effect is to test different time shifts on the data set to maximize a correlation between the two signals. Such a technique has been used in earlier solar wind propagation studies (Collier et al., 1998). Since such a method can not be used with real time predictions and some deterministic models rely on only one time step for their solar wind input (Newell et al., 2007; Shue et al., 1998), such a time delay was not implemented here.

Lastly, an element not controlled for in this experiment is how parameters change as a function of position in the dayside magnetosheath. Although an ideal experiment would compare measurements from the subsolar magnetosheath with those in the solar wind, the amount of spacecraft measurements exactly at the subsolar point is limited. In order to include more data, measurements over the entire dayside magnetosheath are included in the sample data set. Some known spatial variations include draping of magnetic field lines around the obstacle of the magnetosphere (as discussed in section 5) as well as accelerated flow near the flanks of the magnetopause. These flows occur particularly during times of positive Bz whereplasma is accelerated through ⃗ J × ⃗ B forces (Erkaev et al., 2011; Lavraud et al., 2007).

<!-- image -->

## Acknowledgments

Support was provided by the NASA grants 80NSSC18K0764 and NNX16AJ73G and NSF award 1502436 for support of the work. Mike Stevens is acknowledged for providing DSCOVR data. The THEMIS data are freely available and obtained from the website (http://themis.ssl.berkeley. edu/). Analysis was conducted with the SPEDAS software (Angelopoulos et al., 2019). The OMNI data are freely available and were obtained from the website (https://omniweb.gsfc.nasa. gov/).

## 8. Conclusions

Although measurements from an L1 monitor are often used as inputs for predictive geospace models, these parameters are not always what contacts and drives the geospace system. Some plasma monitored by L1 monitors does not reach the Earth, and some plasma can be processed or modified between L1 and the magnetopause. Here measurements from THEMIS in the magnetosheath were compared with corresponding measurements from L1 monitors in the OMNI database to evaluate standard uncertainties in total pressure and magnetic clock angle. The standard deviation in the value in the magnetosheath compared with that at L1 is 0.67 nPa for pressure and 38 ◦ for clock angle. Both pressure and clock angle exhibit larger deviations between L1 and the magnetosheath when the L1 monitors are far from the Earth-Sun line or when the foreshock is on the dayside bow shock. Quantitative relationships between these parameters and the drivers are established.

## References

- Acuña, M. H., Ogilvie, K. W., Baker, D. N., Curtis, S. A., Fairfield, D. H., &amp; Mish, W. H. (1995). The global geospace science program and its investigations. Space Science Reviews , 71 , 5-21. https://doi.org/10.1007/BF00751323
- Angelopoulos, V. (2008). The THEMIS mission. Space Science Reviews , 141 , 5-34. https://doi.org/10.1007/s11214-008-9336-1
- Angelopoulos, V., Cruce, P., Drozdov, A., Grimes, E. W., Hatzigeorgiu, N., King, D. A., et al. (2019). The Space Physics Environment Data Analysis System (SPEDAS). Space Science Reviews , 215 , 9. https://doi.org/10.1007/s11214-018-0576-4
- Archer, M. O., &amp; Horbury, T. S. (2013). Magnetosheath dynamic pressure enhancements: Occurrence and typical properties. Annals of Geophysics , 31 , 319-331. https://doi.org/10.5194/angeo-31-319-2013
- Auster, H. U., Glassmeier, K. H., Magnes, W., Aydogar, O., Baumjohann, W., Constantinescu, D., et al. (2008). The THEMIS fluxgate magnetometer. Space Science Reviews , 141 , 235-264.
- Barker, A. B., Li, X., &amp; Selesnick, R. S. (2005). Modeling the radiation belt electrons with radial diffusion driven bythe solar wind. Space Weather , 3 , S10003. https://doi.org/10.1029/2004SW000118
- Blanco-Cano, X., Kajdic, P., Omidi, N., &amp; Russell, C. T. (2011). Foreshock cavitons for different interplanetary magnetic field geometries: Simulations and observations. Journal of Geophysical Research , 116 , A09101. https://doi.org/10.1029/2010JA016413
- Borovsky, J. E. (2008). The rudiments of a theory of solar wind/magnetosphere coupling derived from first principles. Journal of Geophysical Research , 113 , A08228. https://doi.org/10.1029/2007JA012646
- Borovsky, J. E. (2017). The spatial structure of the oncoming solar wind at Earth and the shortcomings of a solar wind monitor at L1. Journal of Atmospheric and Solar - Terrestrial Physics . https://doi.org/10.1016/j.jastp.2017.03.014
- Burt, J., &amp; Smith, B. (2012). Deep space climate observatory: The DSCOVR mission, Aerospace conference (pp. 1-13), 2012 IEEE. Big Sky, MT: IEEE.
- Cash, M. D., Biesecker, D. A., Pizzo, V., de Koning, C. A., Millward, G., Arge, C. N., et al. (2015). Ensemble modeling of the 23 July 2012 coronal mass ejection. Space Weather , 13 , 611-625. https://doi.org/10.1002/2015SW001232
- Coleman, I. J. (2005). A multi-spacecraft survey of magnetic field line draping in the dayside magnetosheath. Annals of Geophysics , 23 , 885-900.
- Collier, M. R., Slavin, J. A., Lepping, R. P., Szabo, A., &amp; Ogilvie, K. W. (1998). Timing accuracy for the simple planar propagation of magnetic field structures in the solar wind. Geophysical Research Letters , 25 , 2509.
- Crooker, N. U., Luhmann, J. G., Russell, C. T., Smith, E. J., Spreiter, J. R., &amp; Stahara, S. S. (1985). Magnetic field draping against the dayside magnetopause. Journal of Geophysical Research , 90 , 3505-3510. https://doi.org/10.1029/JA090iA04p03505
- Crooker, N. U., Siscoe, G. L., Russell, C. T., &amp; Smith, E. J. (1982). Factors controlling degree of correlation between ISEE 1 and ISEE 3 interplanetary magnetic field measurements. Journal of Geophysical Research , 87 (A4), 2224-2230. https://doi.org/10.1029/ JA087iA04p02224
- Dimmock, A. P., Nykyri, K., &amp; Pulkkinen, T. I. (2014). A statistical study of magnetic field fluctuations in the dayside magnetosheath and their dependence on upstream solar wind conditions. Journal of Geophysical Research: Space Physics , 119 , 6231-6248. https://doi.org/ 10.1002/2014JA020009
- Eastwood, J. P., Lucek, E. A., Mazelle, C., Meziane, K., Narita, Y., Pickett, J., &amp; Treumann, R. A. (2005). The foreshock. Space Science Reviews , 118 , 41-94.
- Erkaev, N. V., Farrugia, C. J., Harris, B., &amp; Biernat, H. K. (2011). On accelerated magnetosheath flows under northward IMF. Geophysical Research Letters , 38 , L01104. https://doi.org/10.1029/2010GL045998
- Facskó, G., Kecskeméty, K., Erdos, G., Tátrallyay, M., Daly, P. W., &amp; Dandouras, I. (2008). A statistical study of hot flow anomalies using Cluster data. Advances in Space Research , 41 , 1286-1291. https://doi.org/10.1016/j.asr.2008.02.005
- Hartinger, M. D., Turner, D. L., Plaschke, F., Angelopoulos, V., &amp; Singer, H. (2013). The role of transient ion foreshock phenomena in driving Pc5 ULF wave activity. Journal of Geophysical Research: Space Physics , 118 , 299-312. https://doi.org/10.1029/2012JA018349
- Hietala, H., &amp; Plaschke, F. (2013). On the generation of magnetosheath high-speed jets by bow shock ripples. Journal of Geophysical Research: Space Physics , 118 , 7237-7245. https://doi.org/10.1002/2013JA019172
- Janhunen, P., Palmroth, M., Laitinen, T., Honkonen, I., Juusola, L., Facsko, G., &amp; Pulkkinen, T. I. (2012). The GUMICS-4 global MHD magnetosphere-ionosphere coupling simulation. Journal of Atmospheric and Solar-Terrestrial Physics , 80 , 48-59. https://doi.org/10.1016/ j.jastp.2012.03.006
- Kan, J. R., &amp; Lee, L. C. (1979). Energy coupling and the solar wind dynamo. Geophysical Research Letters , 6 , 577.
- Kay, J. E., Deser, C., Phillips, A., Mai, A., Hannay, C., Strand, G., et al. (2015). The Community Earth System Model (CESM) large ensemble project: A community resource for studying climate change in the presence of internal climate variability. Bulletin of the American Meteorological Society , 96 (8), 1333-1349. https://doi.org/10.1175/BAMS-D-13-00255.1
- Kaymaz, Z., Siscoe, G. L., &amp; Luhmann, J. G. (1992). IMF draping around the Geotail: IMP 8 observations. Journal of Geophysical Research , 19 , 829-832.
- King, J. H., &amp; Papitashvili, N. E. (2005). Solar wind spatial scales in and comparisons of hourly Wind and ACE plasma and magnetic field data. Journal of Geophysical Research , 110 , A02104. https://doi.org/10.1029/2004JA010649

<!-- image -->

## Journal of Geophysical Research: Space Physics

- Lavraud, B., Borovsky, J. E., Ridley, A. J., Pogue, E. W., Thomsen, M. F., Reme, H., et al. (2007). Strong bulk plasma acceleration in Earth's magnetosheath: A magnetic slingshot effect? Geophysical Research Letters , 34 , L14102. https://doi.org/10.1029/2007GL030024
- Li, X. (2004). Variations of 0.7-6.0 MeV electrons at geosynchronous orbit as a function of solar wind. Space Weather , 2 , S03006. https:// doi.org/10.1029/2003SW000017
- Lyon, J. G., Fedder, J. A., &amp; Mobarry, C. M. (2004). The Lyon-Fedder-Mobarry (LFM) global MHD magnetospheric simulation code. Journal of Atmospheric and Solar-Terrestrial Physics , 66 , 1333.
- McFadden, J. P., Carlson, C. W., Larson, D., Ludlam, M., Abiad, R., Elliott, B., et al. (2008). The THEMIS ESA plasma instrument and in-flight calibration. Space Science Reviews , 141 , 277-302. https://doi.org/10.1007/s11214-008-9440-2
- McPherron, R. L., Hsu, T.-S., &amp; Chu, X. (2015). An optimum solar wind coupling function for the AL index. Journal of Geophysical Research: Space Physics , 120 , 2494-2515. https://doi.org/10.1002/2014JA020619
- Morley, S. K., Welling, D. T., &amp; Woodroffe, J. R. (2018). Perturbed input ensemble modeling with the space weather modeling framework. Space Weather , 16 , 1330-1347. https://doi.org/10.1029/2018SW002000
- Nˇ emeˇ cek, Z., Šafránková, J., Pˇ rech, L., Sibeck, D. G., Kokubun, S., &amp; Mukai, T. (1998). Transient flux enhancements in the magnetosheath. Geophysical Research Letters , 25 , 1273-1276. https://doi.org/10.1029/98GL50873
- Newell, P. T., Sotirelis, T., Liou, K., Meng, C.-I., &amp; Rich, F. J. (2007). A nearly universal solar wind-magnetosphere coupling function inferred from 10 magnetospheric state variables. Journal of Geophysical Research , 112 , A01206. https://doi.org/10.1029/2006JA012015
- Omidi, N., Eastwood, J. P., &amp; Sibeck, D. G. (2010). Foreshock bubbles and their global magnetospheric impacts. Journal of Geophysical Research , 115 , A06204. https://doi.org/10.1029/2009JA014828
- Osmane, A., Dimmock, A. P., &amp; Pulkkinen, T. I. (2015). Universal properties of mirror mode turbulence in the Earth's magnetosheath. Geophysical Research Letters , 42 , 3085-3092. https://doi.org/10.1002/2015GL063771
- Owen, J. A., &amp; Palmer, T. N. (1987). The impact of El Niño on an ensemble of extended-range forecasts. Monthly Weather Review , 115 (9), 2103-2117. https://doi.org/10.1175/1520-0493(1987)115 &lt; 2103:TIOENO &gt; 2.0.CO;2
- Raeder, J., Berchem, J., &amp; Ashour-abdalla, M. (1998). The Geospace Environment Modeling Grand Challenge: Results from a Global Geospace Circulation Model. Journal of Geophysical Research , 103 (A7), 14,787-14,797. https://doi.org/10.1029/98JA00014
- Riley, P., Linker, J. A., &amp; Mikic, Z. (2013). On the application of ensemble modeling techniques to improve ambient solar wind models. Journal of Geophysical Research: Space Physics , 118 , 600-607. https://doi.org/10.1002/jgra.50156
- Šafránková, J., Hayosh, M., Gutynska, O., Nˇ emeˇ cek, Z., &amp; Pˇ rech, L (2009). Reliability of prediction of the magnetosheath Bz component from interplanetary magnetic field observations. Journal of Geophysical Research , 114 , A12213. https://doi.org/10.1029/2009JA014552
- Schwartz, S. J., &amp; Burgess, D. (1991). Quasi-parallel shocks: A patchwork of three-dimensional structures. Geophysical Research Letters , 18 , 373-376.
- Shue, J.-H., Song, P., Russell, C. T., Steinberg, J. T., Chao, J. K., Zastenker, G., et al. (1998). Magnetopause location under extreme solar wind conditions. Journal of Geophysical Research , 103 , 17,691-17,710. https://doi.org/10.1029/98JA01103
- Sibeck, D. G., &amp; Gosling, J. T. (1996). Magnetosheath density fluctuations and magnetopause motion. Journal of Geophysical Research , 101 (A1), 31-40.
- Stone, E. C., Frandsen, A. M., Mewaldt, R. A., Christian, E. R., Margolies, D., Ormes, J. F., &amp; Snow, F. (1998). The Advanced Composition Explorer. Space Science Reviews , 86 , 1.
- Thomsen, M. F., Gosling, J. T., Fuselier, S. A., Bame, S. J., &amp; Russell, C. T. (1986). Hot, diamagnetic cavities upstream from the Earth's bow shock. Journal of Geophysical Research , 91 , 2961-2973. https://doi.org/10.1029/JA091iA03p02961
- Tóth, G., Sokolov, I. V., Gombosi, T. I., Chesney, D. R., Clauer, C. R., De Zeeuw, D. L., et al. (2005). Space Weather Modeling Framework: Anew tool for the space science community. Journal of Geophysical Research , 110 , A12226. https://doi.org/10.1029/2005JA011126
- Turner, D. L., Eriksson, S., Phan, T. D., Angelopoulos, V., Tu, W., Li, X., et al. (2011). Multispacecraft observations of a foreshock-induced magnetopause disturbance exhibiting distinct plasma flows and an intense density compression. Journal of Geophysical Research , 116 , A04230. https://doi.org/10.1029/2010JA015668
- Turner, D. L., Omidi, N., Sibeck, D. G., &amp; Angelopoulos, V. (2013). First observations of foreshock bubbles upstream of Earth's bow shock: Characteristics and comparisons to HFAs. Journal of Geophysical Research: Space Physics , 118 , 1552-1570. https://doi.org/10.1002/jgra. 50198
- Walsh, B. M., Sibeck, D. G., Wang, Y., &amp; Fairfield, D. H. (2012). Dawn-dusk asymmetries in the Earth's magnetosheath. Journal of Geophysical Research , 117 , A12211. https://doi.org/10.1029/2012JA018240
- Wang, B., Nishimura, Y., Zou, Y., Lyons, L. R.,Angelopoulos, V., Frey, H., &amp; Mende, S. (2016). Investigation of triggering of poleward moving auroral forms using satellite-imager coordinated observations. Journal of Geophysical Research: Space Physics , 121 , 10,929-10,941. https://doi.org/10.1002/2016JA023128
- Zhang, H., Sibeck, D. G., Zong, Q.-G., Gary, S. P., McFadden, J. P., Larson, D., et al. (2010). Time History of Events and Macroscale Interactions during Substorms observations of a series of hot flow anomaly events. Journal of Geophysical Research , 115 , A12235. https://doi. org/10.1029/2009JA015180
- Zhang, H., Sibeck, D. G., Zong, Q.-G., Omidi, N., Turner, D., &amp; Clausen, L. B. N. (2013). Spontaneous hot flow anomalies at quasi-parallel shocks: 1. Observations. Journal of Geophysical Research: Space Physics , 118 , 3357-3363. https://doi.org/10.1002/jgra.50376