Ann. Geophys., 29, 2239-2252, 2011 www.ann-geophys.net/29/2239/2011/ doi:10.5194/angeo-29-2239-2011

© Author(s) 2011. CC Attribution 3.0 License.

<!-- image -->

## Accuracy of multi-point boundary crossing time analysis

J. Vogt 1 , S. Haaland 2,3 , and G. Paschmann 4

1 School of Engineering and Science, Jacobs University Bremen, Campus Ring 1, 28759 Bremen, Germany

2 Max-Planck-Institut f¨ ur Sonnensystemforschung, Katlenburg-Lindau, Germany

3 Department of Physics and Technology, University of Bergen, Norway

4 Max-Planck-Institut f¨ ur extraterrestrische Physik, Garching, Germany

Received: 22 June 2011 - Revised: 14 September 2011 - Accepted: 21 November 2011 - Published: 10 December 2011

Abstract. Recent multi-spacecraft studies of solar wind discontinuity crossings using the timing (boundary plane triangulation) method gave boundary parameter estimates that are significantly different from those of the well-established single-spacecraft minimum variance analysis (MVA) technique. A large survey of directional discontinuities in Cluster data turned out to be particularly inconsistent in the sense that multi-point timing analyses did not identify any rotational discontinuities (RDs) whereas the MVA results of the individual spacecraft suggested that RDs form the majority of events. To make multi-spacecraft studies of discontinuity crossings more conclusive, the present report addresses the accuracy of the timing approach to boundary parameter estimation. Our error analysis is based on the reciprocal vector formalism and takes into account uncertainties both in crossing times and in the spacecraft positions. A rigorous error estimation scheme is presented for the general case of correlated crossing time errors and arbitrary spacecraft configurations. Crossing time error covariances are determined through cross correlation analyses of the residuals. The principal influence of the spacecraft array geometry on the accuracy of the timing method is illustrated using error formulas for the simplified case of mutually uncorrelated and identical errors at different spacecraft. The full error analysis procedure is demonstrated for a solar wind discontinuity as observed by the Cluster FGM instrument.

Keywords. Interplanetary physics (Discontinuities; Interplanetary magnetic fields; Instruments and techniques)

<!-- image -->

## 1 Introduction

The analysis of discontinuities in space plasmas has received a lot of attention since the beginning of the space age. In the case of a planar discontinuity moving at constant velocity, its orientation can be estimated from magnetic field measurements using the minimum variance analysis (MVA) technique (Sonnerup and Cahill, 1967; Sonnerup and Scheible, 1998) based on the conservation law for magnetic flux. The MVA framework can also be applied to electric field measurements or plasma data if other conservation laws are used (e.g. Sonnerup et al., 2008), and it further allows to take into account physical or geometrical constraints.

Applications of the MVA technique to solar wind discontinuities were recently challenged in a comprehensive study based on data from ESA's Cluster satellites (Knetter et al., 2004; Knetter, 2005). Such multi-spacecraft missions offer an independent road to boundary parameter estimation through a crossing time analysis that effectively yields a boundary plane triangulation technique or, in brief, the socalled timing method . T. Knetter and colleagues found that the discontinuity normal vectors obtained with the timing approach differ from the MVA normals. Furthermore, the MVA normals at the individual spacecraft are often mutually inconsistent even though previously used quality criteria such as the intermediate-to-minimum eigenvalue ratio were met. The discrepancy became less pronounced when important quality thresholds like the required eigenvalue ratio and/or the change in magnetic field direction across the discontinuity were raised, and then the results turned out to be also more consistent with the timing normals.

The discrepancy of discontinuity normal vector estimates using the two principal methods has crucial implications on the physical interpretation of the measurements. In accordance with previous single-spacecraft studies of solar wind discontinuities (e.g. Tsurutani and Smith, 1979; Neugebauer et al., 1984; Lepping and Behannon, 1986; S¨ oding et al.,

2001), Knetter's MVA results gave significant normal magnetic field components B n for a large fraction of the solar wind directional discontinuities (DDs), and hence put them into the category of rotational discontinuities (RDs). The timing analysis, on the other hand, led to consistently small B n's so that the DDs were either considered to be tangential discontinuities (TDs) or could not be clearly classified (Knetter et al., 2004; Knetter, 2005). The inconsistencies in the relative distributions of RDs and TDs based on different discontinuity analysis methods had been noted already earlier in a study of Horbury et al. (2001) using data from Geotail, IMP 8, and Wind. The state of the problem was summarized by Neugebauer (2006) who also reexamined a large number of solar wind discontinuities observed by the ISEE 3 spacecraft with inconclusive results, and discussed possible physical mechanisms.

The discrepancy in the distributions of boundary orientations obtained with different methods, and the resulting ambiguity in RD/TD classification may, for brevity, be termed discontinuity analysis inconsistency . In 2009, a team has formed at the International Space Science Institute in Bern to investigate the problem in detail. The present paper addresses one of the main team objectives, namely, the construction of a rigorous error analysis scheme for the timing method. Numerical experiments on this issue were carried out by Zhou et al. (2009). The purpose of our study is a fully analytical treatment of the problem. We start by introducing the reciprocal vector formalism in Sect. 2. In Sect. 3, we show how the main variants of the multi-point timing method all allow to write the boundary slowness vector as a linear combination of crossing times and reciprocal vectors. The error analysis in Sect. 4 starts from the slowness vector formula to quantify the mean square errors in boundary orientation and speed in terms of the spacecraft configuration, the estimated parameters, and the uncertainties in crossing times and spacecraft positions. The crossing time uncertainty is studied further in Sect. 5. In Sect. 6, the complete chain of boundary parameter estimation and error analysis is demonstrated using Cluster FGM measurements across a solar wind discontinuity. We conclude in Sect. 7 by summarizing the important steps of the error analysis procedure.

## 2 Reciprocal vectors in multi-spacecraft analysis

To facilitate the use of vectors in the definition of dyads and for the purpose of matrix multiplication, we adopt the notation conventions described, e.g. in Paschmann and Daly (1998): vectors a , b , c ,... are always understood as column vectors. They can be turned into row vectors by means of transposition denoted by the superscript T , e.g. a T . The hat symbol ˆ · indicates unit vectors, matrices are typeset in upright bold, and I denotes the identity matrix.

The positions of the spacecraft are given by r α ( α = 1 ,...,S ). Since we are mainly interested in the Cluster mis- sion with four spacecraft, we focus on S = 4 but consider the more general case where possible. Relative position vectors are written in the form r αβ = r β -r α . If the origin of our coordinate system coincides with the mean position (mesocenter) r ∗ = ( 1 /S) ∑ α r α of the spacecraft array, then obviously r ∗ = 0 and the reference frame is called mesocentric . Spacecraft position vectors in a mesocentric frame are denoted as r ∗ α , hence ∑ α r ∗ α = 0 . The so-called position tensor is defined through

<!-- formula-not-decoded -->

Throughout this paper, we assume that the number of spacecraft is at least four, and that they form a three-dimensional configuration that does not degenerate into a plane or a line. Then the position tensor R ∗ is a non-singular matrix (Vogt et al., 2008), and its inverse is the reciprocal tensor defined through

<!-- formula-not-decoded -->

where the (generalized) reciprocal vectors are given by

<!-- formula-not-decoded -->

Note the identity

<!-- formula-not-decoded -->

In the case S = 4, the vectors q α coincide with the reciprocal vectors of the spacecraft tetrahedron defined through

<!-- formula-not-decoded -->

(Chanteur, 1998) where (α,β,γ,λ) must be a cyclic permutation of ( 1 , 2 , 3 , 4 ) . In this case the symbol K is used for the reciprocal tensor, i.e.

<!-- formula-not-decoded -->

Useful algebraic identities for S = 4 are

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where δαβ denotes the Kronecker delta symbol.

Reciprocal vectors can also be defined for three-spacecraft configurations, see Vogt et al. (2009).

## 3 Boundary parameter estimation from crossing data

The problem of computing boundary parameters from the crossing times and the positions of a multi-spacecraft array has been studied by a number of authors (e.g. Burlaga and Ness, 1969; Russell et al., 1983; Dunlop et al., 1988;

Mottez and Chanteur, 1994; Schwartz, 1998; Dunlop and Woodward, 1998; Harvey, 1998; Soucek et al., 2004; Haaland et al., 2004; Vogt et al., 2008; Zhou et al., 2009). In its simplest and most popular form, the underlying model assumes a planar structure that varies only in the direction of the boundary unit normal vector ˆ n and propagates at a speed V along ˆ n relative to the spacecraft array. The model parameters ˆ n and V are conveniently combined into the boundary slowness vector

<!-- formula-not-decoded -->

The vector m can then be determined from a set of linear equations where the crossing times constitute the known data, and the spacecraft position vectors form the coefficient matrix that has to be inverted. There are essentially three variants of this procedure using (a) relative crossing data with respect to one reference spacecraft (e.g. Russell et al., 1983; Knetter et al., 2004), (b) all relative crossing data that are available (e.g. Soucek et al., 2004; Zhou et al., 2009), or (c) absolute crossing times and spacecraft positions (e.g. Haaland et al., 2004). To facilitate the comparison of these three options, we only consider four-spacecraft configurations and make use of algebraic identities for the tetrahedral reciprocal vectors k α ( α = 1 , 2 , 3 , 4). Note that options (b) and (c) can be easily generalized to configurations with more than four spacecraft by means of the generalized reciprocal vectors q α .

## 3.1 Crossing data relative to one reference spacecraft

To uniquely determine the three-component slowness vector m , knowledge of three relative position vectors r ρα and the corresponding differences tρα = tα -tρ in crossing times are sufficient. Here the subscript ρ denotes the reference spacecraft, and α /negationslash= ρ . The three conditions are thus Vtρα = r ρα · ˆ n which can be divided by the speed V to obtain

<!-- formula-not-decoded -->

Since any subset of three reciprocal vectors k β form a basis of three-dimensional space, the slowness vector can be expressed in the form m = ∑ β( /negationslash= ρ) Cρβ k β . The symbol ∑ β( /negationslash= ρ) indicates summation over all indices β except for β = ρ . To determine the three coefficients Cρα , we insert this ansatz into Eq. (10) to obtain

<!-- formula-not-decoded -->

where the identity k β · r ρα = δβα -δβρ has been used. The slowness vector is thus given by

<!-- formula-not-decoded -->

The restriction α /negationslash= ρ may be dropped by setting tρρ = 0, and then

<!-- formula-not-decoded -->

## 3.2 Using all available relative crossing data

Wecan incorporate all available crossing data into the boundary analysis by assigning the role of reference spacecraft to each one of them in turn, then compute slowness vector estimates m (ρ) using Eq. (12), and, finally, average the results to obtain m = ( 1 / 4 ) ∑ ρ m (ρ) . The result can be easily rearranged to yield:

<!-- formula-not-decoded -->

where tρρ = 0 as before. This form is completely equivalent to the least-squares result obtained by Harvey (1998) for a symmetrical treatment of relative crossing data. Using our notation, his Eq. (12.13) translates to

<!-- formula-not-decoded -->

Since R -1 ∗ r ρα = R -1 ∗ r ∗ α -R -1 ∗ r ∗ ρ = k α -k ρ , we get

<!-- formula-not-decoded -->

and with tρα =-tαρ the least-squares formula can be written in the form of Eq. (14).

## 3.3 Absolute crossing times

If a boundary crossing is unambiguously identified in the data of all spacecraft without reference to another, e.g. as the center time of a jump in one variable, or through correlation with a prescribed model profile, it is more appropriate to think in terms of absolute crossing times tα rather than their relative counterparts. We insert tρα = tα -tρ into Eq. (14) and use the identity ∑ α k α = 0 to obtain the formula

<!-- formula-not-decoded -->

The result holds for arbitrary time offsets.

The following version of Eq. (17) was derived by Chanteur (1998) from spatial interpolation theory, as well as by Harvey (1998) and Vogt et al. (2008) through a least squares approach:

<!-- formula-not-decoded -->

Here t ∗ α = tα -t ∗ , and the mean crossing time t ∗ = ( 1 / 4 ) ∑ α tα , was chosen as a reference point to center the time axis. It is straightforward to show that the linear combination of relative crossing times in Eq. (14) is equal to the respective absolute crossing time in the time frame centered at t ∗ as ( 1 / 4 ) ∑ ρ tρα = t ∗ α .

The case of an accelerated planar discontinuity was considered by Chanteur (1998), see Sect. 14.5.2 of that publication.

## 3.4 Comments on implementation

In all variants of the boundary triangulation approach discussed above, the slowness vector m is given in terms of the crossing times and the reciprocal vectors. It is important to note that the latter have to be computed from the relative crossing position vectors , i.e. from r αβ = r β (t β ) -r α(tα) . Here the spacecraft trajectories r α(t) and r β (t) have to be evaluated at the (absolute) crossing times tα and tβ , respectively. This means that the set of relative crossing times alone is not sufficient to determine the solution uniquely but must be supplemented by at least one absolute time datum such as the crossing time of one reference spacecraft.

The discussion in the following Sect. 4 shows that the relative crossing times which directly enter the slowness vector formulas should be known very precisely to yield accurate boundary parameter estimates. If δt denotes a reference value for the error in relative crossing times, then the additional absolute datum required for obtaining the crossing positions can tolerate an uncertainty δt ′ that is somewhat larger than δt . The resulting positional inaccuracies are of the order ˆ n · u αβ δt ′ where u αβ are the relative spacecraft velocities, corresponding to timing uncertainties ˆ n · u αβ δt ′ /V . For the Cluster mission, ˆ n · u αβ /V is a very small quantity (of the order of 10 -3 or less). This means that as long as δt and δt ′ are of the same order, we can disregard the contribution of the uncertainty in the additional absolute crossing time in the following error analysis.

If, however, instead of the actual crossing position vectors an instantaneous spacecraft configuration is used to compute the reciprocal vectors, another source of error comes into play that can no longer be neglected. Such a procedure yields additional timing inaccuracies of the order ˆ n · u αβ tαβ /V . Since the relative crossing times tαβ can be several orders of magnitude larger than their errors δt , the instantaneous configuration approximation may introduce significant inaccuracies and thus should be avoided.

## 4 Error analysis and array geometry

In this section we present the first part of the error analysis scheme for the timing approach to boundary parameter estimation. We give formulas for the errors in boundary orientation and speed, and assume that the primary uncertainties in crossing times and the positional inaccuracies are given in the form of error covariance matrices. The crossing time errors are quantified further in Sect. 5.

## 4.1 Analysis framework and general error formulas

The quality of boundary parameter estimation suffers from inaccuracies in crossing times and spacecraft positions. The problem was addressed, e.g. by Dunlop and Woodward (1998); Knetter (2005); Zhou et al. (2009). Analytical error formulas were derived by G´ erard Chanteur for the absolute crossing times approach in various contexts (e.g. Chanteur, 1998, 2000, 2003; Cornilleau-Wehrlin et al., 2003; Vogt et al., 2008), and a partial summary of Chanteur's results was also given in the PhD thesis of Knetter (2005). The analysis rests on Eq. (17) which is repeated here for convenience:

<!-- formula-not-decoded -->

Since Eq. (14) exhibits the same structure with tα being replaced by the expression [ ( 1 / 4 ) ∑ ρ tρα ] , the line of reasoning can in principle be applied also to this case.

With only mild assumptions on error correlations, Chanteur arrived at the following formula for the unit normal covariance matrix

<!-- formula-not-decoded -->

and wrote the error in boundary speed V in the form

<!-- formula-not-decoded -->

see Eqs. (4.33) and (4.34) in Vogt et al. (2008). Here

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and 〈 δ r δ r T 〉 γ denotes the positional error covariance for spacecraft number γ . For the Cluster mission, the positional error covariance matrices are available through the Cluster Active Archive (Volpp and Sieg, 2010).

If ˆ e is an arbitrary unit vector perpendicular to ˆ n , then ˆ e T 〈 δ ˆ n δ ˆ n T 〉 ˆ e is a quadratic measure of the angular uncertainty of ˆ n in the plane spanned by the two vectors ˆ e and ˆ n . If small compared to unity, this measure can be associated with the opening half angle (in ˆ e -direction) of an elliptical cone of uncertainty for the boundary unit normal vector:

<!-- formula-not-decoded -->

where

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The formulas (19)-(25) in this subsection provide the general framework for a rigorous error analysis of the timing method. They give the uncertainties in boundary orientation and speed in terms of the error covariance matrices of crossing times and spacecraft positions. For illustrating purposes, we proceed with order-of-magnitude estimates and simplifications that allow to highlight the influence of the spacecraft configuration and the boundary parameters on the overall accuracy.

## 4.2 Primary errors and relative importance

The error term C 1 is controlled by uncertainties in crossing time estimates, and C 2 originates from positional uncertainties (note that the errors in relative position vectors matter here). To assess the relative importance of the two error contributions, we assume crossing time uncertainties ∼ δt , relative positional errors ∼ δr , boundary speeds ∼ V , and inter-spacecraft separations ∼ L . Then C 1 ∼ (δt/L) 2 , C 2 ∼ (δr/V L) 2 , and thus

<!-- formula-not-decoded -->

For the Cluster mission, δr is in the kilometer range or below (Volpp and Sieg, 2010). This has to be compared with the product Vδt that is usually much larger in the geospace context. The Cluster FGM instrument with its high but finite time resolution of about 0.05 s (in normal mode) cannot be expected to yield discontinuity time uncertainties significantly smaller than δt ∼ 0 . 1 s in the presence of noise. Hence for boundary speeds of the order 100 km s -1 and above, C 2 is much smaller than C 1, and the effects of positional errors can be safely neglected against those of timing uncertainties. For instruments operating at spacecraft spin resolution, the timing error is expected to be in the range of the spin period, then this statement holds even for much smaller boundary speeds of order 10 km s -1 .

If the timing uncertainties and positional covariances are the same for each spacecraft and mutually uncorrelated, the slowness error covariance matrix simplifies to

<!-- formula-not-decoded -->

where K is the reciprocal tensor. When in addition the positional error matrix is isotropic, i.e.

<!-- formula-not-decoded -->

then

<!-- formula-not-decoded -->

If positional inaccuracies can be ignored, the term in square brackets reduces to (δt) 2 . In the remainder of the present section this approximation is employed to study the influence of tetrahedron geometry on boundary parameter estimation accuracy. To recover the complete formulas with the effects of positional inaccuracies included, one may replace

<!-- formula-not-decoded -->

or

<!-- formula-not-decoded -->

## 4.3 Influence of the spacecraft array geometry

The error formulas for the simplified case are

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where ˆ e is perpendicular to ˆ n , and δV/V is used as a shorthand notation for √ 〈 (δV ) 2 〉 /V , i.e. the relative rms error in boundary speed. To study the influence of the spacecraft array geometry on boundary parameter accuracy, we write the reciprocal tensor in terms of its eigenvectors and the tetrahedron geometric parameters planarity P , elongation E , and the rms inter-spacecraft distance L . The expression for the resulting quadratic form c T K c is given in Appendix A where also the parameters P , E , and L are defined. Note that P = 1 if all spacecraft are in one plane and E = 1 if they lie on a straight line (string-of-pearls configuration), and that spacecraft configurations close to an ideal tetrahedron correspond to small values of planarity and elongation: P ≈ 0 and E ≈ 0. In the quadratic form c T K c , we set c = ˆ n to compute δV , and c = ˆ e for δθ . Hence the errors depend on the orientation of the spacecraft tetrahedron, on the length scale L , and on the shape parameters E and P . To assess the full range of possible errors, we assume that the boundary unit normal vector is aligned with the three eigenvectors ˆ e ( n ) one by one.

## 4.3.1 Boundary unit normal aligned with the direction of elongation

The direction of elongation is given by the eigenvector ˆ e ( 1 ) to the largest eigenvalue R ( 1 ) ∗ of R ∗ which corresponds to the smallest eigenvalue of K . If ˆ n = ˆ e ( 1 ) , then ˆ e = ˆ e ( 2 ) yields the minimum angular uncertainty, and ˆ e = ˆ e ( 3 ) its maximum value:

<!-- formula-not-decoded -->

The error in boundary speed is given by

<!-- formula-not-decoded -->

This is the best case (highest accuracy) for the speed estimation but the worst case (lowest accuracy) for the computation of the boundary normal.

## 4.3.2 Boundary unit normal aligned with the direction of planarity

The direction of planarity is given by the eigenvector ˆ e ( 3 ) to the smallest eigenvalue R ( 3 ) ∗ of the position tensor, or the largest eigenvalue of the reciprocal tensor. If ˆ n = ˆ e ( 3 ) , then ˆ e = ˆ e ( 1 ) yields the minimum angular uncertainty, and ˆ e = ˆ e ( 2 ) its maximum value:

<!-- formula-not-decoded -->

The error in boundary speed is given by

<!-- formula-not-decoded -->

This is the best case (highest accuracy) for the computation of the boundary normal and the worst case (lowest accuracy) for the speed estimation.

## 4.3.3 Boundary unit normal aligned with the eigenvector to the intermediate eigenvalue

The eigenvector ˆ e ( 2 ) belongs to the intermediate eigenvalues both of the position tensor and the reciprocal tensor. If ˆ n = ˆ e ( 2 ) , then ˆ e = ˆ e ( 1 ) yields the minimum angular uncertainty, and ˆ e = ˆ e ( 3 ) its maximum value:

<!-- formula-not-decoded -->

The error in boundary speed is given by

<!-- formula-not-decoded -->

This is the intermediate case for both boundary normal and speed estimation.

The results for the three cases presented above can be combined to yield representative errors for a particular spacecraft geometry. We average the squares of both the angular uncertainty and the error in speed to obtain

<!-- formula-not-decoded -->

where

<!-- formula-not-decoded -->

Fig. 1. Influence of array geometry on the accuracy of the timing method: reference error V δt/L . Blue and solid contour lines give the relative error in boundary speed δV/V in percent. Red and dashed contour lines give the directional uncertainty δθ in degrees. Control variables are the inter-spacecraft length scale L and the boundary speed both for crossing time inaccuracies δt = 0 . 1 s (annotation at the left y-axis) and δt = 1 s (annotation at the right y-axis). The spacing of the contour lines is logarithmic.

<!-- image -->

The meaning of the term trace ( K ) = ∑ 4 α = 1 | k α | 2 in the context of error amplification was recognized by Vogt and Paschmann (1998) in their study on the accuracy of spatial derivatives, and its importance was confirmed in the thorough analysis presented by Chanteur (2000) who further studied the dependence on L , P , and E . For further details the reader is referred to the original publications and to Vogt et al. (2008). Note that for planarity values close to one, the function A is well approximated as A /similarequal ( 1 -E) -1 ( 1 -P) -1 .

## 4.4 Reference error of the timing method

For geometrically ideal spacecraft configurations characterized by zero values of planarity and elongation, the directional inaccuracy δθ and the relative error in boundary speed δV/V are both given by

<!-- formula-not-decoded -->

For brevity, we refer to the term V δt/L as the reference error (of the timing method).

Figure 1 shows V δt/L as a function of inter-spacecraft length scale L and boundary speed V both in percent (blue solid contours, for δV/V ) and in degrees (red dashed contours, for δθ ). The boundary speed values at the left y-axis are for δt = 0 . 1 s in which case the error formulas are

<!-- formula-not-decoded -->

Fig. 2. Influence of array geometry on the accuracy of the timing method: geometrical error amplification for the worst-case relative orientation of the boundary normal vector with respect to the spacecraft configuration. In this case the geometrical error amplification function is given by 1 / [ ( 1 -E)( 1 -P) ] where E is elongation and P is planarity. The contour lines in the plot are spaced logarithmically.

<!-- image -->

and

<!-- formula-not-decoded -->

For other values of δt , the numerical factors on the righthand side of the equation must be multiplied by δt/ 0 . 1 s. The numerical values of the boundary speeds for the case δt = 1 s have been added in Fig. 1 at the right y-axis for convenience.

The smallest reference errors occur when L is large and both V and δt are small. In this sense magnetopause studies (boundary speed V ∼ 10 km s -1 ) using high-resolution Cluster FGM data ( δt ∼ 0 . 1 s) from the year 2003 ( L ∼ 5000 km) provide a best case scenario as directional inaccuracies could theoretically be as small as 0 . 01 deg, if in fact the magnetopause behaved as an ideal planar structure on the time scale of the transition (500 s) and on length scales close to one Earth radius. A worst case scenario for the reference error is the study of solar wind discontinuities ( V ∼ 100 km s -1 ) using Cluster plasma measurements at spin resolution ( δt ∼ 4 s) from the year 2002 ( L ∼ 100 km) which gives a relative error in boundary speed of 400 %. High-resolution FGM data ( δt ∼ 0 . 1 s) yield a value of 10 %.

## 4.5 Geometrical error amplification

Spacecraft array geometries that deviate from an ideal regular configuration are characterized by non-zero values of elongation and planarity. The errors δθ and δV/V are products of the reference error V δt/L and functions that depend

Fig. 3. Influence of array geometry on the accuracy of the timing method: logarithmically spaced contours of the average geometrical error amplification function A(E,P)/ √ 3 in terms of the elongation E and the planarity P of the spacecraft tetrahedron.

<!-- image -->

only on the shape parameters E and P , so the latter may be termed (geometrical) error amplification factors . The effects of non-ideal configurations are shown in Figs. 2 and 3. The worst-case error amplification both for δV/V and δθ with respect to their reference values is given by the function 1 / [ ( 1 -E)( 1 -P) ] , see Fig. 2. The function A(E,P)/ √ 3 displayed in Fig. 2 can be understood as an average error amplification factor.

Numerical experiments on the accuracy of the timing method were carried out by Zhou et al. (2009). They generated a reservoir of spacecraft tetrahedra with a homogeneous distribution in elongation and planarity, and then simulated crossings of planar discontinuities with timing errors that were identical at all four spacecraft and mutually uncorrelated. The resulting distributions of errors in boundary orientation and speed are shown as function of elongation and planarity in Figs. 1, 2, and 4 of Zhou et al. (2009). They compare nicely with the corresponding contour plots of the present study (Figs. 2 and 3), in particular with regard to the sharp increase in errors for values of elongation and planarity close to unity. We take this as a consistency check of our analytical error formulas that are easier to apply to actual data.

## 5 Crossing time errors

The timing method in boundary parameter estimation rests on the crossing times tα . Our error analysis scheme presented in the previous Sect. 4 requires the crossing time error covariances 〈 δtα δtβ 〉 as input parameters. The present section aims at quantifying these error covariances through a pattern

matching approach: we study the similarity of a signal s with shifted versions of a pattern function p . For notational convenience, we write τ for the crossing time difference and refer to it also as the lag (time) . An overbar ··· denotes the time averaging operation. The averaging window is assumed to be fixed with respect to the pattern function. Thus the window would have to move with the lag time τ if we defined the association measures in terms of the pair s(t) and p(t -τ) . Instead we choose to write the formulas using the pair s(t + τ) and p(t) so that the averaging window is fixed and symmetric with respect to the time origin.

## 5.1 Association measures

A variety of association measures can be employed to quantify the similarity of a time series s and a pattern function p at a time shift τ . Here we choose the mean square deviation

<!-- formula-not-decoded -->

because it allows to derive analytical error formulas, and it is sensitive also to linear variations in the data. The latter statement is not true for Pearson's correlation coefficient

<!-- formula-not-decoded -->

where u ◦ = u ◦ (t) is the centered version of a time series u = u(t) defined through u ◦ (t) = u(t) -u(t) . The coefficient γ is designed to measure linear correlation: if p(t) and s(t) are both linear functions, then γ(τ) = 1 irrespective of the lag time τ . The correlation coefficient can be made sensitive to linear variations in the data by replacing s ◦ and p ◦ in the formula with its non-centered counterparts s and p .

Further association measures such as the mean absolute deviation | s(t + τ) -p(t) | were tested by means of numerical experiments using synthetic data first, and then actual Cluster FGM measurements of solar wind discontinuities. In the noise-free limit the mean absolute deviation allows for an easier identification of crossing times than the mean square deviation. However, in the presence of noise or for actual measurements the differences turned out to be minor.

It may also be noted that mean deviation measures exhibit a misleading dependence on window width in graphical displays of association measures. This problem can be easily rectified by a multiplication with the number of data points in the averaging window to yield cumulative deviation measures (R. Wicks, private communication). The analytical error analysis given below is valid for both the mean square deviation as well as its cumulative counterpart.

## 5.2 Analytical error formulas

The following formula for the crossing time error covariances is derived in Appendix B:

<!-- formula-not-decoded -->

The underlying assumptions can be summarized as follows.

- -Crossing times estimates are assumed to be based on the mean square deviations Iα(τ) =| sα(t + τ) -p(t) | 2 between a pattern p and the signals sα at lag time τ .
- -The pattern p(t) is expected to show a transition at the origin between approximately constant levels at both ends of the data window. Examples are an ideal step (Heaviside) function or a hyperbolic tangent profile. When timing is only relative, a windowed portion of a discontinuity crossing observed at a reference spacecraft ρ may also serve as a pattern function for the signal measured at another spacecraft α .
- -The residuals hα are estimated through

<!-- formula-not-decoded -->

where ˜ τα, ∗ is the lag time at the minimum of the mean square deviation Iα .

- -The residuals hα are assumed to be time-stationary random signals that are well characterized by their means and their correlation functions. Angular brackets 〈···〉 denote the ensemble averaging with respect to the residuals.
- -An overbar ··· indicates time averaging, Tw is the time interval used for averaging, and N is the number of data points in the time window.
- -The time difference parameter /Delta1 in the sum ∑ /Delta1 runs from -Tw to + Tw , at least in principle. In boundary analysis practice, when pattern functions p(t) are characterized by constant levels left and right of the transition, the factor p ′ (t)p ′ (t + /Delta1) effectively cuts off the /Delta1 summation.

Note that although both /Delta1 and τ denote time differences, we prefer to use two different symbols as they appear in different contexts.

A second version of the error covariance formula can be obtained through normalization of the correlation functions. We define

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

As explained in Appendix B, the factor ( 1 -| /Delta1 | /Tw) comes into play through the autocorrelation function p ′ (t)p ′ (t + /Delta1) and was thus included in the definition of G(/Delta1) . The mean square (time) average of hα(t) is the minimum value of the mean square deviation Iα :

<!-- formula-not-decoded -->

The crossing time error covariances can thus be written in the form:

<!-- formula-not-decoded -->

All information on the right-hand side of this equation can be constructed from the measurements. Implementation of the crossing time error covariance formulas is discussed below in Sect. 7 where the complete error analysis scheme is summarized.

In some special cases the sum ∑ /Delta1 in Eq. (52) collapses to a single term.

- -If the pattern function p(t) is an ideal step (Heaviside) function, the transition between the two states at both ends of the data window occurs within a sampling interval, then p ′ (t) = 0 for t /negationslash= 0 and thus G(/Delta1) = 0 for /Delta1 /negationslash= 0. The error formula then simplifies to

<!-- formula-not-decoded -->

- -If the residuals hα(t) and hβ(t) can be represented as mutually uncorrelated white noise, then Hαβ(/Delta1) = 0 for α /negationslash= β or /Delta1 /negationslash= 0, so its only non-zero value is Hαα( 0 ) = 1, and we obtain

<!-- formula-not-decoded -->

The result is consistent with a formula derived by Alexander Khrabrov (private communication; see also Eq. 1.7 in Sonnerup et al., 2008) for this idealized case. In nonlinear and turbulent space plasmas such as the solar wind, however, such correlations in the measurements cannot be disregarded.

## 6 Example

To demonstrate the error analysis scheme presented in this paper, Cluster FGM measurements of a solar wind discontinuity are considered. After computing the boundary parameter estimates, we proceed with the crossing time error covariance formula (52). Particular emphasis will be on the functions G and Hαβ that quantify the effect of correlations in the set of residuals. Then the slowness vector covariances are computed and, finally, the errors of boundary speed and direction.

Fig. 4. Crossing time error analysis using a tanh pattern function: Cluster FGM data (solid) and pattern functions (dashed, magenta) used for illustrating the crossing time error formulas. Shown are the B y components of the interplanetary magnetic field measured by the four Cluster spacecraft (S/C 1: black, S/C 2: red, S/C 3: green, S/C 4: blue) when they crossed a directional discontinuity shortly before and after 19:11:30 UTC.

<!-- image -->

## 6.1 Boundary parameter estimates

The data are shown in Fig. 4. We are looking at the magnetic field signature of a directional discontinuity in the solar wind crossed by all four Cluster spacecraft at around 19:11:30 UTC on 3 February 2003. Superposed are shifted versions of the hyperbolic tangent pattern function

<!-- formula-not-decoded -->

where the parameters B off , B amp, and T dis were obtained from visual comparison with the data. In principle, the model parameters could also be determined through a least-squares fit to a composite profile. The length of the pattern time window was chosen to be 10 s. The actual crossing times tα were determined from minima of the mean square deviations Iα(τ) , see Eq. (45). Relative to the reference time 19:11:00 UTC, their numerical values are 35.345 s, 29.324 s, 30.216 s, and 26.068 s for S/C 1 through S/C 4, respectively. The numbers are given with three digits as the sampling interval is T sam = 44 . 6 ms.

Then the reciprocal vectors k α were computed from the spacecraft positions at tα , and, finally, the boundary slowness vector m from Eq. (17):

<!-- formula-not-decoded -->

Boundary speed and normal unit vector:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The geometrical parameters of the spacecraft configuration are L = 3300 km, P = 0 . 19, and E = 0 . 27. Geometrical error amplification is small. The simplified error analysis presented in Sects. 4.3-4.5 suggests that the relative error in

Fig. 5. Crossing time error analysis using a tanh pattern function. Top: residuals computed from the Cluster FGM data and tanh pattern functions in Fig. 4 as functions of centered array subscripts. The total time window is 10 s (sampling interval 44.6 ms). Bottom: products of correlation functions G(/Delta1) and Hαβ (/Delta1) that enter the sum in the crossing time error formula (52). Shown are the profiles for α = 1. The four colors correspond to spacecraft no. β as listed in the caption of Fig. 4.

<!-- image -->

boundary speed should be of the order of percent, and the directional error should be in the range of one degree.

## 6.2 Crossing time error covariances

To evaluate the crossing time error covariance formula (52), the functions G and Hαβ have to be computed. For the hyperbolic tangent pattern function p(t) chosen here, the (normalized) autocorrelation function G(/Delta1) of the time derivative d p/ d t drops to small values &lt; 0 . 1 beyond ± 50 samples away from the origin ( | /Delta1 | &gt; 2 . 2s), thus effectively limiting the summation in Eq. (52).

The residuals hα(t) in the upper panel of Fig. 5 were constructed according to Eq. (48). Note that by construction the residuals are centered around the actual crossing time. Welldeveloped structures in the diagram already suggest that the ideal white noise model does not apply. Products of correlation functions G(/Delta1) and Hαβ(/Delta1) are displayed in lower panel of Fig. 5 for α = 1. The results for α = 2 , 3 , 4 are qual-

Table 1. Crossing time error analysis using a tanh pattern function: elements of the crossing time error covariance matrix 〈 δtα δt β 〉 for the solar wind discontinuity observed by the FGM instruments onboard the Cluster spacecraft shortly before and after 19:11:30 UTC on 3 February 2003. The matrix elements are given in units of T 2 sam where T sam = 44 . 6 ms is the sampling interval.

| 〈 δt α δt β 〉 /T 2 sam   |   β = 1 |   β = 2 |   β = 3 |   β = 4 |
|----------------------------|---------|---------|---------|---------|
| α = 1                      |    8.82 |    6.04 |    3.97 |    4.93 |
| α = 2                      |    6.04 |    7.08 |    2.68 |    4.04 |
| α = 3                      |    3.97 |    2.68 |    4.11 |    2.62 |
| α = 4                      |    4.93 |    4.04 |    2.62 |    4.07 |

itatively very similar. The numerical values of the sum in Eq. (52) are the integrals under the curves. In our example they are in the range from 12 ( α = 2 ,β = 3) to 31 ( α = β = 1).

All variables on the right-hand side of the crossing time error formula (52) are now available and the crossing time error covariance matrix 〈 δtα δtβ 〉 can be computed which in turn yields the slowness error covariances and all other uncertainties through the formulas in Sect. 4. The resulting matrix elements are given in Table 1. The diagonal elements ( α = β ) of the table can be understood as the square inaccuracies of the timing method at the respective spacecraft. Taking the square root yields values √ 〈 δt 2 α 〉 around 0.1 s, i.e. in the range of 2-3 sampling intervals.

Note that also the off-diagonal elements ( α /negationslash= β ) of the error covariance matrix 〈 δtα δtβ 〉 are positive which reflects the fact that the residuals hα are positively correlated. In other words, the residuals share common substructures. When these common features are incorporated in the pattern function, it should in principle be better adapted to this particular data set. We constructed such an empirical pattern function by first averaging the four residuals hα(t) and then adding the resulting profile to the initial tanh pattern function. Using the empirical pattern function and a new set of residuals, the cross correlation ( α /negationslash= β ) functions Hαβ(/Delta1) were found to be predominantly negative around the origin. Furthermore, the elements of the crossing time error covariance matrix 〈 δtα δtβ 〉 turned out to be smaller in magnitude. Refining the pattern function may thus help to improve the accuracy of the timing method. A detailed study of the effects of empirical pattern functions on crossing time errors would be beyond the scope of the present paper and is left for future work.

## 6.3 Boundary parameter errors

As explained in Sect. 4.1, the errors in boundary speed and normal unit vector are computed from the slowness error covariance matrix 〈 δ m δ m T 〉 which in turn is found from Eq. (21). Following the discussion in Sect. 4.2, we disregard the contribution from the positional inaccuracies and consider the crossing time error covariances only. For the Cluster

Table 2. Crossing time error analysis using a tanh pattern function: elements of the slowness error covariance matrix 〈 δ m δ m T 〉 for the solar wind discontinuity observed by the FGM instruments onboard the Cluster spacecraft shortly before and after 19:11:30 UTC on 3 February 2003. The matrix elements are given in units of 10 -10 ( s m -1 ) 2 .

| 〈 δ m δ m T 〉 10 - 10 ( sm - 1 ) 2 ]   | x      | y      | z      |
|------------------------------------------|--------|--------|--------|
| x                                        | 6 . 81 | - 1.76 | - 1.83 |
| y                                        | - 1.76 | 5 . 81 | - 3.62 |
| z                                        | - 1.83 | - 3.62 | 8 . 97 |

discontinuity crossing studied here, the numerical values of the slowness error covariances are given in Table 2. The resulting uncertainty in boundary speed is δV = 5 km s -1 , and the range of the directional error δθ is 0.6-0.9 deg.

## 7 Summary

The principle variants of the timing approach to boundary analysis discussed in Sect. 3 require slightly different parameter estimation and error analysis strategies. In the present study we concentrated on absolute crossing times determined through minima of the mean square deviation I (τ ) of the data from a predefined pattern function such as a hyperbolic tangent profile. If the relative crossing time approach is employed, we recommend to construct an effective pattern function p(t) for the error analysis as follows: first apply time shifts to the signals so that the transitions all occur at the origin, and then average to obtain p(t) .

The advantages of absolute crossing times over their relative counterparts are not only of technical nature. Comparing the data with a predefined pattern means that we are in explicit control of the features in the data that we wish to associate. In the relative crossing time method one compares segments of two time series around a transition (that has usually been identified by eyeballing) but the result can be distorted by substructures in the data that may move at different speeds than the boundary itself, and that may have been identified by some (pairs of) sensors but not by others. Furthermore, substructures that are moving in the plasma frame have different effects on the two main types of directional discontinuities which motivated our error analysis in the first place: TDs are stationary in the plasma frame whereas RDs propagate through the plasma. In the absolute crossing time method with a predefined pattern, such substructures become part of the residuals and are thus taken care of in the error analysis. Alternatively, they can be made explicit through an empirical pattern function as explained at the end of Sect. 6.

To implement the multi-point crossing time method to boundary parameter estimation and the error analysis scheme presented in this paper, we recommend to proceed as follows.

## 7.1 Crossing times tα and boundary parameters m , ˆ n ,V

Choose a pattern function p(t) , construct the mean square deviations Iα(τ) of p(t) and the shifted signals sα(t + τ) , and identify the crossing times tα as the lag values at the minima of the Iα 's. Take the spacecraft positions at tα to compute the reciprocal vectors k α . Obtain the boundary slowness vector m from Eq. (17), then compute V = 1 / | m | and ˆ n = V m .

## 7.2 Crossing time error covariances 〈 δtα δtβ 〉

Compute the residuals from Eq. (48), the correlation functions p ′ (t)p ′ (t + /Delta1) and hα(t)hβ(t + /Delta1) , and then evaluate the sum on the right-hand side of Eq. (47). Alternatively, compute the functions G(/Delta1) and Hαβ(/Delta1) from Eqs. (49) and (50), and use Eq. (52) to obtain 〈 δtα δtβ 〉 .

## 7.3 Boundary parameter errors 〈 δ ˆ n δ ˆ n T 〉 and 〈 (δV ) 2 〉

Equation (19)-(25) give the mean square errors of the boundary parameters ˆ n and V for general crossing time error covariances 〈 δtα δtβ 〉 and spacecraft position covariance matrices 〈 δ r δ r T 〉 γ . To check if the latter make a significant contribution, carry out an order-of-magnitude assessment similar to the one in Sect. 4.2. If the assessment is negative, positional inaccuracies can be disregarded and the error formulas simplify considerably.

In the second and third step, it is essential to construct the full crossing time error covariance matrix 〈 δtα δtβ 〉 , and then to use the general formula for 〈 δ ˆ n δ ˆ n T 〉 . Correlations in the set of residuals are particularly important. If they are disregarded and an oversimplified white noise model is used to estimate 〈 δtα δtβ 〉 , the crossing time errors may come out far too small.

## Appendix A

## Tetrahedron geometry parameters and the reciprocal tensor

The geometrical shape of the spacecraft configuration can be characterized through the eigenvalues and eigenvectors of the so-called volumetric tensor R vol = ( 1 /S) R ∗ (Robert et al., 1998) that differs from the position tensor R ∗ only by the constant factor, so they share the same set of eigenvectors { ˆ e (n) } ,n = 1 , 2 , 3, and the eigenvalues are related through R (n) vol = ( 1 /S)R (n) ∗ . Assuming that the eigenvalues are arranged in descending order R ( 1 ) ∗ ≥ R ( 2 ) ∗ ≥ R ( 3 ) ∗ ≥ 0, an intrinsic length scale L (inter-spacecraft distance) and two shape parameters P (planarity) and E (elongation) can be defined

as follows for the tetrahedral case S = 4:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The eigenvector ˆ e ( 1 ) to the largest eigenvalue R ( 1 ) is associated with the direction where the configuration appears stretched. The eigenvector ˆ e ( 3 ) to the smallest eigenvalue is normal to the surface of planarity. For further discussion of the geometric quality of a tetrahedron, the reader is referred to Robert et al. (1998). Using the eigenvalues and eigenvectors, the position tensor can be written in the dyadic form

<!-- formula-not-decoded -->

The eigenvalues Q (n) of the generalized reciprocal tensor Q = R -1 ∗ are Q (n) =[ R (n) ] -1 . Furthermore, Q and R ∗ share a common set of eigenvectors, thus

<!-- formula-not-decoded -->

The tetrahedral reciprocal tensor K = ∑ α k α k T α can be expressed in terms of the parameters L , E , P and the eigenvectors ˆ e (n) of R ∗ as follows (see, e.g. Chanteur, 2000):

<!-- formula-not-decoded -->

The associated quadratic form c T K c takes an arbitrary vector c and yields the scalar value

<!-- formula-not-decoded -->

## Appendix B

## Crossing time error covariance

The following analysis addresses the accuracy of crossing time estimation based on the mean square deviation

<!-- formula-not-decoded -->

of a signal s shifted by the lag time τ and a pattern p . Here the overbar ··· indicates time averaging. Angular brackets 〈···〉 denote the ensemble averaging with respect to the residual to be specified in more detail further below.

Let τ ∗ denote the numerical value of the lag time at the minimum of the mean square deviation for the (hypothetical) 'noise-free' case, and ˜ τ ∗ the estimated lag time based on a 'noisy' measurement. Note that in this context the term 'noise' refers to all contributions to the signal other than the given pattern function. If noise was absent, then ˜ τ ∗ = τ ∗ . In the presence of noise, the mean square deviation I (τ ) is nonzero for all values of τ , and the estimated lag time ˜ τ ∗ (i.e. the minimum of the empirical mean square deviation) differs from the true lag time τ ∗ .

The mismatch of pattern and signal at time shift τ ∗ defines the residual:

<!-- formula-not-decoded -->

To accomplish the error analysis, we wish to translate the mean square deviation I ( ˜ τ ∗ ) into a function J(δt) where δt denotes the deviation of the estimated lag from its true value:

<!-- formula-not-decoded -->

Since I ( ˜ τ ∗ ) =| s(t +˜ τ ∗ ) -p(t) | 2 , we start by rearranging as follows:

<!-- formula-not-decoded -->

For the mean square deviation we then obtain

<!-- formula-not-decoded -->

Inserting the Taylor expansions

<!-- formula-not-decoded -->

into J(δt) yields the following quadratic approximation:

<!-- formula-not-decoded -->

We assume the residual and its derivatives to be sufficiently small compared to the derivatives of the pattern function so that only the dominant contributions need to be kept, namely, p ′ h in the linear term, and p ′ 2 in the quadratic term. Computing δt from the condition J ′ (δt) = 0 then leads to δt =-p ′ h/p ′ 2 and thus

<!-- formula-not-decoded -->

for measurements at several sensors α,β such as the FGM instruments onboard the Cluster spacecraft ( α,β = 1 , 2 , 3 , 4).

To arrive at an estimate for the error covariance matrix 〈 δtα δtβ 〉 , we think of the residuals hα and hβ as realizations of time-invariant and ergodic random processes that are well characterized by their means and correlation functions. Then 〈···〉 is the average with respect to the random functions hα and hβ . Since the denominator does not depend on the residuals, it is a constant in the ensemble averaging procedure. For the numerator we obtain

<!-- formula-not-decoded -->

Here N is the number of data points in the time averaging window. The ensemble average of this expression is

<!-- formula-not-decoded -->

where the expression 〈 hα(tµ)hβ(tν) 〉 can be further rearranged as follows

<!-- formula-not-decoded -->

with /Delta1 = tν -tµ . This is the correlation between hα and hβ at time tµ and lag /Delta1 . Since the residuals are assumed to be realizations of random processes that are time-invariant and ergodic, the dependence on tµ can be dropped, and the ensemble average can be replaced by a time average. We then obtain

<!-- formula-not-decoded -->

and thus, after replacing the ν -summation by an equivalent summation over the variable /Delta1 ,

<!-- formula-not-decoded -->

Up to a constant factor, the sum ∑ µ p ′ (tµ)p ′ (tµ + /Delta1) is also a correlation function: if Tw denotes the time interval covered by the time window used to compute averages, the number of terms in the sum is N · ( 1 -| /Delta1 | /Tw) , hence ∑ µ p ′ (tµ)p ′ (tµ + /Delta1) is an approximation of the product N · ( 1 -| /Delta1 | /Tw) · p ′ (t)p ′ (t + /Delta1) .

Combining the partial results yields the following expression for the crossing time error covariances

<!-- formula-not-decoded -->

In principle, the time difference /Delta1 runs from -Tw to Tw . In practice, its scope is limited by the effective range of the correlation functions.

Acknowledgements. The authors thank the International Space Science Institute in Bern for hosting the team project on Directional Discontinuities in the Interplanetary Magnetic Field. The work of JV was supported through DFG grant VO 855/3-1. The authors thank Alexander Khrabrov for clarifying comments on his error formulas, and Robert Wicks for drawing attention to cumulative deviation measures. We also wish to acknowledge the team of the Cluster FGM instrument and the Cluster Active Archive (CAA).

Topical Editor I. A. Daglis thanks S. C. Buchert and G. M. Chanteur for their help in evaluating this paper.

## References

Burlaga, L. F. and Ness, N. F.: Tangential Discontinuities in the Solar Wind, Sol. Phys., 9, 467-477, doi:10.1007/BF02391672, 1969.

- Chanteur, G.: Spatial Interpolation for Four Spacecraft: Theory, in: Analysis Methods for Multi-Spacecraft Data, edited by: Paschmann, G. and Daly, P., pp. 371-393, ISSI/ESA, 1998.
- Chanteur, G.: Accuracy of field gradient estimations by Cluster: Explanation of its dependency upon elongation and planarity of the tetrahedron, pp. 265-268, ESA SP-449, 2000.
- Chanteur, G.: Four spacecraft determination of wave front normals and velocities, in: Spatio-Temporal Analysis and Multipoint Measurements in Space, Orl´ eans, France, 2003, 2003.
- Cornilleau-Wehrlin, N., Chanteur, G., Perraut, S., Rezeau, L., Robert, P., Roux, A., de Villedary, C., Canu, P., Maksimovic, M., de Conchy, Y., Hubert, D., Lacombe, C., Lefeuvre, F., Parrot, M.,

- Pinon, J. L., D´ ecr´ eau, P . M. E., Harvey, C. C., Louarn, Ph., Santolik, O., Alleyne, H. St. C., Roth, M., Chust, T., Le Contel, O., and STAFF team: First results obtained by the Cluster STAFF experiment, Ann. Geophys., 21, 437-456, doi:10.5194/angeo-21-4372003, 2003.
- Dunlop, M. W. and Woodward, T. I.: Multi-Spacecraft Discontinuity Analysis: Orientation and Motion, in: Analysis Methods for Multi-Spacecraft Data, edited by: Paschmann, G. and Daly, P., pp. 271-305, ISSI/ESA, 1998.
- Dunlop, M. W., Southwood, D. J., Glassmeier, K.-H., and Neubauer, F. M.: Analysis of multipoint magnetometer data, Adv. Space Res., 8, 273-277, 1988.
- Haaland, S. E., Sonnerup, B. U. ¨ O., Dunlop, M. W., Balogh, A., Georgescu, E., Hasegawa, H., Klecker, B., Paschmann, G., Puhl-Quinn, P., R` eme, H., Vaith, H., and Vaivads, A.: Fourspacecraft determination of magnetopause orientation, motion and thickness: comparison with results from single-spacecraft methods, Ann. Geophys., 22, 1347-1365, doi:10.5194/angeo22-1347-2004, 2004.
- Harvey, C. C.: Spatial Gradients and the Volumetric Tensor, pp. 307-322, ISSI SR-001, 1998.
- Horbury, T. S., Burgess, D., Fr¨ anz, M., and Owen, C. J.: Three spacecraft observations of solar wind discontinuities, Geophys. Res. Lett., 28, 677-680, doi:10.1029/2000GL000121, 2001.
- Knetter, T.: A new perspective of the solar wind micro-structure due to multi-point observations of discontinuities, Disseration, Universit¨ at K¨ oln, 2005.
- Knetter, T., Neubauer, F. M., Horbury, T., and Balogh, A.: Fourpoint discontinuity observations using Cluster magnetic field data: A statistical survey, J. Geophys. Res., 109, A06102, doi:10.1029/2003JA010099, 2004.
- Lepping, R. P. and Behannon, K. W.: Magnetic field directional discontinuities - Characteristics between 0.46 and 1.0 AU, J. Geophys. Res., 91, 8725-8741, doi:10.1029/JA091iA08p08725, 1986.
- Mottez, F. and Chanteur, G.: Surface crossing by a group of satellites: A theoretical study, J. Geophys. Res., 99, 13499, doi:10.1029/93JA03326, 1994.
- Neugebauer, M.: Comment on the abundances of rotational and tangential discontinuities in the solar wind, J. Geophys. Res., 111, 4103, doi:10.1029/2005JA011497, 2006.
- Neugebauer, M., Clay, D. R., Goldstein, B. E., Tsurutani, B. T., and Zwickl, R. D.: A reexamination of rotational and tangential discontinuities in the solar wind, J. Geophys. Res., 89, 53955408, doi:10.1029/JA089iA07p05395, 1984.
- Paschmann, G. and Daly, P. W.: Analysis Methods for MultiSpacecraft Data, no. SR-001 in ISSI Scientific Reports, ESA Publ. Div., Noordwijk, Netherlands, 1998.
- Robert, P., Roux, A., Harvey, C. C., Dunlop, M. W., Daly, P. W., and Glassmeier, K.-H.: Tetrahedron Geometric Factors, pp. 323-348, ISSI SR-001, 1998.
- Russell, C. T., Gosling, J. T., Zwickl, R. D., and Smith, E. J.: Multiple spacecraft observations of interplanetary shocks ISEE threedimensional plasma measurements, J. Geophys. Res., 88, 99419947, doi:10.1029/JA088iA12p09941, 1983.
- Schwartz, S. J.: Shock and Discontinuity Normals, Mach Numbers, and Related Parameters, in: Analysis Methods for MultiSpacecraft Data, edited by: Paschmann, G. and Daly, P., pp. 249270, ISSI/ESA, 1998.
- S¨ oding, A., Neubauer, F. M., Tsurutani, B. T., Ness, N. F., and Lepping, R. P.: Radial and latitudinal dependencies of discontinuities in the solar wind between 0.3 and 19 AU and -80 ◦ and + 10 ◦ , Ann. Geophys., 19, 667-680, doi:10.5194/angeo-19-667-2001, 2001.
- Sonnerup, B. U. ¨ O. and Cahill, Jr., L. J.: Magnetopause Structure and Attitude from Explorer 12 Observations, J. Geophys. Res., 72, 171-183, 1967.
- Sonnerup, B. U. ¨ O. and Scheible, M.: Minimum and Maximum Variance Analysis, in: Analysis Methods for Multi-Spacecraft Data, edited by: Paschmann, G. and Daly, P., pp. 185-220, ISSI/ESA, 1998.
- Sonnerup, B. U. ¨ O., Haaland, S., and Paschmann, G.: Discontinuity Orientation, Motion, and Thickness, pp. 1-15, ISSI SR-008, 2008.
- Soucek, J., Dudok de Wit, T., Dunlop, M., and D´ ecr´ eau, P.: Local wavelet correlation: applicationto timing analysis of multi-satellite CLUSTER data, Ann. Geophys., 22, 4185-4196, doi:10.5194/angeo-22-4185-2004, 2004.
- Tsurutani, B. T. and Smith, E. J.: Interplanetary discontinuities Temporal variations and the radial gradient from 1 to 8.5 AU, J. Geophys. Res., 84, 2773-2787, doi:10.1029/JA084iA06p02773, 1979.
- Vogt, J. and Paschmann, G.: Accuracy of Plasma Moment Derivatives, pp. 419-447, ISSI SR-001, 1998.
- Vogt, J., Paschmann, G., and Chanteur, G.: Reciprocal Vectors, pp. 33-46, ISSI SR-008, 2008.
- Vogt, J., Albert, A., and Marghitu, O.: Analysis of three-spacecraft data using planar reciprocal vectors: methodological framework and spatial gradient estimation, Ann. Geophys., 27, 3249-3273, doi:10.5194/angeo-27-3249-2009, 2009.
- Volpp, J. and Sieg, D.: ESOC Data Products in the CAA, pp. 209222, Springer, doi:10.1007/978-90-481-3499-1 13, 2010.
- Zhou, X.-Z., Pu, Z. Y., Zong, Q.-G., Song, P., Fu, S. Y., Wang, J., and Zhang, H.: On the error estimation of multi-spacecraft timing method, Ann. Geophys., 27, 3949-3955, doi:10.5194/angeo27-3949-2009, 2009.