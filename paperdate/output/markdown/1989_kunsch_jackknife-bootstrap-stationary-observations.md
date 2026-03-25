## THEJACKKNIFEANDTHEBOOTSTRAPFORGENERAL STATIONARYOBSERVATIONS

## BY HANS R. KUNSCH

## ETH Zurich

We extend the jackknife and thebootstrapmethod of estimating standard errors to the case where the observations form a general stationary sequence. We do not attempt a reduction to ii.d. values. The jackknife calculates the sample variance of replicates of the statistic obtained by omitting each block of l consecutive data once.In the case of the arithmetic mean this is shown to be equivalent to a weighted covariance estimate of the spectral density of the observations at zero. Under appropriate conditions consistency is obtained if I = l(n)→ ∞o and l(n)/n → 0. General statistics are approximated by an arithmetic mean. In regular cases this approximation determines the asymptotic behavior.Bootstrapreplicates are constructed by selecting blocks of length l randomly with replacement among the blocks of observations. The procedures are illustrated by using the sunspot numbers and some simulated data.

1. Introduction. The jackknife [Tukey (1958)] and the bootstrap [Efron (1979)] have become well established as nonparametric estimators of the variance of a statistic. However, the assumption of independence of the observations is crucial. It is easily seen that they give incorrect answers if dependence is neglected; compare Remark 2.1 of Singh (1981). Recently the two methods have been extended to ARMA models by reducing to innovations which are ii.d.; see Davis (1977), Freedman (1984) and Efron and Tibshiriani [(1986), Section 6]. Still ARMA processes are not able to model essential features of many observed time series; compare Priestley (1981), Chapter 11. Fitting models which go beyond ARMA is, however, an extremely difficult task and it seems impossible to take the effects of parameter estimation or misspecification of the model into account. Moreover a variance estimator can be unreliable even if the true distribution differs only slightly from the model and the statistic is robust; see Section 2.4.

Because of these reasons we propose here an extension of the standard jackknife and bootstrap which does not require us to fit a parametric or semiparametric model first. It works for arbitrary stationary processes with short-range dependence expressed, for instance, with mixing conditions. For the jackknife we delete each block of l consecutive observations once and calculate the sample variance of the values of the statistic obtained in this way. Moreover we make a smooth transition between observations left out and observations with full weight, similar to tapering in time series analysis. For the bootstrap we

ReceivedNovember1986;revisedSeptember1988.

Key words and phrases. Variance estimation, jackknife, bootstrap, statistics defined by functionals, time series, infuence function.

AMS 1980 subject classifications.Primary 62G05,62G15; secondary 62M10.

<!-- image -->

®

choose n/l blocks of length I with replacement from the n - I+ 1 blocks of observed data.

If the statistic is not a symmetric function of the observations, leaving out observations in the middle or joining randomly selected blocks causes problems. Our definition in Section 2 takes care of this, but we have to restrict ourselves to statistics which are given by a functional of an empirical marginal with fixed dimension. In Section 3 we show that these procedures are consistent in the case of the arithmetic mean and obtain the asymptotic bias and variance. In this case the jackknife reduces to a standard spectral estimation procedure. In Section 4 we study general statistics by von Mises expansions. We show that for smooth functionals the linear approximation completely determines the asymptotic behavior of the jackknife. Section 5 contains examples with real and simulated data.

Carlstein (1986) has prop sed a variance estimator which selects nonoverlapping blocks. For the arithmetic mean, deletion of blocks is the same as selecting blocks. So in this case our jackknife differs only by using overlapping blocks and tapering. However, for general statistics, deletion is better than selection, both in theory (see Remark 4.1) and in the simulations of Sections 5.1 and 5.2.2.

2. Definitions. When we try to formalize the intuitive ideas from the Introduction, some problems occur. For the jackknife we need to define the statistic with a missing block of observations and with the bootstrap we have to take care how we join two randomly selected blocks. These difficulties can be solved for a certain class of statistics which we are going to introduce in Section 2.1 before defining our jackknife and bootstrap in Sections 2.2 and 2.3. This class is sufficiently general to include many statistics of interest.
2. 2.1. Estimators defined by functionals on empirical distributions. For observations X1,..., Xv from a stationary process the empirical m-dimensional marginal is

<!-- formula-not-decoded -->

where 8, denotes the point mass at y E Rm. In this paper we will always consider statistics Tv of the form

<!-- formula-not-decoded -->

with some fixed m and a functional T with values in R? defined on the set of all probability measures on Rm (or a sufficiently rich subset of it). For simplicity of notation we take q = 1. Often it is convenient to introduce blocks of observations Y,= (Xx,.., X+m-1) and set n = N -- m + 1. Since p = n-1-18y, we are then formally in the case m = 1.

In order to illustrate the scope of this class, we give some examples.

- ExAMPLE 2.1. M, L and R estimators of location and scale [see Huber (1981)] are of the form (2.2) with m = 1.

ExAMPLE 2.2. Functions of linear statistics,

<!-- formula-not-decoded -->

where Φ = (Φ1,.., 中k) and f: R → R. This includes the least-squares estimator of the parameters of an AR model and certain versions of the sample correlations.

with a symmetric kernel Φ.

ExAMPLE 2.4. Statistics defined implicitly as solutions of an equation

<!-- formula-not-decoded -->

This includes robust estimators for the AR model [see Kunsch (1984)] and maximum likelihood and conditional least squares in Markov processes.

In the context of ARMA models, Martin and Yohai (1986) considered estimators which are of a slightly more general form than Example 2.4. They are defined as solutions of

<!-- formula-not-decoded -->

where (a, a2,..., at; 0) → (a, a2,...; 0) for all (at) E R∞. All our procedures and results can be extended to this class.

In order to investigate the asymptotic properties of variance estimators, we need an expression for the asymptotic variance of Tv. So we make the following assumptions on the statistics Tv and the underlying stationary process (Xt).

- (A1) Tv converges almost surely to T(Fm) where Fm denotes the marginal distribution of (Xx, ..., Xm).
- (A2) The infuence function IF(y, Fm) = limeto[T(1 - e)Fm + e8,) T(Fm)]/e [see Hampel, Ronchetti, Rousseeuw and Stahel (1986)] exists for all yeRm.
- (A3) n-1/2Z-, IF(Y, Fm) is asymptotically normal with mean zero and

<!-- formula-not-decoded -->

(A4) The remainder term R in the linearization T(p%) = T(Fm) + n- iZz-,IF(Y, Fm) + Rv is of the order o,(n-1/2).

Obviously, (A3) and (A4) imply that nl/2(T - T(Fm) is asymptotically to Fm, so (A1) follows for instance from weak continuity of T. (A3) holds under as' mixing conditions on (Xt) and moment conditions on IF(Y, Fm). For (A4) many techniques from the ii.d. case can be carried over. In the examples above rigorous conditions can be found in Gastwirth and Rubin (1975) for Example 2.1, Denker and Keller (1983) for Example 2.3, Bustos (1982) and Tjostheim (1986) for Example 2.4.

- 2.2. The jackknife. For the jackknife we delete or downweight blocks of m-tuples in the calculation of the marginal p":

<!-- formula-not-decoded -->

and calculate

<!-- formula-not-decoded -->

The weights w(i) are assumed to satisfy 0 ≤ w,(i) ≤ 1, i E Z, and wn(i) &gt; 0 iff 1 ≤ i ≤ l. Here I is the length of the downweighted block and Iwnlli = ∑ w,(i). In many cases w, will be of the form

<!-- formula-not-decoded -->

for a function h: (0, 1) → (0,1) which is symmetric about x =  and increasing on (0, d). Choosing for h the indicator function 1(0,1) corresponds to simple s smooth; see Section 3.1.

The jackknife estimate of the variance of T is simply the sample variance of the TV)'s with a suitable standardization:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

That this is the right standardization will become clear in Sections 3.1 and 4.1. There we will also discuss the choice of l as a function of sample size and strength of dependence of (Xt).

- 2.3. The bootstrap. In analogy to the ii.d. case we select blocks of length l at random instead of deleting blocks. Assuming n = kl with k ∈ N, the bootstrap m-dimensional marginal is therefore

<!-- formula-not-decoded -->

where Ss,..., Sk are i.i.d. uniform on {O,1,..., n - I}. We can also write this as

<!-- formula-not-decoded -->

or as

<!-- formula-not-decoded -->

where the k blocks (Y*...-Y*),(Y*+.., Yt),...,(Y*+....Y*) are i.d. strap statistics

<!-- formula-not-decoded -->

and approximate the unknown distribution of T - T(Fm) by the distribution of T* - Tv, where Y,..., Yn are fixed, but Ss,..., Sk vary. In particular we use

<!-- formula-not-decoded -->

Here E* denotes expectation with respect to Su,..., Ss. Similarly we can esti2 of T* - Tv have to be evaluated by simulation.

For m &gt; 1 our proposal does not give an estimate of FN. When we write out the bootstrap sample (Y*,..., Y*) in terms of the original observations (X), we obtain n + k(m - 1) data points. The reason for this is that we do not want to use observations from different independent blocks in the calculation of p" *. In this way we reduce the effect of joining independent blocks together.

The rationale for our proposal is as follows: The distribution of Tv depends on the unknown distribution FN of X1,..., X. Even asymptotically, the variance of T depends on the distribution of the whole process and not on some finite marginal; see (A3). Obviously it is impossible to estimate FN from X1,..., X without assuming a special structure like independence or a linear denoting the product of measures. For m = 1 our proposal estimates FN by (p')k and thus coincides with Efron's method if I = 1. However we will let l tend to infinity as n → oo, since in this way we asymptotically get all marginals correct.

The bootstrap marginal is by (2.8) an empirical marginal with random weights n-'ft. For t, s not at the border

<!-- formula-not-decoded -->

This leads to the following modification suggested by a referee. Take

<!-- formula-not-decoded -->

function R(t), independent of (Xt).

- 2.4. Other methods. Carlstein (1986) has proposed using nonoverlapping subseries. In our notation this means to calculate a suitable standardization of the sample variance of (T)')j-o..,k-1, where k = [n/l] and

<!-- formula-not-decoded -->

Obviously we could also take overlapping subseries, i.e., the sample variance of 4.1(i).

given in (A3). We assume that the infuence function exists also at p so that we can use IF(y, p) as estimator of IF(y, Fm). We then calculate

<!-- formula-not-decoded -->

where the w,(k) are lag weights with wn(k) → 1 for fixed k and I = l(n) → 0o, I( n)/n → 0. It is well known from spectral analysis [cf. Priestley (1981), Section 6.2.3] that such weights are needed to obtain consistency. In Sections 3 and 4 we will see that the jackknife is asymptotically equivalent to (2.14) for some special weights wn.

Another method is to fit a parametric model Fg to the data and then to use

<!-- formula-not-decoded -->

However, in complicated models like nonlinear time series the calculation of o2(Fa) may be quite dificult. Often it requires extensive simulations so that jackknifing may be a simpler alternative. Moreover there is always the danger o2( F) and o2(F) may differ considerably even if all finite-dimensional marginals are close and IF(Y, Fm) is bounded. This shows that with dependence, parametric methods are even more dangerous than in i.i.d. situations.

3. The arithmetic mean. Here we investigate the properties of our procedures for the arithmetic mean. This corresponds to m = 1, T(F1) = ∫ xFl(dx) = E[X] = μ and IF(x, Fl) = x - μ. This functional is linear and allows explicit calculations of all quantities of interest. At the same time it will be the first step toward a theory for general functionals, since by (A4) they can be approximated by an arithmetic mean. The effects of the remainder R  in (A4) will be discussed in Section 4.

3.1. Relation of the jackknife to spectral estimation. By definitions (2.3) and (2.4), we have for any real number c and 0 ≤ j ≤ n - l,

<!-- formula-not-decoded -->

In order to obtain a transparent formula for T?', we introduce

<!-- formula-not-decoded -->

Note that α,(t) = (n - I + 1)-1 for l ≤ t ≤ n - I + 1 and ∑α(t) = 1. Hence

<!-- formula-not-decoded -->

is an unbiased estimator of μ. It is asymptotically equivalent to the arithmatic mean Tv if l = o(n). By putting c = μn in.(3.1) it follows that

<!-- formula-not-decoded -->

Hence

<!-- formula-not-decoded -->

REMARK 3.1. Formulas (3.1) and (3.5) show that the jackknife for the arithmetic mean does not change if we replace p%() by Ilwll-' w(t - j)8y. and adjust the standardization. This means that in this case our procedure differs from Carlstein's (1986) method only by using overlapping blocks and general weights wn.

introduce some notation. Let v, be the convolution of w, with itself,

<!-- formula-not-decoded -->

Note that v,(0) = Ilw,ll2. Furthermore we put

<!-- formula-not-decoded -->

As for α,(t), we have β(t, k) = (n - I + 1)-1 for I - Ikl ≤t ≤n - I + 1 and

∑2-↓kβ,(t, k) = 1. Hence

<!-- formula-not-decoded -->

a si m [ - 4+x( -x]g = ()  a yo n similar to the usual sample covariance except that it has a smaller bias.

kwe arrive at the following.

THEOREM 3.1. In the case of the arithmetic mean we have

<!-- formula-not-decoded -->

density at zero. If we choose the weights accordingly, it almost coincides with 0ng from (2.14).

LEMMA 3.1. If l = o(n) and ∑lil IR(j)) &lt; o, then:

<!-- formula-not-decoded -->

The proof is given in the Appendix.

Together with (3.9) this gives

<!-- formula-not-decoded -->

If w,(i) is of the form (2.5), then

<!-- formula-not-decoded -->

The asymptotic bias thus depends on the smoothness of the convolution h * h at zero.

THEoREM 3.2. Consider the jackknife of the arithmetic mean with w, of the form (2.5) and l = l(n) → o. Then:

<!-- formula-not-decoded -->

- (ii) If h* h is twice continuously differentiable around zero, if l = o(n'/3) and ∑k²|R(k)1 &lt; 00,

<!-- formula-not-decoded -->

REMARKs 3.2.  (i) Theorem 3.2 demonstrates the advantage of choosing a smooth h.

- (i) Theorem 3.2 justifies the choice of the standardization for o2ack at least for term in (3.10) which is due to estimation of μ drops out. Moreover, for I = 1 our formula would agree with the usual jackknife. However, the effect is small and the results of the next section do not suggest that this factor brings an improvement also for more general statistics.
- (ii) The condition E|kl'jR(k)| &lt; ∞o, j = 1 or 2, excludes models with longrange dependence. As an example, let us consider the case R(k) ~ Ikl-β, 0 &lt;β&lt;1. A lengthy, but not difficult calculation gives E[o?ack] ~ n-1yi-B2(1 - β)-(2 - β)-1 if l = o(n) and (n) → o. On the other hand, Var[Tv] ~ n-B2(1 - β)-′(2 - β)-1. The jackknife thus underestimates the true variance systematically by a factor (l/n)-β which tends to zero. In situations with long-range dependence, the only possibility to obtain confidence intervals an unknown parameter and to estimate it; cf. Hampel, Ronchetti, Rousseeuw and Stahel (1986), Section 8.1. Beran (1986) has given a procedure which takes the variability of the estimated β for Gaussian observations into account. Nothing seems to be known about non-Gaussian cases.
- (iv) Our procedures can be generalized to spatial data ( Xt)te z2 in an obvious way. In that situation, the smaller bias of R,(k) becomes important. The bias of the usual sample covariance is asymptotically not negligible; see Guyon (1982).

The calculation of Var[ oack ] is lengthy. In the literature there are expressions for the asymptotic variance of a lag weight spectral estimate; see Priestley (1981), (6.2.113) or Brillinger (1975), Theorems 5.6.2 and 5.9.1. However, there is a small problem with the conditions used by these authors. In the next section we want to apply our results not to (Xt) itself, but to (IF(Y, Fm). It is not clear whether their conditions carry over from the former to the latter. The following theorem uses the strong mixing coefficients α(k) and thus avoids this difficulty.

THEoREM 3.3.Consider the jackknife for the arithmetic mean and assume that E[1Xt]6+8] &lt; oo and ∑k2α(k)8/(6+8) &lt; oo. If the wn, are of the form (2.5) with l(n) = o(n), then

<!-- formula-not-decoded -->

The proof is given in the Appendix.

CoROLLARY 3.1.Under the conditions of Theorem 3.3 the jackknife for the arithmetic mean is consistent if I = o(n) and l(n) → o.

REMARK 3.3. If we use disjoint blocks as proposed in Carlstein (1986), then Since this reduction is substantial, overlapping blocks should be used when one can afford the computations.

From Theorems 3.2 and 3.3 we can determine the optimal order of l(n) by equating bias squared and variance. It is in the first case I = O(n1/3) and in the G2 O( n -4/5), respectively. In order to determine not only the order of I(n), but also is actually more than what we are trying to estimate. Carlstein (1986) proposes a method to overcome this well known dilemma of spectral analysis. He assumes an exponential decay of (R(k)) and estimates the decay coefficient. Another possibility is to use subjective judgement based on inspection of the sample correlations.

3.2. Validity of the bootstrap approximation.  By definition the blocks (X*+1,..., X*+iy), j = O..., k - 1, are i.d. with distribution p. This implies that the bootstrapped arithmetic mean T* is of the form

<!-- formula-not-decoded -->

where the U, 's are i.i.d. with

<!-- formula-not-decoded -->

In particular

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and

<!-- formula-not-decoded -->

Comparing this with (3.2), (3.3) and (3.5) we see that the bootstrap and the jackknife with simple deletion lead to the same variance estimate.

THEoREM 3.4. If we choose the weights wn(i) = 1, 1 ≤ i ≤ l, for the jackknife, then in the case of the arithmetic mean 62oot = 6?ack.

In particular For &amp;(T* - TX,..., Xv) to be asymptotically a valid approximation of (T - μ), the first two moments should be asymptotically equivalent:

<!-- formula-not-decoded -->

Similarly to Lemma 3.1(i) we can show that Var(E[T*|X1,..., Xv] - Tv) = O(ln-?). These results imply convergence in probability, but not almost sure convergence. We have to consider fourth moments. If we can show that

<!-- formula-not-decoded -->

and

<!-- formula-not-decoded -->

(B1) and (B2) follow for l = O(n1/2-s). The left-hand side of (3.16) contains fourth moments. Using the inequality (A.1) of the Appendix it can be proved under the conditions of Theorem 3.3. (3.17) involves eighth moments. Similarly s cumulants with the mixing coefficients α(j). However in order to complete the

The distribution of T* - Tv is by (3.13) a k-fold convolution. So except for a very small k, direct calculation is not advisable. However (3.13) together with the central limit theorem for triangular arrays suggest that &amp;(T*|X1, ..., X) will be approximately normal like &amp;(T). For Lindeberg's condition we need an assumption on the fuctuations of partial sums:

<!-- formula-not-decoded -->

The most elegant way to prove (B3) is via strong approximations. If there is a Wiener process W(t) such that with probability 1,

<!-- formula-not-decoded -->

(B3) follows for I(n) = O(n*), α &lt; 1, from (3.18) by well known properties of the Wiener process. For (3.18) one needs E|X;/P &lt; oo for some p &gt; 2 and a quick decay of the strong mixing coefficients; cf. Philipp and Stout (1975), Chapter 7. If I(n) increases slowly, (B3) can be obtained without any restriction on the dependence structure.

<!-- formula-not-decoded -->

The proof is given in the Appendix.

- .With the above conditions we can show:

THE0REM 3.5. If (A1), (A3) and (B1)-(B3) hold, then

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

almost surely.

This is an extension of Theorem 1A of Singh (1981) and of Theorem 2.1 of Bickel and Freedman (1981).

REMARK 3.4. For the arithmetic mean we can have approximate equality proposal (2.12) with R = h * h. A rigorous analysis of this method seems, however, difficult.

A natural question is whether the bootstrap distribution contains more than &gt; (ls| + ll[( - "x(n - 'x)( - °x)]gl7  'uoexo1dde eou ay asn! 0, a straightforward calculation shows that

<!-- formula-not-decoded -->

Hence at least on the average the bootstrap distribution has the correct skewness. This might be surprising because by joining independent blocks, we reduce the dependence. But since we are dealing with weak dependence, the main s strap.

## 4. Nonlinear statistics.

- 4.1. The jackknife. Linearization of T at Fm gives

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We want to show that for large n, ack(Tv) behaves similarly as oJack( L). LN particular, under the conditions given there, nojack( L) converges in probability

The simplest way is to use results on the asymptotic order of R%) which is in regular cases s O,(n-1). Hence we expect ZRQ)2 to be O(n-1). A sufficient *(z -u)o = [(a]g x 'usu 1og 'si sn 1og uouos

Because

<!-- formula-not-decoded -->

and the standardizing factor in oack is O(l-1), the following theorem follows from the Cauchy-Schwarz inequality.

THEOREM 4.1. If Z-R()2 = O(n-1) and w, is of the form (2.5), then 3.3, nojack(Tv) converges to o2, in probability.

However this result is not completely satisfactory because the contribution of the remainders R%) s seems to be of higher order than the difference concrete examples, but we develop a different approach which gives better results.

In the above argument the inequality (4.3) is too coarse. The remainders R§) s   n d a In order to exploit this without using higher-order expansions, we linearize T at p instead of Fm. Assuming that IF( y, p) exists, we write

<!-- formula-not-decoded -->

-   (     m s contribution of SV). It is much smaller than R) because p() and pN are much closer than p(i) and Fm. For instance. For instance, the total variation distance is

<!-- formula-not-decoded -->

Hence we expect S%) to be at most of the order O,(l2n-2). With the same arguments as above we can show:

THEOREM 4.2. If ≥S()2 = O,(l*n-3), if 0ack(MN) = O(n-1) and wn, is of the form (2.5), then noack(Tv) = nack(MN) + O,(18/2n-1).

The following lemmas, which are proved in the Appendix, give sufficient conditions for ZS§)2 = O,(l*n -3). We do not strive for maximal generality, but rather for simplicity of the arguments; see also Remark A.2.

LEMMA 4.1. Let T be a function of linear statistics as in Example 2.2. Assume that f is differentiable with 0f/dx; Lipschitz in a neighbourhood of JΦ dFm and that 中,., 中k are bounded. Then max,ISWl ≤ const. I2n-2.

LEMMA 4.2. Let Tv be a von Mises statistic as in Example 2.3. If the kernel Φ is bounded, max ,)S&lt;'I ≤ const. I2n-2.

LEMMA 4.3. Let T be as in Example 2.4. Assume that there are a C E R and a neighbourhood U. of T(Fm) such that:

- (i) Iy(y, 0)I ≤ C on Rm × Uo.
- (ii) lμ(y, 01) - v(y, 02)I ≤ C|0, - 02l for y E Rm, 0,02 ∈ Uo.
- (ii)  = (3/a0)↓ exists and li(y, 0)l ≤ C on Rm × Uo.
- 0 ≠ (&lt;)uHP(u)L)∫ (△!)

Then max ;IS%'l ≤ const. I2n-2.

We consider next the contribution of L&amp;) - MN). Since MV) is like L%) a order to proceed, we need more information on the difference of IF( y, Fm) and IF( y, p%).

LEMMA 4.4. In the situation and under the conditions of Lemma 4.1 or 4.3 the following condition is satisfied:

- (C) There exist bounded functions hi: Rm → R and random variables Un,i = O(n-1/2), i = 1,.., q, such that

<!-- formula-not-decoded -->

The proof is given in the Appendix. For von Mises statistics (C) holds if the kernel Φ is a linear combination of products of functions of one argument.

THEoREM 4.3. If (C) holds and w, is of the form (2.5), then no?ack( MN) = (-u) +(z/-u) + (NT)u

The proof is given in the Appendix.

CoRoLLARY 4.1. Under the conditions of Theorems 4.2 and 4.3,

<!-- formula-not-decoded -->

REMARKs 4.1. (i) According to Theorem 3.3 and Corollary 4.1, the standard deviation of the jackknife for the linear part dominates all effects of the nonlinearity if l → oo and I = o(n1/2). In particular, the asymptotically optimal choice of I depends only on the correlations of IF(Y, Fm).

- (ii) Theorems 4.2 and 4.3 show that for I = o(n1/3) the dominating effect of the nonlinearity is the use of the empirical infuence function IF( y, p%) instead of IF(y, Fm). Compared to this, the difference between 6 G2 ble. This is of interest also in the classical jackknife with i.i.d. observations and I = 1 for all n.
- (iii) An analogue of Theorem 4.1 holds also for Carlstein's (1986) method, but Theorems 4.2 and 4.3 are limited to. our procedure. In order to obtain the exact order of the effect of the nonlinearity on Carlstein's method,we consider first i.i.d. observations where in regular situations E[(T - T( Fm))²] - s  s w 0 ≠  ym (z-u)o + z-u = [((ud) - N)]g ately that E[no2ar(T)] - E[no2ar( Lv)] ~ l-1. The same behavior is expected to hold under suitable conditions of weak dependence (Theorem 4.1 is not sharp here because of Cauchy-Schwarz). But this means that the nonlinearity of T introduces an additional bias which is of the same order as the bias of the linear part. In particular the optimal choice of I depends also on the nonlinear part. Moreover the effects of the nonlinearity on our procedure are by Corollary 4.1 of smaller order if I = o(n2/5).
- 4.2. The bootstrap. Unfortunately the analysis of our bootstrap procedure turns out to be even more dificult than for the standard bootstrap with I = 1. If we want to generalize Theorem 3.5 to smooth nonlinear functionals T with m = 1, we need the distribution of the Kolmogorov-Smirnov distance between p* and p?. For I = 1 it is not too difficult to show that it behaves like the Kolmogorov-Smirnov distance between p? and Fl for i.i.d. observations; see also Bickel and Freedman (1981), Chapter 4. The difficulty with I &gt; 1 is that the weights attributed to distinct order statistics by p?* are dependent in a way which is difficult to control.

The only case which is fairly easy is the one where T is a function of linear statistics as in Example 2.2. With the delta technique, Theorem 3.5 can be generalized to such statistics; cf. Bickel and Freedman (1981), (3.6). Moreover in this situation the bootstrap distribution will usually give a better approximation than the central limit theorem with an estimated variance. The reason for this is that when the bootstrap and the true distribution are in good agreement for the linear statistics n-1Z Φ(Y), then they will be in good agreement for any transformed statistics f(n- 1Z Φ(Y). However if f is strongly nonlinear, the distribution of f(n-1ZΦ(Y)) can be very nonnormal. Theoretical work to confirm this heuristic is now in progress, An empirical confirmation is given by the simulations reported in Table 5.

## 5. Examples.

- 5.1. The trimmed mean.As our first example we estimate the variance of the 40%-trimmed mean in the situation considered by Carlstein (1986). The observa+ (o ~  s  5n (    (x)

TABLE 1 Simulation study of different estimators of thevariance of the 40%-trimmed mean.The data are from an AR(1) process with 30% innovation outliers as in Carlstein (1986). Series length n = 100.

|                                                                   | β = 0.2    | β = 0.2   | β = 0.2   | β = 0.8    | β = 0.8   | β = 0.8   |
|-------------------------------------------------------------------|------------|-----------|-----------|------------|-----------|-----------|
|                                                                   | E[62]*     | Var(o2)*  | MSE(6)*   | E[62]*     | Var(6²2)* | MSE(62)*  |
| 1. Jackknife split cosine window l=7, =3                          | 3.1 (0.07) | 1.10      | 1.1       | 29 (1.0)   | 211       | 3740      |
| 2.Jackknife splitcosinewindow l=10,=4                             | 3.8 (0.11) | 2.45      | 2.7       | 43 (1.7)   | 560       | 2576      |
| 3. Jackknife splitcosinewindow l = 16, , = 6                      |            |           |           | 、53 (2.5) | 1262      | 2519      |
| 4.Subseries with adaptive choice of length; see Carlstein (1986)t | 4.5 (0.10) | 1.95      | 3.4       | 50 (2.6)   | 1383      | 2827      |
| 5. Truet                                                          | 3.3        |           |           | 88         |           |           |

## window

<!-- formula-not-decoded -->

and compared it with Carlstein's (1986) method of subseries. Since the differences between the two methods are expected to be larger for small samples, we restricted ourselves to the sample size n = 100.

Table 1 shows that for β = 0.2 the jackknife is a clear improvement over the subseries method, whereas for β = 0.8 the improvement is within the order of magnitude of the random error of the simulations. This can be explained by the different subseries lengths chosen by Carlstein's method. For n = 100 the optimal subseries lengths are 3 and 13 for β = 0.2 and 0.8, respectively. Now for short subseries the nonlinear terms become important and increase the bias of Carlstein's method. For longer subseries the effect of the nonlinear terms disappears. Even then the jackknife should have a smaller variance because it corresponds to using overlapping subseries, but this is hardly visible in our simulations.

- " 5.2. AR parameters. In the remaining examples we consider the least-squares estimator T for the parameters 0 = (β1,..., βp, v) of an AR( p) model

<!-- formula-not-decoded -->

It is obviously a multivariate function of linear statistics as in Example 2.2. At the same time it belongs also to the class of Example 2.4 with m = p + 1 and multivariate ,

<!-- formula-not-decoded -->

and

<!-- formula-not-decoded -->

This latter interpretation shows that the infuence function for each component of T is a linear combination of 1,..., p+ 1 see Hampel, Ronchetti, Rousseeuw and Stahel (1986), (4.2.9).

The asymptotic variance of the components of T depends on the distribution of the data. If they follow the AR model (5.2), the psi-function satisfies

<!-- formula-not-decoded -->

This holds then also for the infuence function. Thus E,[IF;(Y, 0)IF(Y, 0)] = 0 for all t ≠ s and all j,k; cf. Kunsch (1984), Section 1.4. By the results of Sections 3 and 4, the optimal choice for I is l(n) = 1 provided the model (5.2) holds. If it does not hold, the influence functions are correlated and we have to let I increase with n in order to obtain consistency.

5.2.1. The sunspot numbers. As an example with real data we consider Wolfer's sunspot numbers from 1770-1889. Efron and Tibshirani (1986) used the same data set so that we can compare our procedure with theirs. The results are summarized in Table 2. For p = 1 there are two groups of methods. The first one estimates the standard error close to 0.05 and contains methods 1(a), 2(a), 3(a), 4 and 5. The remaining methods estimate the standard error to be 0.035 or 0.036. The first group contains all methods which are based on the assumption that the AR(1) model holds. However it is well known that the AR(1) model does not fit at all to the sunspot numbers. We thus trust the second group more. It is also known that an AR(2) model gives a better fit. With this model the standard error of the AR(1) coefficient becomes 0.023 which is closer to the value of the second group.

We also computed the bootstrap histograms for β, and β2. In contrast to the ones obtained by Efron and Tibshirani (1986), they looked very much like normal distributions.

Next we look at the case p = 2. The most striking feature is the large ( 4 and 5 on the other hand. Remember that all of these methods should give roughly the same answers if the AR(2) model were correct. The simulations reported in Table 3 show that these differences cannot be reasonably explained by chance variations. A better explanation is that the AR(2) model does not hold even though it fits better than AR(i). This is known also from other analyses of the data; see Priestley (1981), Chapter 11. Because of this we again trust the estimates of 1(b), 2(b) and 3(b) most.

TABLE2 Estimated standard errors for the parameters of an AR(p) model, p = 1,2,ftted to the sunspot numbers for 1770-1889.

|                                                                     | AR(1) Estimated s.e.   | AR(2) Estimated s.e.   | AR(2) Estimated s.e.   |
|---------------------------------------------------------------------|------------------------|------------------------|------------------------|
| Method                                                              | of β                   | of β1                  | of β2                  |
| 1. Jackknife (a) l = 1                                              | 0.048                  | 0.113                  | 0.099                  |
| (b) l =5                                                            | 0.036                  | 0.075                  | 0.086                  |
| Wn = (0.25, 0.75, 1.0, 0.75, 0.25) 2. Influence function (a) l = 1  | 0.047                  | 0.100                  | 0.090                  |
| (b) l = 5                                                           | 0.035                  | 0.067                  | 0.078                  |
| Wn = (1.0, 0.83, 0.47, 0.17, 0.03) 3. Bootstrap, nB = 200 (a) l = 1 | 0.050                  | 0.105                  | 0.095                  |
| (b) l = 4 4.Bootstrap ofempirical innovations;seeEfronand           | 0.035 0.055            | 0.076 0.070            | 0.086 0.068            |
| Tibshirani (1986) 5.Asymptotic s.e.under the AR(p) model            | 0.053                  | 0.067                  | 0.067                  |

- simulation experiments are shown in Table 4. Note that for p = 1, T,1 is just a version of the lag one correlation. First we see that Carlstein's (1986) method is by far the worst in all situations. Because the statistic considered here is highly nonlinear, this method needs much longer subseries in order to achieve a bias

TABLE 3 Simulation study of different estimates of the standard error for β,β2. The data are from an AR(2) process with β, = 1.372, β2 = -0.677. Number of simulations = 200.

|                                                  | Estimated s.e. for β1   | Estimated s.e. for β1   | Estimated s.e. for β2   | Estimated s.e. for β2   |
|--------------------------------------------------|-------------------------|-------------------------|-------------------------|-------------------------|
|                                                  | Mean                    | S.D.                    | Mean                    | S.D.                    |
| 1. Jackknife l =1                                | 0.068                   | 0.0081                  | 0.067                   | 0.0078                  |
| 2.Jackknifel=5 Wn = (0.25, 0.75,1.0, 0.75, 0.25) | 0.068                   | 0.0118                  | 0.066                   | 0.0107                  |
| 3. Asymptotic s.e. under the AR(2) model         | 0.067                   | 0.0055                  | 0.067                   | 0.0055                  |
| 4.Difference between methods 1 and 2             | -0.00010                | 0.0086                  | 0.00092                 | 0.0080                  |
| 5.Difference between methods 1 and 3             | 0.00095                 | 0.0061                  | 0.00028                 | 0.0059                  |
| 6. Difference between methods 2 and 3            | 0.00105                 | 0.0107                  | -0.00064                | 0.0093                  |

TABLE 4

Simulation study of different estimators for the standard error of the lag one correlation in different

situations.

| Method                                     | AR(1) E[6]*    | β = 0.8 n =48 S.D.(6)*   | MA(1) E[6]*    | α=0.8 n=48 S.D.(6)*   | MA(1) E[6]*     | α=0.8 n =192 S.D.(6)*   |
|--------------------------------------------|----------------|--------------------------|----------------|-----------------------|-----------------|-------------------------|
| 1. Jackknife                               |                |                          |                |                       |                 |                         |
| (a) l = 1                                  | 660'0 (0.0015) | 0.021                    | 0.131 (0.0015) | 0.021                 | 0.0637 (0.0003) | 0.0049                  |
| (b) l = 4, weights wn = (0.5,1.0,1.0,0.5)  | 0.097 (0.0020) | 0.028                    | 0.108 (0.0020) | 0.028                 | 0.0539 (0.0005) | 0.0064                  |
| 2.Infuence function                        |                |                          |                |                       |                 |                         |
| (a) l = 1                                  | 0.103 (0.0019) | 0.027                    | 0.125 (0.0014) | 0.020                 | 0.0629 (0.0003) | 0.0047                  |
| (b) l = 4, weights wn = (1.0,0.8,0.4,0.1)  | 0.096 (0.0021) | 0.030                    | 660'0 (0.0015) | 0.021                 | 0.0524 (0.0004) | 0.0059                  |
| 3.Bootstrap,200replicates (a) l = 1        | 0.097 (0.0014) | 0.020                    | 0.129 (0.0012) | 0.017                 | 0.0634 (0.0005) | 0.0064                  |
| (b) l = 3                                  | 6600 (0.0018)  | 0.026                    | 0.106 (0.0012) | 0.017                 | 0.0549 (0.0004) | 0.0060                  |
| 4. Disjoint subseries (see Carlstein,1986) |                |                          |                |                       |                 |                         |
| (a) l = 4                                  | 0.172 (0.0038) | 0.054                    | 0.162 (0.0046) | 0.065                 | 0.0889 (0.0016) | 0.0230                  |
| (b) l = 8                                  | 0.117 (0.0030) | 0.043                    | 0.107 (0.0029) | 0.041                 | 0.0568 (0.0006) | 0.0091                  |
| (c) l = 12                                 | 0.102 (0.0034) | 0.048                    | 0.089 (0.0026) | 0.037                 | 0.0527 (0.0006) | 0.0094                  |
| 5. Asymptotic s.e. under an AR(1) model    | 0.097 (0.0011) | 0.015                    | 0.127 (0.0006) | 0.009                 | 0.0631 (0.0001) | 0.0021                  |
| 6.Estimated from 1000 simulations          | 0.107          |                          | 0.112          |                       | 0.0540，        |                         |

comparable to the other methods. This leads then to a much larger standard deviation.

The performance of the other methods depends on the number and the distribution of the observations. In the AR(1) case the bias of all methods is similar. The parametric method 5 has the smallest variance, as was to be expected. In accordance with the theory the variance increases as I increases.

In the MA(1) case the methods differ also in their bias. The methods 1(a), 2(a), 3(a) and 5 are always biased upward. Increasing I reduces the size of the bias and changes its sign for n = 48. Except in the case of the bootstrap, the variance increases with 1. From the point of view of mean square error, the estimates with a larger bias but smaller variance are better for the small sample size n = 48. There the parametric estimate is by far best although the model is wrong. With the larger sample size n = 192 the bias becomes dominant and the

TABLE5

Nonnormality of thebootstrap distribution:Simulation study of truncated skewness=E[z3] and ( )-() )x = Z a  - =x ss . Tv is the least-squares estimator of the AR(1) parameter. Data are sample of size 60 of a Gaussian AR(1) process with β = 0.8. Number of bootstrap replicates 1000.

| *(NL)   | K(TN)*   |   1 | E[Y(T)]       |   S.D.(Y(T) | E[K(T*)]t                      |   S.D.(k(T* )t |
|---------|----------|-----|---------------|-------------|--------------------------------|----------------|
| - 0.78  | 0.62     |   2 | -0.17 (0.013) |        0.18 | 0.18 (0.016) 0.39 (0.025) 0.50 |           0.22 |
|         |          |   4 | -0.39 (0.016) |        0.22 |                                |           0.36 |
|         |          |   6 | -0.51 (0.019) |        0.27 | (0.035)                        |           0.49 |

nonparametric methods 1(b), 2(b) and 3(b) with I &gt; 1 are best. The number of simulations is too small to see differences between the jackknife, the bootstrap and the influence function.

Since the statistic considered is strongly nonlinear, its distribution is not close to the normal. We wanted to see how much the bootstrap distribution picks up of this nonnormality. For the bootstrap distribution one needs more replicates than for the bootstrap variance; see Efron and Tibshirani (1986). We thus restricted ourselves to one situation and took v to be known. The results of Table 5 show that the bootstrap indeed refects the nonnormality of the distribution to some extent. How much depends on the block size l. In particular, small I's are not good although I = 1 is optimal for the jackknife.

## APPENDIX

## Proofs of results from Sections 3 and 4.

PROOF OF LEMMA 3.1. For (i) we write

<!-- formula-not-decoded -->

say. By a standard argument Var(Z2) = n-1Z R(j) + o(ln-2). Furthermore by definition (3.2), α(t) ≤ (n - I + 1)-1. Hence

<!-- formula-not-decoded -->

and

<!-- formula-not-decoded -->

Finally

<!-- formula-not-decoded -->

For (i) we have by definition

<!-- formula-not-decoded -->

Now βn(t, k) = α(t) for l &lt;t ≤ n - l + 1 and Iβn(t,k) - αn(t)I ≤ 2(n - I + 1)-1. So the assertion follows by similar arguments as above.

PROOF OF THEOREM 3.3. Let S(i) = ∑w,(t - j)(X, - μ). In a first step one shows that

<!-- formula-not-decoded -->

and

<!-- formula-not-decoded -->

This is done by straightforward calculations using ∑ j²|R( j)l &lt; oo and the form (2.5) of w,. In a next step one shows that

<!-- formula-not-decoded -->

This is done by using the following inequality for s ≤ t &lt; u &lt; v (assuming μ = 0):

<!-- formula-not-decoded -->

which follows by a repeated application of Theorem 17.2.3 of Ibragimov and Linnik (1971). In a last step one has to show that on the right-hand side of (3.5) we may replace μ, by μ, i.e.,

<!-- formula-not-decoded -->

For this we use again (A.1). We leave the details to the reader.

REMARK A.1. An alternative proof is obtained by observing that the proof of Theorems 5.6.2 and 5.9.1 by Brillinger (1975) uses only summability of fourthorder cumulants. This follows from (A.1) and Zk2α(k)/(6+8) &lt; oo. In general,

summability of nth order cumulants follows from ∑kn-2α(k)8/(2n-2+8) &lt; oo and appropriate moments.

PRoOF OF LEMMA 3.2. By the Borel-Cantelli lemma |Xt - μl = O(t1/P)

PRooF OF THEoREM 3.5. We have to show that the conditional distribution of n1/2o-(T* - Tv) given X1,..., Xv is asymptotically standard normal. By (B2) we may replace T by E[TIX,..., X]. By (3.13), T is a sum of k ii.. variables Un, and by (B1) the conditional variance of n'/2T* converges to 1. Hence we only have to check the Lindeberg condition which is E[Z2, l/Zn,.I&gt;e]] = o(k-1), where Zn,i = n-1/21(Un,i - E[U,i]). But

<!-- formula-not-decoded -->

which is zero for n large enough by (B2) and (B3).

PRooF oF LEMMA 4.1. A Taylor expansion to the first order shows that

<!-- formula-not-decoded -->

where IITn, - JΦ dpll ≤IIJΦ d(p() - p%)ll. By the Hahn decomposition

<!-- formula-not-decoded -->

Hence the lemma follows from (4.5) and the assumed Lipschitz continuity of af/ax,

PROOF OF LEMMA 4.2. We have

<!-- formula-not-decoded -->

p.口

PRooF OF LEMMA 4.3. By (A1), the ergodic theorem and the assumptions of the lemma ∫(y, Tv) dpN(y) ≠ 0 for N large enough. Hence by a standard 0 = ()( ( )  )    ] a has a solution TV) such that max ,TV) - Tvl → 0. A Taylor expansion to the

first order gives

<!-- formula-not-decoded -->

where IT, N - Tl ≤ |TV) - Tvl. By the assumptions of the lemma

<!-- formula-not-decoded -->

uniformly in j. But then we can solve (A.2) for TQ) - Tv to obtain

<!-- formula-not-decoded -->

By the usual formula for the influence function of an M-estimator [see Hampel, Ronchetti, Rousseeuw and Stahel (1986), (2.3.5)],

<!-- formula-not-decoded -->

The lemma follows now by combining (A.3) and (A.4).

REMARK A.2. The essential point in the proof of Lemmas 4.1 and 4.3 is the straightforward estimate max,/ / g d( p() - p%)I ≤ suplg( y)|ln-1. However this is in general not optimal and boundedness of g is not really necessary. If wn corresponds to simple deletion, then

<!-- formula-not-decoded -->

Finding a bound for the maximum of the second term is an analogous problem to checking (B3) and the discussion following (B3) applies also here. But note that for good results we need small rates in the strong approximation (3.18). For (Xt)

ii.d. this is available [see Csorg? and Révész (1981)] but not for the dependent case [see Philipp and Stout (1975)]. General weights complicate the situation further.

PRooF oF LEMMA 4.4. We only give the proof for M-estimators, the other case being straightforward. By (2.3.5) of Hampel, Ronchetti, Rousseeuw and Stahel (1986) IF(y, Fm) = M- ↓(y, T(Fm)) and IF( y, p%) = M4( y, T) where M = - J(y, T(Fm)) dFm and MN = - J(y, Tv) dpn. Arguing as in (A.3)

shows that MN - M = O,(n-1/2) and thus

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

PROOF OF THEOREM 4.3. By assumption (C),

IF(Y, p%)IF(Y, P%) - IF(Y, F")IF(Y, Fm)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Inserting this in (3.9) for the linear jackknife, we obtain n(6jack(Mv) -

(-u)o + (z/1-u)0 = (-u)o + oxaz 2e (u "x)I)

Acknowledgments. I wish to thank two referees for their careful reading and helpful comments on earlier versions of this paper which led to a great improvement in the presentation of our results. I also thank Ed Carlstein for discussions.

## REFERENCES

- BERAN, J. (1986). Estimation, testing and prediction for self-similar and related processes. Ph.D.
- thesis,ETH Zurich.
- B1CKEL,P.J.and FREEDMAN, D.A.(1981). Some asymptotic theory for the bootstrap. Ann.Statist. 9 1196-1217.
- BRILLINGER, D. R. (1975). Time Series, Data Analysis and Theory. Holt, Rinehart and Winston,
- New York.
- BusTos, O.(1982). General M-estimates for contaminated p-th order autoregressive processes: Consistency and asymptotic normality.Z.Wahrsch.verw.Gebiete 59 491-504.
- CARLsTEIN, E.(1986).The use of subseries values for estimating the variance of a general statistic from a stationary sequence. Ann. Statist. 14 1171-1179.
- CsORG?, M. and REvEsz, P. (1981). Strong Approximations in Probability and Statistics. Academic, New York.
- DAvis, W.W. (1977). Robust interval estimation of the innovation variance of an ARMA model.
- Ann.Statist.5700-708.
- DENKER, M. and KELLER, G. (1983). On U-statistics and von Mises' statistics for weakly dependent processes. Z. Wahrsch. verw. Gebiete 64 505-522.

- EFRoN, B. (1979). Bootstrap methods: Another look at the jackknife. Ann.Statist.7 1-26.
- FREEDMAN, D. A. (1984). On bootstrapping two-stage least-squares estimates in stationary linear models.Ann.Statist.12 827-842.
- EFRoN,B.and T1BsHIRAN1, R.J.(1986). Bootstrap methods for standard errors, confidence intervals and other measures of statistical accuracy (with discussion). Statist. Sci.1 54-77.
- GAsTwIRTH, J. L.and RuBIN,H. (1975). The behavior of robust estimators on dependent data. Ann. Statist.3 1070-1100.
- GuYoN, X. (1982). Parameter estimation for a stationary process on a d-dimensional lattice. Biometrika 69 95-105.
- HAMPEL, F. R., RoNCHETTI, E. M., RoUsSEEUw, P. J. and STAHEL, W. A. (1986). Robust Statistics: TheApproachBased onInfluenceFunctions.Wiley,NewYork.
- IBRAGIMov,I.A.and LINNIK,Yu.V.(1971).Independent and Stationary Sequences of Random Variables.Wolters-Noordhoff, Groningen.
- HUBER,P. J.(1981).Robust Statistics.Wiley,New York.
- KUNscH, H. R. (1984). Infinitesimal robustness for autoregressiye processes. Ann. Statist. 12 843-863.
- MARTIN, R. D. and YoHA1, V. J. (1986). Infuence functionals for time series. Ann. Statist. 14 781-818.
- PHILiPp,W. and SroUT, W. (1975). Almost sure invariance principles for partial sums of weakly dependentrandomvariables.Mem.Amer.Math.Soc.161.
- SERFLING,R.J.(1980).Approximation Theorems of Mathematical Statistics.Wiley,NewYork.
- PRIEsTLEY, M. B. (1981). Spectral Analysis and Time Series 1, 2. Academic, New York.

SINGH, K. (1981). On the asymptotic accuracy of Efron's bootstrap. Ann. Statist. 9 1187-1195.

- TUKEy, J. (1958). Bias and confidence in not quite large samples (abstract). Ann. Math. Statist. 29 614.
- TJosTHEIM, D. (1986). Estimation in nonlinear time series models. Stochastic Process. Appl. 21 251-273.

SEMINARFURSTATISTIK ETHZENTRUM CH-8092ZURICH SWITZERLAND