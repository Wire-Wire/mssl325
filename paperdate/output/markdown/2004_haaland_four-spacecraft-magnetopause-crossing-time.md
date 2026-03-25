<!-- image -->

## Four-spacecraft determination of magnetopause orientation, motion and thickness: comparison with results from single-spacecraft methods

- S. E. Haaland 1,5 , B. U. ¨ O. Sonnerup 2 , M. W. Dunlop 3 , A. Balogh 4 , E. Georgescu 5 , H. Hasegawa 2 , B. Klecker 5 ,

G. Paschmann 1,5 , P. Puhl-Quinn 5 , H. R` eme 6 , H. Vaith 5 , and A. Vaivads 7

1 International Space Science Institute (ISSI), Bern, Switzerland

2 Dartmouth College, Hanover, NH, USA

3 Rutherford-Appleton Labs, Oxford, UK

4 Imperial College, London, UK

5 Max-Planck Institute f¨ ur extraterrestrische Physik (MPE), Garching, Germany

6 Centre d' ´ Etude Spatiale des Rayonnements (CESR), Toulouse, France

7 Swedish Institute of Space Physics, Uppsala, Sweden

Received: 7 April 2003 - Revised: 2 September 2003 - Accepted: 8 October 2003 - Published: 2 April 2004

Abstract. In this paper, we use Cluster data from one magnetopause event on 5 July 2001 to compare predictions from various methods for determination of the velocity, orientation, and thickness of the magnetopause current layer. We employ established as well as new multi-spacecraft techniques, in which time differences between the crossings by the four spacecraft, along with the duration of each crossing, are used to calculate magnetopause speed, normal vector, and width. The timing is based on data from either the Cluster Magnetic Field Experiment (FGM) or the Electric Field Experiment (EFW) instruments. The multi-spacecraft results are compared with those derived from various singlespacecraft techniques, including minimum-variance analysis of the magnetic field and deHoffmann-Teller, as well as Minimum-Faraday-Residue analysis of plasma velocities and magnetic fields measured during the crossings. In order to improve the overall consistency between multi- and single-spacecraft results, we have also explored the use of hybrid techniques, in which timing information from the four spacecraft is combined with certain limited results from single-spacecraft methods, the remaining results being left for consistency checks. The results show good agreement between magnetopause orientations derived from appropriately chosen single-spacecraft techniques and those obtained from multi-spacecraft timing. The agreement between magnetopause speeds derived from single- and multi-spacecraft methods is quantitatively somewhat less good but it is evident that the speed can change substantially from one crossing to the next within an event. The magnetopause thickness varied

substantially from one crossing to the next, within an event. It ranged from 5 to 10 ion gyroradii. The density profile was sharper than the magnetic profile: most of the density change occured in the earthward half of the magnetopause.

Key words. Magnetospheric physics (magnetopause, cusp and boundary layers; instruments and techniques) - Space plasma physics (discontinuities)

## 1 Introduction

The magnetopause, its orientation, motion, and structure, have been studied extensively since this electric current layer, marking the outer boundary of Earth's magnetic field, was first discovered in the early sixties (Cahill and Amazeen, 1963). However, it has not been a simple matter to obtain reliable information from single-spacecraft data. The two spacecraft, ISEE 1 and 2, operating in the late seventies and early eighties, provided greatly expanded opportunities for magnetopause studies and led to new and convincing results, for example, concerning the current layer motion and thickness (Berchem and Russell, 1982). We refer the reader to that paper for the ISEE-based techniques and results, and for a brief summary of various single-spacecraft methods employed in the sixties and seventies to estimate magnetopause speeds and thicknesses. In the eighties and nineties, two new methods were added: the normal component of the deHoffmann-Teller (HT) frame velocity (Sonnerup et al., 1987) and the related Minimum Faraday Residue (MFR) method (Terasawa et al., 1996), based on the constancy of the tangential electric field in a frame moving with

the magnetopause. Both methods employ plasma and magnetic field data to calculate the convection electric field. Recently, results from these two methods were compared with magnetopause velocities derived from time delays of the passage of the boundary across the spacecraft pair AMPTE/IRM and AMPTE/UKS (Bauer et al., 2000).

One of the important objectives of the four-spacecraft Cluster mission is to allow for the determination of the orientation, speed, and thickness of the magnetopause current layer without use of single-spacecraft techniques that employ measured plasma velocities, since, at least in the past, plasma measurements generally have had larger experimental uncertainties than, for example, magnetic field measurements. To obtain the sought-after information from the timing of the passage of the magnetopause, a minimum of four observing spacecraft is needed. Even then, the determination from timing information alone has unavoidable ambiguities (Dunlop and Woodward, 1998, 2000), as will be discussed further in the present paper. The required timing information can be obtained from any quantity measured at sufficient time resolution by all four spacecraft, provided a well-defined change in that quantity occurs at the magnetopause. In the present paper timing from magnetic field measurements, as well as from plasma density measurements, is used.

Amethod, based on timing alone, for determination of the orientation, speed and thickness of a discontinuity moving past four observing spacecraft was first presented by Russell et al. (1983), who applied it to interplanetary shocks. Their method uses the measured time differences between the passage of the discontinuity over the spacecraft, along with the known separation vectors between them and, to obtain the discontinuity thickness, the duration of each crossing. The basic assumptions underlying the technique are that the velocity and orientation of the discontinuity, assumed planar, remain constant during the entire interval of its passage over the four spacecraft. We shall refer to this technique as the Constant Velocity Approach (CVA). It has been reviewed recently by Harvey (1998) and Schwartz (1998), and has become a frequently used tool in the interpretation of magnetopause data from the four Cluster spacecraft. The CVA frequently predicts substantial differences in the magnetopause thickness for the four spacecraft crossings in an event.

The assumption in CVA of a constant velocity is well justified for interplanetary discontinuities but is problematic for the magnetopause, which has been observed from singlespacecraft to abruptly move in and then out again, indicating rapid and large changes in its velocity. Such behavior follows from the fact that a patch of magnetopause of unit area, 1 km 2 , say, has extremely low mass, while the magnetosheath pressure to which it is exposed undergoes rapid, and sometimes substantial fluctuations. Under typical conditions (total pressure = 1 nPa; N = 15 protons/cm 3 ; thickness d = 500 km; γ = cp / cv =2), a pressure imbalance of 10% will produce an acceleration of about 8 km/s 2 but an accompanying thickness change of only some 2.4% (12 km). This result suggests that it may be desirable to use the assumption of a constant thickness rather than a constant velocity. We de- velop and use this approach in the present paper and refer to it as the Constant Thickness Approach (CTA). However, as we shall see, large thickness variations during a Cluster magnetopause event can by no means be excluded. If present, such variations must have been caused by convective or internal effects, such as time dependent reconnection, rather than by one-dimensional compression or expansion. The CTA frequently predicts substantial changes in magnetopause speed over relatively short time intervals.

In two recent papers, Dunlop et al. (2001, 2002) have concluded from studies of Cluster magnetopause events that the magnetopause speed was usually not constant during an event but could change drastically over times of the order of a minute or less, whereas the thickness showed more modest variations. The method employed in reaching this conclusion makes use of magnetopause normal vectors obtained from minimum variance analysis of the magnetic field data taken during each of the four crossings, in addition to the timing information. It leads to the determination of both the magnetopause speeds and thicknesses. This method and its underlying assumptions have been described by Dunlop and Woodward (1998, 2000). It is referred to as the Discontinuity Analyzer (DA) and will be employed in the present paper, albeit in a form that deviates somewhat from the original version.

The main purpose of our paper is to compare the results from CVA, CTA, and DA with each other and with results from various single-spacecraft techniques. We will also examine simple modifications of CVA, CTA, and DA that can be implemented to improve the consistency with singlespace-craft methods. The presentation is organized as follows. Details of the CVA, CTA, and DA methods are presented in Sect. 2. In Sect. 3, data from the fluxgate magnetometer (FGM) experiments (Balogh et al., 2001), from the ion spectrometer (CIS) experiments (R` eme et al., 2001), and from the electric field wave (EFW) experiments (Gustafsson et al., 2001) on board the Cluster spacecraft, are presented for a benchmark case: an encounter of the four spacecraft with the magnetopause on 5 July 2001, in the approximate interval 06:21-06:27 UT. Magnetopause velocities derived from CVA, CTA, and DA, are presented in Sect. 4 and compared with velocities obtained from single-spacecraft methods. The comparison leads to the conclusion that certain modifications of CVA, CTA, and DA are desirable. These modifications, which involve use of plasma velocities measured by the Cluster ion spectrometer (CIS/HIA) on board spacecraft 3 (C3), are also implemented and tested in Sect. 4. They are denoted by CVAM, CTAM and DAM. In Sect. 5, we present our results for magnetopause orientations, thicknesses, and normal magnetic field components. Section 6 contains a discussion of our findings and their implications for methodology, as well as for magnetospheric physics. Section 7 contains a summary of our main conclusions. Certain details of our methods for determining magnetopause crossing times and crossing durations are discussed in the Appendix.

## 2 Multi-spacecraft methods

A magnetopause event seen by Cluster consists of four complete individual magnetopause crossings, one by each of the spacecraft (C1-C4). We order these crossings according to increasing time, with the first crossing (CR0) at center time t = t 0 = 0, the second crossing (CR1) at t = t 1 ≥ t 0, the third (CR2) at t = t 2 ≥ t 1 , and the final crossing (CR3) at t = t 3 ≥ t 2. (In the event to be analyzed here, the corresponding spacecraft ordering will be C4, C1, C2, and C3.)

Weexpress the instantaneous velocity, V(t) , of the magnetopause as a function of time in terms of the following polynomial

<!-- formula-not-decoded -->

where Ai , i = 0 , 1 , 2 , 3, are constants to be determined from the timing data. Equation (1) may be thought of as producing a kind of low-pass filtered description of the magnetopause motion during the event. It is possible that contributions from higher frequencies are substantial, at least in some cases. In two of the methods to be used here, the polynomial is of lower order: in CVA we set A 1, A 2, and A 3 equal to zero and in DA we set A 3 = 0.

With the above expression for V(t), we find the magnetopause thicknesses, di (i = 0 , 1 , 2 , 3 ) , to be

<!-- formula-not-decoded -->

where the square bracket on the right represents the average magnetopause speed, V ave i , during crossing CR i , which has center time t i and duration 2 τi . In other words,

<!-- formula-not-decoded -->

The distance travelled by the magnetopause, between crossing CR i and crossing CR0 along a fixed normal direction, n , is then

<!-- formula-not-decoded -->

where R i (i = 1 , 2 , 3 ) is the position vector of the spacecraft that experiences crossing CR i relative to the spacecraft that encounters the first magnetopause crossing (CR0) in the event. For simplicity, we assume R i to be independent of time during the event.

The Eqs. (1)-(4) are common to the various methods we will investigate but, from this point on, each technique must be described separately.

## 2.1 Constant velocity approach: CVA

In this approach (Russell et al., 1983) we put A 1 = A 2 = A 3 = 0 so that the magnetopause velocity is constant during the event: V(t) = A 0. Equation (4) then becomes

<!-- formula-not-decoded -->

where the vector m is defined by

<!-- formula-not-decoded -->

The three Eqs. (5) can be solved for the three components of m and, since | n | 2 = 1, we then obtain the velocity V(t) = A 0 = 1 / | m | and n = m A 0. From Eq. (2) one finds the individual magnetopause thicknesses to be simply di = 2 τi A 0.

A modified version of CVA, referred to as CVAM, will also be used, in which a constant acceleration of the magnetopause is included via a nonzero value of the coefficient A 1 = k CVAM A 0 in Eq. (1). The constant k CVAM can be determined by requiring the average magnetopause velocity during one of the crossings (in our example, the C3 traversal), derived from CVAM, to agree with the velocity along the normal, deduced from the plasma instrument on board that spacecraft (in our example, CIS/HIA on board C3), except for an adjustment to account for any reconnection-associated flow across the magnetopause.

## 2.2 Constant thickness approach: CTA

In this case, we first solve the four Eqs. (2) for the four quotients Ai/d(i = 0 , 1 , 2 , 3 ) , where d is the constant, but presently unknown, magnetopause thickness during the event. By substitution of the resulting Ai/d values into Eq. (4) we then find

<!-- formula-not-decoded -->

where M = n /d . Again, this set of three equations can be solved for M , whereupon d = 1 / | M | and n = M d . The four coefficients Ai are then known, and the average magnetopause velocity during each of the four crossings can be calculated from Eq. (3).

This method will also be modified (to CTAM) by allowing the magnetopause thickness observed at one (or possibly two) selected spacecraft to be different, by a multiplicative factor, k CTAM, from the common thickness at the other three (two) spacecraft. The factor k CTAM is determined by requiring the average magnetopause speed, obtained from CTAM at one spacecraft (in our case C3), to agree with the corresponding plasma result, appropriately adjusted for any reconnection-associated flow across the magnetopause.

## 2.3 Discontinuity analyzer: DA

In its simplest form, this approach is based on the fact that n can be determined from minimum variance analysis (with

use Orientation and Motion

Table 1. Overview of methods, and their acronyms, and symbols. 4 Haaland et al.: Four Spaccraft Determination of Magnetopa

|                          |                           |                                                                    | MP parameters returned    | MP parameters returned    | MP parameters returned    |
|--------------------------|---------------------------|--------------------------------------------------------------------|---------------------------|---------------------------|---------------------------|
| Symbol                   | Acronym                   | Method                                                             | Normal                    | Speed                     | Acceleration              |
|                          | Single spacecraft methods | Single spacecraft methods                                          | Single spacecraft methods | Single spacecraft methods | Single spacecraft methods |
|                          | MVAB                      | Minimum Variance Analysis of magnetic field                        | Yes                       | No                        | No                        |
|                          | MVABC                     | Minimum Variance Analysis with constraint 〈 B 〉 · n = 0          | Yes                       | No                        | No                        |
|                          | MFR †                     | Minimum Faraday Residue analysis                                   | Yes                       | Yes                       | No                        |
|                          | MFRC                      | Minimum Faraday Residue analysis with constraint 〈 B 〉 · n = 0   | Yes                       | Yes                       | No                        |
|                          | HT §                      | DeHoffmann-Teller analysis                                         | No                        | Yes                       | Yes                       |
|                          | CIS                       | Plasma velocity along n from the CIS instruments                   | No                        | Yes                       | No                        |
| Multi spacecraft methods | Multi spacecraft methods  | Multi spacecraft methods                                           | Multi spacecraft methods  | Multi spacecraft methods  | Multi spacecraft methods  |
|                          | Model                     | Model magnetopause                                                 | Yes                       | No                        | No                        |
|                          | Nbull                     | Origin for polar plots (Figure 5). Averaged MVABC from all four SC | Yes                       | No                        | No                        |
|                          | CVA                       | Constant Velocity Approach                                         | Yes                       | Yes                       | No                        |
|                          | CVAM                      | Constant Velocity Approach, modified so that V = V CIS ∗ for C3    | Yes                       | Yes                       | Yes                       |
|                          | CTA                       | Constant Thickness Approach                                        | Yes                       | Yes                       | Yes                       |
|                          | CTAM                      | Constant Thickness Approach - modified so that V = V CIS ∗ for C3  | Yes                       | Yes                       | Yes                       |
|                          | DA                        | Discontinuity analyzer                                             | No                        | Yes                       | Yes                       |
|                          | DAM                       | Discontinuity analyzer - modified so that V = V CIS ∗ for C3       | No                        | Yes                       | Yes                       |

- † The Minimum Faraday Residue method (Khrabov and Sonnerup, 1 998a) is based on conservation of Faraday's law across a curr ent sheet. It returns a direction and a velocity of the magnetopa use current layer.
- § DeHoffmann-Teller analysis (Khrabov and Sonnerup, 1998b) returns a frame of reference in which the electric field vanis hes (or nearly vanishes). The speed of this frame relative to the spacecraft frame can then be regarded as the speed of a rigid structure, e.g., the magnetopause current layer.

∗ V CIS is adjusted for reconnection flow.

Single-spacecraft normals (Panel c and d)

Table 1.

Overview of methods, and their acronyms, and symbols.

maximum and then drops abruptly to its low magneto derived from DAM, to agree with the reconnection-adjusted normal plasma velocity from one of the spacecraft (in our case C3).

lobe level near the inner edge of the magnetic field At the same time, the plasma temperature increase anisotropy factor indicates a transition from T &lt; T ⊥ , as For convenient reference, a summary of methods, with their corresponding acronyms and symbols are given in Table 1.

||

## pected in the high-latitude/tail magnetosheath, T ‖ &gt; 2.4 Center time and crossing time

Single-spacecraft normals (Panel c and d) approximately [-6.8, -15.0, 6.2] R E GSE. The magnetopause moved inward past the four spacecraft, which therefore observed a transition from magnetospheric to magnetosheath conditions. This same event has also been analyzed by Dunlop (2003), using the original version of DA. And two-dimensional structures within the magnetopause in this same event have been examined by Hasegawa et al. (2003), using the Grad-Shafranov based reconstruction technique, as deor without the constraint 〈 B 〉· n = 0, where 〈 B 〉 is the average magnetic field measured during the magnetopause crossing) of the magnetic data in each crossing, and requiring that these four normals are nearly aligned so that a single, average normal can be used. In our application of DA, which differs slightly from the way it was originally described (and later used) by Dunlop and Woodward (1998), we put A 3 = 0 and use Eqs. (4) to calculate A 0, A 1, and A 2. The average magnetopause velocity at each of the four crossings is then obtained from Eq. (3), with A 3 = 0. The magnetopause thickness for each crossing is obtained from Eq. (2).

in the magnetosphere. The plasma velocity also dr scribed by Hu and Sonnerup (2002). Figure 1 contains an overview of magnetic field and plasma data during the event. The top three panels show the GSE magnetic field components (Balogh et al., 2001) at 4s resolution, for each of the four spacecraft, while the following three panels show plasma density, parallel and perpendicul temperatures for C1 and C3, and temperature anisotropy facThe additional knowledge of n provides the advantage of allowing the determination of both the velocity and the thickness for each crossing. The disadvantage is that the time dependence of the magnetopause velocity is parabolic rather than cubic, which is considerably more restrictive and, as we shall see, severely limits the ability to realistically describe the actual (albeit effectively low-pass filtered) magnetopause velocity variations during an event.

magnetosheath-like plasma, immediately earthwa magnetopause indicates, either that the event wa close to the reconnection site, or that the reco was small, or that the reconnection configuration dependent and spatially localized to a small part After suitable preprocessing of the data, described in the Appendix, we perform a cross correlation between the maximum variance field component (or the density) in crossing CR0 and the corresponding component (density profile) in CR1, CR2, and CR3, in order to establish their optimal center crossing times, t i (i = 1 , 2 , 3 ) , relative to CR0.

ar tisunward flow at about 100 km/s in the lobe. This occurs over the entire magnetopause width. For C3, the plasma momentum changes across the m topause are consistent with the occurrence of re the slope of the regression line in a plot of pl ity components in the HT frame versus the corres Alfv´ en velocity components is +1.03 (this so-ca correlation plot is presented for our event in Has 2003). This result, including the positive sign, presence of reconnection flow that is parallel (as antiparallel) to the magnetic field. For the exp ward plasma transport across the magnetopause, it earthward directed normal magnetic field componen ever, the absence of a substantial boundary layer The center time, t i , and crossing time, 2 τi , for each crossing enters into the calculations and must be determined according to a uniquely specified and consistent procedure. When FGMdata are used for the timing, our method consists of first identifying a data interval, for each spacecraft, that includes the main magnetic field transition in the magnetopause, as well as short adjoining regions in the magnetosphere and magnetosheath in which the field is more or less constant. Standard variance analysis (see, e.g. Sonnerup and Scheible, 1998) is performed on the combined set of measured field vectors for the four intervals, and the field component along the resulting maximum variance eigenvector is plotted as a function of time for each spacecraft. When EFW timing is used, time plots of the inferred plasma density are used in place of the maximum variance magnetic field component.

tor, A p = ( T || /T ⊥ -1) from the CIS/HIA instrument (R` eme et al., 2001). The bottom three panels show the GSE velocity components at the standard 4s spin resolution from the CIS/HIA instrument for C1 and C3 and from CIS/CODIF for C4. For C1 and C3, the proton velocities derived from CIS/CODIF (not shown) are in good agreement with those The DA calculation can also be performed by use of individual normal vectors determined for each of the crossings. In Eq. (4) we then replace the common normal n by the average normal from two adjoining crossings, at t = t i and t = t i + 1, say. We also replace R i by ( R i + 1 -R i ) and perform the integration from t i to t i + 1.

from CIS/HIA. No CIS plasma data are obtained from C2. The event displays an unambiguous transition from the hot, tenuous magnetospheric plasma to the cool, dense magnetosheath plasma. This is a true magnetopause event and A modified version (DAM) of DA will also be used, in which a nonzero coefficient A 3 in Eq. (1) is incorporated to yield a cubic velocity curve. As before, this coefficient is determined by requiring the average magnetopause speed, not simply a current layer in the magnetosheath.

Further- netopause.

For the crossing by C1 the Wal´ en slop

+0.57 (Hasegawa et al., 2003). The interpretatio sult is not clear but it may indicate that incipient

more, except for a narrow density foot, seen by C1 but not

C3 on the magnetospheric side, there is no evidence in Fig-

Next, the duration of the crossings are determined. Several methods are conceivable here; we found the following method to give the most reliable results; first, select the crossing, i = p , say, whose time profile of the maximum variance field component best fits a chosen functional form, in our case the following temporal hyperbolic tangent curve:

<!-- formula-not-decoded -->

and by a least-squares fitting determine the actual optimal value of τp for this particular crossing. (For density data, a formula similar to Eq. (8) is employed.)

Time profiles from the other crossings are stretched (longer duration) or compressed (shorter duration) versions of the above. The amount of stretching, ki , is determined through a least-square minimization scheme (see Appendix). By use of these stretching factors, ki , we now can determine the τi value, and thus the optimal fit of the hyperbolic tangent profile (8), for each of the four crossings.

The hyperbolic tangent curve has the property that 76% of the total field change, /Delta1B max, (or density change, /Delta1N ) occurs within a time interval 2 τi . The magnetopause thicknesses given in our paper are defined in this fashion. Note that the most suitable functional form for characterization of the magnetopause transition may vary from event to event but should be the same for all four crossings within an event.

## 3 Test case

We now apply the CVA, CTA, and DA methods to a magnetopause event observed by Cluster on 5 July 2001, in the interval 06:21-06:27 UT, when the spacecraft constellation was located on the dawnside flank of the magnetosphere at approximately [ -6.8, -15.0, 6.2] RE GSE. The magnetopause moved inward past the four spacecraft, thereby observing a transition from magnetospheric to magnetosheath conditions. This same event has also been analyzed by Dunlop (private communication, 2003), using the original version of DA. In addition, two-dimensional structures within the magnetopause in this same event have been examined by Hasegawa et al. (2003), using the Grad-Shafranov based reconstruction technique, as described by Hu and Sonnerup (2003).

Figure 1 contains an overview of the magnetic field and plasma data during the event. The top three panels show the GSE magnetic field components (Balogh et al., 2001) at 4-s resolution, for each of the four spacecraft, while the following three panels show plasma density, parallel and perpendicular temperatures for C1 and C3, and temperature anisotropy factor, Ap = (T || /T ⊥-1 ) from the CIS/HIA instrument (R` eme et al., 2001). The bottom three panels show the GSE velocity components at the standard 4-s spin resolution from the CIS/HIA instrument for C1 and C3 and from CIS/CODIF for C4. For C1 and C3, the proton velocities derived from CIS/CODIF (not shown) are in good agreement with those from CIS/HIA. No CIS plasma data are obtained from C2.

The event displays an unambiguous transition from the hot, tenuous magnetospheric plasma to the cool, dense magnetosheath plasma. This is a true magnetopause event and not simply a current layer in the magnetosheath. Furthermore, except for a narrow density foot, seen by C1 but not C3 on the magnetospheric side, there is no evidence in Fig. 1 of a boundary layer, populated by magnetosheath-like plasma, and located immediately earthward of the magnetopause. If one moves inward across the magnetopause, i.e. from right to left in the figure, the plasma density first has a maximum and then drops abruptly to its low magnetospheric lobe level near the inner edge of the magnetic field transition. At the same time, the plasma temperature increases and the anisotropy factor indicates a transition from T || &lt;T ⊥ , as expected in the high-latitude/tail magnetosheath, to T ‖ &gt;T ⊥ in the magnetosphere. The plasma velocity also drops to antisunward flow at about 100 km/s in the lobe. This drop-off occurs over the entire magnetopause width.

For C3, the plasma momentum changes across the magnetopause are consistent with the occurrence of reconnection: the slope of the regression line in a plot of plasma velocity components in the HT frame versus the corresponding Alfv´ en velocity components is +1.03 (this so-called Wal´ en correlation plot is presented for our event in Hasegawa et al., 2003). This result, including the positive sign, indicates the presence of reconnection flow that is parallel (as opposed to antiparallel) to the magnetic field. For the expected earthward plasma transport across the magnetopause, it implies an earthward directed normal magnetic field component. However, the absence of a substantial boundary layer, containing magnetosheath-like plasma, immediately earthward of the magnetopause, indicates either that the event was observed close to the reconnection site, or that the reconnection rate was small, or that the reconnection configuration was time dependent and spatially localized to a small part of the magnetopause. For the crossing by C1 the Wal´ en slope is only +0.57 (Hasegawa et al., 2003). The interpretation of this result is not clear but it may indicate that incipient reconnection was at hand during this traversal.

The four complete magnetopause traversals are followed by two brief intervals (around 06:25:50 UT and 06:27:30 UT) in the magnetosheath, where the data suggest either the passage of an FTE-like structure, or a partial re-entry into the magnetopause layer. These intervals will not be analyzed here.

The top panel in Fig. 2 shows the maximum variance field component seen by each spacecraft and the hyperbolic tangent curve optimally fitted to the field data, as described in Sect. 2.4. The fit is excellent for C1 and C4 but less good for C2 and C3, where substantial positive and negative deviations from the hyperbolic curve are present within the main magnetopause transition, in particular on its magnetosheath side. We do not know whether the fluctuations are caused by 2D/3D local structures or by rapid changes, including brief reversals, of the magnetopause motion. The Bx and Np

Fig. 1. Time plots of prime-parameter quantities measured by Cluster spacecraft (C1-C4) at the magnetopause on 5 July 2001, 06:18-06:30 UT. Top three panels: GSE magnetic field components from FGM experiments. Middle three panels: plasma density Np , temperatures T ‖ and T ⊥ , and anisotropy factor Ap = (T ‖ /T ⊥-1 ) from CIS/HIA experiments. Bottom three panels: GSE plasma velocity components from CIS/HIA (C1 and C3) and CIS/CODIF (C4). Color code: black=C1; red=C2; green=C3; blue=C4.

<!-- image -->

Cluster Magnetic Field

-30 2 -10 0 10 20 30 No data Fig. 2. Fitting of hyperbolic tangent curves for magnetopause encounters by Cluster on 5 July 2001, 06:22:30-06:25:30 UT. Top panel: fitting to maximum variance magnetic field component (6-s sliding averages at 0.2-s resolution). Bottom panel: Fitting to plasma density data, derived from EFW instruments (4-s sliding averages at 0.2-s resolution). Color code as in Fig. 1.

<!-- image -->

0622:30

0623:00

0623:30

panels of Fig. 1 show possible evidence of a brief velocity reversal at C3 around 06:24:20-06:24:25 UT. There is a similar but slightly delayed Bx signature at C2 but the timing relative to C3 is not consistent with simple outward/inward motion of a plane magnetopause layer. The optimal data window we arrive at from the procedure described in Sect. 2.4 and in the Appendix is such that these features are suppressed; this implies the interpretation that they are not produced by velocity reversals and, therefore, should not be allowed to influence the CTA velocity determination. Comparison with singlespacecraft determinations of the magnetopause speed, to be discussed later in the paper, tends to confirm this conclusion.

The bottom panel in Fig. 2 shows the corresponding results for the EFW density data, estimated from the spacecraft potentials (Gustafsson et al., 2001). The density ramps are steep and well defined, albeit with a distinct, low-density 'foot' structure (boundary layer), seen by C4, C1, and C2 on the magnetospheric side and a maximum in the middle of the magnetopause, followed by pulsations in the magnetosheath. Although these features in the EFW density profiles may be somewhat contaminated by spin-modulation of the spacecraft potential, comparison with the CIS/HIA densities from C1 and C3, shown in Fig. 1, indicates that they are, for the most part, real. The density foot, density max-

0624:00

0624:30

0625:00

0625:30

imum, and magnetosheath pulsations notwithstanding, the EFW-based timing for this event has less ambiguity than the timing obtained from FGM.

The center times, t i , and durations, 2 τi , for the four crossings, determined as described in Sect. 2.4, are given for FGM and EFW in Table 2, along with the spacecraft separation vectors, Ri , relative to C4. The durations, 2 τi , derived from EFW are shorter than those from FGM because the density ramp occupies only the earthward portion of the total current layer thickness. But there are also significant differences in the center times, t i , derived from the FGM and the EFW data. In particular, the time lapse between the first (C4) and the last (C3) crossing in the event is some 8 s shorter for the EFW timing. The probable explanation for this discrepancy is that, in approximate terms, the density ramp maintains its thickness and location near the inner edge of the magneticfield transition, while the magnetic structure in the middle and outer portions of the current layer increases its width substantially sometime after the second (C1) but before the last (C3) crossing.

In Sects. 4 and 5, we present an overview of the results from the various multi-spacecraft and single-spacecraft techniques. Discussion of the results is given in Sect. 6.

Table 2. Separation distances, Ri , (GSE), crossing durations, 2 τ i , and center crossing times, t i , relative to the the C4 crossing.

|                             | Spacecraft   | Spacecraft   | Spacecraft   | Spacecraft   |
|-----------------------------|--------------|--------------|--------------|--------------|
| Parameter                   | C1           | C2           | C3           | C4           |
| R x [km]                    | 1669.0       | - 387.0      | 724.0        | 0.0          |
| R y [km]                    | 1622.0       | 1580.0       | 2513.0       | 0.0          |
| R z [km]                    | 1290.0       | 1224.0       | - 401.0      | 0.0          |
| Crossing time, t i (FGM)[s] | 6.7          | 33.5         | 44.4         | 0.0          |
| Duration 2 τ i (FGM) [s]    | 8.02         | 17.34        | 16.76        | 8.80         |
| Crossing time, t i (EFW)[s] | 6.15         | 28.35        | 36.80        | 0.00         |
| Duration 2 τ i (EFW) [s]    | 3.70         | 3.96         | 4.72         | 3.78         |

## 4 Magnetopause speed

## 4.1 Speeds from CVA, CTA, and DA

The magnetopause velocity obtained from CVA is -40 km/s for FGM timing and -48 km/s for EFW timing, the negative sign indicating that, as required for a transition from the magnetosphere to the magnetosheath, the motion is earthward, i.e. it is opposite to the direction of the magnetopause normal vector. The CTA and DA methods both give curves representing the inferred instantaneous (but heavily low-pass filtered) magnetopause velocity as a function of time during the event. These curves are shown in Fig. 3, both for FGM timing (upper panel) and for EFW timing (lower panel). To facilitate intercomparison of FGM- and EFW-based results, the time axis for the EFW-based curves has been stretched so that their end time at C3 is the same as for the FGM-based curves.

By use of Eq. (3) at the four crossings, i.e. at t = t i (i = 0 , 1 , 2 , 3 ) , one can calculate the predicted average velocity during each crossing, i.e. the average over the time interval from ( t i -τi ) to ( t i + τi ). These results, which are appropriate for comparison with the plasma measurements, are shown by symbols in the figure (filled crosses for CV A, filled circles for CTA, and filled semicircles for DA). Except for CVA (and, later on, CVAM), these points usually do not fall exactly on their corresponding curves. This is a consequence of the curvature of the curves. The agreement between the results from CVA, CTA, and DA is seen to be fair to poor. The main disagreement occurs at the last crossing (C3). However, except for DA at C3, all three approaches show negative velocities, as required. And, on average, the velocity magnitudes are in a believable range. We also note that CTA and DAboth show outward acceleration of the magnetopause, i.e. a slowing down of its inward motion, in the interval between the center times for the crossings by C1 and C2. We return to this feature in Sect. 6.

## 4.2 Speeds from single-spacecraft techniques

Figure 3 also shows results from single-spacecraft determinations of the magnetopause velocity, using CIS/HIA plasma data for C1, C3, and CIS/CODIF (H + ) data for C4. For each spacecraft, the results from three methods are given.

First, three velocity vectors measured by CIS/HIA (for SC4; CIS/CODIF) in the middle of, or bracketing, the magnetopause are averaged and dotted into the corresponding individual normal vector for the crossing, determined from minimum variance analysis of the measured magnetic field during the crossing (MVAB; e.g. Sonnerup and Scheible, 1998) but with the constraint added that the average normal magnetic field component be zero (MVABC; for further discussion, see Sect. 5). The results are denoted by 'CIS' in the figure. This procedure should provide the velocity of a tangential discontinuity, across which no plasma flow occurs. In the presence of reconnection and the associated plasma flow across the magnetopause, from the magnetosheath to the magnetosphere, the plasma flow along the negative normal direction should be larger than the actual inward magnetopause speed by an amount of the order of the Alfv´ en speed based on 〈 B 〉· n , the average normal component of the magnetic field. This correction should be kept in mind for C3. Its magnitude is estimated to be about 10 km/s.

Second, the normal velocities obtained from the unconstrained and constrained ( 〈 B 〉· n = 0 ) Minimum-FaradayResidue technique (Khrabov and Sonnerup, 1998a) are shown, and are denoted in the figure by 'MFR' and 'MFRC', respectively. The expectation is that for a tangential discontinuity, the results from MFR and MFRC should coincide. This behavior is obtained at C4 but not at C1, presumably as a consequence of some systematic errors in the prediction from MFR for this crossing. In both of these crossings, we believe the magnetopause was nearly a tangential discontinuity, a conclusion confirmed in the study by Hasegawa et al. (2003). At C3, their results illustrate that a reconnection-associated, inward-directed plasma flow across the magnetopause had developed in a region between an Xtype null in the transverse field and a large magnetic island. The inward speed from MFR should then represent the true magnetopause speed, while the inward speed from MFRC, which would represent the total plasma flow speed perpendicular to a tangential discontinuity type of magnetopause, should be larger by an amount equal to the Alfv´ en speed based on the normal component of the magnetic field and the density in the magnetosheath. This is in fact what the MFR and MFRC results show at C3, the difference between the two velocities being about 10 km/s, corresponding to a normal field component of about -1.6 nT. We estimate the purely statistical uncertainty in the MFR velocity to be about ± 2 km/s.

Finally, the deHoffmann-Teller velocities have been determined (see Khrabov and Sonnerup, 1998b) and then dotted into the individual normals from MVABC. These results are identified by the symbol 'HT' in Fig. 3. When used with

/BD Fig. 3. Magnetopause velocity curves, derived from multi-spacecraft timing in Fig. 2, using the constant velocity approach (CVA), the constant thickness approach (CTA), and the discontinuity analyzer approach (DA). Curves in the upper panel are based on FGM timing; those in the lower panel are based on EFW timing and are shown on a stretched time scale ( k ∗ time ) to facilitate comparison with FGM curves. The filled symbols are predicted average velocities during each crossing duration (2 τ ): filled crosses=CVA; filled circles=CTA; filled semicircles=DA. Velocities predicted from single-spacecraft methods, based on prime-parameter data, are shown for comparison: CIS=three CIS measurements of normal plasma speed in middle of magnetopause; MFR and MFRC=results of unconstrained and constrained ( 〈 B 〉· n = 0 ) Minimum Faraday Residue analysis; HT=normal component of deHoffmann-Teller velocity with normal from MVABC. Color code as in Fig. 1.

<!-- image -->

the correct normal, this method (like MFR) should give the actual magnetopause velocity.

It is seen that the velocities predicted from CIS, MFRC, and HT are almost the same. Since the MFR, MFRC, and HT calculations require a long data interval (in the range of 76-125 s) while the CIS method is based on only three velocity measurements (12 s), this result suggests that for the present event, the curvature of the actual low-pass filtered velocity curve was relatively small at C4, C1, and C3. But in general, the CIS method is better suited to point-wise comparison with the results from multi-spacecraft methods than MFR, MFRC, and HT.

The single-spacecraft predictions can now be compared with the magnetopause velocity curves in Fig. 3, obtained from the four-spacecraft methods, namely CVA, CTA, and DA. For the FGM-based curves for CVA and DA, one finds poor agreement, overall, with the single-spacecraft results. For CTA, the agreement is good for C4 but fair to poor for

C1 and C3. The EFW-based curves, except the DA curve at C3, show somewhat better overall agreement. In particular, the CTA curve based on EFW timing appears reasonably consistent with the single-spacecraft (CIS-based) prediction at both C4 and C3.

## 4.3 Speeds from modified methods: CVAM, CTAM, and DAM

It is clear from Fig. 3 that the magnetopause velocities derived from the CIS measurements are needed to judge which of the three methods (CVA, CTA, and DA) and which of the data sets used for the timing (FGM or EFW), give the most consistent results. Figure 3 also suggests that it may be desirable to alter these methods so as to incorporate some of the plasma velocity measurements into the calculations, while leaving others for consistency checking. Therefore, we have made simple modifications of the three time-based methods to require the resulting velocity at C3 to agree with

<!-- image -->

k*time [s]

Fig. 4. Velocity curves from modified multi-spacecraft methods: CVAM, CTAM, and DAM. Upper panel; FGM based results, lower panels; EFW based results. Symbols and other notation as in Fig. 3.

/BD the plasma-based CIS value at C3, except for a correction of 10 km/s to take into account the reconnection flow across the magnetopause, which we expect to be present in this crossing. To implement this modification, an extra degree of freedom must be incorporated in each of the three methods. For CVA this is done by allowing for a constant acceleration; the resulting technique is denoted by CVAM. For CTA it is done by allowing the magnetopause thickness in the C3 crossing to differ from the common thickness in the three other crossings; the resulting method is called CTAM. For DA it is done by allowing for a cubic rather than a quadratic velocity polynomial; the method is then referred to as DAM. The velocity curves resulting from CVAM, CTAM, and DAM are shown in Fig. 4 for FGM- as well as EFW-based timing. They will be discussed in Sect. 6.

## 5 Normal vectors, normal field components and thicknesses

## 5.1 Normal vectors

The normal vectors, derived from CVA and CTA, as well as from CVAM and CTAM, are shown in the polar plots on the left in Fig. 5. The top left plot is based on FGM timing, the bottom left plot on EFW timing. The two plots on the right, which show the single-spacecraft predictions, will be discussed in detail later on. The GSE components of the various normal vectors are also provided in the figure. The 'bull's eye' in each plot represents the vector 〈 n MVABC 〉 =[0.58426; -0.81125; 0.02250] (GSE components), which is the average of the four normal vectors obtained by minimum variance analysis (MVAB) of the magnetic field measured in each crossing, using the constraint 〈 B 〉· n = 0 (MVABC; see Sonnerup and Scheible, 1998). For each crossing and each technique, the analysis was performed for 7 data intervals, nested around the center of the magnetopause and containing from 19 to 31 data points at 4-s resolution. For MV ABC, the average of the resulting seven normal vectors, denoted by n MVABC, was used to represent the constrained normal for each individual crossing. The spread of these individual normals around the event average, 〈 n MVABC 〉 , is illustrated in the upper left panel by the 1 sigma uncertainty ellipse around the origin. The event average (the bull's eye normal) was used in our DA and DAM calculations. (Experiments were also performed in which nest averages of n MVABC from adjoining crossings were used in DA and DAM, in place of a single event normal: the results were not significantly different.)

The constraint 〈 B 〉· n = 0 is not consistent with the occurrence of reconnection signatures in the data from C3, whose signatures indicate the presence of a nonzero, and in fact a negative, normal magnetic field component, connecting the internal and external magnetic field lines. It is used because it gives extremely stable results, whereas the normal vector determination from MVAB without constraint gives normal vectors that have a strong dependence on the data interval used and that, even after averaging over the seven nests, tend to have unacceptable directions and normal components of the magnetic field. In the presence of reconnection at small rates, the normal magnetic field component is expected to be small enough so that the use of the MVABC normal in the single-spacecraft determinations of the magnetopause speeds is justified. As mentioned already, the average, 〈 n MVABC 〉 , of the four MVABC normals is used as the reference normal for the event.

The polar plots in Fig. 5 represent projections of the unit hemisphere onto its 'equatorial' plane, i.e. the plane perpendicular to 〈 n MVABC 〉 . The vertical axis in each plot points toward the Sun. The horizontal axis point mostly from north to south but with a small dusk-to-dawn component, as a consequence of the fact that 〈 n MVABC 〉 has a small, but positive, GSE Z component.

Panels (a) and (b) in Fig. 5 also show the orientation of a model normal taken from the work of Fairfield (1971). It deviates by some 17 ◦ from our reference normal, pointing more northward and slightly more tailward. As it happens, the two results from CVAM lie close to this direction.

In panel (c) of Fig. 5, the normal vectors from the various single-spacecraft methods are presented (the dashed lines are explained in Sect. 5.2). For each technique, the vector shown is the average over the same 7 nested data intervals as before, and the variation in the normals from each nest analysis is illustrated by narrow, one-sigma standard-deviation ellipses. For MVA, these average normals are widely scattered: the result from C1 is outside the plot and is shown only schematically. Note that for each technique, the standard deviations of the average normal from the 7 nests are smaller than the ellipse axes shown, by a factor of √ 6.

For C1 and C3, where CIS/HIA data are available, and for C4, where CIS/CODIF data can be used, the top right panel in Fig. 5 also shows the normals and error estimates obtained from Minimum Faraday Residue analysis of the 7 nested data segments, without constraint (MFR; see Khrabov and Sonnerup, 1998a), as well as with the constraint 〈 B 〉· n = 0 (MFRC). As illustrated by their small error ellipses, the MFR and MFRC normals have stable (nearly nest-sizeindependent) behavior and agreement, within about 5 ◦ , with the event normal, 〈 n MVABC 〉 , at the origin of the plot.

Panel (d) in Fig. 5 shows the same normal vectors as panel (c), but now with their associated error ellipses, describing statistical uncertainties in the normal, calculated from the data comprising the smallest nest (Khrabov and Sonnerup, 1998a, c), instead of fluctuations in the nest results. These statistical uncertainties are seen to be substantial for the MVAB normals, as well as for the MFR normals. To avoid clutter, ellipses are not shown for the constrained normals. Again, the uncertainty of the normal at the center of each ellipse would be represented by an ellipse that is a factor √ 6 smaller.

## 5.2 Normal component of B

The dashed line for each spacecraft in panel (c) of Fig. 5 separates the regions of positive and negative values of the average normal component of the magnetic field, 〈 B 〉· n . Each line passes through the point representing the corresponding normal, n MVABC, and the normal field component is positive above and to the right of the line. The actual values of the normal field component from the various normal vector determinations, excluding those that are constrained to give 〈 B 〉· n = 0, are provided in Table 3 for each of the four spacecraft. Also given for each spacecraft are the field components along the event normal, 〈 n MVABC 〉 (the bull's eye normal), as well as along n CVAM , and n CTAM , using both FGM and EFW timing. The large values obtained from MVAB for C1, C2, and C4 are a further indication that these normal vectors are substantially in error. This is also the case for the model normal and for the two normals from CVAM.

## 5.3 Thicknesses

The results from the four-spacecraft thickness determinations, as well as those from the various single-spacecraft methods, are shown in Table 3. It is seen that for the FGMbased timing, CVAM gives a thickness increase by a factor of about two in the time interval between the first and second pair of crossings; CTAM gives the constant thickness of 416 km for C1, C2, and C4, and a separate thickness of 601 km for C3; DAM gives the thicknesses 186, 478, 242 and 731 km for the crossings by C4, C1, C2, and C3, respectively. Visual inspection of Fig. 1 indicates that at 06:23:21 UT, C1 was near the inner edge of the magnetopause layer while C4 was near the outer edge (both locations specified by the 76% criterion discussed earlier). This means that the magnetopause thickness at that time was about equal to the spacecraft separation along n , i.e. about 344 km. This value is comparable to those given in Table 4 for C4 and C1.

The results based on EFW timing reflect the smaller thicknesses associated with the density ramps; the thickness variations from crossing to crossing are also found to be much less.

<!-- image -->

Plot origin and model normals

[ 0.5843  -0.8113   0.0225]

NBULL

[ 0.5060  -0.8050   0.3090]

MODEL

## Normals from FGM (Panel a)

[ 0.5321  -0.8327   0.1529]

CVA

[ 0.4929  -0.8071   0.3251]

CVAM

[ 0.5512  -0.8315   0.0693]

CTA

[ 0.5382  -0.8378   0.0918]

CTAM

Normals from EFW (Panel b)

[ 0.5324  -0.8358   0.1340]

CVA

[ 0.5052  -0.8095   0.2990]

CVAM

[ 0.5422  -0.8325   0.1143]

CTA

[ 0.5381  -0.8343   0.1204]

CTAM

<!-- image -->

Fig. 5. Polar plots of magnetopause normal vectors. Panels (a) and (b) : multi-spacecraft results from FGM- and EFW-based timing, respectively. The bull's-eye normal (denoted NBULL) is the average of the four spacecraft normals, derived from minimum variance analysis of the magnetic field (using 7 nested intervals), with constraint 〈 B 〉· n = 0 . The ellipse represents the 1-sigma scatter in this normal. Panels (c) and (d): single-spacecraft results with scatter ellipses from 7-nest analysis and from statistical errors in smallest nest, respectively. The bull's eye normal is the same as in the left plots. Dashed lines in panel (c) separate regions of positive and negative normal magnetic field components. GSE components of the normal vectors are listed. Color code as in Fig. 1.

## 6 Discussion

## 6.1 Magnetopause velocity

We first discuss the FGM-based results (upper panel) in Fig. 3. Judging from the CIS-based velocities at C4, C1, and C3, the constant velocity of -40 km/s from CVA provides only an approximate description of the actual magnetopause motion. The CTA and DA curves are in fair agreement with each other for C4, C1, and C2 but are in strong disagreement for C3. The agreement with the CIS-based velocities is poor, except at C4. The behavior of the DA curve at and beyond the C3 crossing is clearly incorrect and is the direct result of the parabolic, rather than cubic, nature of the curve. But even if DA is performed in its original form, in which one uses individual normal vectors at the four spacecraft to calculate the average normal vector and normal velocity for each pair of temporally adjoining crossings, rather than a continuous velocity curve, the resulting velocity average between the C2 and C3 crossings lies close to the DA curve in the figure, i.e. it is much less negative than both the CTA result, and the single-spacecraft (CIS) result from C3 (Dunlop, private communication, 2003).

A substantial disagreement of CTA with the CIS-based velocity at C3 remains, even when an allowance is made for a reconnection-associated, inward plasma flow of some 10 km/s across the magnetopause. At C4 and C1 the discrepancy between the CTA and DA results and the single-spacecraft results are somewhat less drastic, with CTA giving the better agreement.

We next turn to the EFW-based results (lower panel) in Fig. 3. The CVA velocity is now -48 km/s, which, allowing for the reconnection flow, is in better agreement with the CIS-based velocity at C3. The agreement at C4 and C1 has also improved. The DA curve remains unreasonable at C3 but has improved somewhat at C4 and C1. Finally, the CTA curve now shows substantially better agreement at C3, while at C4 and C1 the results are nearly the same as for the FGMbased curves. The velocity variations during the event, predicted from the EFW-based CTA, are much smaller than the corresponding FGM-based variations. The discrepancy between the two curves is particularly strong at C2.

In Fig. 4, each of the three multi-spacecraft methods has been given an additional degree of freedom, which has been used to specify that the magnetopause velocity at C3 must equal the CIS-based value, corrected for an inward reconnection flow of 10 km/s. The predicted velocities at C4 and C1 can still be checked against their CIS-based values. For DAM, the FGM- and the EFW-based curves are now cubic. As required, the DAM velocities remain negative during the entire event but the predicted speed at C2 is still small. The agreement with the single-spacecraft (the CIS-based) results is particularly poor at C4. The two straight lines from CV AM differ in that the FGM-based line shows an inward (constant) acceleration, while the EFW-based line has a modest outward acceleration from the magnetopause. The agreement at C4 and C1 is poor for the FGM-based curve and moder-

Table 3. Normal components 〈 B 〉· n in units of nanotesla [nT] for the various normals.

|                   | Spacecraft            | Spacecraft            | Spacecraft            | Spacecraft            |
|-------------------|-----------------------|-----------------------|-----------------------|-----------------------|
| Method            | C1                    | C2                    | C3                    | C4                    |
| CVA               | - 3 . 1               | - 3 . 5               | -3.2                  | 4.1                   |
| CTA               | - 1.2                 | - 1.6                 | - 1.1                 | - 2.2                 |
| CVAM              | - 6.8                 | - 7.0                 | - 7.2                 | - 7.8                 |
| CTAM              | - 1.8                 | - 2.3                 | - 1.8                 | - 2.9                 |
| Model             | - 6.4                 | - 6.5                 | - 6.7                 | - 7.3                 |
| EFW based         | Normal component [nT] | Normal component [nT] | Normal component [nT] | Normal component [nT] |
| CVA               | - 2.7                 | - 3.2                 | - 2.8                 | - 3.8                 |
| CTA               | - 2.2                 | - 2.6                 | - 2.2                 | - 3.3                 |
| CVAM              | - 6.2                 | - 6.4                 | - 6.5                 | - 7.2                 |
| CTAM              | - 2.4                 | - 2.8                 | - 2.4                 | - 3.4                 |
| Model             | - 6.4                 | - 6.5                 | - 6.7                 | - 7.3                 |
| Single-Spacecraft | Normal component [nT] | Normal component [nT] | Normal component [nT] | Normal component [nT] |
| Methods MVAB      | 21.2                  | - 9.0                 | 0.2                   | - 5.0                 |
| MVABC ∗           | - 0.3                 | - 0.1                 | 0.9                   | - 0.8                 |
| MFR               | 1.3                   |                       | - 1.6                 | - 0.2                 |

ately poor for the EFW curve. However, the latter curve is better because the single-spacecraft results show that the average acceleration in the interval between the crossings by C1 and C3 must in fact be outward. At C4, the two CTAM curves agree with each other and with the single-spacecraft result. They also agree approximately with each other at C1 but, compared with the CIS-based result, both still show an inward speed that is too small. At C2, the FGM-based prediction from CTAM of the inward speed is much larger than the prediction from DAM but is still substantially smaller than the EFW-based prediction from CTAM. Except at C4, the latter curve lies close to the EFW-based CV AM prediction.

Using FGM timing, we have also tried a version of CTAM in which the magnetopause thicknesses are assumed pairwise to be the same (C4=C1 and C2=C3). The result is a nearly constant velocity during the event, yielding a poor agreement with the CIS-based velocities at C4 and C1. On this basis, we conclude that the assumption of pairwise equal magnetic thicknesses, with larger but equal widths at C2 and C3, is not valid: only at C3 is the thickness substantially larger. The implication is that the reconnection bubble on the magnetopause, found in the field map reconstructed from C3 data by Hasegawa et al. (2003), started its development around the time of the C2 crossing and then grew to its full size in the short time interval ( /similarequal 10 s) between the C2 and C3 crossings. This bubble appears to influence the EFW density ramp only to a modest extent but it thickens the magnetic structure outside the ramp a great deal. The rate of magnetic thickening may explain the discrepancy around the C2 crossing, between the FGM- and EFW-based CTAM curves in Fig. 4. The long magnetic duration of the C2 crossing

Table 4. Magnetopause thickness based on the durations (from Table 2) and the calculated velocities for the different methods.

|             | Spacecraft                  | Spacecraft                  | Spacecraft                  | Spacecraft                  |
|-------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|
| Method      | C1                          | C2                          | C3                          | C4                          |
| FGM based : | Magnetopause thickness [km] | Magnetopause thickness [km] | Magnetopause thickness [km] | Magnetopause thickness [km] |
| CVA         | 319.2                       | 690.1                       | 667.0                       | 350.2                       |
| CTA         | 414.1                       | 414.1                       | 414.1                       | 414.1                       |
| DA          | 389.4                       | 442.0                       | 55.3                        | 379.8                       |
| CVAM        | 302.2                       | 721.6                       | 724.3                       | 323.0                       |
| CTAM        | 416.1                       | 416.1                       | 601.2                       | 416.1                       |
| DAM         | 478.1                       | 242.6                       | 731.4                       | 186.4                       |
| CIS         | 483.6                       | -                           | 918.4                       | 440.0                       |
| EFW based : | Magnetopause thickness [km] | Magnetopause thickness [km] | Magnetopause thickness [km] | Magnetopause thickness [km] |
| CVA         | 177.8                       | 190.3                       | 226.8                       | 181.7                       |
| CTA         | 181.8                       | 181.8                       | 181.8                       | 181.8                       |
| DA          | 205.4                       | 130.6                       | 7.3                         | 167.5                       |
| CVAM        | 192.3                       | 176.3                       | 196.8                       | 204.4                       |
| CTAM        | 182.6                       | 182.6                       | 201.8                       | 182.6                       |
| DAM         | 273.0                       | 38.0                        | 205.9                       | 53.1                        |
| CIS         | 223.1                       | -                           | 258.7                       | 189.0                       |

resulted mainly from slow average magnetopause motion, created by the expansion of the outer portion of the magnetic structure. This expansion caused the outer edge of the magnetic structure to move earthward only very slowly, while at the same time the inner portion, containing the density ramp, was moving inward at a speed of the order of 50 km/s. On the other hand, the long duration of the C3 crossing was caused by encountering the resulting thickened portion of the magnetopause. As stated above, this behavior was the result of rapid reconnection that started at about the time of the C2 crossing.

Another consistency check between single-spacecraft and multi-spacecraft velocity predictions comes from the singlespacecraft technique of determining both the deHoffmannTeller (HT) frame velocity and its acceleration (e.g. Khrabov and Sonnerup, 1998b). In the present case, the latter provides a prediction of the slope of the velocity curve at C4, C1, and C3. For C4, the HT acceleration (from the smallest nest) along the (outward directed) normal vector is -0.6 km/s 2 , corresponding to a small negative slope of the velocity curve at C4. This behavior is consistent with the CTA and CTAM results, both for FGM- and EFW-based timing. On the other hand, the slopes from DA and, in particular, DAM at C4, while having the predicted negative sign, are too large. At C1, the HT acceleration along the normal is again -0.6 km/s 2 , whereas the slopes from CTA and CTAM are seen to be either slightly negative or zero. Here the DA results show approximately the right behavior while DAM gives a negative slope that is much too large. At C3, the normal HT acceleration is found to be -0.9 km/s 2 , which, in terms of direction and approximate magnitude, agrees with the FGM-based, but not the EFW-based, CTA and CTAM results. The DA results give the wrong sign of the slope, while

DAM gives the right sign but with a magnitude that is too large. In summary, the HT acceleration results are consistent with a cubic description of the velocity curve, with only a moderate difference between its maximum and minimum values. The CTA or CTAM curves appear to provide the best agreement with this description.

In summary, we find that no single curve in Fig. 3 or Fig. 4 provides entirely satisfactory agreement with all three velocities derived from single-spacecraft methods. In Fig. 3, the best agreement is provided by the EFW-based CTA and CVA curves. In Fig. 4, the best two curves are from the FGMbased CTAM, followed by the EFW-based CVAM curve.

We now discuss possible sources of the discrepancy between single-spacecraft normal velocities and those from the various multi-spacecraft methods. First, one needs to consider the accuracy of the magnetopause velocities derived from single-spacecraft information. If the inward plasma speeds at C1 and C3 were overestimated by some 10 km/s, then either of the two CTA curves in Fig. 3 would have provided satisfactory agreement. The consistency of the magnetopause speeds, calculated by the methods we have denoted by CIS, HT, and MFRC, along with the stability relative to nest size (standard deviation &lt; 2 km/s), suggests that any error in the single-spacecraft predictions would be the result of systematic errors, either in the measured plasma velocity vectors, or in the normal vector directions used. We cannot entirely exclude the possibility that the composite of these errors could be sufficiently large to account for the discrepancy but we consider it unlikely.

The errors in the multi-spacecraft techniques come from the timing and from violations of the various model assumptions. For our event, the EFW-based timing seems to be less ambiguous than that based on FGM. But a remaining problem is that the separation vector between C1 and C4 (and to a lesser extent between C2 and C3) happens to be nearly tangential to the magnetopause. This orientation is an important source of uncertainty in the translation of time delays into velocities. Additionally, for CVA, the model assumption of a constant velocity seems likely to be invalid. For CTA the model assumption of a constant thickness is suspect, in particular for the FGM data. In fact, the CIS velocities, together with the crossing durations from these data, give the approximate thicknesses 440, 484 and 918 km at C4, C1, and C3, respectively, indicating a near doubling of the magnetic thickness in the time interval between the two early crossings and the last crossing. The likely explanation for this behavior is the passage of a substantial reconnectionassociated magnetic island past C3 (Hasegawa et al., 2003). The EFW-based thicknesses calculated in the same way (189, 223, and 259 km at C4, C1, and C3, respectively) show much less variation. For both the FGM and EFW data, the DAM method, which does not contain the assumption of a constant thickness, or a constant velocity, actually predicts a substantial, and probably unrealistic, thinning of the layer at C2. For this reason, and because of the poor agreement of the DAM velocity curve with the CODIF-based velocity at C4, we conclude that the most basic of the DA model

assumptions we used is being violated: the magnetopause cannot be represented by a plane surface of fixed orientation. But even the original version of DA, in which the individual MVABC normals are used and averaged between pairs of adjoining crossings, gives a small average velocity in the interval between the two last crossings (C2 and C3) and an associated small magnetopause width (Dunlop, private communication, 2003). A small-amplitude undulation of the magnetopause surface provides a possible explanation: in calculations not given here, we have found that an increase in the travel distance along the event normal of 70 km for C1, a decrease of 20 km for C2 and an increase of 120 km for C3 will produce an FGM-based DAM curve that agrees perfectly with the CIS-based velocities, not only at C3, but at C4 and C1, as well (at C2, the predicted velocity then becomes -18 km/s, with a corresponding magnetopause width of 312 km). This example demonstrates that results from the multi-spacecraft methods can be very sensitive to the presence of small-amplitude undulations on the magnetopause. Such behaviour can be seen in the field maps obtained by Hasegawa et al. (2003).

## 6.2 Normal vectors

An overview of the various single-spacecraft determinations of the magnetopause normal direction for all four crossings was presented in the two right-hand panels of Fig. 5. With the exception of three of the MVAB results, all calculations lead to normals that fall within a 5 ◦ cone around the center of the plot, i.e. around the average, 〈 n MVABC 〉 , of the four individual MVABC normals. This result indicates that the magnetopause orientations during the four crossings were not vastly different. But the differences, while small, are nevertheless significant. The MVABC normals from C1 and C3 are similar, pointing mainly northward by some 1 to 3 ◦ relative to the reference normal; the MVABC normal from C2 points tailward/southward by about 4 ◦ and the MVABC normal from C4 points sunward/southward by some 2 ◦ , relative to the reference normal. These results support the view that the magnetopause surface was not entirely flat but exhibited smallamplitude undulations.

We now discuss the left-hand panels in Fig. 5. The FGMbased normal vectors (top panel) from CVA and CTA differ from the reference normal by 8.1 ◦ and 3.4 ◦ , respectively, both deviations being approximately toward the model normal. This is also the case for the EFW-based CVA and CTA normals (lower left panel) but the two normals are now closer together. In both panels, the CTAM normal is very close to the CTA normal, while the CVAM normals are close to the model normal of Fairfield (1971), deviating by some 17 ◦ from 〈 n MVABC 〉 . The resulting normal magnetic field components are negative for all the normals (see Table 3) but are unacceptably large for the two CVAM vectors and for the model normal.

In summary, we have seen that the normal vectors from the EFW-based CVA, CTA, and CTAM are closely clustered (Fig. 5, panel (b)) and that they all give a magnetic field com- ponent along the normal in the range of -2.2 to -3.8 nT (Table 3). They agree within 1 to 2 ◦ with the single-spacecraft normal at C3, calculated from MFR (see panels (c) and (d) in Fig. 5), but deviate by some 6 to 7 ◦ from the reference normal, 〈 n MVABC 〉 . We have shown that the MFR result at C3 accounts for the presence of reconnection flows, known to be present in this crossing, in a quantitatively believable way: the flow across the magnetopause is about -10 km/s and the field component along the MFR normal is -1 . 6 nT, with a corresponding normal Alfv´ en speed of -10 km/s. For this reason we believe this normal to be accurate, probably within 1 or 2 ◦ . For the other three crossings, we have no clear evidence that well developed reconnection flows were present. For them we expect the individual normal directions from MVABC to be accurate, again within 1 or 2 ◦ . The fact that the multi-spacecraft results in panels (a) and (b) of Fig. 5 are not closer to the origin must, therefore, be the result of violations of some of their underlying model assumptions.

We now describe briefly the calculations leading to the error ellipses in the two right panels of Fig. 5. In the top right panel, the ellipses represent the fluctuations in the normal vectors derived from a set of 7 nested data segments, centered at the midpoint of the magnetopause, with the innermost segment containing 19 data points and the outermost segment containing 31 points at 4-s resolution. The resulting 7 normal vectors are used to form the matrix 〈 ni nj 〉 , the average (denoted by 〈〉 ) being over the 7 members of the set. The eigenvalues and eigenvectors of this matrix are calculated. The largest eigenvalue is slightly less than unity, and the corresponding eigenvector represents the optimal composite (average) normal. The square root of the other two eigenvalues and their corresponding eigenvectors represent the two axes of an ellipse characterizing the scatter of the individual nest results around the average. By placing this ellipse on the plane tangent to the unit sphere with its center at the point of contact, whose point marks the average normal, and with its axes in the proper orientation, a cone of uncertainty of the average normal is defined. The intersection of this cone with the surface of the sphere produces a closed curve. The projection of this curve onto the equatorial plane of the sphere defines the one-sigma boundary of the scatter domain for the normal. Only for a narrow cone is the projected curve close to an ellipse. Note that this uncertainty estimate simply measures the sensitivity of the result to the choice of data interval. It does not include the purely statistical uncertainties for the individual normal vector calculations, which are shown separately (for the 19-point nest) in the panel (d) of Fig. 5 (for the MVAB error calculation, see Khrabov and Sonnerup, 1998c; for MFR, see Khrabov and Sonnerup, 1998a).

The error curves, shown in panels (c) and (d) in Fig. 5, for the unconstrained MVAB normals are elongated, or extremely elongated, indicating a large uncertainty of the normal vector estimate to rotations about the maximum variance MVAB eigenvector. This behavior is expected when the ratio of intermediate to minimum eigenvalue of the magnetic variance matrix is not large: the estimated normal vector is

Fig. 6. Hodogram pair from minimum variance analysis (MVAB) of prime-parameter magnetic field in the portion of the magnetopause crossing by C1, chosen to maximize the eigenvalue ratio λ 2 /λ 3 . The eigenvalues of the variance matrix are λ 1 = 358, λ 2 = 2 . 25, and λ 3 = 0 . 245 nT 2 . The predicted normal vector forms an angle of more than 60 ◦ with the bull's-eye normal in Fig. 5. The normal field component is 13.4 nT. In spite of the good eigenvalue separation, the predicted normal is a poor one.

<!-- image -->

uncertain but the maximum variance eigenvector defines a good tangent to the magnetopause, around which the estimated normal can rotate, sometimes by large angles, as the nest size changes. Note that for each spacecraft the long axis of the error curve points approximately toward the corresponding constrained normal n MVABC. This is the expected behavior, although the expectation that they actually reach this normal is not always met.

A remarkable fact is that the CV A and CTA normals, both of which are derived entirely from timing information, also turn out to be nearly perpendicular to the maximum variance eigenvectors, which are derived entirely from the magnetic structure of the magnetopause. For example, if the longest nest interval is used for the MVAB calculation, the angle between the maximum variance eigenvector and the FGMbased CVA normal is 88.5 ◦ , 87.4 ◦ , 91.9 ◦ , and 90.0 ◦ for C1, C2, C3, and C4, respectively. The corresponding angles for CTA are 90.4 ◦ , 88.4 ◦ , 93.2 ◦ , and 91.4 ◦ . We conclude that the condition where the normal vector is perpendicular to the maximum variance eigenvector cannot be used to decide whether the CVA or the CTA normal is the better one.

A rule of thumb that has been widely used in judging the quality of the minimum-variance eigenvector from MVAB as a predictor of the magnetopause normal is the following. For the prediction to be of acceptable quality, the ratio of intermediate to minimum variance (the eigenvalue ratio) should exceed 10 (see, e.g. Sonnerup and Scheible, 1998). Most of the normals derived for our event from MVAB without constraint do not satisfy this quality condition. However, Fig. 6 shows one particular calculation where the eigenvalue ratio was close to 10 but where the normal vector was nevertheless poorly predicted: it points in an unreasonable direction and leads to a normal component of the magnetic field that is unreasonably large. The difficulty in this case is that both of the two smallest eigenvalues are small (0.245 and 2.25 nT 2 ). This example illustrates the danger of accepting a normal vector prediction exclusively on the basis of the eigenvalue ratio, without examination of the magnetic hodograms. It is a situation where some additional constraint on the normal vector is needed. In our present study, we have used the condition 〈 B 〉· n = 0.

## 6.3 Normal magnetic field components

The normal field components associated with those normal vectors from MVAB and MFR that fall within the 5 ◦ cone surrounding the reference normal (see Fig. 5) have small positive or negative values (see Table 2), with a slightly negative, but insignificant, average of 〈 B 〉· n =-0 . 08 ± 1 . 46 nT. The CVA, CTA, and CTAM normals all give small but significant negative values, namely 〈 B 〉· n =-3 . 48 ± 0 . 39 nT, -1 . 53 ± 0 . 43 nT, and -2 . 20 ± 0 . 45 nT from FGM timing, and -3 . 13 ± 0 . 43 nT, -2 . 58 ± 0 . 45 nT, and -2 . 75 ± 0 . 41 nT from EFW timing, respectively. We note that the results from the Wal´ en test for C1 and C3, mentioned earlier, indicate the presence of a negative normal magnetic field component, at least during the C3 crossing. The above results are consistent with this prediction and furthermore, indicate that the magnitude of the normal component was small. MFR from C3 gives what we judge to be the best prediction for this crossing, namely -1 . 6 nT. The large magnitude of the normal field components from CVAM and from the Fairfield model normal (see Table 3) indicate that the corresponding normal directions are not believable.

## 6.4 Magnetopause thickness and structure

In an overall sense, our FGM-based results for the magnetopause thickness in Table 4 are within the range of those obtained by Berchem and Russell (1982). Since the plasma and field conditions in the magnetosheath adjacent to the magnetopause correspond to an ion gyroradius of about 50 km and an ion inertial length of about 60 km, it is evident that the magnetopause is many gyroradii/inertial lengths thick. It follows that, in the event studied, the Hall-current term in the generalized Ohm's law should not be an important local factor in determining the observed magnetopause structure. Except for the effects of pressure anisotropy, the structure can be studied, at least approximately, by use of ordinary MHD. Numerical MHD simulations of the solar-wind magnetosphere interaction have indicated a layered structure of the magnetopause such that the various current systems that close on the magnetopause occupy different parts of the layer (Siscoe et al., 2000). For example, the currents connecting the magnetopause with the magnetosheath and shock, and also the Chapman-Ferraro currents, close in the outer parts of the magnetopause layer, while the Region 1 currents close in the inner part. If the local current directions in these systems are significantly different at the spacecraft location, the observed magnetic hodograms for the magnetopause will show a substantial intermediate variance. This is the situation where a good determination of the magnetopause normal from MVAB (without constraint) can be expected. On the other hand, if the current directions are locally nearly the same, then a hodogram of the type shown in Fig. 6 will result and the unconstrained MVAB will fail to produce a good normal. The point is that, in terms of hodogram behavior, the local magnetopause structure in this event may have been controlled, not by local plasma conditions but by the configuration of the global magnetopause current systems. Similarly, the average local magnetopause thickness may have been a consequence of global rather than local effects, although the local thickness may have been modulated by convecting structures, such as tearing mode islands, or FTEs in status nascendi. We emphasize that the above statements refer to the properties of the specific event we have discussed here: other magnetopause observations have indicated the occasional occurence of small magnetic thicknesses so that local control, including the Hall effect, was important.

For our event, the widths of the density ramps are typically about one-half of the magnetic widths and the ramps occupy the earthward half of the magnetic structure. Such behaviour suggests that the transport of magnetosheath plasma across the magnetic field is efficient within the magnetopause layer. Such transport could be the result of direct magnetic connections of the type seen near X-lines in the reconstruction maps of Hasegawa et al. (2003). The EFW-based ramp widths at C2 and C4, derived from DAM and given in Table 4, are unrealistically small and suggest that the corresponding velocity curve in Fig. 4 predicts velocities at C2 and C4 that are too small.

## 7 Conclusions

The principal conclusions from our study are:

- (1) For our test event, the directions normal to the magnetopause, determined from the multi-spacecraft technique CTA and from the hybrid technique CTAM are in reasonably good agreement ( /similarequal 5 ◦ ), with the directions found from the single-spacecraft methods MVABC, MFR, and MFRC (see Fig. 5). The performance of CVA and, in particular, CVAM is less good. On the whole, the EFW-based timing results have less ambiguities than those based on FGM. For the event we have studied, MVAB does not perform well. Constraining the method by the requirement 〈 B 〉· n = 0 seems to be a reasonable way to obtain good normal directions.
- (2) The magnetopause velocity curves from the various multi-spacecraft and hybrid techniques agree with each other and with the results from the various singlespacecraft techniques in an approximate sense, but not in detail. It is not clear whether the problem lies entirely with the multi-spacecraft methods or is caused in part by the single-spacecraft methods. Although the latter have to be used with extreme care to make sure the results are stable with respect to modest changes in the data interval, we find them to be essential in judging which of the multi-spacecraft methods provides the most believable results.
- (3) The magnetopause thicknesses derived from the various techniques are uncertain to the same extent as the corresponding velocities. On the whole, they fall in a range that is consistent with earlier results. The magnetic thickness was not constant during our event but increased toward the end as a consequence of the passage through a growing reconnection bubble. The plasma density-based thicknesses were substantially less than the magnetic ones and showed less variability.
- (4) We have concluded that, for the event studied, a nonplanar geometry of the magnetopause surface during the event is one of the main reasons for the lack of consistency between the single- and the multi-spacecraft velocity results. On the whole, our study illustrates the extreme care that must be exercised if one wants accurate and consistent answers concerning magnetopause orientation, motion, and thickness.

## Appendix

As seen in Eqs. (1) to (4), the crossing times and crossing durations are key elements in the multi-spacecraft methods. These must be uniquely and consistently determined. We have used the following procedure:

(1) To eliminate undesirable high-frequency fluctuations, filter the data from each spacecraft by application of a sliding rectangular window (of width 6 s for FGM and 4s for EFW

- results used here), in both cases retaining a time resolution of 0.2 s;
- (2) the duration of the first crossing, CR0, can now be established according to Eq. (8). The time profiles of the other crossings will be stretched (or compressed) by a factor ki with respect to the duration of crossing CR0;
- (3) flip the part of the B max (t) profile (or density profile) to the left of its midpoint to create a peaked pulse;
- (4) shift the pulse up (or down) so that its value approaches zero (or nearly zero) at the two ends;
- (5) renormalize the pulse to unit amplitude;
- (6) time shift the pulses from CR1, CR2, and CR3 so that their peaks occur at the same time as that of the first crossing, i.e. at t = t 0 = 0;
- (7) multiply each pulse by a raised-cosine window function, [1 + cos (πt/T ) ] / 2, of variable width 2 T ;
- (8) for CR1, CR2, and CR3, multiply by suitable first-guess stretching factors ki . Cross correlation of the resulting pulses for CR1, CR2, and CR3 with that for CR0 then leads to small corrections to the time shifts in step (6) and to the stretching factors in step (8).

The resulting time shifts and crossing durations depend on the choice of window width, 2T. A narrow window places the main emphasis on the steep part of the original B max (t) (or density) profiles. As the window widens, increasing emphasis is placed on the behavior at the magnetospheric and magnetosheath edges of the profiles. An optimal window width is selected by searching for the minimum in the normalized residual from the least-squares determination of the stretching factors. The window size is the same for both members of a correlation/least-squares pair (CR0-CR1; CR0-CR2; CR0-CR3) but varies from pair to pair. The window shape produces pulse shapes for the correlation that approach zero smoothly at the beginning and end times.

In summary, one seeks to minimize the square of the deviation between the maximum variance field component (or density profile) in CR0 and the corresponding component in the three other crossings, by applying to each an optimal time shift and time stretching (or compression) factor, ki , determined by trial and error. This step is not entirely trivial because it requires the resampling of the measured discrete data sets for CR1, CR2, and CR2. Some iteration may be needed to obtain the overall optimum for t i and ki = τi /τ 0 , (i = 1 , 2 , 3 ) .

Acknowledgements. We thank L. Kistler for help in verifying the data from CIS/CODIF from C4. The research was initiated during extended research visits by B. Sonnerup to MPE, Garching, and to ISSI, Bern, in Fall of 2001 and Spring/Summer, 2002. His work was supported by the Alexander-von-Humboldt Foundation and by the National Aeronautics and Space Administration, Office of Space Science, under Grant NAG5-36375 to Dartmouth College. Parts of the data analysis were done with the Queen Mary University, London Science Analysis System for Cluster (QSAS). The editor thanks the referees for assisting in evaluating this paper.

Topical Editor T. Pulkkinen thanks H. Biernat and another refereee for their help in evaluating this paper.

## References

- Balogh, A., Carr, C. M., Acu˜ na, M. H., Dunlop, M. W., Beek, T. J., Brown, P., Fornaco ¸n, K. H., Georgescu, E., Glassmeier, K. H., Harris, J., Musmann, G., Oddy, T., and Schwingenschuh, K.: The Cluster magnetic field investigation: Overview of in-flight performance and initial results, Annal. Geophysicae, 19, 1207, 2001.
- Bauer, T. M., Dunlop, M. W., Sonnerup, B. U. ¨ O., Sckopke, N., Fazakerley, A. N., and Khrabrov, A. V.: Dual spacecraft determinations of magnetopause motion, Geophys. Res. Lett., 27, 1835, 2000.
- Berchem, J. and Russell, C. T.: The thickness of the magnetopause current layer - ISEE 1 and 2 observations, J. Geophys. Res., 87, 2108-2114, 1982.
- Cahill, L. J. and Amazeen, P. G.: The Boundary of the Geomagnetic Field, J. Geophys. Res., 68, 1835, 1963.
- Dunlop, M. W. and Woodward, T. I.: Multi-spacecraft discontinuity analysis:Orientation and motion, in Multi-Spacecraft Analysis, chap. 11, ISSI, 271-306, 1998.
- Dunlop, M. W. and Woodward, T. I.: Cluster magnetic field analysis techniques, in Proceedings of the Cluster-II Workshop on Multiscale/Multipoint Plasma Measurements, ESA SP-449, London, UK, 2000.
- Dunlop, M. W., Balogh, A., Cargill, P., Elpic, R. C., Fornaco ¸n, K.H., Georgescu, E., Sedgemore-Schultess, F., and the FGM team: Cluster observes the Earth's magnetopause: coordinated fourpoint magnetic field measurements, Annal. Geophysicae, 19, 1449, 2001.
- Dunlop, M. W., Balogh, A., and Glassmeier, K. H.: Fourpoint Cluster application of magnetic field analysis tools: The discontinuity analyzer, J. Geophys. Res., 107, 1385, doi:10.1029/2001JA00589, 2002.
- Fairfield, D. H.: Average and unusual locations of the Earth's magnetopause and bow shock, J. Geophys. Res., 6700-6717, 1971.
- Gustafsson, G., Andr´ e, M., Carozzi, T., Eriksson, A. I., F¨ althammar, C. G., Grard, R., Holmgren, G., Holtet, J. A., Ivchenko, N., Karlsson, T., Khotyaintsev, Y., Klimov, S., Laakso, H., Lindqvist, P. A., Lybekk, B., Marklund, G., Mozer, F. S., Mursula, K., Pedersen, A., Popielawska, B., Savin, S., Staziewicz, K., Tanskanen, P., Vaivads, A., and Wahlund, J. E.: First results of electric field and density measurements by Cluster EFW based on initial months of operation, Annal. Geophysicae, 19, 1219, 2001.
- Harvey, C. C.: Spatial gradients and the volumetric tensor, in: Multi-Spacecraft Analysis, chap. 12, ISSI, edited by Paschmann, G. and Daly, P., 307-348, 1998.
- Hasegawa, H., Sonnerup, B. U. ¨ O., Dunlop, M. W., Balogh, A., Haaland, S. E., Klecker, B., Paschmann, G., Lavraud, B., Dandouras, I., and R` eme, H.: Reconstruction of two-dimensional magnetopause structures from cluster observations: Verification of method, Annal. Geophysicae, in press, 2004.
- Hu, Q. and Sonnerup, B. U. ¨ O.: Reconstruction of two-dimensional structures in the magnetopause: Method improvements, J. Geophys. Res., 108, doi:1029/2002JA009323, 2003.
- Khrabov, A. V. and Sonnerup, B. U. ¨ O.: Orientation and motion of current layers: Minimization of the Faraday residue, Geophys. Res. Lett., 25, 2373-2376, 1998a.
- Khrabov, A. V. and Sonnerup, B. U. ¨ O.: DeHoffmann-Teller analysis, in: Multi-Spacecraft Analysis, chap. 9, ISSI, edited by Paschmann, G. and Daly, P., 221-248, 1998b.

Khrabov, A. V. and Sonnerup, B. U. ¨ O.: Error estimates for minimum variance analysis, J. Geophys. Res., 103, 6641-6651, 1998c.

R` eme, H., Aoustin, C., Bosqued, J. M., Dandouras, I., Lavraud, B., Sauvaud, J. A., Barthe, A., Bouyssou, J., Camus, T., CoeurJoly, O., Cros, A., Cuvilo, J., Ducay, F., Garbarowitz, Y ., Medale, J. L., Penou, E., Perrier, H., Romefort, D., Rouzaud, J., Alcayde, D., Jacquey, C., Mazelle, C., d'Uston, C., M¨ obius, E., Kistler, L. M., Crocker, K., Granoff, M., Mouikis, C., Popecki, M., Vosbury, M., Klecker, B., Hovestadt, D., Kucharek, H., Kuenneth, E., Paschmann, G., Scholer, M., Sckopke, N., Seidenschwang, E., Carlson, C. W., Curtis, D. W., Ingraham, C., Lin, R. P., McFadden, J. P., Parks, G. K., Phan, T., Formisano, V., Amata, E., Bavassano-Cattaneo, M. B., Baldetti, P., Bruno, R., Chioncho, G., Lellis, A. D., Marcucci, M. F., Pallochia, G., Korth, A., Daly, P. W., Graeve, B., Rosenbauer, H., Vasyliunas, V., McCarthy, M., Wilber, M., Eliasson, L., Lundin, R., Olsen, S., Shelley, E. G., Fuselier, S., Ghielmetti, A. G., Lennartsson, W., Escoubet, C. P., Balsiger, H., Friedel, R., Cao, J.-B., Kovrazhkin, R. A., Papamastorakis, I., Pellat, R., Scudder, J., and Sonnerup, B. U. ¨ O.: First multispacecraft ion measurements in and near the Earth's magnetosphere with the identical Cluster ion spectrometry (CIS) experiment, Annal. Geophysicae, 19, 1303-1354, 2001.

- Russell, C. T., Mellott, M. M., Smith, E. J., and King, J. H.: Multiple spacecraft observations of interplanetary shocks: Four spacecraft determination of shock normals, J. Geophys. Res., 88, 4739-4748, 1983.
- Schwartz, S. J.: Shock and discontinuity normals, mach numbers, and related parameters, in: Multi-Spacecraft Analysis, chap. 10, ISSI, edited by Paschmann, G. and Daly, P., 249-270, 1998.

Siscoe, G. L., Crooker, N. U., Erickson, G. M., Sonnerup, B. U. ¨ O., Siebert, K. D., Weimer, D. R., White, W. W., and Maynard, N. C.: Global geometry of magnetospheric currents inferred from MHD simulations, Geophys Monogr. Ser., AGU, Washington, D.C., USA, 41, 2000.

Sonnerup, B. U. ¨ O. and Scheible, M.: Minimum and maximum variance analysis, in: Multi-Spacecraft Analysis, chap. 8, ISSI, edited by Paschmann, G. and Daly, P., 185-220, 1998.

- Sonnerup, B. U. ¨ O., Papamastorakis, I., Paschmann, G., and L¨ uhr, H.: Magnetopause properties from AMPTE/IRM observations of the convection electric field - Method development, J. Geophys. Res., 92, 12 137-12 159, 1987.
- Terasawa, T., Kawano, H., Yamamoto, T., and Kokubun, S.: On the determination of a moving MHD structure: Minimization of the residue of integrated Faraday's equation, J. Geophys. Geomagn., 48, 603, 1996.