## Solar wind spatial scales in and comparisons of hourly Wind and ACE plasma and magnetic field data

## J. H. King 1

QSS Group, Inc., Lanham, Maryland, USA

## N. E. Papitashvili 2

Space Physics Data Facility, NASA Goddard Space Flight Center, Greenbelt, Maryland, USA

Received 24 June 2004; revised 17 November 2004; accepted 16 December 2004; published 16 February 2005.

[1] Hourly averaged interplanetary magnetic field (IMF) and plasma data from the Advanced Composition Explorer (ACE) and Wind spacecraft, generated from 1 to 4 min resolution data time-shifted to Earth have been analyzed for systematic and random differences. ACE moments-based proton densities are larger than Wind/Solar Wind Experiment (SWE) fits-based densities by up to 18%, depending on solar wind speed. ACEtemperatures are less than Wind/SWE temperatures by up to  25%. ACEdensities and temperatures were normalized to equivalent Wind values in National Space Science Data Center's creation of the OMNI 2 data set that contains 1963-2004 solar wind field and plasma data and other data. For times of ACE-Wind transverse separations &lt;60 RE , random differences between Wind values and normalized ACE values are  0.2 nT for j B j ,  0.45 nT for IMF Cartesian components,  5 km/s for flow speed, and  15 and  30% for proton densities and temperatures. These differences grow as a function of transverse separation more rapidly for IMF parameters than for plasma parameters. Autocorrelation analyses show that spatial scales become progressively shorter for the parameter sequence: flow speed, IMF magnitude, plasma density and temperature, IMF X and Y components, and IMF Z component. IMF variations have shorter scales at solar quiet times than at solar active times, while plasma variations show no equivalent solar cycle dependence.

Citation: King, J. H., and N. E. Papitashvili (2005), Solar wind spatial scales in and comparisons of hourly Wind and ACE plasma and magnetic field data, J. Geophys. Res. , 110 , A02104, doi:10.1029/2004JA010649.

## 1. Introduction

[2] The objective of this analysis is to quantify systematic and random differences in hourly resolution interplanetary magnetic field (IMF) and plasma data from the Advanced Composition Explorer (ACE) and Wind spacecraft. Random differences are studied as functions of the separation between the spacecraft along and across the Sun-Earth direction and of solar cycle phase, and solar wind feature scale sizes are estimated. Study of systematic differences, done as functions of time and solar wind speed, helps one to assess whether cross normalization of one data set to another is needed for joint usage. We have not searched for dependences of differences on flow type (e.g., corotating streams versus coronal mass ejections).

[3] Several prior studies of correlation levels between data from pairs of spacecraft have been performed, typically at resolution higher than hourly [see Collier et al. , 2000;

1 Formerly at National Space Science Data Center, NASA Goddard Space Flight Center, Greenbelt, Maryland, USA.

2 Also at QSS Group, Inc., Lanham, Maryland, USA.

Weimer et al. , 2003, and references therein]. These studies did not address systematic offsets between source pairs.

[4] In preparation of the hourly resolution OMNI 2 data set (briefly described below), the National Space Science Data Center (NSSDC) acquired ACE 4-min IMF data and 64-s electrostatic analyzer plasma data from the ACE Science Center described by Garrard et al. [1998]. The ACE MAG (Magnetometer) and SWEPAM (Solar Wind Electron, Proton and Alpha Particle Monitor) investigations are best described by Smith et al. [1998] and by McComas et al. [1998]. NSSDC also acquired Wind 1-min IMF data and 92-s Faraday cup plasma data from the MFI (Magnetic Field Investigation) team at GSFC and SWE (Solar Wind Experiment)/ion team at MIT. See Lepping et al. [1995] and Ogilvie et al. [1995] for descriptions of the Wind MFI and SWE investigations. No Wind 3DP plasma data have been used in this analysis. Only data taken beyond the Earth's bow shock have been included.

[5] The ACE plasma parameters were based on taking moments of distribution functions. Two sets of Wind ionbased parameters were available, one obtained taking nonlinear fits of observed distributions to anisotropic, convecting Maxwellians and the other based on moment calculations. Only the fits-based Wind set was directly compared to the ACE data, as this set is believed to be

significantly more reliable by the Wind SWE team. However, the Wind fits-based and moments-based parameters are compared to each other herein. Wind SWE data processing is described by Kasper [2002] (dissertation excerpts available at ftp://nssdcftp.gsfc.nasa.gov/spacecraft\_ data/wind/plasma\_swe/2-min/thesis.pdf ).

- [6] For OMNI 2, hourly averages of ACE and Wind IMF and plasma parameters were built from the above-cited 1-4 min resolution data time-shifted from ACE or Wind to Earth. Consistent with the finding of Richardson and Paularena [1998], the time shift assumed that variation phase fronts share an orientation normal to the ecliptic and intercepting that plane midway between the Parker IMF spiral angle and the normal to the Sun-Earth line (refer to Figure 1). It is these hourly averages, web-accessible with display and analysis capabilities along with concurrent IMP 8 and Genesis data from http://nssdc.gsfc.nasa.gov/ftphelper/ merged.html, that form the basis for this paper.

## 2. OMNI 2 Data Set

- [7] Briefly, OMNI 2 is a 41-year (1963-2004), 20-spacecraft compilation of near-Earth, hourly resolution solar wind magnetic field and plasma (proton and, since 1971, alpha particle) data, 1967-2001 energetic proton fluxes, and geomagnetic activity indices (Kp, Dst, AE) and sunspot number. Additional computed parameters are plasma flow pressure, electric field ( V -B ), Alfven Mach number, and plasma beta.
- [8] The OMNIWeb page at http://nssdc.gsfc.nasa.gov/ omniweb discusses the OMNI 2 data set and its creation in detail. It discusses: (1) the time shifting of 1-5 min resolution ACE, Wind and ISEE 3 data from about an hour upstream to Earth prior to building ''Earth-time'' hourly averages; (2) the data cleaning activities, especially the creation and use of a comprehensive IMP 8 bow shock database [ Merka et al. , 2003]; (3) the comparisons and cross normalizations of data from many spacecraft pairs; and (4) the prioritizations across spacecraft in choosing one source for hours with multiple available sources. It provides access to plots and lists of any OMNI 2 parameters, scatterplots and linear regression fits for any parameter pair, parameter distribution histograms, filtering by value(s) of any parameter(s), and links to all online higher-resolution data contributing to OMNI 2.

## 3. Linear Regression Analysis

- [9] The results presented in this paper are based on linear regression analysis with error in both variables. The algorithms are as given by Press [1986]. Regressions were performed for hourly Wind and ACE flow speeds and magnetic field magnitude and GSE Cartesian components. Rather than take similar regressions for plasma proton densities and temperatures, however, we chose to take regressions in (base 10) logarithms of densities and temperatures owing to the more log normal distributions of these parameters.
- [10] With a generic ''x'' representing any of the ACEmeasured physical parameters just identified, and ''y'' representing equivalent Wind measurements, we take as our model that y = a + bx. For each run, we have a series of
3. x(i), y(i) values. Further, we take the standard deviations, s x(i) and s y (i), in the hourly averages (i.e., in the x(i), y(i) values) for use in the weighting factors of the regression equations.
- [11] The chi-square function whose minimization yields the values of a and b in the assumed linear relation between x and y is:

Figure 1. Schematic of the passage of a solar wind variation phase plane over ACE, then over Wind. Inertial coordinate system coincides with GSE at time t 0 when the plane passes ACE. Solar wind carries the phase plane (shown bounded only for convenience) approximately in the -X direction with speed V . Phase plane is assumed normal to the ecliptic and is assumed to intersect the ecliptic ( X -Y ) plane at an angle midway between the Parker spiral angle (shown with the B vector) and the Y axis direction. The phase plane is shown at two time points, t 0 and t 1. Plane crosses ACE at t 0 . Between t 0 and t 1 , as the plane is convecting, Wind moves with the Earth's rotation about the Sun. Plane crosses Wind at time t 1 . Impact parameter, labeled ''IP,'' is the length of the Y -Z plane projection of the vector joining ACE at t 0 and Wind at t 1 .

<!-- image -->

n

o

n

<!-- formula-not-decoded -->

The weighting factors, w(i), are 1/( s y (i) 2 + b 2 s x (i) 2 ).

- [12] It is useful to note that with this weighting, we are counting most heavily those hourly averages with the least natural variability during the relevant hours. This is most appropriate for assessing systematic differences because the possible errors in ''Earth time'' hourly averages (built from higher-resolution data time-shifted using the previously discussed simplified time-shift approach) are likely to be greater for times of more natural temporal variability of physical parameters than for very quiet and uniform solar wind conditions.
- [13] The linear regression equations of Numerical Recipes provide, in addition to values of a and b, also values for the uncertainties in a and b, the chi-square function and the crosscorrelation coefficient (Cr). We have modified the code to

o

additionally compute a measure D of the spread of points about the y = a + bx line as:

 



<!-- formula-not-decoded -->

More precisely, D is the root weighted mean square difference between the hourly averaged Wind-measured parameter value (y(i)) and the concurrent but normalized ACE-measured parameter value (a + bx(i)). Owing to the heavier weighting of quieter hours, this measure of the scatter of data points (as in a scatterplot) about the best fit regression line underestimates the scatter one would compute with unweighted averaging.

- [14] There are four ''filters'' we use in performing regressions of parameter pairs. We can filter against the numbers of fine-scale points in each hourly average, to ensure that the hour's coverage exceeds some level and that we do not compare hourly averages based on data taken only during limited and possibly different parts of the hour. We can filter by time span and by flow speed range. Finally, we can filter against the Wind-ACE Impact Parameter (IP), which we define as the distance by which a downstream spacecraft misses seeing a plasma element previously seen by an upstream spacecraft, assuming a 390 km/s radial plasma flow and allowing for Earth's  30 km/s orbital motion; refer to http://nssdc.gsfc.nasa.gov/ftphelper/ impact.html and the schematic in Figure 1. (During the 1998-2001 period of this analysis, the plasma flow speed occurrence distribution was maximal and nearly equally (  5.6%) in 380-390 and 390-400 km/s bins. Medians and averages were 412 and 430 km/s.) Note that the maximum ACE-Earth impact parameter for an assumed 390 km/s solar

Figure 2. Scatterplot of Wind Bz hourly averages (7635 points from 1998 to 1999) versus concurrent ACE averages. Best fit linear regression equation is shown at the top of the plot. Quantity Cr is the correlation coefficient.

<!-- image -->

Figure 3. Similar to Figure 2 but for log density (10,235 points from 1998 to 2001). Apparent digitization in the logdensity plot results from OMNI's use of F6.1 as the format for densities.

<!-- image -->

wind is about 60 RE . Recall that for time shifts of field and plasma parameter values, we used observed flow speeds and not assumed constant speeds as used in the IP calculations.

- [15] In all our analysis, we set the fine-scale points filter to ensure that each hourly average has at least 75% of the possible coverage. The IP filter is set to various values in various runs, although most runs use IP &lt; 60 RE . For these conditions and for all time and flow speeds, we have available for analysis 7638 hours of concurrent Wind and ACEIMFdata from the years 1998 to 1999 and 10,235 hours of concurrent plasma data from the years 1998 to 2001.
- [16] By way of orientation of the reader to our analysis and results, we show in Figures 2 and 3 scatterplots and best fit regression lines for the parameters Bz and the logarithm of the density (log N ) for all speeds and available times, but for IP &lt; 60 RE . For Bz the best fit line is Bz (Wind) = 0.046 (±0.010) + 0.993 (±0.003)  Bz (ACE). The correlation coefficient is 0.97 and D (defined above) is 0.480 nT. Neglecting the uncertainties in the slope and intercept, we compute that any systematic difference (divergence between best fit line and the line y = x) between Wind and ACE Bz values is less than 0.1 nT over the Bz range   8 to + 21 nT. On the other hand, there is an irreducible random difference (D) between Wind Bz hourly averages and concurrent, normalized ACE Bz values of almost 0.5 nT.
- [17] For log N , the best fit line is log N (Wind) =   0.108 (±0.004) + 1.065 (±0.005)  log N (ACE). The correlation coefficient is 0.97 and D is 0.059. This is equivalent to N (Wind)/ N (ACE) = 0.78  N (ACE) 0.065 as a systematic offset. This says that N (Wind)/ N (ACE) ranges from 0.82 to 0.95 as N (ACE) ranges from 2 to 20 cm   3 and that N (Wind)/ N (ACE) is systematically different than unity by &lt;10% over the N (ACE) range 9-196 cm   3 . Relative to

Figure 4. Means and standard deviations of Wind and ACE Bz values in 20 bins of equal Bz (ACE) width, defined between the minimum and maximum ACE values. Equation for the best regression fit (the straight line) is shown at the top of the plot. Vertical and horizontal bars show the standard deviations in the bin averages. Histogram shows the numbers of points in the bins, with its scale on the right vertical axis.

<!-- image -->

random differences, we have log N (Wind)  log N (ACEn) ± 0.059, which is equivalent to saying that the relative random difference in N (Wind) and N (ACEn) is ( N (Wind)   N (ACEn))/ N (ACEn) = 10 0.059   1.0 = 15%. [ N (ACEn) denotes the normalized value of N (ACE).]

Figure 5. Similar to Figure 4 but for log density.

<!-- image -->

Table 1. Regression Fit Parameters for Various IMF and Solar Wind Variables

| P     | a              | b             | D         |   Cr |
|-------|----------------|---------------|-----------|------|
| j B j | 0.018 ± 0.014  | 0.991 ± 0.001 | 0.221nT   | 0.99 |
| B x   | 0.111 ± 0.007  | 0.991 ± 0.002 | 0.456 nT  | 0.97 |
| B y   |   0.009 ± 0.008 | 1.000 ± 0.002 | 0.435 nT  | 0.98 |
| B z   | 0.046 ± 0.010  | 0.993 ± 0.003 | 0.480 nT  | 0.97 |
| V     |   1.621 ± 0.691 | 1.008 ± 0.001 | 4.41 km/s | 1    |
| log N |   0.108 ± 0.004 | 1.065 ± 0.005 | 0.059     | 0.97 |
| log T |   0.452 ± 0.052 | 1.098 ± 0.011 | 0.105     | 0.94 |

[18] The clustering of points in Figures 2 and 3 makes it difficult to see whether there are any hidden trends. Accordingly we present Figures 4 and 5 which are based on the same data, but wherein we have taken 20 bins along the x axis (i.e., in ACE Bz and log N values) and have computed means and simple standard deviations in those means. It is clear that in both cases, the means follow the best fit regression lines very closely except for extreme density values where there are very few points. One may also see from Figure 5 that except for a little asymmetry, the distribution of log N values is approximately normally distributed.

[19] Table 1 shows the results for all the geophysical parameters for the same time and IP conditions as for the results just displayed and discussed for Bz and for log N . These and additional results will be further discussed in the following sections on systematic and random differences between Wind and ACE parameters.

## 4. Systematic Differences

[20] We begin the assessment of the systematic differences between Wind and ACE parameters by a study of the data of Table 1. Consider first magnetic field magnitude and components. The systematic differences between the Wind and ACE IMF intensity is less than 0.1 nT over the range 0 to 13 nT. The corresponding ranges over which the systematic differences between Wind and ACE are less than 0.1 nT for the Bx , By and Bz components are 1 to 23 nT,  1 to + 1 and   8 to 21 nT, respectively.

[21] The systematic differences between the Wind and ACE IMF intensities are less than the random differences in the intensity, as expressed by the D parameter of Table 1, over the range 0-26 nT. The corresponding ranges over which the systematic differences between Wind and ACE are less than the random differences for the Bx , By and Bz components are   40 to 64 nT,   8 to +8 and   60 to 72 nT, respectively. These are the ranges in which almost all IMF values occur. Accordingly no cross normalizations of IMF data between Wind and ACE were performed in creating the OMNI 2 data set.

[22] Consider next systematic differences between Wind and ACE plasma parameters. For solar wind speed, Table 1 shows a random difference of  4.4 km/s. The flow speed range over which the systematic difference between Wind and ACE values is less than 4.4 km/s is 0 to  750 km/s, which includes the range in which most flow speed values are observed. No flow speed cross normalizations were performed in creating OMNI 2.

[23] Systematic differences in Wind and ACE densities were introduced in the preceding section, as integrated over

Table 2. N (Wind)/ N (ACE) Values

|                  |   N (ACE) Value |   N (ACE) Value |   N (ACE) Value |   N (ACE) Value |
|------------------|-----------------|-----------------|-----------------|-----------------|
|                  |            2    |            5    |           10    |           20    |
| V < 350 km/s     |            0.97 |            1.01 |            1.04 |            1.07 |
| V = 350-450 km/s |            0.83 |            0.86 |            0.88 |            0.9  |
| V > 450 km/s     |            0.82 |            0.82 |            0.82 |            0.82 |

all flow speeds and over the 4-year span 1998-2001. It was shown that N (Wind)/ N (ACE) increases from 0.82 to 0.95 as N (ACE) increases from 2 to 20 cm   3 . There are three further analyses to be made in understanding this result better. The first two seek time and flow speed dependences in the N (Wind)N (ACE) relation. The third assesses the extent to which the N (Wind)   N (ACE) differences may be due to the fact that the densities were produced by moments analysis of the ACE/SWEPAM electrostatic analyzer data at LANL and by taking nonlinear fits of the Wind/SWE Faraday cup data at MIT.

[24] No significant temporal dependence was found in systematic differences between N (Wind) and N (ACE) upon performing four separate regressions for each of the years 1998-2001. Details are given in the OMNIWeb documentation pages.

- [25] There was, however, significant flow speed dependence seen upon performing separate regression analyses for the flow speed bins V &lt; 350 km/s, 350 &lt; V &lt; 450 and V &gt; 450 km/s. Table 2 shows N (Wind)/ N (ACE) ratios in these speed bins at density values of 2, 5, 10 and 20 km/s. While there is fairly good agreement at very low flow speeds, ACE densities exceed Wind densities by 10-18% at the normal and higher speeds observed almost all the time.
- [26] As mentioned earlier, both fits-based and momentsbased Wind plasma parameters were determined at MIT and provided to NSSDC, although we have used only the fitsbased values in this paper (except in this section) and in OMNI 2. We have done regression analysis for the Wind density values determined by these two methods. For IP &lt; 60 RE and for 1998-1999, we find:

<!-- formula-not-decoded -->

The analysis was over 11,860 hours, and yielded a cross correlation coefficient of 0.99 and a D value of 0.025. A separate run for the 2000-2001 period yielded virtually the sameresult. That we do not find log N (fits) = log N (moments) we attribute to the difference between the moments versus fitting approaches.

- [27] The Wind moments versus fits result immediately above is to be compared to the Wind-ACE relation of Table 1:

<!-- formula-not-decoded -->

Evaluating these equations at N = 2, 5, 10, and 20/cc yields N (Wind, fits)/ N (Wind, mom) ratios of 0.895, 0.919, 0.938, 0.957 and N (Wind, fits)/ N (ACE) ratios of 0.816, 0.866, 0.906, 0.947, respectively. In both cases, moments-based densities have to be reduced to match fits-based densities.

At large N values, the difference between the N (Wind, fits) values and the N (ACE) value is comparable to the difference between the N (Wind) values determined from moments and fits approaches. However, N (ACE) values at lower densities are higher, relative to N (Wind, fits) values, than might be expected from the difference in the Wind moments and fits approaches by about 8%. The difference in details of the Wind and ACE instruments and/or moments calculations may be responsible for this.

[28] It is also of interest to note that the random difference between Wind and ACE densities, as measured by D, is more than twice that of the equivalent difference between fits-based and moments-based Wind densities. This is in large part due to the fact that ACE and Wind measure differing plasma elements, while the Wind-Wind analysis is based on common plasma elements.

[29] Finally, consider the temperature equation of Table 1. This corresponds to T (Wind)/ T (ACE) ratios of 0.95, 1.04, 1.14 and 1.25 at T (ACE) values of 25, 63, 160 and 400 thousand deg K. As for densities, we find only small time dependences in the T (Wind)   T (ACE) relation but significant flow speed dependence. Table 3 gives values of T (Wind)/ T (ACE) in speed bins at the same four temperature values. Whereas the ACE densities generally exceed Wind densities, the opposite is true for temperatures.

[30] Comparison of Wind fits-based and moments-based temperature values yielded:

<!-- formula-not-decoded -->

with a cross correlation coefficient of 0.78 and a D value of 0.163. In general, ACE moments-based temperatures agree with Wind fits-based temperatures better than do Wind temperatures determined by the two approaches agree with each other. This supports the significantly greater level of confidence of the MIT Wind/SWE team in their fits-based results than in their moments-based results.

- [31] Owing to the significant differences between Wind (fits-based) and ACE values, for both densities and temperatures, cross normalization of ACE values to equivalent Wind values were performed in creating the OMNI 2 data set. That the Wind/SWE density data set was chosen as the baseline was the result of analysis at MIT [ Kasper , 2002] comparing electron densities inferred from observed, fitsbased proton densities and alpha particle densities, plus a model-based contribution for electrons from higherZ species, with total electron density from the independent Wind/ WAVES instrument. From this analysis the uncertainty in the Wind SWE fits-based proton density was estimated as 2%. (See also Maksimovic et al. [1998] for an earlier finding of good agreement level between Wind/SWE and Wind/ WAVES density estimates.) Wind temperature data were

Table 3. T (Wind)/ T (ACE) Values

|                  |   T (ACE) Value, K |   T (ACE) Value, K |   T (ACE) Value, K |   T (ACE) Value, K |
|------------------|--------------------|--------------------|--------------------|--------------------|
|                  |              25    |              63    |             160    |             400    |
| V < 350 km/s     |               0.69 |               0.97 |               1.36 |               1.91 |
| V = 350-450 km/s |               1.03 |               1.09 |               1.16 |               1.23 |
| V > 450 km/s     |               0.97 |               1.05 |               1.13 |               1.22 |

Table 4. Differences (D) Between Wind and Normalized ACE Values

| Impact         | Physical Parameters   | Physical Parameters   | Physical Parameters   | Physical Parameters   | Physical Parameters   | Physical Parameters   | Physical Parameters   |
|----------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
| Parameter, R E | j B j                 | B x                   | B y                   | B z                   | V                     | log N                 | log T                 |
| 0-60           | 0.221                 | 0.456                 | 0.435                 | 0.480                 | 4.432                 | 0.059                 | 0.105                 |
| 60-120         | 0.232                 | 0.610                 | 0.621                 | 0.840                 | 5.611                 | 0.059                 | 0.106                 |
| 120-180        | 0.291                 | 1.142                 | 1.033                 | 1.335                 | 6.580                 | 0.068                 | 0.106                 |

chosen as the temperature baseline for consistency with the density baseline choice.

## 5. Random Differences

[32] In making the regression runs whose slopes and intercepts were studied in the prior section to assess systematic differences between parameter pairs, we also computed both cross correlation coefficients and the root weighted mean square differences (D) between the Wind values and the normalized ACE values. Both these parameters give measures of the random differences between ACE and Wind parameters that result largely from the fact that the two spacecraft were measuring somewhat differing plasma regimes for the intervals and at the locations from which data were time-shifted to Earth for a common hour. That our assumption of time-invariant phase front orientations, discussed earlier, is sometimes violated also contributes to these differences.

[33] Refer back to the D column of Table 1. These are the differences between data points and a best fit regression line, for the favorable condition of ACE-Wind IP &lt; 60 RE and as taken over the 18 (46) months of available concurrent IMF (plasma parameter) data. These show that there are

Figure 6. Autocorrelations and cross correlations for j B j , Bx , and Bz hourly averages from ACE and Wind. Color distinguishes the source; blue is the only cross correlation. Most correlations are for 1998-1999, but the green lines are for 1995-1996. See color version of this figure at back of this issue.

<!-- image -->

Figure 7. Similar to Figure 6 but for flow speed and logs of density and temperature. See color version of this figure at back of this issue.

<!-- image -->

irreducible differences in ACE and Wind hourly averages of  0.2 nT in IMF magnitude,  0.45 nT in IMF components,  4.4 km/s in flow speed,  0.06 in log density and  0.11 in log temperature. (Note that these latter are equivalent to relative random differences in density and temperature of  15% and 30%.) With a simplified time-shift assumption, one cannot hope to characterize solar wind parameters at the nose of the Earth's bow shock at hourly resolution to levels more accurate than these values, given the availability of an L1 upstream solar wind monitor with IP up to 60 RE .

[34] That the D value for IMF magnitude is significantly less than for the IMF components is consistent with others' earlier findings [e.g., Ness et al. , 1964] of the preponderance of IMF directional variations over compressional variations.

[35] It is of interest from the perspective of both heliospheric science and space weather applications to examine the D value as a function of the ACE-Wind impact parameter and, for IP &lt; 60 RE , as a function of delay of one hour average relative to another.

[36] Table 4 shows the D values for all the physical parameters of Table 1, but additionally in the IP bins 60120 RE and 120-180 RE . Except for temperature, the D value for all parameters increases with IP. The relative increase is greater for the IMF parameters than for the plasma parameters, consistent with earlier authors' findings of shorter distance scales in IMF structures than in plasma structures [e.g., Richardson and Paularena , 2001].

[37] It is of interest to examine coherency on scales larger than those provided by the Wind-ACE IP values encountered during the times of data availability. To do so, we take autocorrelations and cross correlations of ACE and Wind parameters, considering lags up to 6 hours. Figures 6 and 7 show the results of these calculations. Note that for each parameter, the ACE and Wind autocorrelations and the Wind-ACE cross correlation are all very similar except at zero lag where the autocorrelations are unity by definition

and where the cross correlations, being affected by the irreducible Wind-ACE differences discussed above, are somewhat less than unity.

- [38] Figure 6 shows that the IMF magnitude is autocorrelated over a significantly longer scale than the IMF components, again consistent with the predominance of Alfvenic over compressional variations. The scale of Bx (and of By , not shown) is greater than that of Bz ; this is most likely the result of multihour-scale coherency imposed on Bx and By by interplanetary sector structure.
- [39] Figure 7 shows that the flow speed correlation falls off most slowly (of all the parameters addressed) as a function of lag, while log N and log T fall off at approximately the same rates as each other. Their falloff is more similar to the IMF intensity than to the IMF Bx and By components. This suggests again that scale sizes of interplanetary structures are greatest when defined in terms of flow speed variations, next greatest when defined in terms of IMF magnitude variations, next for density and temperature variations and least for IMF directional variations.
- [40] There is no universally accepted approach to quantifying a scale size from an autocorrelation or crosscorrelation function. However, if we accept the Richardson and Paularena [2001] definition of scale size as the distance over which the relevant autocorrelation function falls by 10%, then we have the following scale sizes: V ,  1400 RE ; j B j ,  450 RE ; log N and log T ,  300 RE ; Bx and By ,  200 RE ; Bz ,  100 RE .
- [41] Since we have seen that Wind, ACE autocorrelation and cross-correlation functions track each other closely, and since we have Wind data for the solar quiet 1995-1996 period in addition to the 1998-1999 solar active period, we also compute 1995-1996 Wind autocorrelation functions in order to assess the extent to which solar wind structure scale sizes may depend on solar cycle phase. These 1995-1996 Wind autocorrelation functions are also displayed in Figures 6 and 7, as green lines. It is clear that for IMF parameters, the autocorrelation function falls more rapidly at solar quiet times than at solar active times, but that there is far less solar cycle dependence in the plasma parameters. Magnetic field structures, which tend to be of smaller scale sizes than plasma structures at solar active times, are even smaller than plasma structures at solar quiet times. This IMF result is consistent with Collier et al. [1998], who showed upon taking Wind-IMP IMF correlations in 2-hour intervals that periods of high correlation were less frequent at solar minimum than at solar maximum. Earlier work of Kelly et al. [1986] suggested such solar cycle dependence in IMF scale lengths may be associated with the much greater occurrence rate of Coronal Mass Ejections at solar maximum than at solar minimum. If true, then the lack of solar cycle dependence in scale lengths of plasma parameters suggests that CME's organize field and plasma variations on scales longer than other IMF organizing factors but on scales comparable to or shorter than other plasma parameter organizing factors.

## 6. Summary and Conclusions

- [42] We have briefly described the OMNI 2 data set and in particular have quantified systematic and random differ-
2. ences between the hourly averaged solar wind magnetic field and plasma parameters from Wind and ACE that were used in building OMNI 2.
- [43] By studying systematic differences between these parameters, we have demonstrated the need to normalize ACE density and temperature values to equivalent Wind values. This involved decreasing ACE moments-based proton densities by 18% to match Wind/SWE fits-based densities at flow speeds &gt;450 km/s, and by 10-17% (density dependent) for 350 &lt; V &lt; 450 km/s. It also involved increasing ACE temperatures (at V &gt; 350 km/s) by T -dependent amounts from 0% at 25,000 ° K to 25% at 400,000 ° K. For flow speed and for magnetic field parameters, differences between best fit regression lines and the line y = x were smaller than the random scatter of data points about the regression line throughout the range of parameter space encountered physically, so no other parameter normalizations were done.
- [44] We showed irreducible random differences between nominally concurrent and collocated ACE and Wind hourly averages for each IMF and plasma parameter. Upon excluding all times when the Wind-ACE impact parameter exceeded 60 RE , these differences amounted to 0.2 nT, 0.45 nT, 4.4 km/s, 0.06 and 0.11 in j B j , B Cartesian components, V , log N and log T . These must be considered the irreducible uncertainties in hourly averaged parameters at the bow shock nose, given observations from an ACElike orbit, if one does time shifting of higher-resolution data using time-invariant algorithms that allow for only spacecraft positions and flow speeds.
- [45] We also showed, as have earlier researchers using higher-resolution data, that magnetic structures are largely Alfvenic rather than compressional, that magnetic structures tend to have smaller scale sizes than do plasma structures, especially when the latter are defined by flow speed variations, and that magnetic structures have smaller scale sizes at solar quiet periods (1995-1996) than at solar active periods (1998-1999). Plasma structure scales have little or no dependence on solar cycle phase.
- [46] Acknowledgments. We thank the teams who created and provided the Wind and ACE magnetic field and plasma data used in this analysis, including R. P. Lepping, A. Szabo, A. J. Lazarus, J. C. Kasper, N. F. Ness, C. W. Smith, D. J. McComas, and R. Skoug.
- [47] Shadia Rifai Habbal thanks Fausto T. Gratton, Helfried K. Biernat, and John T. Steinberg for their assistance in evaluating this paper.

## References

Collier, M. R., J. A. Slavin, R. P. Lepping, A. Szabo, and K. W. Ogilvie (1998), Timing accuracy for the simple planar propagation of magnetic field structures in the solar wind, Geophys. Res. Lett. , 25 , 2509.

- Collier, M. R., A. Szabo, J. A. Slavin, R. P. Lepping, and S. Kokubun (2000), IMF length scales and predictability: The two length scale medium, Int. J. Geomagn. Aeron. , 2 , 3.
- Garrard, T. L., A. J. Davis, J. S. Hammond, and S. R. Sears (1998), The ACE Science Center, Space Sci. Rev. , 86 , 649.

Kasper, J. C. (2002), Solar wind plasma: Kinetic properties and microinstabilities, Ph.D. dissertation, Mass. Inst. of Technol., Cambridge.

- Kelly, T. J., N. U. Crooker, G. L. Siscoe, C. T. Russell, and E. J. Smith (1986), On the use of a sunward libration-point-orbiting spacecraft as an interplanetary magnetic field monitor for magnetospheric studies, J. Geophys. Res. , 91 , 5629.
- Lepping, R. P., et al. (1995), The Wind magnetic field investigation, Space Sci. Rev. , 71 , 207.

Maksimovic, M., J.-L. Bougeret, C. Perche, J. T. Steinberg, A. J. Lazarus, A. F. Vin ˜as, and R. J. Fitzenreiter (1998), Solar wind density intercom-

21562202a, 2005, A2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2004JA010649 by University College London, Wiley Online Library on [25/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicabl

- parisons in the Wind spacecraft using WAVES and SWE experiments, Geophys. Res. Lett. , 25 , 1265.
- McComas, D. J., S. J. Bame, P. Barker, W. C. Feldman, and J. L. Phillips (1998), Solar wind electron proton alpha monitor (SWEPAM) for the Advanced Composition Explorer, Space Sci. Rev. , 86 , 563.
- Merka, J., A. Szabo, T. W. Narock, J. H. King, K. I. Paularena, and J. D. Richardson (2003), A comparison of IMP 8 observed bow shock positions with model predictions, J. Geophys. Res. , 108 (A2), 1077, doi:10.1029/2002JA009384.
- Ness, N. F., C. S. Scearce, and J. B. Seek (1964), Initial results of the IMP 1 magnetic field experiment, J. Geophys. Res. , 69 , 3531.
- Ogilvie, K. W., et al. (1995), SWE, a comprehensive plasma instrument for the Wind spacecraft, Space Sci. Rev. , 71 , 55.
- Press, W. H. (1986), Numerical Recipes: The Art of Scientific Computing [CD-ROM], Cambridge Univ. Press, New York.
- Richardson, J. D., and K. I. Paularena (1998), The orientation of plasma structure in the solar wind, Geophys. Res. Lett. , 25 , 2097.
- Richardson, J. D., and K. I. Paularena (2001), Plasma and magnetic field correlations in the solar wind, J. Geophys. Res. , 106 , 239-251.
- Smith, C. W., J. L'Heureux, N. F. Ness, M. H. Acun ˜a, L. F. Burlaga, and J. Scheifele (1998), The ACE magnetic field experiment, Space Sci. Rev. , 86 , 613.
- Weimer, D. R., D. M. Ober, N. C. Maynard, M. R. Collier, D. J. McComas, N. F. Ness, C. W. Smith, and J. Watermann (2003), Predicting interplanetary magnetic field (IMF) propagation delay times using the minimum variance technique, J. Geophys. Res. , 108 (A1), 1026, doi:10.1029/ 2002JA009405.

               

                   

         

J. H. King and N. E. Papitashvili, Mail Code 612.4, Goddard Space Flight Center, Greenbelt, MD 20771, USA. (jking@mail630.gsfc.nasa.gov; natasha@mail630.gsfc.nasa.gov)

21562202a, 2005, A2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2004JA010649 by University College London, Wiley Online Library on [25/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicabl

Figure 6. Autocorrelations and cross correlations for j B j , Bx , and Bz hourly averages from ACE and Wind. Color distinguishes the source; blue is the only cross correlation. Most correlations are for 1998-1999, but the green lines are for 1995-1996.

<!-- image -->

Figure 7. Similar to Figure 6 but for flow speed and logs of density and temperature.

<!-- image -->