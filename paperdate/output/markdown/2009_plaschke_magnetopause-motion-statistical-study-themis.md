## Statistical study of the magnetopause motion: First results from THEMIS

F. Plaschke, 1 K.-H. Glassmeier, 1 H. U. Auster, 1 V. Angelopoulos, 2

O. D. Constantinescu, 1 K.-H. Fornac ¸on, 1 E. Georgescu, 3 W. Magnes, 4 J. P. McFadden, 5 and R. Nakamura 4

Received 23 May 2008; revised 30 September 2008; accepted 6 November 2008; published 27 January 2009.

[1] During its early coast phase the configuration of the five Time History of Events and Macroscale Interactions during Substorms (THEMIS) spacecraft resembled pearls on a string. Between April and September 2007 they traversed the magnetopause boundary layer far more than 6000 times. The radial extension of the spacecraft configuration as well as the resolution due to the high number of simultaneous observation points along the orbit provided us with the unique opportunity to study the spatiotemporal evolution of the magnetopause location. In this study we present single and multiple spacecraft analyses with a special emphasis on a statistical analysis of the magnetopause motion reconstructed from crossing locations and times by spline interpolation. Our observations allow us to infer a higher stability of the magnetopause surface against deformation in field-aligned direction. Its overall stability increases with decreasing distance to the Earth as well. Additionally, we were able to determine amplitude, velocity and period distributions of the boundary oscillations.

Citation: Plaschke, F., K.-H. Glassmeier, H. U. Auster, V. Angelopoulos, O. D. Constantinescu, K.-H. Fornac ¸on, E. Georgescu, W. Magnes, J. P. McFadden, and R. Nakamura (2009), Statistical study of the magnetopause motion: First results from THEMIS, J. Geophys. Res. , 114 , A00C10, doi:10.1029/2008JA013423.

## 1. Introduction

[2] The Earth's dipole magnetic field is compressed and confined to the magnetospheric cavity as a result of the continuous solar wind flow. The boundary layer which separates solar wind and magnetospheric plasma is called the magnetopause (MP). In their pioneering work, Chapman and Ferraro [1931] first proposed such a boundary to form at times of incident particle streams. After Biermann [1951] showed that the solar wind is instead a constant feature, the MP was predicted to be permanently present as well.

[3] The MP is a region characterized by the pressure balance between the total pressure at the magnetosheath side and the magnetic pressure at the magnetospheric side. Therefore the strong dependence of shape and location of this region on the dynamic pressure of the solar wind appears to be obvious. The dependence on

1 Institut fu ¨ r Geophysik und Extraterrestrische Physik, Technische Universita ¨t Braunschweig, Braunschweig, Germany.

2 Institute of Geophysics and Planetary Physics, University of California, Los Angeles, California, USA.

3 Max-Planck-Institut fu ¨ r Sonnensystemforschung, Katlenburg-Lindau, Germany.

4 Space Research Institute, Austrian Academy of Sciences, Graz, Austria.

5 Space Sciences Laboratory, University of California, Berkeley, California, USA.

strength and orientation of the interplanetary magnetic field has been noted by Aubry et al. [1970]. Afterward in situ satellite measurements of the location of the MP under various solar wind conditions facilitated the quantitative empirical modeling of its shape and location [e.g., Fairfield , 1971; Howe and Binsack , 1972; Holzer and Slavin , 1978; Formisano et al. , 1979; Sibeck et al. , 1991; Roelof and Sibeck , 1993; Petrinec and Russell , 1996; Shue et al. , 1997]. An elucidating comparison and benchmark of some of these models has been presented by Safra ´nkova ´ et al. [2002].

[4] Nevertheless, these static models are not able to take account for the constant dynamic motion of the MP. Several mechanisms presumably contribute to this motion at different time and length scales: The time varying solar wind and magnetosheath pressure is accountable for motion with periods in the range between seconds and hours [ Elphic and Southwood , 1987; Song et al. , 1988; Sibeck et al. , 1989]. Intrinsic instabilities of the boundary layer such as the Kelvin-Helmholtz instability are supposed to produce MP motion in the time scale of minutes [ Southwood , 1968; Walker , 1981; Fujita et al. , 1996]. Other causes of magnetopause motion may be reconnection-related phenomena and flux transfer events [ Song et al. , 1988].

[5] The determination of the MP motion is subject to strong assumptions on working with single spacecraft observations. Early estimates of its flapping velocity at low latitudes were computed by Cahill and Amazeen [1963] and Aubry et al. [1971] among others. The direct determination of the velocity is indeed only possible, if

several spacecraft are present in the area of the MP motion. Multispacecraft observations were therefore first performed when ISEE and AMPTE satellite pair data were available [ Elphic and Russell , 1979; Berchem and Russell , 1982; Le and Russell , 1994; Phan and Paschmann , 1996].

- [6] Later the CLUSTER mission, which consists of four spacecraft in near-tetrahedral configuration, provided the opportunity to determine the velocity direction of the MP by comparison of the time differences between spacecraft MP crossings and the corresponding positions of the probes. Different approaches to perform this task have been introduced and compared to previously applied single-spacecraft techniques for instance by Haaland et al. [2004a, 2004b]. Very recently, Paschmann et al. [2005] and Panov et al. [2008] presented statistical analyses of near-tail dawn and high-latitude MP crossings respectively seen by the CLUSTER spacecraft. The interspacecraft separation in these cases was on the order of a few hundred kilometers. Unfortunately, because of the relatively small extension of the CLUSTER probe configuration with respect to the expected amplitude of MP motion (up to several Earth radii), the velocities determined remained snapshots of the MP motion. Only the empirical reconstruction method introduced by de Keyser [2005] allowed in some cases for an indirect determination of the temporal evolution of the MP position.
- [7] The new five spacecraft mission Time History of Events and Macroscale Interactions during Substorms (THEMIS) [ Angelopoulos , 2009] now yields the opportunity to further unravel the spatiotemporal structure of the MP motion. All five probes were launched simultaneously on 17 February 2007, into very similar elliptical and nearequatorial orbits. At all times during the coast phase (from February to mid-September 2007) their configuration resembled pearls on a string. The intervals between the probes on their orbit did not exceed a couple of hours. Taking into account the velocity of the spacecraft at the MP distance of roughly 1 km/s and the fact that the orbit apogee was of the order of the bow shock standoff distance, the spacecraft configuration often crossed the MP in quasi-radial direction with its radial extension being of the order of or less than a few Earth radii ( R E). As this coincides with the expected amplitudes of MP flappings, the THEMIS spacecraft configuration was almost perfect for the study of the spatiotemporal evolution of the MP location along its normal direction.
- [8] Hence, we determine in this statistical study the characteristics of the MP surface undulations and its motion presenting distributions of its deformation directions, velocity, amplitude and oscillation periods. The analysis is divided into three parts: the single spacecraft analysis, where detected MP crossings are looked at independently, the multicrossing analysis, where groups of subsequently detected MP crossings are examined, and finally the spatiotemporal analysis of the MP motion, where a spline based interpolation of the observed MP crossing positions and times is done from which motion characteristics are inferred. The MP model from Shue et al. [1997] is used to provide a reference MP normal direction, to which the actual surface inclination can be compared, and an equivalent one-dimensional standoff

distance, which is necessary for the spline interpolation based motion analysis.

## 2. Data and Single Spacecraft Analysis

- [9] Spin frequency sampled data of the digital fluxgate magnetometers (FGM) onboard the probes [see Auster et al. , 2007, 2009] were available to us covering practically all spacecraft and days of interest from April to September. In addition particle data of the ESA instrument [ McFadden et al. , 2009] were available for large parts of these intervals. We manually selected 6697 MP crossings starting from 4 April 2007 till 9 September 2007. MP crossings were only selected for probes and times, when both, magnetic field data and particle data, were available for correct identification. As an example we show in Figure 1 the crossings found on 19 June 2007, between 0930 UT and 1015 UT. As can be seen in Figure 1, the first probe ThA was in the magnetosphere and ThB in the magnetosheath during the whole interval. Probes ThC, ThD and ThE, however, were in the region of MP motion and observed several subsequent MP crossings.
- [10] The positions of the spacecraft and the magnetic field vector data were transformed into a 5 ° aberrated geocentric solar magnetospheric (AGSM) coordinate system. This is necessary as the aberration of the incidence angle of the solar wind due to the motion of the Earth perpendicular to the solar wind direction has a significant influence on the MP location (e.g., noted by Safra ´nkova ´ et al. [2002]). The partial orbits of the probes during the selected example interval are depicted in Figure 2 in this coordinate system. ThA is trailing the configuration, ThB is leading it. In between probes ThC, ThD and ThE are separated by less than half an Earth radius.
- [11] As previously mentioned the common THEMIS orbit is highly excentrical and near equatorial. In the Earth-Sun reference coordinate system the orbit rotates about 150 ° during the five months of observation. Its apogee was first located near 18 h local time at the dusk sector. The trajectory thus swept over the dayside low-latitude magnetosphere and magnetosheath regions, and ended up in midSeptember at the dawn flank. This coverage is reflected in the distribution of observed MP crossings in dependence on the AGSM longitude angle which is depicted in Figure 3. The AGSM longitude angle is measured between the AGSM x coordinate axis and the line from Earth to the projection of the MP crossing location onto the AGSM ecliptic plane, and counted positive in eastward direction. As can be seen in Figure 3 the coverage of large parts of the dayside sector is good and equilibrated, which ensures statistical results to be representative for the whole dayside region and even may be distinguished for different longitude sectors (noon sector and flanks). The AGSM latitude angle distribution is also shown in Figure 3. The angle does only change in the range of ±25 ° around 0 ° , which confirms that the orbits are indeed near-equatorial.
- [12] For further analysis we need to compute the normal direction of the MP for every observed crossing. Therefore we take magnetic field data in a ±15 s vicinity around the detected crossings to determine it at the crossing location and time using the standard minimum variance analysis (MVA) introduced by Sonnerup and Cahill [1967]. In this

21562202a, 2009, A1, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2008JA013423 by University College London, Wiley Online Library on [25/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicab

Figure 1. Module of the magnetic field measured by the five THEMIS probes on 19 June 2007. Grey solid lines show identified MP crossings.

<!-- image -->

analysis the normal n MVA is defined as the direction of least variance in the magnetic field assuming the MP to be a perfect tangential discontinuity. These directions have to be compared to a chosen standard normal direction for each point.

[13] In order to perform this task we selected the MP location model introduced by Shue et al. [1997]:





<!-- formula-not-decoded -->

This function, which describes the form of the magnetopause surface, directly and intuitively relates the angle q between the AGSM x line (aberrated Earth-Sun line) and the MP observation location as well as its radial distance r to the standoff distance of the MP r 0. Hence, we can use this model not only to compare MVA determined MP normal directions to the respective standard normal directions obtained from the model surface, but also to compute equivalent MP standoff distances r 0 from the observed crossing positions ( r , q ). This mapping to a onedimensional spatial axis is necessary for the spatiotemporal analysis of the MP motion via spline interpolation of the crossing positions and times, which is explained in detail in section 4. The model from Shue et al. [1997] is one of the models tested and shown to be qualified by Safra ´nkova ´ et al. [2002] to match different satellite observations. The exponent a has been found to be dependent on the z component of the solar wind magnetic

21562202a, 2009, A1, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2008JA013423 by University College London, Wiley Online Library on [25/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicab

Figure 2. Partial orbits of the five THEMIS probes on 19 June 2007, projection to the ecliptic plane in aberrated GSM coordinates.

<!-- image -->

field Bz and the dynamic pressure p SW [ Shue et al. , 1997]:

<!-- formula-not-decoded -->

where Bz is given in units of nT and p SW in nPa. Nevertheless, the dependence of a on both solar wind

Figure 3. Distribution of observed MP crossings over longitude and latitude angles in the aberrated GSM coordinate system.

<!-- image -->

<!-- image -->

parameters is far from being strong. Thus we assume it to be of constant value a = 0.5959, which is equivalent to Bz =   1 nT and p SW = 1 nPa.

- [14] As mentioned before standoff distances r 0 as well as model normal vectors n model (directions perpendicular to the model MP surface at the crossing locations) could be computed for all MP crossings under these assumptions. Figure 4 shows the distribution of these standoff distances. The highest numbers of MP crossings can be associated with distances r 0 ranging, as expected, from 10 R E to 13 R E.
- [15] A comparison of MVA estimates of the normal vectors n MVA with the model normal vectors also yields a good agreement and qualifies the MP model of Shue et al. [1997] for our purpose. The total angle of deviation Q between n MVA and n model is small as can be seen in Figure 5 (bottom). Figure 5 (bottom) shows the distribution of Figure 5 (top) normalized by dividing the number of crossings in each angle bin by sin Q in order to take account for the asymmetry (tending toward higher angles) a similar histogram would show for a set of random directions in space (equal number of events per solid angle). 71% of all events in the distribution of Figure 5 (bottom) lie within the first eight bins ranging from 0 ° to 20 ° of total deviation Q .
- [16] The analysis of the total angle of deviation between both modeled and measured normal vectors did not reveal any dependence on the AGSM longitude and latitude angles. Flank and noon sector distributions are virtually indistinguishable. An interesting result instead is obtained looking more carefully to the directions of the angular deviation.
- [17] For that purpose we have to introduce a boundary normal coordinate system, which defines MP surface inplane directions. We do not use the coordinate system used by Russell and Elphic [1978] or Berchem and Russell [1982], which aligns one coordinate axis with the GSM z axis because this direction is not of local physical relevance, since the Earth's magnetic field is not strictly dipolar and, hence, the GSM z axis is not locally field aligned. Instead one axis (basis vector e l ) of our right-handed orthogonal local boundary normal coordinate system shall be aligned with the local magnetic field direction just inside the MP computed for each crossing point and time with the Tsyganenko 89 external field model [e.g., Tsyganenko , 1990]. The in-plane basis

Figure 4. Distribution of observed MP crossings over model estimated standoff distances r 0 .

<!-- image -->

Figure 5. (top) Distribution of the total angle Q between the MP model normals n model and the MP normals n MVA estimated with the MVA. Binning used is 2.5 ° . (bottom) The distribution has been normalized with 1/sin Q to counter the asymmetry of a random direction distribution (equal number of events per solid angle) tending toward higher angles.

<!-- image -->

Figure 6. Sketch of the orientation of the coordinate axes in the boundary normal coordinate system defined in the text: The basis vectors e l and e m lie tangential to the MP surface. e l is locally aligned with the magnetospheric magnetic field B computed with the Tsyganenko 89 model (field line depicted with dotted line). e n is the local normal to the model MP.

<!-- image -->

vectors e l and e m shall point magnetically northward and westward, respectively. Hence, both of them lie tangential to the MP plane and therefore perpendicular to the model normal direction and last basis vector e n = e l -e m = n model (see Figure 6). The directions in our coordinate system will from now on be denoted with l , m and n .

[18] Figure 7 shows the distribution of deviation directions and values of all 6697 registered crossings. Each point represents one crossing. The radial distance between the center of Figure 7 and the point shows the total angle Q between the model normal and the MVA estimation. The corresponding azimuth angle F to the position of the point shows the direction of the deviation and hence the direction of local inclination of the MP surface with respect to the local magnetic field direction. An azimuth angle of F = 0 indicates that the MP surface was inclined in field perpendicular direction. For further computations this azimuth angle shall increase clockwise from the positive m axis as defined by the relations l =   Q sin F and m = Q cos F and indicated in Figure 7. This transformation simply maps the angular deviations ( Q , F ) of the MVA determined normal vectors from the model defined normal vectors onto the l and m directions (field aligned and field perpendicular, respectively). Hence, it is used here to separate both contributions. [19] Histograms with binning in l and m directions from Figure 7 as depicted by vertical and horizontal lines on the edges of Figure 7 are shown in Figure 8. The now much

Figure 7. Distribution of angular deviations of MVA determined MP normal directions from model normals in the tangential l -m -plane coordinate system. l points in local field direction and m in perpendicular direction to it according to the Tsyganenko 89 external field model. The radial distance of the points to the center is equal to the total deviation angle Q . Dashed circles mark angular distances of Q = 30 ° , 60 ° , and 90 ° to the center. The arrow indicates the direction in which the angle F is counted (see text for details). Vertical and horizontal lines at the edge of the Q = 90 ° circle mark the limits of the bins used in Figure 8.

<!-- image -->

Figure 8. Distributions of angular deviations of MVA determined MP normal directions from model normals in tangential l and m directions as defined in the text. Normalization applied to correct for probability inequalities of occurrence of deviations under the assumption of a random direction distribution: see Appendix A for explanation.

<!-- image -->

<!-- image -->

more complex normalization applied to the shown distributions is explained in Appendix A. It can be easily seen that the distribution in m direction perpendicular to the magnetic field is much broader than in l direction. The distributions do not change significantly over the AGSM longitude or latitude angles, which is the reason why only the histogram including all crossings is shown. This result can be very intuitively explained: A deformation in field direction is associated with a deformation of field lines leading to higher magnetic tension. The stability of the MP against a deviation of its normal in this direction is higher than against a simple displacement and compression of field lines, which would result in a similar angular deviation of the normal in field perpendicular direction. This is reflected for instance in the stabilizing parts of the instability criterion for Kelvin-Helmholtz (KH) driven waves [e.g., McKenzie , 1981]:

<!-- formula-not-decoded -->

Here the indices 1 and 2 denote the MP adjacent regions inside and outside of the magnetosphere, respectively; r is the plasma mass density, k the KH wave vector and u and v represent the flow and Alfve ´n velocities. As can be seen high values of k  v 1  k  B 1 have a stabilizing effect against KH waves and therefore wave-like motion of the MP normal in field parallel direction is diminished. As a consequence high-amplitude surface waves on the MP will tend to be guided in field perpendicular direction with a substantial fraction of the associated restoring forces being of compressional nature. This is reflected in the results shown in Figure 8, which thus suggests that a significant contribution of the observed MP surface deformations may well be KH instability generated.

## 3. Temporal Grouping and Multicrossing Results

[20] Making use of the large quantity of observed MP crossings we are now able to reduce further the data by temporally and, because of the close flight configuration of THEMIS, also spatially grouping the crossing events. Each group shall be composed of subsequently observed MP crossings, time lags between which do not exceed 10 min. In addition we demand the groups to consist of at least 5 consecutive crossing events. The result are 289 groups containing over 21 MP observations in average.

[21] We intentionally allow for crossings to belong to one group, although they may not have been observed by one single spacecraft. Instead observations of several or all of the five THEMIS spacecraft contribute to each of the groups in most cases. Hence, the groups constitute themselves a result of multispacecraft measurements made possible by the special configuration of THEMIS. Collective properties of the crossings belonging to each group can now be further analyzed.

[22] The angular deviations of the MP surface normal from the model normal directions, shown in Figure 7, can be divided into several subsets according to the previously defined groups. Thus, a set of several normal vector angular deviations ( l , m ) exists for each of the groups and the direction of maximum and minimum variability of the MP surface can be obtained thereof. For this purpose we computed the covariance matrix of these angular deviations in l and m directions as well as the respective eigenvectors and eigenvalues. In other words, we applied a MVA to the angular deviation data of each group. It should be noted for clarification that the term ''angular deviation'' refers to the quantity which is displayed in Figure 7 and from which the variance and the standard deviation can be computed. These can be obtained from the MVA results: The eigenvectors point in the directions of minimum and maximum angular deviation variance in the boundary tangential l -m -plane and therefore indicate the direction of preferential inclination of the MP surface for the observed crossings within one group. The eigenvalues themselves represent the variance in the above mentioned directions. Standard deviations of the angular deviations in the respective directions given by the eigenvectors can be obtained by simply computing the square roots of the eigenvalues. These standard deviations are depicted in Figure 9. As can be seen the combinations of maximum and minimum standard deviations group within a relatively narrow area in comparison to the possible area of occurrence, which is delimited by solid lines in Figure 9. The distribution does not exhibit much internal structure.

[23] In Figure 9 each cross belongs to one group and its position depicts the type of the MP motion. Events with predominantly normal motion of the MP, which are char-

Figure 9. Distribution of group standard deviations of angular variations of MVA determined MP normals with respect to the corresponding model normals in the directions of maximum and minimum variance. Solid lines delimit the area of possible combinations.

<!-- image -->

acterized by a nonundulated MP plane, are expected to appear in the bottom left corner of Figure 9, which corresponds to low variability of the MP normal. Close to the diagonally limiting line the crosses belong to events with variability of the MP surface normal in no preferential direction. Groups of crossings showing an apparent preferential MP surface variability direction are to be found on the lower edge of Figure 9, with variability increasing to the right. Both latter types would indicate an undulated MP plane.

[24] Interestingly neither classical flapping MP events of no MP surface variability (bottom left corner in Figure 9) nor single wave events, which would be characterized by a clear maximum variability direction (bottom right corner), are predominant. All group events cluster in a medium position. The mean standard deviation in maximum variability direction is about 35 ° . In the minimum variability direction it comes close to 16 ° .

[25] The radial distance of the crosses in Figure 9 to the origin are estimates for the direction-independent standard deviation s t of the angular MP normal deviations. We depicted the relation between this quantity and the mean AGSM radial standoff distance of the observed MP crossings h r 0 i in the corresponding groups in Figure 10. The linear trend has been added to Figure 10 to show the dependence:

<!-- formula-not-decoded -->

where s t is given in degrees. Obviously stronger undulation of the MP surface is statistically seen when the MP is closer to the Earth and the magnetosphere is further compressed.

[26] A possible explanation is as follows: When the magnetosphere is more expanded, the magnetospheric magnetic field at the magnetopause is weaker. As a result, the restoring forces that act against surface deformation are weaker as well. MP undulations are in this case of largerscale and global motion of the MP without high angular deviation of its normal is more frequent. When the magnetosphere is more compressed the higher restoring forces favor situations when oscillations can be associated more with localized wavelike undulations and structures.

[27] A dependence of the distribution in Figure 9 on the mean AGSM longitude of the group MP crossing positions could not be found. The same applies to the azimuth directions F of the maximum variability of the MVA determined MP normals belonging to each group with respect to the model normals, which are depicted in Figure 11. As can be seen the maximum variability directions cluster around an azimuth angle of 0 ° corresponding to the direction perpendicular to the local magnetic field. Figure 11 indeed demonstrates that the distributions of Figure 8 are independent of the location where the MP crossings were observed. As expected in this interpretation the linear trend in Figure 11 (top) resembles a constant line very close to the expected azimuth angle of 0 ° . In Figure 11 (bottom) a very slight trend is observable, which can be attributed to the little spreading in AGSM latitude angle of the crossing positions, nevertheless displaying overall little deviation of the approximated azimuth angle from F = 0 ° . This result is only obtained, if the local normal coordinate system ( l , m , n ) is chosen as defined before with the l direction being aligned with the magnetospheric magnetic field. In all other cases a linear trend and higher scattering of azimuth angles appears, which is a clear sign that our choice of the boundary normal coordinate system oriented with the local magnetic field direction is the most senseful giving us confidence in our results and the interpretation thereof.

## 4. Spatiotemporal Analysis

[28] For a full spatiotemporal analysis of the MP motion, its position has to be estimated for all times between

Figure 10. Relation between total standard deviation s t (radial distance to origin in Figure 9) and mean model computed standoff distance h r 0 i of the corresponding groups. Trend of data added to the picture.

<!-- image -->

21562202a, 2009, A1, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2008JA013423 by University College London, Wiley Online Library on [25/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicab

Figure 11. Azimuth angle F of the maximum angular variability direction of MP crossings corresponding to each group against AGSM (top) longitude and (bottom) latitude of the mean observation locations of the crossings belonging to each group. An azimuth angle of 0 ° corresponds to highest variability of the MP normal vectors in the direction perpendicular to the local magnetic field ( m direction). ±90 ° instead means that highest variability is found in the direction aligned with the local magnetic field direction just inside the magnetosphere. Linear trend (solid line) has been added to both panels.

<!-- image -->

<!-- image -->

detected MP crossings. Therefore we use a standard spline interpolation method to bridge the time gaps when no crossings are detected [see Glassmeier et al. , 2008]. Before this can be done, a stricter selection criterion than for the previously used groups has to be applied. For instance it is nonsensical to spline-interpolate several crossings seen subsequently only by one satellite, because the resulting curve would only resemble the satellite motion along the MP normal. The temporal grouping described in section 3 is the basis for further subdivision of the MP crossing sets. If two consecutive crossings are registered by two different satellites, the motion direction of the MP is the same at both crossings and the positions of the satellites correspond to this inbound or outbound motion, then both crossings will belong to the same set of crossings used for one spline interpolation. Two consecutive crossings seen by the same satellite are accepted to take account for radial MP motion reversals. In all other cases they will belong to two different sets. It is demanded that every subset of consecutive MP crossings should consist of at least four crossing events, since cubic spline interpolation with less points would not yield a unique result.

[29] Using the outlined subdivision of groups a set of 452 subgroups remains available for applying the spline interpolation. The result is a spatiotemporal estimate of the MP position and motion in radial direction expressed in terms of a time varying model standoff distance r 0, which does not differ significantly from the MP motion in normal MP direction even at higher AGSM longitudes at the flanks [see Shue et al. , 1997, Figure 1]. The spline interpolation is therefore performed using r 0 estimates as position data for the MP at the crossing times.

[30] From these spline interpolates maximal velocities (in both inbound and outbound directions), peak to peak amplitudes and oscillation periods can be derived, since a full functional form of the MP motion is given.

[31] In Figure 1 a time interval selected for spline interpolation of 10 MP crossings would be ranging from 0949:43 UT (crossing detected at ThD) to 0958:41 UT (ThC detected crossing). The positions of the spacecraft ThC and ThD have also been converted to an equivalent standoff distance r 0 using the MP model. Figure 12 displays the trajectory of the spacecraft expressed in terms of this equivalent standoff distance (diagonal solid lines). The observed crossing points of the MP with the trajectories of the probes are depicted with bullet points. The spatiotemporal positions of these points have been used to perform a spline interpolation, which is also shown in Figure 12. This interpolation yields extremal velocities (squares in Figure 12) as well as the peak to peak amplitudes, which are defined as the differences of consecutive

Figure 12. Example of standard spline interpolation of MP crossing positions and times. Model estimated standoff distance r 0 of the MP (thick wavy solid line) over time during the interval 0948 UT to 1000 UT on 19 June 2007. Top and bottom diagonal solid lines correspond to the transformed positions of THEMIS probes ThD and ThC. Filled circles mark the observed crossing points. Squares show points of maximal MP velocity, and vertical solid lines show extrema of the amplitude. The peak to peak amplitudes for the statistical analysis are computed using the r 0 differences of consecutive MP extremal positions ( A 1 , A 2 , and A 3 in this case). The half periods used for the frequency statistics are time differences between consecutive MP r 0 extrema and are denoted with T 1 , T 2, and T 3 .

<!-- image -->

21562202a, 2009, A1, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2008JA013423 by University College London, Wiley Online Library on [25/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicab

Figure 13. (a) Histogram of spline interpolation estimated maximum velocities of the MP at the subsolar point. Bin size is 10 km/s. (b) The distribution of velocities (our result depicted with a solid line) is compared to the dayside results of low-latitude-like boundary layer crossings observed with CLUSTER at high latitudes analyzed by Panov et al. [2008] (dashed line). Numbers of velocity determinations of both distributions have been normalized to the respective values in the second bin (20 to 40 km/s). Bin size is 20 km/s. (c) A variable (nonconstant) bin size has been used. The solid line indicates our result, which has been normalized to the maximum occurrence number of 1 for the comparison with the result obtained by Berchem and Russell [1982] (dashed line).

<!-- image -->

extrema in the estimated MP standoff distance. In Figure 12 these amplitudes are denoted with A 1 , A 2 and A 3 . The temporal distances between consecutive extrema in r 0 are used to estimate the oscillation half periods of the MP

motion, which are denoted with T 1 , T 2 and T 3 in our example.

[32] A histogram showing all extremal velocity values of the estimated MP motion is depicted in Figure 13a. As can be seen the decay of the amount of velocity determinations with increasing velocity resembles an exponential function. The half maximum value is already reached at about 40 km/ s. More than 82% of all extremal velocities are below the line of 100 km/s. Taking into account a typical magnetoacoustic phase speed of about 500 km/s it can be stated that in the vast majority of times the motion of the MP can be considered quasi-static with respect to excited waves in the magnetosphere. It should be noted that this is not in disaccord with the observed undulations of the MP and the associated surface waves on it. In such a case the radial MP velocity would be the particle velocity of the medium transmitting the surface wave, i. e. the MP itself, which could be considered a tense membrane on which waves can propagate.

[33] Figure 13b shows a comparison with high-latitude MP motion velocity determinations from Panov et al. [2008] (dashed line), when a low-latitude-like boundary layer was apparent (see text in the paper for details). The total number of their determinations is 38, whereas in our case the sample size is 1288. In this panel both velocity distributions have been normalized to the respective numbers of events in the second bin (20-40 km/s). Results disagree mainly in the low-velocity range, where our findings display a much higher relative occurrence rate. Interestingly, except for this range both results are in remarkably good agreement, although they were obtained at different geomagnetic latitudes. Deviations between them are apparent at the 60 to 80 km/s and the 140 to 160 km/s bins, where the relative numbers of determinations in the results from Panov et al. [2008] exceed the ones from our findings. A comparison between our velocity distribution and the result obtained by Berchem and Russell [1982] is shown in Figure 13c. 30 events contribute to their statistics. In this case the numbers of events have been normalized to 1 with respect to the maximum value in one bin in order to make the results comparable. Again disagreement between the results is to be fount at the low-velocity part. Nevertheless, we can confirm the earlier findings from Berchem and Russell [1982] and Panov et al. [2008] on the basis of a much larger statistical sample size.

[34] The distribution of peak to peak amplitudes of the estimated MP motion at the subsolar point is shown in Figure 14. Interestingly an outstandingly large number of peak to peak amplitudes lies within the first bin, demonstrating that in a notable amount of cases the MP does not move very much around its stable location. This corresponds with the relatively high occurrence rate for lowvelocity MP motion determinations. Beside this the distribution very much resembles an exponential decay toward larger amplitudes with an approximate half maximum number reached at 0.5 R E, which is a typical value for the amplitude of the MP motion [e.g., Song et al. , 1988]. Computation of the mean value of all determined peak to peak amplitudes yields a larger value of about 5000 km, which corresponds to 0.78 R E.

[35] We shall check this statistical result against other observations. We start with the assumption that the location

21562202a, 2009, A1, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2008JA013423 by University College London, Wiley Online Library on [25/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicab

Figure 14. Distribution of peak to peak amplitudes determined from MP motion estimation via spline interpolation of observed MP crossing points in space and time. Amplitudes of MP motion expressed in terms of time varying standoff distance r 0 and given in multiples of the Earth radius R E. Histogram bin size is 0.1 R E.

<!-- image -->

of the MP boundary is determined by the equilibrium between magnetic pressure p mag = B mag 2 /2 m 0 on the magnetospheric side and total pressure p SH on the magnetosheath side:

<!-- formula-not-decoded -->

Here B eq denotes the strength of the equatorial geomagnetic field and r 0, as previously introduced, the standoff distance of the MP. Rewriting equation (5) yields the MP position as a function of the magnetosheath pressure and equatorial magnetic field:

!

<!-- formula-not-decoded -->

As long as the MP motion remains in the quasi-static regime, the above stated formulae can be used to derive a characteristic relative variability in the solar wind pressure needed to explain the observed MP motion amplitudes:

<!-- formula-not-decoded -->

Here k = 1/ K is the compressibility of the magnetosphere and K the corresponding magnetospheric bulk modulus introduced by Glassmeier et al. [2004]:

<!-- formula-not-decoded -->

Discretization of the above stated equation (7) and reorganization yields a testable relation:

<!-- formula-not-decoded -->

Assuming the characteristic peak to peak amplitude to be the mean value obtained of h D r 0 i = 5000 km and taking the mean value of the MP standoff position of h r 0 i = 74300 km we obtain:

<!-- formula-not-decoded -->

Assuming the MP boundary to be a tangential discontinuity the pressure on each point of the boundary can be assumed to be proportional to the solar wind dynamic pressure ( p SH  p SW), with variable constant of proportionality due to the changing angle of incidence of the particles and the character of the interaction [ Spreiter et al. , 1966]. It follows directly:

<!-- formula-not-decoded -->

Bowe et al. [1990] find characteristic values for the fractional variability of solar wind density and velocity of h s n / n i = 0.12 and h s v / v i = 0.02. s denotes here the standard deviation of the indexed quantities. This yields a total fractional variation of the solar wind dynamic pressure of:

D

E

D

E

<!-- formula-not-decoded -->

Since for the variation in the MP position D r 0 a value of the peak to peak amplitude has been taken, the fractional variability value h s p SW / p SW i computed with the standard variations of velocity and number density necessarily underestimates the value for D p SW/ p SW. For purely sinusoidal variations the standard deviation s p is related to the peak-to-peak amplitude D p via D p = ffiffi ffi 8 p s p . With this factor we obtain

<!-- formula-not-decoded -->

which is in very good agreement with the value (10) calculated using characteristic quantities of the statistical analysis.

[36] Finally, we show the distribution of half MP oscillation periods T in Figure 15. As can be seen the distribution exhibits a maximum around 50 s. The decrease in occurrence rate for lower-frequency oscillations of the MP is qualitatively in good agreement with results from Ivchenko et al. [2000], who found a similar distribution for the interarrival times of the MP seen by the Geotail satellite.

[37] Nevertheless, both results are not fully comparable, since the MP interarrival times will spread around the real oscillation half periods. This becomes clear if we assume the satellite to be located radially off-centered with respect to the MP motion. In this case a series of short and long time intervals between two consecutive crossings will be observed, where the real full period may be approximated by the sum of two consecutive interarrival times. Taking this into account as well as the decrease of the respective occurrence rates with increasing half period duration, the mapping of the real half period distribution toward higher

21562202a, 2009, A1, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2008JA013423 by University College London, Wiley Online Library on [25/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicab

Figure 15. Distribution of half oscillation periods determined from the spline interpolation of the MP motion. Binning used is 25 s. The result obtained by Ivchenko et al. [2000] for the distribution of interarrival times of the MP seen by the Geotail satellite is depicted with dotted lines.

<!-- image -->

periods onto the interarrival time distribution shown in Figure 15 becomes explainable.

[38] Because of the criteria applied for the grouping of the MP crossings (maximal separation of 10 min) oscillations with half periods of around and above 600 s are underrepresented in our distribution. Taking this also into account we can state that both distributions can be considered to be quantitatively in good agreement as well.

## 5. Conclusions

- [39] The configuration of the five THEMIS spacecraft in its early mission phase (coast phase) was particularly useful for the study of the MP surface deformation characteristics and allowed for a spatiotemporal analysis of the MP motion using spline interpolation due to the sufficient spatial resolution in radial direction at the MP location.
- [40] It could be shown that the variability of the surface inclination in the direction perpendicular to the local magnetospheric field is much larger than in the direction parallel to the ambient field proving an increased stability of the MP against deformation in the latter direction. This result is independent of the AGSM longitude or latitude; however, it is crucially dependent on the local boundary coordinate system used, which in our case is aligned with the Shue et al. [1997] model MP normal and, more important, the Tsyganenko 89 magnetic field direction at the location of the respective MP crossing observed. The result is in agreement with the criterion for stability of the MP against generation of KH waves suggesting that a significant part of the observed deformations may have been originated because of this mechanism.
- [41] However, clear waves with surface undulations being restricted to one direction or events where no significant MP normal deviations are observed over some time are the exception. Even though in most cases there is a preferential direction of the variability, which spreads around the field perpendicular direction, the corresponding value in the complementary direction is in the very most cases not negligible.
- [42] The overall variability has been found to be dependent on the estimated average standoff distance of the MP suggesting that its surface is subject to stronger inclination when the distance of the Earth to the MP is decreased and the magnetosphere is further compressed.
- [43] The maximal MP velocities determined were in most cases within the quasi-static regime giving rise to the supposition that the MP remains almost always in quasiequilibrium and its global motion may be reasonably good explained with the temporal variation of parameters on which its static location depends. Our velocity distribution confirm previous results from Berchem and Russell [1982] and Panov et al. [2008] based now on a much larger sample size. Interestingly the agreement with the findings from Panov et al. [2008] is particularly good although their velocity distribution was obtained from high-latitude MP crossings. However, in a significant number of times we found the velocity of the MP to be lower than 10 km/s, which was not seen in the previous studies. In accordance, the peak to peak amplitude distribution has its maximum between 0 and 0.1 R E showing that again in a significant number of cases the MP stays close to its stable location without moving much.
- [44] A previous determination of the oscillation period distribution reported by Ivchenko et al. [2000], which was inferred from interarrival times of the MP observed with the Geotail satellite, could also be confirmed on the basis of a larger statistical sample size. Both results are quantitatively in good agreement and show the tendency of the MP toward fluctuations on the time scale of the order of 100 s.

## Appendix A: Normalization of Distributions in Figure 8

- [45] The normalization applied in Figure 8 should not remain unmentioned, since the probability of occurrence distribution is complicated each time the data are transformed to the next coordinate system. In Figure 5 a normalization with sin Q was sufficient to counter the relatively small number of low Q directions in a random distribution of directions. For the composition of Figure 7 the following transformation equations regarding the known angle Q and the azimuth angle of deviation direction F hold:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

0

This is equivalent to:

ffiffiffiffiffiffiffiffiffiffiffiffiffiffi ffi

p

1

<!-- formula-not-decoded -->

Therefore the transformation of a surface element of the direction half sphere (sin Q d F d Q ) now yields in the local normal coordinate system:

ffiffiffiffiffiffiffiffiffiffiffiffiffiffi ffi

<!-- formula-not-decoded -->

As a result a deviation angle bin value in the upper part of Figure 8 covering angles between m = m 1 and m = m 2 has to be correctly normalized by division with:

q

ffiffiffiffiffiffiffiffiffiffiffiffiffi

<!-- formula-not-decoded -->

The bins of Figure 8 (bottom) have also been normalized in an analogous way.

- [46] Acknowledgments. The IGEP team was financially supported by the German Zentrum fu ¨r Luft- und Raumfahrt under grant 50QP0402. THEMIS was made possible and is supported in the US by NASA NAS502099. K.H.G. is grateful for financial support through INTAS grant 051000008-7978.
- [47] Zuyin Pu thanks the reviewers for their assistance in evaluating this paper.

## References

- Angelopoulos, V. (2009), The THEMIS mission, Space Sci. Rev. , doi:10.1007/s11214-008-9336-1, in press.
- Aubry, M. P., C. T. Russell, and M. G. Kivelson (1970), Inward motion of
- the magnetopause before a substorm, J. Geophys. Res. , 75 , 7018-7031.
- Aubry, M. P., M. G. Kivelson, and C. T. Russell (1971), Motion and structure of the magnetopause, J. Geophys. Res. , 76 , 1673-1696.
- Auster, H. U., et al. (2007), ROMAP: Rosetta Magnetometer and Plasma Monitor, Space Sci. Rev. , 128 , 221-240, doi:10.1007/s11214-006-9033-x.
- Auster, H. U., et al. (2009), The THEMIS fluxgate magnetometer, Space Sci. Rev. , doi:10.1007/s11214-008-9365-9, in press.
- Berchem, J., and C. T. Russell (1982), The thickness of the magnetopause current layer: ISEE 1 and 2 observations, J. Geophys. Res. , 87 , 21082114.
- Biermann, L. (1951), Kometenschweife und solare Korpuskularstrahlung, Z. Astrophys. , 29 , 274-286.
- Bowe, G. A., M. A. Hapgood, M. Lockwood, and D. M. Willis (1990), Short-term variability of solar wind number density, speed and dynamic pressure as a function of the interplanetary magnetic field components: A survey over two solar cycles, Geophys. Res. Lett. , 17 , 1825-1828.
- Cahill, L. J., and P. G. Amazeen (1963), The boundary of the geomagnetic field, J. Geophys. Res. , 68 , 1835-1843.
- Chapman, S., and V. C. A. Ferraro (1931), A new theory of magnetic storms: 1. The initial phase, J. Geophys. Res. , 36 (77-97), 171-186.
- de Keyser, J. (2005), The Earths magnetopause: Reconstruction of motion and structure, Space Sci. Rev. , 121 , 225-235, doi:10.1007/s11214-0066731-3.
- Elphic, R. C., and C. T. Russell (1979), ISEE-1 and 2 magnetometer observations of the magnetopause, in Magnetospheric Boundary Layers , edited by J. Lemaire, Eur. Space Agency Spec. Publ., ESA-SP , 148 , 43 - 50.
- Elphic, R. C., and D. J. Southwood (1987), Simultaneous measurements of the magnetopause and flux transfer events at widely separated sites by AMPTE UKS and ISEE 1 and 2, J. Geophys. Res. , 92 , 13,666-13,672.
- Fairfield, D. H. (1971), Average and unusual locations for the Earths magnetopause and bow shock, J. Geophys. Res. , 76 , 6700-6716.
- Formisano, V., V. Domingo, and K.-P. Wenzel (1979), The three-dimensional shape of the magnetopause, Planet. Space Sci. , 27 , 1137-1149, doi:10.1016/0032-0633(79)90134-X.
- Fujita, S., K. H. Glassmeier, and K. Kamide (1996), MHD waves generated by the Kelvin-Helmholtz instability in a nonuniform magnetosphere, J. Geophys. Res. , 101 , 27,317-27,326, doi:10.1029/96JA02676.
- Glassmeier, K.-H., D. Klimushkin, C. Othmer, and P. Mager (2004), ULF waves at Mercury: Earth, the giants, and their little brother compared, Adv. Space Res. , 33 , 1875-1883, doi:10.1016/j.asr.2003.04.047.
- Glassmeier, K.-H., et al. (2008), Magnetospheric quasi-static response to the dynamic magnetosheath: A THEMIS case study, Geophys. Res. Lett. , 35 , L17S01, doi:10.1029/2008GL033469.
- Haaland, S., et al. (2004a), Four-spacecraft determination of magnetopause orientation, motion and thickness: Comparison with results from singlespacecraft methods, Ann. Geophys. , 22 , 1347-1365.
- Haaland, S., B. U. O ¨ . Sonnerup, M. W. Dunlop, E. Georgescu, G. Paschmann, B. Klecker, and A. Vaivads (2004b), Orientation and motion of a discontinuity from Cluster curlometer capability: Minimum variance of current density, Geophys. Res. Lett. , 31 , L10804, doi:10.1029/2004GL020001.
- Holzer, R. E., and J. A. Slavin (1978), Magnetic flux transfer associated with expansions and contractions of the dayside magnetosphere, J. Geophys. Res. , 83 , 3831-3839.
- Howe, H. C., Jr., and J. H. Binsack (1972), Explorer 33 and 35 plasma observations of magnetosheath flow, J. Geophys. Res. , 77 , 3334-3344. Ivchenko, N. V., D. G. Sibeck, K. Takahashi, and S. Kokubun (2000), A statistical study of the magnetosphere boundary crossings by the Geotail satellite, Geophys. Res. Lett. , 27 , 2881 - 2884, doi:10.1029/ 2000GL000020.
- Le, G., and C. T. Russell (1994), The thickness and structure of high beta magnetopause current layer, Geophys. Res. Lett. , 21 , 2451-2454.
- McFadden, J. P., C. W. Carlson, D. Larson, M. Ludlam, R. Abiad, B. Elliott, P. Turin, M. Marckwordt, and V. Angelopoulos (2009), The THEMIS ESA plasma instrument and in-flight calibration, Space Sci. Rev. , doi:10.1007/s11214-008-9440-2, in press.
- McKenzie, J. F. (1981), Stability of planetary magnetospheric boundaries and mechanisms leading to leakage across them, Adv. Space Res. , 1 , 111-122, doi:10.1016/0273-1177(81)90094-6.
- Panov, E. V., J. Bu ¨chner, M. Fra ¨nz, A. Korth, S. P. Savin, H. Re `me, and K.-H. Fornac ¸on (2008), High-latitude Earths magnetopause outside the cusp: Cluster observations, J. Geophys. Res. , 113 , A01220, doi:10.1029/ 2006JA012123.
- Paschmann, G., S. Haaland, B. U. O ¨ . Sonnerup, H. Hasegawa, E. Georgescu, B. Klecker, T. D. Phan, H. Re `me, and A. Vaivads (2005), Characteristics of the near-tail dawn magnetopause and boundary layer, Ann. Geophys. , 23 , 1481-1497.
- Petrinec, S. M., and C. T. Russell (1996), Near-Earth magnetotail shape and size as determined from the magnetopause flaring angle, J. Geophys. Res. , 101 , 137-152, doi:10.1029/95JA02834.
- Phan, T. D., and G. Paschmann (1996), Low-latitude dayside magnetopause and boundary layer for high magnetic shear: 1. Structure and motion, J. Geophys. Res. , 101 , 7801-7816, doi:10.1029/95JA03752.
- Roelof, E. C., and D. G. Sibeck (1993), Magnetopause shape as a bivariate function of interplanetary magnetic field Bz and solar wind dynamic pressure, J. Geophys. Res. , 98 , 21,421-21,450.
- Russell, C. T., and R. C. Elphic (1978), Initial ISEE magnetometer results-Magnetopause observations, Space Sci. Rev. , 22 , 681-715.
- Safra ´nkova ´, J., Z. Nemecek, S. Dusı ´k, L. Prech, D. G. Sibeck, and N. N. Borodkova (2002), The magnetopause shape and location: A comparison of the Interball and Geotail observations with models, Ann. Geophys. , 20 , 301-309.
- Shue, J.-H., J. K. Chao, H. C. Fu, C. T. Russell, P. Song, K. K. Khurana, and H. J. Singer (1997), A new functional form to study the solar wind control of the magnetopause size and shape, J. Geophys. Res. , 102 , 9497-9512, doi:10.1029/97JA00196.
- Sibeck, D. G., W. Baumjohann, R. C. Elphic, D. H. Fairfield, and J. F. Fennell (1989), The magnetospheric response to 8-minute period strongamplitude upstream pressure variations, J. Geophys. Res. , 94 , 25052519.
- Sibeck, D. G., R. E. Lopez, and E. C. Roelof (1991), Solar wind control of the magnetopause shape, location, and motion, J. Geophys. Res. , 96 , 5489-5495.
- Song, P., R. C. Elphic, and C. T. Russell (1988), ISEE 1 and 2 observation of the oscillating magnetopause, Geophys. Res. Lett. , 15 , 744-747.
- Sonnerup, B. U. O., and L. J. Cahill Jr. (1967), Magnetopause structure and altitude from Explorer-12 observations, J. Geophys. Res. , 72 , 171-183. Southwood, D. J. (1968), The hydromagnetic stability of the magnetospheric boundary, Planet. Space Sci. , 16 , 587-605.
- Spreiter, J. R., A. L. Summers, and A. Y. Alksne (1966), Hydromagnetic flow around the magnetosphere, Planet. Space Sci. , 14 , 223-253.
- Tsyganenko, N. A. (1990), Quantitative models of the magnetospheric magnetic field-Methods and results, Space Sci. Rev. , 54 , 75-186.
- Walker, A. D. M. (1981), The Kelvin-Helmholtz instability in the lowlatitude boundary layer, Planet. Space Sci. , 29 , 1119 - 1133, doi:10.1016/0032-0633(81)90011-8.

               

                   

         

- V. Angelopoulos, Institute of Geophysics and Planetary Physics, University of California, Box 951567, 2712 Geology Building, Los Angeles, CA 90095-1567, USA.
- H. U. Auster, O. D. Constantinescu, K.-H. Fornac ¸on, K.-H. Glassmeier, and F. Plaschke, Institut fu ¨r Geophysik und Extraterrestrische Physik, TU Braunschweig, Mendelssohnstrasse 3, D-38106 Braunschweig, Germany. (f.plaschke@tu-bs.de)
- E. Georgescu, Max-Planck-Institut fu ¨ r Sonnensystemforschung, MaxPlanck-Strasse 2, D-37191 Katlenburg-Lindau, Germany.
- W. Magnes and R. Nakamura, Space Research Institute, Austrian Academy of Sciences, Schmiedlstrasse 6, A-8042 Graz, Austria.
- J. P. McFadden, Space Sciences Laboratory, University of California, 7 Gauss Way, Berkeley, CA 94720-7450, USA.