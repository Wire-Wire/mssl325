## RESEARCH ARTICLE

10.1029/2018SW002113

## Key Points:

- We use Geotail data in front of bow shock in 1997 -2016 as a proxy of actual IMF interacting with the magnetosphere
- Cross -correlation analysis reveals that the OMNI IMF data are of very good, moderate, and poor quality in 42%, 33%, and 25%, respectively
- We find that the PC index can serve as a quality estimator for OMNI database

## Supporting Information:

- Supporting Information S1

## Correspondence to:

M. V. Vokhmyanin, m.vokhmyanin@spbu.ru

## Citation:

Vokhmyanin, M. V., Stepanov, N. A., &amp; Sergeev, V. A. (2019). On the evaluation of data quality in the OMNI interplanetary magnetic field database. Space Weather , 17 , 476 -486. https://doi. org/10.1029/2018SW002113

Received 31 OCT 2018 Accepted 1 MAR 2019 Accepted article online 7 MAR 2019 Published online 22 MAR 2019

©2019. American Geophysical Union. All Rights Reserved.

<!-- image -->

<!-- image -->

## On the Evaluation of Data Quality in the OMNI Interplanetary Magnetic Field Database

M. V. Vokhmyanin 1 , N. A. Stepanov 1,2 , and V. A. Sergeev 1

1 Institute and Department of Physics, Saint Petersburg State University, St. Petersburg, Russia, 2 Arctic and Antarctic Research Institute, St. Petersburg, Russia

Abstract The OMNI database is formed by propagating the solar wind measured at around Lagrange point L1, whose result may differ from the actual solar wind in the vicinity of the bow shock nose. To test the quality of the OMNI database, we cross -correlate the 2 -hr intervals of 1 -min interplanetary magnetic field (IMF) data provided mostly by ACE and WIND spacecraft with Geotail measurements in front of the bow shock (10,409 cases in 1997 -2016). We used two metrics: Pearson correlation coefficient ( CC ) and prediction efficiency ( PE ). Confirming previous studies, we found that the prediction quality of actual IMF degrades continuously with increasing distance of OMNI spacecraft from the Sun -Earth line, with the amounts of poor and good predictions become nearly equal for RYZ ≥ 65 RE (they constitute ~12% of the entire database). In roughly 20% of the analyzed data, low CC and PE values were the consequence of low IMF variability (a low signal -to -noise ratio). The remaining data set includes 42% of very good data ( CC ≥ 0.8), 33% of relatively good data (0.5 ≤ CC &lt;0.8 and PE ≥ 0), 10% of data having correct variability but wrong absolute values (0.5 ≤ CC &lt;0.8 and PE &lt;0), and 15% of poor data ( CC &lt;0.5). We also discovered that the OMNI data are generally of a good quality when the PC index of geomagnetic activity correlates well with the solar wind -magnetosphere coupling factor suggested by Kan and Lee (1979, https://doi.org/ 10.1029/GL006i007p00577).

Plain Language Summary Many space weather activity studies use measurements of the solar wind magnetic field made at ~1.5 × 10 6 km distance from the Earth, which are propagated to the Earth's magnetic field and are available to the community in the OMNI database. It is assumed that they correspond to the solar wind magnetic field near the front of the Earth's bow shock, where the solar wind and the Earth's magnetic fields interact. We compare OMNI data to the independent measurements near the bow shock and found that this assumption is violated for ~25% of the distant solar wind data under analysis. The amount of unreliable data can be decreased by using measurements made closer to the Sun -Earth line or by using those data that correlate well with the polar magnetic activity ( PC index).

## 1. Introduction

Magnetospheric activity is controlled largely by the solar wind (SW) and its interplanetary magnetic field (IMF). During the last two decades, the monitoring of SW at the L1 Lagrange point, located approximately 230 RE upstream, has provided a continuous data stream of the IMF and SW plasma parameters. After estimating the SW phase front orientations and propagation to the Earth's bow shock subsolar point (roughly at 14 RE), these recomputed continuous SW data are widely available to the community for the research and application purposes in the highly popular OMNI database (see King &amp; Papitashvili, 2005, and website at https://omniweb.gsfc.nasa.gov/). The quality of that research depends on how accurately these data correspond to the actual SW that reaches the magnetosphere and drives magnetospheric dynamics. The size of that SW flow tube that directly interacts with the dayside magnetosphere during the reconnection process is known to be as small as ~4RE (Burke et al., 1999). This suggests that the SW measured at 230 RE may miss the magnetosphere.

The accuracy of the propagated SW data and a number of related questions have been addressed in many studies, which compared the parameters measured at 2 points in the SW, particularly by correlating the observations made at around the L1 point, for example, ISEE -3, ACE, WIND, and DSCOVR, to the observations of the near -Earth monitor (such as ISEE -1, IMP -8, Geotail, and Cluster) -see, for example, Crooker et al. (1982), Kelly et al. (1986), Zastenker et al. (2000), Collier et al. (1998, 2000), Richardson and Paularena (2001), Weimer and King (2009), Case and Wild (2012), and Jackel et al. (2013). In the

<!-- image -->

following, we pay the main attention to the variations of the SW magnetic field (IMF) whose variations basically control the changes of the dayside reconnection process. Whereas many different combinations of SW and IMF parameters have been tested and proposed to represent best the driver of magnetospheric activity, most of them contain a combination of magnetic field and flow parameters in the form V α B β sin γ ( θ /2) (with α , β , and γ power law coefficients, see, e.g., a summary in Newell et al., 2007). In fact, on short time scale (a few hours or less) the driver variations described by these formulas are predominantly controlled by the variation of IMF BZ magnetic field component, and the above mentioned combinations highly correlate to each other. In the following, we adopt the approximation for the driver to be in the form EKL = VSW B sin 2 ( θ /2), first suggested by Kan and Lee (1979) and thereafter confirmed, for example, by Troshichev et al. (1988) using PC index and by Grocott et al. (2009) based on statistics of cross -polar cap potential.

In most studies the authors use a cross -correlation method to find the optimal time lag between time shifted data intervals (using either 2 -or 6 -hr -long data segments, with data at ~1 -min time resolution) and use the coefficient of linear correlation (correlation coefficient [ CC ]) to characterize the similarity of variations (e.g., Crooker et al. (1982), Kelly et al. (1986), Zastenker et al. (2000), Collier et al. (1998, 2000), Richardson and Paularena (2001)). In general the proportion of ' good correlation ' events in the magnetic field (with CC &gt; 0.8) was about 24% (for 2 -hr intervals in Crooker et al., 1982) to 30 -40% (for 6 -hr intervals in Richardson &amp; Paularena, 2001), compared with 10 -20% data showing a ' poor correlation ' ( CC &lt; 0.5). Several factors have been identified, which influence the similarity of variations. The most important physical factors include the SW inhomogeneity (characterized by the spacecraft distance from the Sun -Earth (SE) line, RYZ , in comparison to statistical IMF correlation scale) and the magnetic field cone angle (the angle between vector B and X axis of the Geocentric solar magnetosphere (GSM) coordinate system), with smaller influence coming from the time evolution of SW structures (e.g., dependence on spacecraft differences in X -coordinate) and some other effects. As concerns the typical inhomogeneity scale, for the IMF components the scale lengths perpendicular to the flow were about 45 RE (Richardson &amp; Paularena, 2001), with scale length defined as a distance on which the average CC value degrades by 0.1. Larger scales were observed for plasma parameter variations compared to the magnetic field. The CC s were on average significantly larger (by 0.1 -0.2) when the IMF direction was perpendicular to X (in Geocentric solar ecliptic coordinate system, GSE), compared to radial IMF case. These dependencies were confirmed by other authors who used a different measure to quantify the CC degradation, namely, a number ratio of ' good ' correlation events to ' bad ' correlation events (Collier et al., 1998, 2000; Crooker et al., 1982). No clear changes of correlation were reported for small distances perpendicular to SE line (at Δ RYZ &lt; 20 -30 RE according to Crooker et al., 1982, and Richardson &amp; Paularena, 2001). In addition, all authors noticed that the correlations were higher when the IMF variability was high, which partly may correspond to the signal/noise ratio aspect of the correlation method.

The accurate determination of the propagation time delay from L1 to the Earth, in the presence of interplanetary inhomogeneities of different types and sizes, with variable phase fronts, and so forth, is a nontrivial task. Whereas a number of methods of determining the phase fronts have been tested and proved to work well in specific situations (see, e.g., Jackel et al., 2013; Mailyan et al., 2008; Weimer &amp; King, 2009, for examples of recent efforts), a massive testing sometimes provided a mixed result showing that although statistically, there is almost no difference between the flat propagation and delay times used in OMNI, there are times when the propagation estimates can be substantially different (Case &amp; Wild, 2012).

In combination, the inhomogeneity of the SW, the uncertainties in the time delay estimation together with other factors may significantly corrupt the predicted SW parameters as compared to the SW and IMF, which actually interact with the Earth's magnetosphere. De facto the OMNI database appeared to be the main resource of information about SW variations for various kinds of studies, and it is often used for studies and modeling of specific events in which the cost of inaccurate driver characterization can be large (Ashour -Abdalla et al., 2008). In these cases, the questions about ' Which (and how many) data in OMNI database are not accurate (means, do not correspond well to the real drivers)? ' and ' Which methods can help to identify the bad (or good) data? ' are worth studying.

In this paper we investigate these problems in two aspects. First, in section 3, we study a large database of the Geotail spacecraft observations in the SW near the nose of the bow shock and compare them with the OMNI data. Although looking somewhat similar to previous two -spacecraft studies, in this analysis we shall also

<!-- image -->

analyze the question about how many good/bad data exist in the OMNI database. Here we mostly use the standard cross -correlation method and two different metrics to analyze observations made in the vicinity of the SE line by Geotail, taking advantage of the large database available for years 1997 -2016. Also, in addition to previous studies, we discuss the noise in the database. We shall also analyze the SW driver proxy for the magnetosphere ( EKL ) as given by OMNI and Geotail data (section 4).

In section 5, we explore the possibility to evaluate the quality of OMNI data. We analyze the cross -correlation between the PC index (ground -based polar cap magnetic index after Troshichev et al., 1988) and EKL SWdriver computed using OMNI database. The idea behind such comparison is that the PC index, which has been constructed to characterize the intensity of twin -vortices global magnetospheric convection, is known to show a prompt response and high correlation to the SW driver, particularly EKL (Maggiolo et al., 2017; Newell et al., 2007; Troshichev et al., 1988). Even more, the correlation between polar cap magnetic perturbations and EKL in the SW has been used in the procedure of PC index derivation to correct for seasonal and UT variations of effective ionospheric conductivity in the polar cap (see, e.g., Troshichev et al., 2006), so the PC is often considered as a possible ground -based proxy for EKL parameter in the near -Earth SW. To test PC capability as data quality estimator, we again compare its results with the data quality estimation based on Geotail -OMNI comparison. We discuss the results in the section 6.

## 2. Data

The OMNI database (omniweb.gsfc.nasa.gov) is well known by the space weather researchers being the main source of SW data. This high -resolution (1 -and 5 -min) data set is a compilation of records made on ACE, WIND, and IMP -8 spacecraft. The data are time shifted from the spacecraft position to the bow shock nose, assuming the SW is organized in series of consecutive flat phase fronts. The propagation of these fronts relative to the SW flow is ignored. See more details in King and Papitashvili (2005) and website at https:// omniweb.gsfc.nasa.gov/html/HROdocument.html. In this study, we operate with 1 -min OMNI magnetic field and SW flow speed data during 1997 -2016, which originate from the L1 point: WIND about 51% and ACE 49%. Very rare cases with data from IMP -8 having geocentric orbit were excluded from the analysis. Gaps in magnetic field and flow speed data account for 7% and 20% of the total time coverage, respectively.

Because of small (~4 RE) size of the SW flow tube directly interacting with the magnetosphere, for the verification of the OMNI data it is crucial to use actual measurements the point where distant spacecraft data are time shifted, that is, bow shock nose. Among all available spacecraft Geotail provides the most long -term and large database at this preferred location. Launched in 24 July 1992, into an orbit with 30 RE apogee in the magnetospheric tail and 10 RE perigee, this spacecraft continues to operate. We analyze 64 -s magnetic field measurements made by Geotail Magnetic Field Experiment (Kokubun et al., 1994) available at http://cdaweb.sci.gsfc.nasa.gov (the GE\_K0\_MGF data set). Components of the magnetic field vector were recalculated to the 1 -min step using linear interpolation between two nearest points. We use a semiempirical model of the bow shock surface by Wu et al. (2000) to select SW segments of the Geotail orbit when it was outside the model bow shock by more than 1RE. An example of SW intervals is shown in Figure S1 in the supporting information. These intervals account for 23.7% of the Geotail data in 1997 -2016. Geotail key parameter data are known to include the offsets in BZGSE IMF component (King &amp; Papitashvili, 2010). They were corrected by subtracting the annual offsets between OMNI and Geotail data (see Figure S2 for illustration). No scale factor was applied to cross -normalized OMNI and Geotail data, as we suggest that this does not significantly affect the correlation analysis. In this study, we consider Geotail data when the spacecraft was close to the bow shock nose -no more than 10 RE in the YZ plane. These periods account for 71% of SW Geotail data.

## 3. Evaluation of OMNI Data Quality by Comparing OMNI and GEOTAIL IMF Data

Similar to Crooker et al. (1982), we compare data in a 120 -min time window. Using 60 -min time step, we obtained 10,409 intervals where more than 90 points are available from each data sets. Unlike Crooker et al. (1982) who computed a hybrid CC (square root of the average squares of the CC s of three components and magnitude), we use vector correlation, which provides a single parameter characterizing a similarity

<!-- image -->

<!-- image -->

CC

Figure 1. (a) Distribution and cumulative distribution function ( cdf ) of the cross -correlation time delays between OMNI and Geotail interplanetary magnetic field data; red curve shows the average correlation coefficient ( CC ) for each bin; (b -d) distributions of the correlation coefficients and prediction efficiency ( PE ) indices between OMNI and Geotail data with cdf for each GSM component separately (b and c).

between OMNI and Geotail data series (e.g., equation (11) in Tsyganenko &amp; Sitnov, 2005). Namely, for the vector quantity (B) the Pearson linear CC can be generalized to be

<!-- formula-not-decoded -->

where X , Y , or Z are the IMF components (GSM); i is the minute within 120 -min interval; apostrophe signifies quantities calculated from OMNI data, and dBi s are the deviations from the average value of X , Y , or Z IMF components.

To estimate the quality of the time shifting made from L1 to the bow shock, we check the cross -correlation between OMNI and Geotail within +/ -30 -min lag time. Figure 1a shows the distribution of the delays, Δ TOM/GT = TOM -TGT . As shown by cumulative distribution function curve (cdf, black curve) the majority (70%) of CC peaks concentrates within -1 -to 6 -min delays, and the average correlation for this interval is high, being about 0.75. A small positive shift is because Geotail stays ahead of the bow shock and records SW before its contact with the bow shock. The correlation degrades at long delays (red curve in Figure 1 a): for Δ TOM/GT more than 6 min or less than -1 min, average CC is only 0.56. That means large delays may be unphysical in origin, appearing due to a weak correlation between two signals.

High linear correlation does not imply the identity of data series but rather indicates similarity in their variances. When the variance is weaker than the noise, the correlation may be useless for comparing two signals. In such cases another metric, the prediction efficiency ( PE ) index (see, e.g., Pulkkinen et al., 2011) is a more appropriate indicator:

<!-- formula-not-decoded -->

Here XOM and XGT are OMNI and Geotail values. The PE index may take negative values when the difference between data sets surpasses the variance of the experimental data. PE equal to zero suggests that only the means of the analyzed data coincide. In these cases ( PE &lt; 0) the test data are considered to be of poor

<!-- image -->

Figure 2. Distributions of good (blue) and bad (red) cases depending on the amplitude of the magnetic field variance (a) and on the OMNI spacecraft distance from the Sun -Earth line (b); black curves denote ratios of poor/good cases; (c) distribution of cases with σ B &lt; 1.3 nT or RZY &gt; 65 RE for each year. PE = prediction efficiency.

<!-- image -->

quality when PE takes negative values. For better visibility in Figure 1d, we do not show PE lower than -1 (8.5% of total).

For the most part of our database, the correlation is relatively high, but a significant amount of poor cases is also presented. Looking separately for different components in Figures 1b and 1c, the cumulative distribution functions show that the best correlation is obtained for BZ (green curve), slightly lower for BY (magenta), and the lowest for BX component (blue). These results agree with the previous studies. So far, the most extensive database was studied by Richardson and Paularena (2001), who compared the IMF and plasma measurements at two spacecrafts using 6 -hr -long intervals. Using a convention that the correlation between signals is poor when CC &lt; 0.5 and very good when CC ≥ 0.8, we found 24% (20% compare to Richardson &amp; Paularena, 2001), 16% (12%), and 14% (13%) of bad data for BX , BY , and BZ , respectively. The amount of very good correlation events is also similar: 31% (34%), 43% (43%), and 46% (45%) in BX , BY , and BZ data, respectively. The median vector correlation and PE values, 0.74 and 0.20, are comparable to the BY result.

Figure 1d shows the relationship between two metrics, CC and PE , and reveals that zero PE values correspond approximately to CC within 0.5 -0.7 range. Note the sharp upper boundary, which indicates that there are no cases with positive PE when CC , is low. There are also almost no cases with high CC and negative PE . So we could use only CC score to filter poor and very good data. For intermediate CC values, between 0.5 and 0.8, almost one third of cases has negative PE and should be rather classified as being bad.

The numbers in Figure 1d indicate the fraction of points in the areas shown by the dashed lines. For the entire data set we have about 37% intervals when OMNI and Geotail magnetic data closely match to each other (upper right quadrant in Figure 1d) and about 31% when the correlation is relatively good ( PE ≥ 0 and CC between 0.5 and 0.8, upper central quadrant). For the rest 32% intervals the signals disagree in their variance or/and in their mean values. Among them 18% of cases strongly disagree, CC is below 0.5, and in other 14% cases the offsets between signals exceed the variance.

Low CC and PE could be due to a weak variance of the analyzed parameter (Crooker et al., 1982). In Figure 2a, we show the distributions of poor and good cases depending on the standard deviation σ B, which is computed as a square root of the sum of squares of the standard deviations for each IMF component taken at 1 -min resolution. Black curves show ratios between number of poor ( PE &lt; 0, or CC &lt; 0.5) and good ( PE ≥ 0, or very good for CC ≥ 0.8) cases. Both ratios exceed or almost equal to a unity when σ B is lower than ~1.3 nT. This deterioration indicates that the signal -to -noise ratio significantly decreases in case of low σ B. So we cannot define the quality of the corresponding data. For the statistics that are more reliable, we should exclude OMNI data with σ B below 1.3 nT (1,874 cases, i.e., 18.0%). This provides clearer estimates: 41.9% cases with CC ≥ 0.8, 32.7% of cases with 0.5 ≤ CC &lt; 0.8 and PE ≥ 0, and 14.8% cases with CC &lt; 0.5. The rest 10% of cases having moderate CC but negative PE scores are of the questionable quality.

Previous studies pointed out that the correlation between data from two remote spacecraft depends on the distance between them in the plane perpendicular to the SE line. Figure 2b shows distribution of distances RZY between GSE X axis and the OMNI spacecraft (ACE or Wind) for positive (blue) and negative (red) PE . Black curves indicate the number ratio of poor and good cases defined by either CC or PE scores. So for better

<!-- image -->

8

0.8

0.6

'EKL

0.4

0.2

0

0

<!-- image -->

0.2

0.4

12%

24%

6%

I

I

1:

1.

1

CCB

0.6

1

I

I

1

0.8

1

PEB

1

Figure 3. Left: correlation coefficients ( CC ) between vector B by Geotail and in OMNI database versus correlation coefficients and between EKL ; right: same for prediction efficiency ( PE ) indices.

prediction of the IMF in front of the bow shock the distant spacecraft should be located closer to the SE line. The ratios significantly increase when distances are greater than 15 RE, which was not noticed in previous studies, but very few data are left if we exclude such cases. The poor/good ratio further increases and exceeds a unity for RZY &gt; 60 -70 RE; these OMNI data definitely contain a large fraction of incorrect IMF data. In this study, we suggest to exclude OMNI data with RZY &gt; 65 RE to clean the database of inappropriate data. This would cost 1,138 cases lost, i.e., 11% of all database. Note the increased amount of such cases in 2010 -2012, as shown by Figure 2c. We exclude these preknown poor OMNI data and obtain 43.8% (+1.9% increase) cases with CC ≥ 0.8 and 13.4% ( -1.4% decrease) cases with CC &lt; 0.5.

## 4. Evaluation of OMNI Data Quality by Comparing OMNI and GEOTAIL EKL

Whereas correlation analyses and evaluation of statistical quality properties in our and previous studies were done for the IMF data, it is also interesting to provide similar analysis for the parameter EKL , which shows a better control of the magnetic activity in general (and PC index in particular):

<!-- formula-not-decoded -->

where θ is the IMF clock angle in YZ plane. Because of the problems with Geotail plasma measurements and taking into account the long autocorrelation time of SW velocity (44 -hrs, Maggiolo et al., 2017), that is, the variability of EKL on small time scales (minutes to hours) comes mostly from the magnetic field variations, so Geotail EKL were calculated using Geotail IMF, B , and OMNI SW speed, Vsw . The CC and PE indices calculated for the vector B and for EKL are compared in Figure 3. For these plots, we used the data set with a reduced noise obtained by filtering out RZY &lt; 65 RE and σ B ≥ 1.3 nT, altogether 7,759 records. The median values of EKL characteristics are 0.788 and 0.468 for CC and PE in the reduced noise data set, whereas in the original entire data set they were 0.764 and 0.379, respectively.

The plots in Figure 3 show that distribution of the data fractions in poor and good areas (using thresholds at CC =0.5 and PE =0) is very similar for EKL and IMF vector B . This indicates that using EKL as a parameter to estimate OMNI data, we probably do not lose the information regarding the quality of IMF data. This is essential for the next section 3 based on the comparison between EKL and PC index.

## 5. Evaluation of PC Index as Possible Data Quality Estimator

The usage of the IMF spacecraft measurements in front of the bow shock is the direct way of quality evaluation of the OMNI data (and of any measurements made at about L1 point); however, we rarely have such opportunity. It looks attractive to explore other possible tools, particularly, the PC index, which is known to correlate well with SW driver (Myllys et al., 2016; Troshichev et al., 1988) and is routinely available at 1 -min resolution for all years covered by the OMNI database. PC index represents the intensity of the

0%

6%

8%

37%

7%

0%

<!-- image -->

Figure 4. Distributions of the (a) correlation coefficients ( CC ) between PC and EKL , solid curves indicate average CC for each bin; (b -d) distributions of the correlation coefficients and prediction efficiency indices between EKL and PC index (choice between PCN or PCS depends upon which of them gives best results).

<!-- image -->

twin -vortices (DP2) current system in the center of the polar cap. It is calculated from the horizontal geomagnetic variations in the polar cap. The reference levels as well as seasonal and diurnal variations are removed by calibrating the index to the simultaneous EKL values (Troshichev et al., 2006). In this study, we utilize AARI version of the PC index calculated for both northern Thule ( PCN ) and southern Vostok ( PCS ) stations in 1997 -2016, which are available online at the Polar Cap Magnetic Index website (http://pcindex.org).

Like in section 2, we compare OMNI EKL and PC when more than 90 1 -min data points of each variable are available in 120 -min window. This gives us 122,667 cases. The PC index responds to the variations in EKL with 20 -to 25 -min delay (Maggiolo et al., 2017; Myllys et al., 2016; Troshichev et al., 1988). So the cross -correlation analysis is performed within -5 -to 45 -min range of time delays. Figure 4a shows histograms of the peak cross -CC s between OMNI EKL and PCS (blue line) or PCN (red line). In both hemispheres the distributions are very similar, with ~60% of the delays being between 10 and 30 min, that is, between the cdf inflection points. Peak CC ~ 0.61 values are observed within Δ T ~ 17 -20 min for PCN and at slightly wider range Δ T ~ 14 -22 min for PCS . Outside these ranges the median CC falls, indicating that in the corresponding cases the PC index is contaminated by the noise or contains wrong data records.

Figures 4b and 4c show distributions of the peak CC and PE . Here we demonstrate distributions for highest CC (and PE ) values obtained for either PCN or PCS . Median CC is about 0.66, and median PE is -0.66, which are noticeably lower than CC and PE obtained after comparing EKL from OMNI and from Geotail ( CC =0.76 and PE = 0.38 for all unfiltered 10,846 cases). Only 30% of all PCN and PCS records have positive PE . Note also significant amount of negative PE with CC &gt; 0.5 (Figure 4b). This may indicate the presence of considerable offsets between PC and EKL . The offsets appear due to a number of factors including the PC index derivation problems, like base -level offsets and appearance of negative PC values (whereas EKL is always positive). Since we cannot expect the exact match between EKL and PC absolute levels, in the following, we shall concentrate on analyzing the behavior of variances given by the CC s.

Northern PCN and southern PCS indices may sometimes show different behavior contributed, for example, by the auroral oval conductance changes (which affect differently the perturbation in the dark and illuminated polar caps) or by the effects of IMF BY or positive BZ ; see, for example, chapter 11 of Troshichev (2017). However, there is no significant difference between CC distributions for PCN and PCS . So in the further analysis in each data record we choose those of two PC records (south or north), which has the higher CC value, that is, those most relevant for the analyzed time interval.

<!-- image -->

Figure 5. Distributions of cases with poor (red) and good (blue) correlation between OMNI EKL and PC index depending on σ EKL.

<!-- image -->

As we have shown in the previous section, weak variance in the IMF affects the reliability of correlation analysis. In Figure 5, we evaluate the sensitivity of PC/EKL correlation to EKL variance ( σ EKL). The amount of poor data is noticeably larger for small σ EKL, and it sharply decreases with the growth of σ EKL until the 0.15 -mV/m value, which we choose as a cutoff parameter. This helps us clean the data set from the events in which low correlation does not indicate the physics but rather reflects the low signal/noise ratio. About 80% of the initial data set (98,454 cases) meets this criterion. Because EKL strongly depends on B , the percentage of cases with high σ EKL is almost the same as for the cases with high σ B (~82%).

Distribution of the CC s for EKL between data from OMNI and Geotail ( CCOM/GT ) against the CC s between OMNI EKL and PC index ( CCOM/PC ) for the events with σ EKL &gt; 0.15 mV/m is presented in Figure 6a (7,498 cases). The correspondence between these scores is quiet poor. Though in the presence of data scatter there are very few points (7%) in the area with CCOM/PC ≥ 0.5 and CCOM/GT &lt; 0.5. This indicates that good OMNI data can be recognized as having high CCOM/P C values, so PC index can serve as a rough OMNI database validator. However, the opposite is not true: Under good OMNI data (high CCOM/GT ), one can find many points with low CCOM/PC value -14% of all cases or ~19% of only good OMNI data. This is the amount of good data that would be lost if we filter cases with CCOM/PC &lt; 0.5.

Figure 6b shows distributions of cases with low CCOM/GT &lt;0.5 (red) and high CCOM/GT ≥ 0.5 (blue) depending on the CCOM/PC . Median CCOM/PC values for distributions of poor and good cases are 0.480 and 0.721, respectively. Black curves indicate that the ratios of poor to good cases decrease for greater CCOM/PC . Although the amount of poor cases as classified by CCOM/GT for EKL decreases more rapidly than for IMF vector B , two ratios are very close.

The rate of decrease saturates for CCOM/PC &gt; 0.7, and this value may be considered as a cutoff parameter to clean the OMNI database. This gives us 6% of poor ( CC &lt; 0.5 obtained for vector B ), 27% of good (0.5 ≤ CC &lt; 0.8 and PE ≥ 0), and 57% of very good ( CC ≥ 0.8) data left at the cost of almost 60% OMNI data lost (including those with low EKL variability). Choosing 0.5 (or 0.6) as a cutoff CCOM/PC value gives us 9 (8), 31(30), and 49 (52) % of poor, good, and very good data left, respectively. The amount of data lost would be significantly lower, about 37 (47) %. So we indeed could use PC index to improve the quality of the OMNI IMF database, but the cutoff CCOM/PC values should be defined individually depending on the objectives of the study.

<!-- image -->

CCOMIPC

CCOMIPC

Figure 6. (a) Correlation coefficients ( CC ) between EKL data from OMNI and Geotail ( CCOM/GT ) against the correlation coefficients between OMNI EKL and PC index ( CCOM/PC ). (b) Distributions of cases with low CCOM/GT &lt; 0.5 (red) and high CCOM/GT ≥ 0.5 (blue) depending on the CCOM/PC ; black curves indicate the poor to good data ratios considering EKL (yellow dots) and interplanetary magnetic field B (green dots).

<!-- image -->

## 6. Discussion

With no doubts, the OMNI database is a great resource for space weather and magnetospheric studies. Predictability of magnetospheric dynamics and of space weather in general strongly depends on the actuality of the available SW and IMF data (Ashour -Abdalla et al., 2008), and this poses a specific difficult question about a quality of any specific data in the OMNI database. There are a few physical factors that could provide a difference between the parameters acting on the subsolar bow shock and those in the OMNI database. First, the size of the SW flow tube, which directly interacts with the dayside magnetosphere during the reconnection process, is as small as being only four RE (Burke et al., 1999). The intrinsic SW inhomogeneity and the evolution of the particular SW structure between its observation and the Earth's bow shock contact represent a one important source of errors, being most important for the distant observations near the L1 point. The propagation errors and foreshock effects can modify the pristine SW variations; the latter effect is important for near -Earth spacecraft observations. Wrong derivation of the SW phase fronts and technical problems could provide additional sources of errors.

Being in qualitative agreement to previous studies, our study provides a quantitative estimation of these effects. Particularly, we found that within period of study, 1997 -2016, OMNI contains roughly 17% of records being strongly contaminated by the IMF inhomogeneous structure, that is, those records with large fraction of wrong IMF data. For example, when doing statistical (magnetospheric) models, these periods should be deselected to suppress the noise in the data. We also used another metric, the PE that is sensitive to the offsets between values. This allows us to distinguish another 13% of data for which the offsets between OMNI and Geotail exceed the variance of the signal, i.e., having negative PE scores. The quality of these data depends on whether the subject of study requires the exact IMF values or investigates only the variability.

In about 20% of data, the low IMF variability makes impossible to diagnose the correspondence to actual data. These records may not be wrong, and their removal would eliminate some specific SW states. But they should be excluded if we are interested in making the true statistics of actual data as they appear in OMNI. We found that the portion of poor cases (with low correlation between OMNI and Geotail) is equal or exceeds the portion of good cases when IMF variance ( σ B ) becomes lower than 1.0 -1.5 nT, which should be considered as a noise amplitude when analyzing 2 -hr intervals of the IMF data. We estimate that the actual percentage of poor IMF data is about 15% and another 10% having negative PE . The majority of the analyzed cases (75%) have good quality ( CC ≥ 0.5 and PE ≥ 0), and almost half of them have CC ≥ 0.8. Considering longer time intervals, the amount of poor data would certainly decrease with weaker influence of small -scale inhomogeneities.

The IMF data measured far from the SE line are often wrong. An increase of poor to good ratio with greater RZY distances shown by Figure 2b looks very similar to the previous results found by Collier et al. (2000), who define the IMF scale length as being about 100 RE. Here we define the scale length of the IMF to be about 65 RE, because for greater scales the percentage of cases with low CC and PE significantly increases. As we see in Figure 2b, the spacecraft used in the OMNI data set rarely stayed at RYZ &gt; 65 RE (11% of the analyzed data). The corresponding cases certainly contain wrong IMF data, but the overall improvement of the OMNI data set is very small: plus 1.9% of very good data and minus 1.4 of poor data. However, we should not ignore the information about the spacecraft distance from the SE line. As shown by Figure 2c, the spacecraft trajectories vary, and there are years (2010 -2012) when the IMF scale length is crossed far more often.

Another possibility to filter wrong IMF data could be to compare SW driver EKL with the ground -based PC index of geomagnetic activity. In Figure 3, we demonstrate that high (low) correlation between OMNI and Geotail EKL values corresponds to high (low) correlation between IMF vectors. Therefore, we can estimate OMNI data by comparing EKL , or when the in situ EKL data in front of the bow shock nose are absent, we could think of using the PC index data, which are almost continuously available since 1975 in the Northern hemisphere and since 1992 in the Southern hemisphere.

However, using PC index as a validator is problematic. First, the absolute levels of EKL and PC often disagree resulting in almost 70% of cases having negative PE (Figure 4c). Therefore, we can use only correlation analysis, and it would be impossible to identify cases where CC is high despite significant offsets between signals

<!-- image -->

(about 10% of data, Figure 4d). For reliable CC estimates, we have to choose intervals with high variability, σ EKL &gt; 0.15 mV/m.

Another problem is not sufficiently high correlation of PC index with its SW driver. In Figure 6a, 14% of cases with high -quality data ( CC EKL OM = GT ≥ 0.5) have low correlation with PC index, and, therefore, they would be missed without in situ EKL measurements. Several factors affect PC index, preventing it from being an exact EKL proxy (including perturbations due to strong IMF BY and NBZ ionospheric currents and different contributions of oval conductivity -related field -aligned current systems in sunlit and dark polar caps -see a more detailed discussion of those effects in Troshichev, 2017).

Nevertheless, we can distinguish good OMNI data by choosing 2 -hr intervals with the above restrictions: RZY &lt; 65 RE (12% of data lost), σ EKL &gt; 0.15 mV/m (another 15% of data lost), and CCEKL/PC ≥ 0.6 (another 25% of data lost). According to our estimates, so selected data would be very good, relatively good, and poor in 52%, 30%, and 8% cases, respectively. Another 9% cases contain errors in absolute values. Therefore, by sacrificing half of the data the proportion of very good/good/poor data improves from 42%/33%/15% to 52%/30%/8%. A more strict restriction, for example, CC EKL OM = PC ≥ 0.8, would increase these ratios to 66/22/ 4%, but in the cost of 80% of data lost.

## 7. Conclusions

The OMNI database is mostly formed by the measurements made at around Lagrange point L1, which may differ from the SW in the vicinity of the bow shock nose. To test the quality of the high -resolution OMNI database compiled mostly from ACE and WIND data, we compared the 2 -hr intervals of 1 -min IMF data with Geotail measurements in front of the bow shock, that is, when the YZ distance from the bow shock nose was lower than 10RE (10,409 cases in 1997 -2016).

We use the Pearson linear CC generalized to the vector form (Tsyganenko &amp; Sitnov, 2005). The correlation between OMNI and Geotail data reaches maximal values mostly around -1 -to 6 -min delays, which suggests the time shifting of measurements at L1 is done correctly. We also use the PE , which detects the offsets between signals. Using both of these metrics helps more objective characterization.

In agreement with previous studies we found that some (20% in our data set) low correlation and PE parameters are due to low IMF variability, that is, low signal -to -noise ratio problem. These records may not be wrong, but simply the tools (metrics) fail. For true statistics we remove cases with IMF variance lower than 1.3 nT and divide the analyzed intervals into four groups: 42% of very good data ( CC ≥ 0.8), 33% of relatively good data (0.5 ≤ CC &lt; 0.8 and PE ≥ 0), 10% of data having correct variability but wrong absolute values (0.5 ≤ CC &lt; 0.8 and PE &lt; 0), and 15% of poor data ( CC &lt; 0.5).

We confirm that the prediction quality of actual IMF degrades continuously with increasing distance of spacecraft used in the OMNI data set from the SE line. The amounts of poor and good predictions become nearly equal when this distance exceeds 65 RE. Those intervals, about 10 -15% of database, can be easily excluded when doing statistical studies.

The quality of the OMNI IMF data can be verified by comparing always available ground PC index of geomagnetic activity and its SW driver EKL . Despite some problems due to mismatch between these quantities, PC index can serve as a filter of good OMNI data. If we exclude data with low correlation ( CC &lt;0.6) between OMNI EKL and PC the percentage of very good data increases from 42 to 52%, while poor cases fall from 14 to 8%. However, half of the data would be lost among which 70% are actually the good quality data. Further investigations are required to improve the potential of PC index as EKL proxy and as an OMNI database validator.

Results of our study can find different applications in the research of SW drivers for space weather and related aspects. Particularly, magnetospheric and ionospheric modelers may benefit from possibility to lower the noise level in the database when doing their statistical studies of SW driver effects. The researches investigating specific events and global simulations would certainly benefit by discarding the events for which the characterization of SW driver is unreliable. Specific details of application always depend on trade -off between data quality and their sufficient amount to reach the goal, so they are not commented here.

<!-- image -->

## Acknowledgments

This work was supported by the Russian Science Foundation Grant 14 -05 -00072. The PC index data are available at the Polar Cap Magnetic Index website (https://pcindex.org/). The OMNI data are available at the SPDF -OMNIWeb Service -Nasa website (https://omniweb.gsfc.nasa.gov/). We thank O. Troshichev for useful discussions.

## Space Weather

## References

- Ashour -Abdalla, M., Walker, R. J., Peroomian, V., &amp; El -Alaoui, M. (2008). On the importance of accurate solar wind measurements for studying magnetospheric dynamics. Journal of Geophysical Research , 113 , A08204. https://doi.org/10.1029/2007JA012785
- Burke, W. J., Weimer, D. R., &amp; Maynard, N. C. (1999). Geoeffective interplanetary scale sizes derived from regression analysis of polar cap potentials. Journal of Geophysical Research , 104 (A5), 9989 -9994. https://doi.org/10.1029/1999JA900031
- Case, N. A., &amp; Wild, J. A. (2012). A statistical comparison of solar wind propagation delays derived from multispacecraft techniques. Journal of Geophysical Research , 117 , A02101. https://doi.org/10.1029/2011JA016946
- Collier, M. R., Slavin, J. A., Lepping, R. P., Szabo, A., &amp; Ogilvie, K. (1998). Timing accuracy for the simple planar propagation of magnetic field structures in the solar wind. Geophysical Research Letters , 25 (14), 2509 -2512. https://doi.org/10.1029/98GL00735
- Collier, M. R., Szabo, A., Slavin, J. A., Lepping, R. P., &amp; Kokubun, S. (2000). IMF length scales and predictability: The two length scale medium. International Journal of Geomagnetism and Aeronomy , 2 (1), 3 -16.
- Crooker, N. U., Siscoe, G. L., Russell, C. T., &amp; Smith, E. J. (1982). Factors controlling degree of correlation between ISEE 1 and ISEE 3 interplanetary magnetic field measurements. Journal of Geophysical Research , 87 (A4), 2224 -2230. https://doi.org/10.1029/JA087iA 04p02224
- Grocott, A., Badman, S. V., Cowley, S. W. H., Milan, S. E., Nichols, J. D., &amp; Yeoman, T. K. (2009). Magnetosonic Mach number dependence of the efficiency of reconnection between planetary and interplanetary magnetic fields. Journal of Geophysical Research , 114 , A07219. https://doi.org/10.1029/2009JA014330
- Jackel, B. J., Cameron, T., &amp; Weygand, J. M. (2013). Orientation of solar wind dynamic pressure phase fronts. Journal of Geophysical Research: Space Physics , 118 , 1379 -1388. https://doi.org/10.1002/jgra.50183
- Kan, J. R., &amp; Lee, L. C. (1979). Energy coupling function and solar wind -magnetosphere dynamo. Geophysical Research Letters , 6 (7), 577 -580. https://doi.org/10.1029/GL006i007p00577
- Kelly, T. J., Crooker, N. U., Siscoe, G. L., Russell, C. T., &amp; Smith, E. J. (1986). On the use of sunward libration -point orbiting spacecraft as an interplanetary magnetic field monitor for magnetospheric studies. Journal of Geophysical Research , 91 (A5), 5629 -5636. https://doi.org/ 10.1029/JA091iA05p05629
- King, J., &amp; Papitashvili, N. (2010), One min and 5 -min solar wind data sets at the Earth's bow shock nose. Retrieved from http://omniweb. gsfc.nasa.gov/html/HROdocum.html
- King, J. H., &amp; Papitashvili, N. (2005). Solar wind spatial scales in and comparisons of hourly Wind and ACE plasma and magnetic field data. Journal of Geophysical Research , 110 , A02104. https://doi.org/10.1029/2004JA010649
- Kokubun, S., Yamamoto, T., Acuña, M. H., Hayashi, K., Shiokawa, K., &amp; Kawano, H. (1994). The Geotail magnetic field experiment. Journal of Geomagnetism and Geoelectricity , 46 (1), 7 -22. https://doi.org/10.5636/jgg.46.7
- Maggiolo, R., Hamrin, M., De Keyser, J., Pitkänen, T., Cessateur, G., Gunell, H., &amp; Maes, L. (2017). The delayed time response of geomagnetic activity to the solar wind. Journal of Geophysical Research: Space Physics , 122 , 11,109 -11,127. https://doi.org/10.1002/ 2016JA023793
- Mailyan, B., Munteanu, C., &amp; Haaland, S. (2008). What is the best method to calculate the solar wind propagation delay? Annales de Geophysique , 26 (8), 2383 -2394.
- Myllys, M., Kilpua, E. K. J., Lavraud, B., &amp; Pulkkinen, T. I. (2016). Solar wind -magnetosphere coupling efficiency during ejecta and sheath -driven geomagnetic storms. Journal of Geophysical Research: Space Physics , 121 , 4378 -4396. https://doi.org/10.1002/2016JA022407
- Newell, P. T., Sotirelis, T., Liou, K., Meng, C. -I., &amp; Rich, F. J. (2007). A nearly universal solar wind -magnetosphere coupling function inferred from 10 magnetospheric state variables. Journal of Geophysical Research , 112 , A01206. https://doi.org/10.1029/2006JA012015
- Pulkkinen, A., Kuznetsova, M., Ridley, A., Raeder, J., Vapirev, A., Weimer, D., et al. (2011). Geospace environment modeling 2008 -2009 challenge: Ground magnetic field perturbations. Space Weather , 9 , S02004. https://doi.org/10.1029/2010SW000600
- Richardson, J. D., &amp; Paularena, K. I. (2001). Plasma and magnetic field correlations in the solar wind. Journal of Geophysical Research , 106 (A1), 239 -252. https://doi.org/10.1029/2000JA000071
- Troshichev, O., Janzhura, A., &amp; Stauning, P. (2006). Unified PCN and PCS indices: Method of calculation, physical sense and dependence on the IMF azimuthal and northward components. Journal of Geophysical Research , 111 , A05208. https://doi.org/10.1029/2005JA011402
- Troshichev, O. A., Andrezen, V. G., Vennerstrom, S., &amp; Friis -Christensen, E. (1988). Magnetic activity in the polar cap -A new index. Planetary and Space Science , 36 (11), 1095 -1102.
- Troshichev, O. (2017). Polar cap magnetic activity (PC index) and space weather monitoring. Editions Universitaires Europeennes, (pp. 140).
- Tsyganenko, N. A., &amp; Sitnov, M. I. (2005). Modeling the dynamics of the inner magnetosphere during strong geomagneticstorms. Journal of Geophysical Research , 110 , A03208. https://doi.org/10.1029/2004JA010798
- Weimer, D. R., &amp; King, J. H. (2009). Improved calculations of interplanetary magnetic field phase front angles and propagation time delays. Journal of Geophysical Research , 113 , A01105. https://doi.org/10.1029/2007JA012452
- Wu, D. J., Chao, J. K., &amp; Lepping, R. P. (2000). Interaction between an interplanetary magnetic cloud and the Earth's magnetosphere: Motions of the bow shock. Journal of Geophysical Research , 105 (A6), 12,627 -12,638. https://doi.org/10.1029/1999JA000265
- Zastenker, G. N., Dalin, P. A., Petrukovich, A. A., Nozdrachev, M. N., Romanov, S. A., Paularena, K. I., et al. (2000). Solar wind structure dynamics by multipoint observations. Physics and Chemistry of the Earth, Part C: Solar, Terrestrial &amp; Planetary Science , 25 (1 -2), 25,137 -25,140. https://doi.org/10.1016/S1464 -1917(99)00055 -0