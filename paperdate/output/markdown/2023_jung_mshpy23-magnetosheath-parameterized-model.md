<!-- image -->

## Mshpy23: a user-friendly, parameterized model of magnetosheath conditions

Jaewoong Jung 1,2* , Hyunju Connor 1 , Andrew Dimmock 3 , Steve Sembay 4 , Andrew Read 4 , and Jan Soucek 5

1 NASA Goddard Space Flight Center, Greenbelt, MD, USA;

2 Department of Astronomy, University of Maryland, College Park, MD, USA;

3 Swedish Institude of Space Physics, Uppsala, Sweden;

4 University of Leicester, Leicester, UK;

5 Institute of Atmospheric Physics, Academy of Sciences of the Czech Republic

## Key Points:

- Our user-friendly magnetosheath model parameterizes plasma and magnetic field conditions based on the MHD, gas-dynamic, and analytic models.
- Our model results show good agreement with the magnetosheath observations of THEMIS and Cluster.
- Our model also provides a tool for calculating a soft X-ray image from various vantage points, supporting the upcoming LEXI and SMILE missions.

Citation: Jung, J., Connor, H., Dimmock, A., Sembay, S., Read, A., and Soucek, J. (2024). Mshpy23: a user-friendly, parameterized model of magnetosheath conditions. Earth Planet. Phys. , 8 (1), 89-104. http://doi.org/10.26464/epp2023065

3 # [ Abstract: Lunar Environment heliospheric X-ray Imager (LEXI) and Solar wind-Magnetosphere-Ionosphere Link Explorer (SMILE) will observe magnetosheath and its boundary motion in soft X-rays for understanding magnetopause reconnection modes under various solar wind conditions after their respective launches in 2024 and 2025. Magnetosheath conditions, namely, plasma density, velocity, and temperature, are key parameters for predicting and analyzing soft X-ray images from the LEXI and SMILE missions. We developed a userfriendly model of magnetosheath that parameterizes number density, velocity, temperature, and magnetic field by utilizing the global Magnetohydrodynamics (MHD) model as well as the pre-existing gas-dynamic and analytic models. Using this parameterized magnetosheath model, scientists can easily reconstruct expected soft X-ray images and utilize them for analysis of observed images of LEXI and SMILE without simulating the complicated global magnetosphere models. First, we created an MHD-based magnetosheath model by running a total of 14 OpenGGCM global MHD simulations under 7 solar wind densities (1, 5, 10, 15, 20, 25, and 30 cm ) and 2 interplanetary magnetic field components (± 4 nT), and then parameterizing the results in new magnetosheath conditions. We compared the magnetosheath model result with THEMIS statistical data and it showed good agreement with a weighted Pearson correlation coefficient greater than 0.77, especially for plasma density and plasma velocity. Second, we compiled a suite of magnetosheath models incorporating previous magnetosheath models (gas-dynamic, analytic), and did two case studies to test the performance. The MHD-based model was comparable to or better than the previous models while providing self-consistency among the magnetosheath parameters. Third, we constructed a tool to calculate a soft X-ray image from any given vantage point, which can support the planning and data analysis of the aforementioned LEXI and SMILE missions. A release of the code has been uploaded to a Github repository.

Keywords:

magnetosheath; python; modeling

## 1. Introduction

Magnetic  reconnection  is  a  key  process  that  transfers  mass, momentum, and energy from solar wind to the Earth's magnetosphere. Recent series of satellites, namely Cluster, Time History of Events  and  Macroscale  Interactions  during  Substorms  (THEMIS), and  Magnetospheric  Multiscale  (MMS),  have  enabled  a  space science community  to study smaller and smaller scales of magnetic reconnection, greatly improving our understanding of fundamental  physics.  However,  these  in-situ  measurements  are somewhat  limited  for  studying  global-scale  reconnection  that governs  the  holistic  behavior  of  the  Earth's  magnetospheric systems under the dynamic solar wind and interplanetary magnetic field (IMF) conditions.

Recently,  Lunar  Environment  heliospheric  X-ray  Imager  (LEXI; http:sites.bu.edu/lexi) and Solar wind-Magnetosphere-Ionosphere Link Explorer (SMILE; Branduardi-Raymont et al., 2018) are

scheduled to launch in 2024 and 2025, respectively, for addressing global nature of the solar wind-magnetosphere interaction. Both LEXI and SMILE will have a wide field-of-view soft X-ray imager on board, observing the soft X-rays emitted in the magnetosheath by the charge exchange between highly charged solar wind ions and exospheric  hydrogen  atoms.  The  soft  X-ray  images  can  capture the magnetosheath and its boundary motion under dynamic solar wind/IMF conditions, helping to understand the large-scale reconnection pattern on the magnetopause. LEXI will provide wide fieldof-view  images  of  the  Earth's  dayside  system  from  the  lunar surface during its operation period of less than 2 weeks. SMILE will also observe the dayside system in soft X-ray but from a highlyelliptical  polar  orbit,  providing  over  40  hours  of  continuous images per orbit during its 3-year mission period.

Magnetosheath plasma  number  density,  velocity,  and   temperatures are required parameters for calculating a soft X-ray image of the Earth's dayside system. Previous studies (Connor et al., 2021, Sun TR et al., 2019) utilized global magnetohydrodynamics (MHD) models to create expected soft X-ray images from various vantage points.  Although  MHD  models  (Raeder  et  al.,  2001;  Tóth  et  al., 2005;  Lu  JY  et  al.,  2019a;  Qu  BH  et  al.,  2021)  provides  realistic magnetosheath parameters during various solar wind/IMF conditions, the simulation takes considerable time, and the analysis of the modeling results requires sophisticated techniques and knowledge of a particular model in use, which may be a difficult task for non-experts of modeling.

This paper developed a user-friendly magnetosheath model that parameterizes  plasma  and  magnetic  field  conditions  based  on MHD, gas-dynamic, and analytic models. First, we developed an MHD-based magnetosheath model and compared its results with THEMIS  data  of  2007-2014. Second,  by  adding  several   magnetosheath models in the previous literature, we compiled a suite of magnetosheath  models,  Mshpy23.  We  compared  the  result  of each model in the Mshpy23 suite with the in-situ data of Cluster and THEMIS. Finally, we showed an example of X-ray image simulation using our MHD-based magnetosheath model. Our Mshpy23 code  is  written  in  Python3  and  publicly  available  at  https:// github.com/jjung11/Mshpy.

## 2. MHD-Based Magnetosheath Model

## 2.1 Coordinates and Boundaries

One  of  the  most  commonly  used  coordinate  systems  in  space physics is Geocentric Solar Ecliptic (GSE) coordinates system. It has its X -axis pointing from the Earth's center toward the Sun and Z -axis pointing in the direction of the north ecliptic pole. The Y -axis lies  on  the  ecliptic  plane,  pointing  an  opposite  direction  to  the Earth's orbit around the Sun. However, the GSE coordinate system is not ideal for the magnetosheath parameter model because the bow shock  (BS)  and  magnetopause  (MP)  continuously  move  in response to solar wind/IMF conditions. Instead, we adopted a new coordinate system for our magnetosheath  model.  First,  we converted GSE to aberrated GSE coordinates, to account for the Earth's orbital motion. In that way, the incoming, upstream solar wind is parallel to the X -axis. Next, we adopted two angles and a fractional distance to represent a point in the magnetosheath, as

׋ θ seen in Figure 1. Two angles are longitude ( ) and latitude ( ) in aberrated GSE coordinates and the fractional distance ( f ) is

<!-- formula-not-decoded -->

R r mp r bs where is  the aberrated GSE position vector and and are the  geocentric  distance  to  the  MP/BS  in  the  given  latitude  and longitude direction,  respectively.  In  our  magnetosheath   coordinates, f = 0 indicates the MP location and f = 1 the BS location.

Bz This new  magnetosheath  coordinate  system  requires   magnetosheath boundary locations. Numerous empirical models of the MP  have  been  developed  in  the  literature,  primarily  based  on satellite crossing observatoins. Key references in this field include works by Fairfield  (1971),  Sibeck  et  al.  (1991),  Roelof  and  Sibeck (1993), Petrinec and Russell (1993, 1996), Kuznetsov and Suvorova (1998), Shue et al. (1997, 1998), Boardsen et al. (2000), Chao JK et al. (2002), Lin RL et al. (2010), Lu JY et al. (2011), and Liu ZQ et al. (2015). These  models  often  utilize  ellipsoidal  or  quadratic   equations or adopt the Shue model function to describe the MP. They parameterize  MP  crossings  at  low  latitudes,  taking  into  account factors like solar wind dynamic pressure and the IMF component. Notably, Shue 1998 model has gained widespread recognition  for  its  versatility  in  predicting  both  open  and  closed  MP configurations along with its ability to provide reasonable predictions for the distant tail region. Recent developments have led to models  accounting  for  MP  shape  asymmetry,  including  those proposed by Lin RL et al.  (2010);  Lu  JY  et  al.  (2011);  and  Liu  ZQ et al. (2015).

Regarding  Earth's  BS,  a  multitude  models  has  been  proposed since  its  prediction  and  discovery,  starting  with  Seiff  (1962)  and Spreiter et al. (1966). These models aim to replicate the BS's standoff distance, shape, and responses to solar wind parameter variations. many of these models are based on the fitting of observed BS crossing while incorporating gas-dynamic or MHD principles, as demonstrated by N ě me č ek and Šafránková (1991) and Peredo et  al.  (1995).  In  contrast,  some  models  rely  on  MHD  simulations results,  as  exemplified  by  Cairns  and  Lyon  (1995).  Je ř áb  et  al. (2005) improved the 3-D empirical BS model initially proposed by N ě me č ek and Šafránková (1991) through modifications to the BS surface function. Merka et al. (2005) introduced corrections to the Peredo et al.  (1995)  model,  focusing  on  the  effects  of  upstream Mach  number  on  the  BS.  Following  the  case  of  MP  modeling, there have been efforts to model BS asymmetry recently (Wang M et al., 2018; Lu JY et al., 2019b).

Currently we have implemented a magnetopause model of Shue et al. (1998) and a bow shock model of Jelínek et al. (2012), due to their simple model formulation and wide usage. Shue et al. (1998) developed  a  widely-used,  empirical  MP  model  with  boundary crossing data of ISSEE1/2, AMPTE/IRM, IMP8, and, Interball 1 satellites. Based on the model, the radial distance of the MP is given by:

<!-- formula-not-decoded -->

θz r 0 α 1 where is  the  solar  zenith  angle,  and  the  standoff  distance and the level of tail flaring are given by:

׋ θ f f f Figure 1 . Diagram of the magnetosheath model coordinates. (a) longitude in the XY plane and (b) latitude in the XZ plane with a fractional distance   between MP (  = 0; blue curve) and BS (  = 1; orange curve). The aberrated GSE coordinates are used in these plots.

<!-- image -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

r 0 α 1 Bz Pd The  parameters and depend  on  IMF and  solar  wind dynamic pressure .

Jelínek et al. (2012) developed an empirical BS model by using the THEMIS  data  and  a  method  of  determination  of  the  most propable boundary locations. The following equation explains the BS shape as a function of aberrated GSE coordinates.

<!-- formula-not-decoded -->

R 0 R E λ ׫ Pd X GSE R E R E where =  15.02 , =  1.17, =  6.55,  and is  the  solar  wind dynamic  pressure.  We  also  included  a  BS  model  of  Je ř áb  et  al. (2005)  in  Mshpy23.  Je ř áb  et  al.  (2005)  utilized  only  BS  crossing data below &lt; 8 (flank region) and thus their model tends to  locate  the  BS  more  earthward  than  the  Jelínek's  BS  model, creating a very narrow magnetosheath (&lt; 1 ) under most solar wind/IMF conditions when combined with the MP model of Shue et  al.  (1998).  To  avoid  this  issue,  we  adopted  the  BS  model  of Jelínek  et  al.  (2012)  as  a  default  BS  model  of  Mshpy23,  while providing an option for users to manually select their preferred BS model.

θ ׋ Our MHD-based model, also named Mshpy23-MHD, operates like the following. First, a user inputs a location of interest in a typical GSE coordinate system along with solar wind and IMF conditions at the bow shock nose. Then, our model calculates magnetosheath boundaries under the given solar wind conditions and obtains f , , and of the input location by using the boundary information. Finally,  the  model  calculates  magnetosheath  parameters  at  the given  point  by  linearly  interpolating  the  MHD-based  magnetosheath  values  at  the  nearby  seed  points.  The  next  section describes how we extracted the MHD-based values at each seed grid.

## 2.2 Parameterization of MHD Model

Open  Geospace  Global  Circulation  Model  (OpenGGCM)  global magnetosphere-ionosphere  MHD  model  was  used  to  extract MHD-based magnetosheath values as a function of solar wind/IMF conditions. OpenGGCM solves a semi-conservative form of the MHD equations in a stretched 3D Cartesian grids. The semiconservative form means that OpenGGCM numerically conserves mass, momentum, and plasma energy, but not the total energy, to avoid instability arising when forcing a fully conservative form (Raeder et al., 2008). OpenGGCM inputs solar wind and IMF conditions and outputs are plasma density, velocity, temperature, and electromagnetic fields in the simulation domain. This study used a

R E standalone OpenGGCM model, ranging (-500, 25), (-48, 48), and (-48, 48) for x , y , and z directions in the GSE coordinates. Model details and applications can be found in Raeder et al. (2001, 2008), Connor et al. (2012, 2014, 2015, 2016, 2021), Oliveira and Raeder (2015), Ferdousi and Raeder (2016), Ferdousi et al. (2021), Cramer et  al.  (2017),  Jensen  et  al.  (2017),  Shi  Y  et  al.  (2017),  and  Kavosi et al. (2018).

3 Bz Bx By Vx Vy Vz 5 Magnetosheath  parameters  change  in  response  to  solar  wind (SW) and IMF conditions. For this project, we tested a total of 14 SW/IMF conditions: seven solar wind plasma number densities at 1, 5, 10, 15, 20, 25, and 30 cm and two IMF at  -4  and 4 nT. Other SW/IMF parameters stay constant, IMF = = 2 nT, solar wind velocity =  400 km/s, = =  0  km/s,  and temperature T = 10 K. The dipole tilt angle was set at zero.

X GSE R E θ ׋ For each SW/IMF condition, we determined the MP and BS locations within the MHD simulation, using maximum and minimum gradients of plasma density along a radial direction. We focused only on the dayside magnetosheath ( &gt; 0) because soft X-ray emissions  are  stronger  in  the  dayside  magnetosheath  (Connor et al., 2021). Also, for simplicity, we don't consider the polar cusp impact on an MP shape, i.e., no dips near the cusps. When finding the  MP  location  with  density  gradients,  we  forced  the  radial distance between nearby MP points to be less than 0.8 for  a smooth  MP  shape  near  polar  cusps.  After  the  magnetosheath boundaries  are  determined,  we  set  up  the  seed  grids  for  our magnetosheath model, with a spatial resolution of 0.1 in the fractional distance f and 1° in and .  Finally, we read the modeled magnetosheath  parameters  at  every  grid  and  save  them  as  the database for our MHD-based model in Mshpy23. These grid values are linear interpolated to obtain magnetosheath parameters at a location given by a user.

## 2.3 Comparison with THEMIS Statistics

The  THEMIS  mission  was  launched  in  2007  into  highly  elliptical and nearly equatorial orbits for studying magnetospheric substorms. A total of five THEMIS satellites cover vast areas of the Earth's magnetosphere,  providing  crucial information of the Sun-Earth  interactions.  This  study  utilized  7  years  of  THEMIS magnetosheath observations (2007-2014) published in Dimmock et  al.  (2017).  They  conducted  a  statistical  study  of  the  dayside magnetosheath conditions, using 3-min averages of THEMIS Fluxgate Magnetometer (FGM) and Electrostatic  Analyzer  (ESA)  data that  are  matched  with  the  20-min  averages  of  OMNI  solar wind/IMF conditions before each THEMIS data point. By averaging the  THEMIS  and  OMNI  data,  their  dataset  not  only  suppresses small-scale transient effects in the magnetosheath and solar wind but also includes solar wind propagation effect from the BS nose to  the  THEMIS  locations  in  the  magnetosheath.  Dimmock  et  al. (2017)  calculated  the  BS  and  MP  position  using  models  of  Shue et al. (1998) and Verigin et al. (2001) with the 20-min average of OMNI data, and then obtained the Magnetosheath Interplanetary Medium (MIPM)  coordinates  of  the  corresponding  THEMIS  data point  using  the  boundary  information.  MIPM  is  an  extension  of the  Geocentric  Interplanetary  Medium  (GIPM)  reference  frame (Verigin et al., 2006). In GIPM, axes are defined as follows:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

t B ˆ X gipm where . Then MIPM coordinates are defined as:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Note  that  THEMIS  data  points  were  collapsed  to  the  equatorial plane  by  simple  projection  because  THEMIS  satellites  have  a nearly  equatorial  orbit.  We  used  these  THEMIS  datasets  in  the MIPM coordinates and their corresponding OMNI data for the validation of our MHD-based magnetosheath model. The main difference between the coordinate system used in this paper and MIPM coordinates  is  that  the  latter  organizes  magnetosheath  points based on the shock geometry, either Parker spiral or ortho-Parker spiral. This difference may affect the comparison of plasma properties between the two coordinate systems. We acknowledge this issue and plan to incorporate MIPM coordinates into our model in the  next  version  to  provide  a  more  accurate  description  of  the plasma  properties  in  the  interplanetary  medium,  particularly  in cases where the shock geometry may have a significant impact on plasma properties.

Bx By ∣ V ∣ Bz Bz N sw 3 N sw 3 ׋ N sw 3 3 From the THEMIS and OMNI data set of Dimmock et al. (2017), we estimated  average  magnetosheath  conditions  for  the  12  solar wind/IMF conditions used in our magnetosheath model. We first selected  the  THEMIS  data  when  solar  wind  and  IMF  satisfy  the following  conditions:  0  &lt; &lt;  4  nT,  0  &lt; &lt;  4  nT,  300  &lt; &lt; 500  km/s.  Then,  we  further  down-selected  the  THEMIS  data  to match each solar wind/IMF condition. For IMF =  4  and  -4 nT, we selected  the  THEMIS  observations  during  IMF =  2-6  and from -6 to -2 nT, respectively. For solar wind plasma density ( ) at 5, 10, 15, 20, 25, and 30 cm , we selected the THEMIS observations when ranges between 0-10, 5-15, 10-20, 15-25, 20-30, and 25-35 cm ,  respectively.  Finally,  the  selected  THEMIS  data for  each  solar  wind/IMF  condition  were  bin-averaged  with  the resolution  of  0.1  in f and  7.5°  in .  The  total  number  of  THEMIS data  points  used  in  our  study  is  ~224,000.  However,  some  bins have very low counts. For &gt; 25 cm , 87% of the bins had less than  10  counts,  thus  making  it  difficult  to  obtain  statistical magnetosheath conditions. In this study, we compared our MHDbased model results with  the  THEMIS  magnetosheath  data  only for the conditions of solar wind density below 25 cm ,  and only on the dayside.

Figure 2 compares the MHD-based magnetosheath model results with the THEMIS statistical data for northward (left) and southward (right)  IMF.  From  top  to  bottom,  magnetic  field  magnitude, plasma  density,  plasma  speed,  and  temperatures  are  shown.  In this  figure,  we  used  only  the  THEMIS  data  within f =  0.3-0.7 because  the  THEMIS  data  points  of f &lt;  0.3  or f &gt;  0.7  can  be

r W r W affected by the motion of the bow shock and magnetopause and thus are prone to errors. In reality, this means these bins can be mixed with the magnetosphere or solar wind data, thus potentially contaminating the  statistical  analysis  of  magnetosheath   conditions. Darker red dots mean that the THEMIS data points are statistically strong. The blue line is the y = x reference line. All the data points  will  be  aligned  with  this  blue  line  if  our  model  results perfectly  match  with  THEMIS  statistical  data.  The  upper  left corners show the weighted Pearson correlation coefficients ( ). Here, weights are based on the number of THEMIS bin counts so that the statistically insignificant data points are penalized in the calculation.

Plasma density, speed, and magnetic field magnitude in Figure 2 shows  a  Pearson  correlation  coefficient  larger  than  or  equal  to 0.78  for  both  southward  and  northward  IMF  cases.  Our  data points  are  not  perfectly  aligned  with  the  blue  line,  but  this  is understandable  considering  the  following  issues  in  the  THEMIS dataset. First, transient structures like Kelvin-Helmholtz instability and mirror modes in the magnetosheath might modify statistical average of plasma properties. Second, the uncertainty in the solar wind propagation (Sivadas and Sibeck, 2022) may cause mismatch when pairing OMNI data with THEMIS data. Third, the empirical models of MP (Shue et al., 1998) and BS (Verigin et al., 2001) can f ϕ locate the boundaries different from reality, and thus THEMIS data points may falsely fall into different bins (i.e. and ). Fourth, the statistical  magnetosheath  data  are  gathered  when  SW  and  IMF are close to - not exactly at - a given upstream condition. On the other hand, the MHD-based magnetosheath data are obtained when the upstream values are exactly same as the given conditions for at least 20 minutes. Lastly, some bins still have low counts to determine average magnetosheath conditions. Despite these uncertainties  in  the  statistical  THEMIS  dataset,  our  modeldata comparison shows remarkably good agreement. We also see outliers, the data points largely deviated from the expected correlations, in the magnetic field and density plots of Figure 2. These data  points  are  typically  associated  with  the  extreme  driving conditions like interplanetary coronal mass ejections (ICMEs). The large  magnetic  field  and  density  of  the  upstream  solar  wind during ICMEs can cause strong compression of the magnetosheath and creates abnormally large values in the THEMIS observations. Thus, we advise caution to users when using the Mshpy23-MHD model for such rare conditions.

5 Unlike  the  aforementioned  magnetosheath  parameters,  the  ion temperature shows a large discrepancy. There are several physical explanations  for  this.  First,  the  default  solar  wind  temperature used in OpenGGCM is 10 K, different from the typical solar wind

0.3 ≤ f ≤ 0.7

Jung J et al.: Mshpy23: a user-friendly, parameterized model of magnetosheath conditions

<!-- image -->

Bz Bz Bz r W Figure 2 . Comparison between the THEMIS statistical magnetosheath data and the MHD-based magnetosheath model results for IMF = 4 nT (left) and -4 nT (right). THEMIS data for IMF = 2-6 nT and from -6 to -2 nT are used for obtaining statistical magnetosheath conditions for IMF = 4 and -4 nT, respectively. From top to bottom, magnetic field magnitude, plasma density, plasma speed, and temperature are shown. Colors represent the number of THEMIS bin counts used in the calculation of averaged magnetosheath parameters. Blue lines represent the perfect model-data match lines. The upper left corner shows the Pearson correlation coefficient ( ) weighted by the number of THEMIS bin counts.

<!-- image -->

4 temperature of 3 10 K (Dimmock and Nykyri, 2013). Considering this difference of solar wind temperature, it is not surprising that our  modeled  magnetosheath  reveals  higher  temperatures  than the  observations.  Second,  the  global  MHD  model  does  not address full dynamics in the magnetosheath and its surrounding areas. Magnetosheath temperature is heavily influenced by numerous  kinetic  processes  such  as  magnetic  islands,  turbulent  reconnection,  ion-scale waves  and  turbulence,  and   magnetosheath  jets  (Karimabadi  et  al.,  2014). In  addition,  the   magnetosheath temperature is usually anisotropic, controlled by instabilities such as the mirror mode, firehose, and ion cyclotron, which maintain the magnetosheath plasma to marginal stability (Soucek et al., 2015). Since these processes are omitted in the global MHD model,  it  is  understandable  to  see  the  disagreement  between modeled and observed temperatures. Therefore, we advise users of our magnetosheath model to use our temperature results with caution.  This  temperature  discrepancy  could  be  improved  in future  by  employing  kinetic  hybrid  models  but  this  is  beyond  a scope of the present work.

## 3. Mshpy23: Compilation of Magnetosheath Models

## 3.1 Additional Magnetosheath Models

The previous section introduced the MHD-based magnetosheath model, a default model of Mshpy23. The Mshpy23 code includes three additional magnetosheath models in previous literature so that users can choose or compare various models of their interest. The first model is Mshpy23-Spreiter, based on Spreiter et al. (1966) that calculated plasma density, velocity, and temperature of the magnetosheath  in  terms  of  upstream  solar  wind  parameters under  hydrodynamics.  The  magnetosheath  model  of  Spreiter et al. (1966) have been widely used and have shown good agreement with in-situ space observations (see the review of Stahara, 2002). Soft X-ray physicists have also utilized this model for calculating near-Earth soft X-ray emissions (e.g., Robertson and Cravens,  2003;  Carter  et  al.,  2010).  We  obtained  a  file  used  in Carter et al. (2010) that parameterizes the model results of Spreiter et al. (1966). The file includes the solar wind versus magnetosheath ratios of  plasma  density  and  velocity  as  a  function  of   magne-

f ׋ tosheath locations so that the two magnetosheath parameters are obtained by simply multiplying the ratios  to  the  upstream  solar wind  parameters.  The  magnetosheath  temperatures  are  then calculated  by  equation  28  of  Spreiter  et  al.  (1966).  We  read  the ratio of Spreiter et al. (1966) using the same magnetosheath grids ( , θ , )  as  the Mshpy23-MHD model and used the ratios as seed parameters. We also adopted Shue et al. (1998) and Jelínek et al. (2012) boundary models for Mshpy23-Spreiter, instead of outdated boundary models in Spreiter et al. (1966). We compared the Mshpy23-Spreiter results with the THEMIS statistical data (not shown in our paper) and found that performance of this gasdynamic model is comparable to the Mshpy23-MHD model.

∇ B 0 B ϕ B B ∇ ϕ B ∇ 2 ϕ B 0 The second magnetosheath model is Mshpy23-RV from Romashets and Vandas (2019) that calculates only magnetic field vectors in the magnetosheath as a function of IMF and solar wind dynamic pressure.  Their  model  is  an  improved  version  of  Kobel and Flückiger (1994). Kobel and Flückiger (1994) model assumed that  currents  are  concentrated  at  the  magnetosheath  boundaries  (i.e.  magnetopause  and  bow  shock),  and  that  inside  of magnetosheath is current-free, i.e. . Subsequently, magnetosheath magnetic field ( ) can be expressed as magnetic potential ( ), ,  satisfying  the  Laplace  equation, . For simplicity, they assumed that magnetopause and bow shock are confocal paraboloids. Romashets and Vandas (2019) improved the magnetosheath boundary models by using the BS model of Formisano (1979)  and  the  MP  model  of  Formisano  et  al.  (1979), allowing non-confocal shape of magnetosheath boundaries. The requirement  of  Romashets  and  Vandas  (2019)  model  for  the boundary  models  are  they  should  be  able  to  be  described  in parabolic  equation  with  standoff  distances  and  foci  for  the MP(BS). We used Jelínek et al. (2012) MP/BS models as they satisfy the requirements, and also Vandas et al. (2020) used these boundary models for applying Romashets and Vandas (2019) model.

ρ f ρ d ρ ♥ ρ d 0 . 8 0 . 2 tanh 4 f The third magnetosheath model is Mshpy23-SE from Soucek and Escoubet (2012) and provides only magnetosheath plasma velocity with  solar  wind  velocity  input.  Their  model  utilized  the  idea  of Kobel and Flückiger (1994) that when IMF is nearly parallel to the solar wind flow, magnetic field lines can be considered as plasma stream lines. Soucek and Escoubet (2012) inputted the direction of solar wind velocity as the IMF direction, solved magnetic potentials  following  Kobel  and  Flückiger  (1994),  and  obtained  the magnetic field lines as a proxy of plasma stream lines. The plasma velocity directions are obtained from the stream lines. The magnitude of plasma velocity is obtained by solving the Rankine-Hugoniot relation and the continuity equation with an adhoc model of plasma density. In the model density at a fractional distance is related to the density on the same flowline near the shock as: .  Soucek  and  Escoubet  (2012)  used  the BS model of Farris et al. (1991) and the MP model of Shue et al. (1998). In contrast to the time-averaged flaring parameter used in Farris  et  al.  (1991)  BS  model,  Mshpy23-SE  incorporated  the  BS model  developed  by  Jelínek  et  al.  (2012).  This  implementation enables the BS location and shape to dynamically adjust to varying SW/IMF conditions.

Instead  of  using  time-averaged  flaring  parameter  of  Farris  et  al. (1991)  BS  model,  Mshpy23-SE  implemented  the  BS  model  of

Jelínek et al. (2012), allowing the BS location changes under various solar wind/IMF conditions.

The Mshpy23 code also allows users to manually adjust MP and BS locations.  If  spacecraft  observes  the  magnetosheath  boundaries at different locations than the Mshpy23 MP/BS models, users can radially move the model boundaries to match with the observed boundary locations. The examples are shown in Section 3.1.

## 3.2 Comparison with Satellite Magnetosheath Crossing

We conducted an analysis of two magnetosheath crossing events by comparing the Mshpy23 results with satellite observations. The first  event  involved  the  crossing  of  the  magnetosheath  by  the THEMIS C satellite on June 28, 2008. Figure 3a shows the location of  the  satellite  during  the  event,  projected  on  the  GSE XY (top) and XZ (bottom) planes. The satellite was in the magnetosphere at 13:00  UT  (orange  dot)  and  moved  to  the  upstream  solar  wind along  the  blue  line  after  passing  through  the  magnetosheath between 14:08 and 19:00 UT. To implement time-varying magnetosheath boundaries, we used the THEMIS C trajectory from NASA CDAWeb and SW/IMF conditions from NASA OMNI data (King and Papitashvili,  2005)  as  input  for  Mshpy23.  It  is  important  to  note that  for  satellite  crossings  like  this,  we  need  SW/IMF  conditions matched to the spacecraft position array to determine the magnetosheath boundaries corresponding to each spacecraft position.

R E To match the THEMIS magnetopause crossing data, we manually shifted the Shue MP by 0.5 earthward for the entire duration. In Figure  3b,  we  compare  the  Mshpy23  model  results  with  the THEMIS C observations (black). The green, blue, red, and magenta lines represent the MHD-based magnetosheath model (Mshpy23MHD), the Romashets and Vandas magnetic field model (Mshpy23RV), the Soucek &amp; Escoubet plasma velocity model (Mshpy23-SE), and the Spreiter  gas-dynamic  magnetosheath  model  (Mshpy23Spreiter), respectively.

Bz Vx Vy ∣ V ∣ In  Figure  3,  both  Mshpy23-MHD  and  Mshpy23-RV  results  show good agreement with the THEMIS observations. Mshpy23-MHD predicts number  density better than Mshpy23-Spreiter and plasma velocity (namely, , ,  and )  better than Mshpy23-SE model. As expected, Mshpy23 shows large discrepancy in temperature  because  both  Mshpy23-MHD  and  Mshpy23-Spreiter  are based  on  fluid  approaches  and  thus  omit  full  kinetic  processes that affect a magnetosheath temperature. Overall, Mshpy23-MHD performs  reasonably  well  compared  to  other  magnetosheath models. Additionally, Mshpy23-MHD  satisfies self-consistency among all the magnetosheath parameters to some extent since its seed data are calculated under the MHD theory.

R E R E The second example event is the Cluster magnetosheath crossing on 4 May 2003, which was used in Connor and Carter (2019) for the  analysis  of  near-Earth  soft  X-ray  emission.  As  seen  in  the Figure 4a Cluster 4 was located in the magnetosheath at 08:00 UT (orange dot) and crossed the magnetosheath along the blue line during 11:50-13:10 UT before entering the upstream solar wind. Figure  4b  compares  the  modeled  magnetosheath  parameters with the Cluster observations (black) in the same format as Figure 3b. Here we shifted MP by 0.9 sunward and BS by 1.2 earthward  to  match  with  observed  Cluster  boundary  crossings.  The

Bx By Bz ∣ B ∣ Vx Vy Vz ∣ V ∣ Figure 3 . The magnetosheath crossing event on 28 June 2008. (a) THEMIS C orbit (blue) projected on the GSE XY (top) and XZ (bottom) planes. The starting location for THEMIS C is shown as an orange dot. Orange lines represent the BS locations at the start (solid) and the end (dashed) of the THEMIS event, calculated from Jelínek et al. (2012). Similarly, red lines are the MP locations at the start (solid) and the end (dashed) of this event, calculated from Shue et al. (1998) model. (b) Model-data comparison of magnetosheath parameters. The THEMIS C observations (black) are compared with the MHD-based magnetosheath model (green), the Romashets and Vandas magnetic field model (blue), the Soucek and Escoubet plasma velocity model (red), and the Spreiter gas-dynamic model (purple). Magnetic field , , , , plasma velocity , , , , number density, and temperature are shown from top to bottom. The gray shaded area indicates when THEMIS passes through the magnetosheath.

<!-- image -->

modeled magnetosheath values are obtained after adjusting the boundaries.  Similar  to  the  THEMIS  event,  the  Mshpy23-MHD predicts magnetosheath parameters better or comparable to the other magnetosheath models.

## 4. Modeling of Soft X-ray image

## 4.1 Soft X-ray Image Calculation

C 6 N 6 N 7 Ne 9 S 10 O 7 O 8 Soft X-ray is emitted when a highly charged solar wind ion steals an electron from an exospheric neutral and the electron moves to a  lower  energy  state.  This  process  is  called  "Solar  Wind  Charge Exchange (SWCX)".  The  SWCX  source  ions  in  solar  wind  include , , , , , , and . They produces a variety of soft X-ray emission lines in the energy of 0.4-1.0 keV.

LEXI and SMILE will have an soft X-ray instrument on board, visual- izing the dayside magnetospheric system in soft X-ray. The Earth's magnetosheath emits strong soft X-rays because solar wind ions are densely populated in the magnetosheath. Soft X-ray imaging of the magnetosheath enables us to capture the magnetopause motion (Collier and Connor, 2018; Sun TR et al., 2019; Jorgensen et al., 2019) and thus unveil reconnection modes under time-varying  SW/IMF  conditions.  To  support  mission  planning  and  data analysis of LEXI and SMILE, we developed a simple Mshpy23-Xray tool  that  simulates  soft  X-ray  images  expected  from  various vantage points under different upstream conditions.

The SWCX energy flux along a line of sight for a single emission line is given by the following equation (Kuntz, 2019):

<!-- formula-not-decoded -->

Figure 4 . The magnetosheath crossing event on 4 May 2003 in the same format of Figure 3. (a) Cluster 4 orbit projected on the GSE XY (top) and XZ (bottom) planes. (b) Model-data comparison of magnetosheath parameters.

<!-- image -->

E n n O 7 v rel v rel where is a photon energy emitted after the charge exchange, is  a  neutral  density, n is  an  ion  density  of  a  certain  charge  state (e.g., ),  and is  a  relative  velocity between the ion and the neutral. Exospheric neutrals are originated from the upper atmosphere  whose  energy  (or  temperature)  is 0.1  eV  (Qin  JQ  and Waldrop, 2016). It is expected that exospheric neutrals are much slower  than  the  magnetosheath  plasmas  whose  energy  ranges rom several hundreds eV to a few keV. Neutral velocity is negligible in  solar  wind  charge  exchange.  Assuming  a  negligible  neutral velocity, can be approximated as a plasma velocity:

<!-- formula-not-decoded -->

v r v t v t √ 3 kT ♥ m p σ v rel v rel b Ω s s 0 s where is  an ion bulk velocity, and is  an ion thermal velocity, . is  a  charge  exchange  cross  section  and depends on . is a probability of emission after SWCX. d is a solid  angle  that  corresponds  to  an  X-ray  image  resolution.  The integral  is  done  along  the  line  of  sight  distance ,  from to .

Equation  (12)  can  be  simplified  by  grouping  the  parameters provided by Mshpy23 and applying several assumptions. Here we define a potential reaction rate Q :

<!-- formula-not-decoded -->

n p where is a solar wind proton density. Hydrogen atoms are the most dominant species in the exosphere above 1500 km altitude (Zoennchen  et  al.,  2022).  We  used  the  following  exospheric density model of Cravens et al. (2001):

<!-- formula-not-decoded -->

R E N 0 3 cm 3 with neutral density at 10 , = 25 cm , n n is in . Then, the Equation (12) is written as:

<!-- formula-not-decoded -->

σ b n ♥ n p E 1 E 2 Following Schwadron and Cravens (2000) and Pepino et al. (2004), we assumed  that  the  atomic  parameters  ( , )  and  abundance ratio is constant along a line of sight. Then total energy flux for a certain energy band [ , ] can be written as

where

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

α An effective  scale  factor  ( )  combines  abundance,  cross  section and emission probability of solar wind ion species including C, N, Ne,  S,  and  O.  Abundance  can  be  determined  from  the  in-situ measurements  of  solar  wind  ions,  e.g.  data  from  the  Advanced Composition Explorer  (ACE)  Solar  Wind  Ion  Composition   Spec-

Ej σ b α 16 2 trometer (SWICS) (Whittaker and Sembay, 2016). Other parameters ( , , and ) can be theoretically and/or experimentally obtained (Betancourt-Martinez,  2017).  However,  due  to  the  limitations  of observations, theory, and experiment, exact alpha values are not fully understood and still under active studies. Here we adopt = 6.0 × 10 eV cm , following Cravens et al. (2001).

## 4.2 Example of Image Calculation

3 5 B 2 , 2 , 5 P αn n n p v rel We calculated soft X-ray images during steady upstream conditions of  solar  wind  density  at  10  cm ,  velocity  at  (400,  0,  0)  km/s, temperature = 10 K, and IMF nT in GSE coordinates. Figure 5a and 5b show X-ray emissivity rates ( ) on an

X, Y, Z GSE R E X, Y, Z GSE R E B 2 , 2 , 5 3 Figure 5 . (a) Magnetosheath X-ray emission on the XY plane computed from Mshpy23-Xray and (b) Jorgensen et al. (2019) emission model. Both cases used Je ř áb et al. (2005) MP model and Jelínek et al. (2012) BS model for magnetosheath boundaries. (c) Soft X-ray emissivity map calculated from Mshpy23-Xray by locating a virtual spacecraft at = (0, 30, 0) , (d) and = (0, 0, 30) . The images use 0.25° × 0.25° angular resolution. Note that our model does not support the cusp structure. For all the models used for images, IMF was set to nT. Solar wind velocity was set to 400 km/s, solar wind density 10 cm .

<!-- image -->

equatorial  plane  calculated  from  Mshpy23-Xray  and  a  simple emissivity model of Jorgensen et al. (2019), respectively. The minimum and  maximum  emission  rates  are  labeled  at  the  bottom. Mshpy23-Xray  first  defined  the  magnetosheath  boundaries  of Shue et al. (1998) and Jelínek et al. (2012), obtained magnetosheath parameters from Mshpy23-MHD, and finally calculated X-ray emission rates on the equatorial plane as seen in Figure 5a. Jorgensen et al. (2019) introduces the following formula of soft X-ray emission rate:

F r 3 1 r r r ref R E A 1 A 2 α β 3 Vx Vy Vz Bx By Bz A 1 5 3 1 5 3 1 α 2 β 2 A 2 5 3 1 r ref R E where a unit of is eV cm s , points a location of interest, r is  a  geocentric  distance  of  the  location,  and  theta  is  an  angel between and  the  sun-earth  line. =  10 .  Jorgensen  et  al. (2019) fitted the parameters , , B , , and using a PPM (piecewise parabolic method)-MHD code simulation with following solar wind conditions: solar wind density n =  22.5  cm ;  velocity = 400  km/s, = =  0;  and  interplanetary  magnetic  field = =  0, =  5  nT.  Parameters  fitted  were =  3.2285  ×  10 eV cm s , B =  -1.7985  ×  10 eV  cm s , =  2.4908, = -1.6458, = 1.3588 × 10 eV cm s , = 10 .  For  Figure 5b,  we  used  the  same  boundary  models  of  Mshpy23,  i.e.,  Shue et al. (1998) and Jelínek et al. (2012).

<!-- formula-not-decoded -->

Figure 5a and 5b showed good agreement between the two emissivity models. Their emission rates are comparable. They are also stronger near a subsolar point and weakens as moving toward the flank. This is because less exospheric neutrals are available in the magneotsheath flank due to its long distance to the Earth's upper atmosphere, the source region of exopsheric neutrals.

Figure  5c  and  5d  show  soft  X-ray  images  expected  from  two

N

sw

: 20.00 cm -3

V

sw

: 400.00 km s -1

-1

Flux: 8.00e+08 cm -2  s

Bx

: 2.00 nT

By

: 2.00 nT

Bz

: -5.00 nT

Input simulation

<!-- image -->

X, Y, Z GSE R E R E 2 1 1 R E virtual spacecrafts at = (0, 30, 0) and (0, 0, 30) and calculated from Mshpy23-Xray. The colors represents integrated Xray emission rates along lines of sight within a 30° × 30° field of view, in a unit of keV cm s sr . The image angular resolution is set at 0.25° × 0.25°. The blue circular areas in Figure 5c and 5d are  the  region  surrounding  the  Earth  ( r &lt;  2.1 ),  and  no  X-ray calculation is done in this region. As expected, our images show strong  magnetosheath  emissions  and  are  comparable  to  the images  in  previous  literature  (Cravens  et  al.,  2001;  Walsh  et  al., 2016; Sibeck et al., 2018; Connor et al., 2021) that utilized a global MHD model for the image calculation. One caveat of our images do  not  show  cusps,  another  strong  X-ray  source,  because  the current version of Mshpy23 does not include cusp features. This will be our future task.

3 5 R E R E Real X-ray images can be different from the ideal images in Figure 5c-5d because of other X-ray backgrounds in the sky (e.g., light sources, diffuse astronomical backgrounds, and heliospheric backgrounds) and  instrument  effects  (e.g.,  intrumental   background,  Poisson noise, limited field-of-view, and instrument responses) (Sibeck et al., 2018; Jung et al., 2022). Figure 6 shows ideal  (left)  and  realistic  (right)  images  expected  from  the  SMILE soft X-ray instrument (SXI). We used solar wind density of 10 cm , velocity of (400, 0, 0) km/s, temperature of 10 K, and IMF of (2, 2, -5)  nT  in  GSE  coordinates.  The  left  figure  in  Figure  6  shows  an ideal  image  of  SMILE  SXI  calculated  from  Mshpy23-Xray,  when SMILE is located at (3.5, -2.3, 17.1) and SXI points at (3.5, -2.3, 0) in  GSE  coordinates  with  a  16°  ×  27°  FOV.  The  right  figure shows a realistic X-ray image obtained from a SMILE SXI tool with the left figure as input. This tool is developed by the SXI instrument team, and not included in Mshpy23. This SXI tool processes input spatial maps by folding them through the instrument response to predict the total observed X-ray counts map for a specified integration time and energy band. Here we used 5 minutes exposure time.  The  instrument  response  is  the  telescope's  effective  area,

Position: (3.5, 1.7, 17.2) R E Aim Point: (10.0, 0.0, 0.0) GSE Earth limb angle = 28.84 degrees

SXI CX Counts: 300 s

X, Y, Z GSE R E Figure 6 . (Left) Side-view of simulated soft X-ray emissivity map observed by SMILE at = (3.5, -2.3, 17.1) . White rectangle is the assumed field-of-view of 16° × 27°. (Right) Simulated image processed with SMILE SXI tool.

<!-- image -->

which varies with energy and angular position within the field-ofview.  To  the  output  map,  Poisson  noise  is  added,  and  the processed version is obtained by subtracting the predicted background model and correcting for the telescope vignetting function.  The  resulting  foreground  SWCX  emission  prediction  has noise  per  pixel  appropriate  to  the  total  input  components  and background  subtraction  process.  The  synthetic  SXI  image  in Figure  6b  still  shows  strong  magnetosheath  emission  but  with non-negligible noises. The SMILE Modeling Working Group (MWG)  have  been  developing  several  image  analysis  tools  that extract  a  magnetopause  location  from  noisy  soft  X-ray  images (e.g.  see  Samsonov  et  al.,  2022).  Such  image  analysis  tools  will help to extract the magnetopause motion under various upstream conditions and thus unveil dayside reconnection modes.

## 5. Model Limitation and Fut Work

In this section, we discuss future directions for improving Mshpy23.  Firstly,  we  plan  to  enhance  the  model  by  including more  SW/IMF  conditions.  As  noted  in  Section  2.3,  the  current version  of  Mshpy23  did  not  account  for  the  impact  of  various SW/IMF  conditions,  leading  to  a  mismatch  with  observed  data under high solar wind density conditions. Additionally, as seen in Figure 2, Mshpy23-MHD tends to overestimate temperature (average 1.662 times higher than THEMIS data). However, the primary focus of soft X-ray imaging is to accurately identify the MP position for studying reconnection mode, making the absolute magnitude of  emission  less  critical.  Instead,  the  model's  ability  to  precisely represent  the  boundary  location  and  structure  holds  greater importance. To address these limitations and improve the model's performance, we will incorporate OpenGGCM runs under multiple SW velocities, stronger/weaker IMF, various directions for IMF, and diverse  SW  temperatures.  This  comprehensive  approach  will enhance  the  accuracy  of  our  model  predictions  under  a  wider range of SW/IMF conditions.

Secondly,  our  goal  is  to  enhance  the  boundary  prediction  of Mshpy23 by incorporating more sophisticated models for the MP and BS. The current version of the model only includes testing a few  simple  MP/BS  models,  and  we  have  not  tested  the  Verigin et  al.  (2001)  model,  which  was  used  in  the  compilation  of  our THEMIS  dataset  (Dimmock  et  al.,  2017).  We  recognize  that  the rotational symmetry of the Jelínek et al. (2012) BS model may lead to inaccurate predictions for magnetosheath parameters, particularly in the flank regions. Therefore, we will address this limitation by incorporating  additional  boundary  models,  including  the  Lin RL et al. (2010) MP and Verigin et al. (2001) BS model. This expansion will  provide  our  model  users  with  more  choices  and  options  for representing the magnetosheath boundaries more accurately. For users  who  seek  to  use  our  model  in  actual  event  analysis,  we advise complementing the model with in-situ measurement data from heliospheric satellite like THEMIS or MMS, as demonstrated in our adjustments in Section 3.2.

Thirdly, our plan includes the expansion of the model's coverage to encompass the nightside magnetosheath domain. At present, the model is limited to the dayside magnetosheath domain with a longitude range of -90° &lt; longitude &lt; 90°. However, our objective is  to  extend  the  supported  magnetosheath  longitude  range  to approximately  -120°  &lt;  longitude  &lt;  120°.  This  expansion  poses challenges because  the  current  method  of  defining   magnetosheath  boundaries  for  Mshpy23-MHD  seed  grids,  which  relies on plasma density gradients along a radial direction, is not wellsuited for the nightside magnetosheath. To overcome these challenges  and  validate  the  nightside  magnetosheath  data,  we  are exploring alternative methods for determining nightside MP and BS locations. One approach is to utilize data from other missions such  as  Geotail,  Cluster,  or  MMS,  which  have  the  potential  to provide  valuable insights into  the  nightside  magnetosheath conditions.  By  integrating  data  from  these  missions,  we  aim  to improve the  accuracy  and  reliability  of  the  nightside   magnetosheath representation in our model.

Fourthly, we will include the polar cusp region in Mshpy23. The current  version  of  Mshpy23  does  not  take  into  account  polar cusps that are strong emission regions of soft X-ray and ENA. The difficulty of modeling coordinates in the magnetosheath, including the polar  cusp  with  its  complex  shape,  results  in  a  limitation  to accurately represent  points  in  this  region  with  suitable   coordinates. This, in turn, makes it challenging to model the cusp region in the magnetosheath modeling approach. However, we plan to include an analytic cusp model in the future version of Mshpy23.

Lastly, we plan to consider the dipole tilt effect in our model. The tilt of the Earth's magnetic dipole axis with respect to the rotational axis  creates  an  asymmetric  magnetopause  shape  (Samsonov  et al., 2016). Although the dipole tilt impact on the magnetosheath parameters  are  not  well  understood,  this  limitation  could  affect the  accuracy  of  the  Mshpy23  predictions.  Therefore,  we  plan  to test  the  dependence  of  Mshpy23  on  dipole  tilt  to  improve  the accuracy of our predictions.

We aim to enhance the model-data validation process by incorporating a more extensive set of in-situ observations spanning the entire magnetosheath region and creating statistically robust data samples.  However,  the  current  THEMIS  dataset  utilized  in  this study is limited to magnetosheath parameters near the equatorial region,  constrained  by  its  orbit.  Additionally,  the  distribution  of data points among the magnetosheath bins is uneven, leading to statistically inadequate bin-averages. Notably, about 47% of total bins  (1174  bins)  contain  fewer  than  10  data  points,  resulting  in limited statistical representation.

To address  these  limitations  and  improve  our  model  validation, we plan to include magnetosheath observations from the Cluster and  MMS  missions.  By  incorporating  data  from  these  missions, particularly during special conjunctions where Cluster, MMS, and THEMIS  all  traverse  the  magnetosheath  simultaneously,  we  can expand  the  data  coverage  to  higher  latitude  and  obtain  more comprehensive and representative samples for model validation. The  analysis  of  data  from  these  special  conjunctions,  alongside comparisons  to  the  OpenGGCM  MHD  model,  will  enable  us  to enhance the precision and reliability  of  our  current  model.   Integrating data from multiple sources will offer a more robust validation framework and provide a more comprehensive understanding of  the  magnetosheath's  dynamics  and  behavior  across  various spatial regions.

## 6. Summary

We  developed  a  Mshpy23  Python  tool  that  calculates  plasma density, velocity, temperature, and magnetic fields of the magnetosheath  with  solar  wind  and  IMF  input.  This  tool  includes  four different models: the MHD-based model newly developed in this paper,  the  gas-dynamic  model  of  Spreiter  et  al.  (1966),  the magnetic field  model  of  Romashets  and  Vandas  (2019),  and  the velocity  model  of  Soucek  and  Escoubet  (2012)  that  are  named Mshpy23-MHD, Mshpy23-Spreiter, Mshpy23-RV, and Mshpy23-SE, respectively.

Figure  7  shows  a  schematic  diagram  of  Mshpy23.  First,  a  user inputs a position in the magnetosheath and SW/IMF conditions at a bow shock nose in the GSE coordinate system. The input position can be an array of various dimensions such as a satellite trajectory, 2D grids on equatorial/meridional planes, and 3D grids of global magnetosheath.  The  SW/IMF  input  can  also  be  an  array  if  the input  position  is  given  as  a  time-varying  array  (e.g.,  a  satellite trajectory).  Second,  Mshpy23 obtains MP and BS locations using Shue  et  al.  (1998)  and  Jelínek  et  al.  (2012)  as  default  models, except the Mshpy23-RV. Romashets and Vandas (2019) magnetic field model requires parabolic MP shape, so Shue et al. (1998) MP model cannot be used. Following  Vandas  et  al.  (2020),  we  used Jelínek  et  al.  (2012)  MP  model  for  the  Mshpy23-RV.  Mshpy23 provides an option to use another BS model of Je ř áb et al. (2005) by  entering  a  desired  BS  model  name  as  input.  As  shown  in Section  3.2,  a  user  can  adjust  MP/BS  positions  radially  with  an optional  input  to  Mshpy23  for  matching  the  boundaries  with satellite  observations.  Third,  Mshpy23  calculates  magnetosheath parameters from a selected magnetosheath model among Mshpy23-MHD, Mshpy23-Spreiter, Mshpy23-RV, and Mshpy23-SE. Finally,  in  case  that  the  input  positions  are  2D  or  3D  arrays, Mshpy23-Xray can calculate the 2D cut of X-ray emissivity or the soft  X-ray  images  seen  from  a  virtual  spacecraft.  Mshpy23-Xray uses Mshpy23-MHD as a default magnetosheath model.

3 Bz Mshpy23-MHD  is  constructed  from  14  OpenGGCM  simulations under  seven  solar  wind  densities  of  1,  5,  10,  15,  20,  25,  and 30 cm and two IMF components of -4 and 4 nT. The model results  are  compared  with  the  THEMIS  statistical  data  from Dimmock  et  al.  (2017).  Plasma  density,  velocity,  and  magnetic field  magnitudes  showed  good  model-data  agreement  with weighted  Pearson  coefficients  larger  than  0.78.  However,  the model tends to show higher temperature than the observations, because  only  one  solar  wind  temperature  were  used  in  the OpenGGCM  simulations and because MHD  physics cannot address full heating mechanisms in the magnetosheath.

Mshpy23 also includes three additional magnetosheath models of previous  literature.  Mshpy23-Spreiter  provides  plasma  number density,  speed,  and  temperature,  Mshpy23-RV  provides  only magnetic fields, and Mshpy23-SE provides only plasma velocities. We  conducted  model-data  comparison  for  the  magnetosheath crossing events of THEMIS and Cluster and checked performance of all  magnetosheath models in our tool. Mshpy23-MHD was on par with other magnetosheath models while satisfying self-consistency among magnetosheath parameters under MHD physics.

Mshpy23-Xray calculates a soft X-ray image of the dayside magnetosheath, using Mshpy23-MHD  as  a  default  magnetosheath model.  By  inputing  a  virtual  sapcecraft  position  and  SW/IMF conditions of interest, a user can produce an expected soft X-ray images without sophisticated knowledge of a gloabl MHD model. Our X-ray images show good agreement with the ones in previous literature (Jorgensen et al., 2019; Connor et al., 2021) except that cusp  signatures  are  missing  due  to  the  current  limitation  of Mshpy23-MHD.

Mshpy23 is an user-friendly, open-source code that parameterizes global magnetosheath environment under various SW/IMF condtions. Mshpy23-MHD is an empirical magnetosheath model based on the MHD theory. It is upgraded from a widely used empirical model based on Spreiter et al. (1966). Mshpy23-Spreiter, Mshpy23RV,  and  Mshpy23-SE  also  increase  users'  accessibility  to  other magnetosheath models without writing new codes from scratch. Finally, Mshpy23-Xray quickly reproduces soft X-ray images from various vantage points under different SW/IMF conditions without simulating a global magnetosphere model (e.g., MHD, hybrid, or particle-in-cell  simulations).  This  will  support  the  planning  and data analysis of LEXI and SMILE soft X-ray instruments.

## Acknowledgments

This  work  is  supported  by  the  NSF  grant  AGS-1928883  and  the NASA  grants,  80NSSC20K1670  and  80MSFC20C0019.  Hyunju  K. Connor gratefully acknowledges support from NASA GSFC IRAD, HIF, and ISFM funds.

Figure 7 . Schematic diagram of Mshpy23.

<!-- image -->

Jung J et al.: Mshpy23: a user-friendly, parameterized model of magnetosheath conditions

## References

- Betancourt-Martinez, G. L. (2017). Benchmarking charge exchange theory in the dawning era of space-borne high-resolution x-ray spectrometers. College Park: University of Maryland.
- Boardsen, S. A., Eastman, T. E., Sotirelis, T., and Green, J. L. (2000). An empirical model of the high-latitude magnetopause. J. Geophys. Res.: Space Phys. , 105 (A10), 23193-23219. https://doi.org/10.1029/1998JA000143
- Branduardi-Raymont, G., Wang, C., Escoubet, C. P., Adamovic, M., Agnolon, D., Berthomier, M., Carter, J. A., Chen, W., Colangeli, L., … Zhu, Z. (2018). Smile definition study report. ESA/SCI.

https://doi.org/10.5270/esa.smile.definition\_study\_report-2018-12

- Cairns, I. H., and Lyon, J. G. (1995). MHD simulations of Earth's bow shock at low Mach numbers: standoff distances. J. Geophys. Res.: Space Phys. , 100 (A9), 17173-17180. https://doi.org/10.1029/95JA00993
- Carter, J. A., Sembay, S., and Read, A. M. (2010). A high charge state coronal mass ejection seen through solar wind charge exchange emission as detected by XMM -Newton . Mon. Not. Roy. Astron. Soc. , 402 (2), 867-878. https://doi.org/10.1111/j.1365-2966.2009.15985.x
- Chao, J. K., Wu, D. J., Lin, C. H., Yang, Y. H., Wang, X. Y., Kessel, M., Chen, S. H., and Lepping, R. P. (2002). Models for the size and shape of the Earth's magnetopause and bow shock. COSPAR Colloq. Ser. , 12 , 127-135. https://doi. org/10.1016/S0964-2749(02)80212-8
- Collier, M. R., and Connor, H. K. (2018). Magnetopause surface reconstruction from tangent vector observations. J. Geophys. Res.: Space Phys. , 123 (12), 10189-10199. https://doi.org/10.1029/2018JA025763
- Connor, H. J., Raeder, J., and Trattner, K. J. (2012). Dynamic modeling of cusp ion structures. J. Geophys. Res.: Space Phys. , 117 (A4), A04203. https://doi.org/ 10.1029/2011JA017203
- Connor, H. K., Zesta, E., Ober, D. M., and Raeder, J. (2014). The relation between transpolar potential and reconnection rates during sudden enhancement of solar wind dynamic pressure: OpenGGCM-CTIM results. J. Geophys. Res.: Space Phys. , 119 (5), 3411-3429. https://doi.org/10.1002/2013JA019728
- Connor, H. K., Raeder, J., Sibeck, D. G., and Trattner, K. J. (2015). Relation between cusp ion structures and dayside reconnection for four IMF clock angles: OpenGGCM-LTPT results. J. Geophys. Res.: Space Phys. , 120 (6), 4890-4906. https://doi.org/10.1002/2015JA021156
- Connor, H. K., Zesta, E., Fedrizzi, M., Shi, Y., Raeder, J., Codrescu, M. V., and FullerRowell, T. J. (2016). Modeling the ionosphere-thermosphere response to a geomagnetic storm using physics-based magnetospheric energy input: OpenGGCM-CTIM results. J. Space Weather Space Clim. , 6 , A25. https://doi. org/10.1051/swsc/2016019
- Connor, H. K., and Carter, J. A. (2019). Exospheric neutral hydrogen density at the nominal 10 RE subsolar point deduced from XMM-newton X-ray observations. J. Geophys. Res.: Space Phys. , 124 (3), 1612-1624. https://doi. org/10.1029/2018JA026187
- Connor, H. K., Sibeck, D. G., Collier, M. R., Baliukin, I. I., Branduardi-Raymont, G., Brandt, P. C., Buzulukova, N. Y., Collado-Vega, Y. M., Escoubet, C. P., … Jung, J. (2021). Soft X-ray and ENA imaging of the Earth's dayside magnetosphere. J. Geophys. Res.: Space Phys. , 126 (3), e2020JA028816. https: //doi.org/10.1029/2020JA028816
- Cramer, W. D., Raeder, J., Toffoletto, F. R., Gilson, M., and Hu, B. (2017). Plasma sheet injections into the inner magnetosphere: two-way coupled OpenGGCM-RCM model results. J. Geophys. Res.: Space Phys. , 122 (5), 5077-5091. https://doi.org/10.1002/2017JA024104
- Cravens, T. E., Robertson, I. P., and Snowden, S. L. (2001). Temporal variations of geocoronal and heliospheric X-ray emission associated with the solar wind interaction with neutrals. J. Geophys. Res.: Space Phys. , 106 (A11), 24883-24892. https://doi.org/10.1029/2000JA000461
- Dimmock, A. P., and Nykyri, K. (2013). The statistical mapping of magnetosheath plasma properties based on THEMIS measurements in the magnetosheath interplanetary medium reference frame. J. Geophys. Res.: Space Phys. , 118 (8), 4963-4976. https://doi.org/10.1002/jgra.50465
- Dimmock, A. P., Nykyri, K., Osmane, A., Karimabadi, H., and Pulkkinen, T. I. (2017). Dawn-dusk asymmetries of the earth's dayside magnetosheath in the magnetosheath interplanetary medium reference frame. In S. Haaland,
- et al. (Eds.), Dawn-dusk Asymmetries in Planetary Plasma Environments (pp. 49-72). Washington: American Geophysical Union.

https://doi.org/10.1002/9781119216346.ch5

- Fairfield, D. H. (1971). Average and unusual locations of the Earth's magnetopause and bow shock. J. Geophys. Res. , 76 (28), 6700-6716. https:// doi.org/10.1029/JA076i028p06700
- Farris, M. H., Petrinec, S. M., and Russell, C. T. (1991). The thickness of the magnetosheath: constraints on the polytropic index. Geophys. Res. Lett. , 18 (10), 1821-1824. https://doi.org/10.1029/91GL02090
- Ferdousi, B., and Raeder, J. (2016). Signal propagation time from the magnetotail to the ionosphere: OpenGGCM simulation. J. Geophys. Res.: Space Phys. , 121 (7), 6549-6561. https://doi.org/10.1002/2016JA022445
- Ferdousi, B., Raeder, J., Zesta, E., Cramer, W., and Murphy, K. (2021). Association of auroral streamers and bursty bulk flows during different states of the magnetotail: a case study. J. Geophys. Res.: Space Phys. , 126 (9), e2021JA029329. https://doi.org/10.1029/2021JA029329
- Formisano, V. (1979). Orientation and shape of the Earth's bow shock in three dimensions. Planet. Space Sci. , 27 (9), 1151-1161. https://doi.org/10.1016/ 0032-0633(79)90135-1
- Formisano, V., Domingo, V., and Wenzel, K. P. (1979). The three-dimensional shape of the magnetopause. Planet. Space Sci. , 27 (9), 1137-1149. https://doi. org/10.1016/0032-0633(79)90134-X
- Jelínek, K., N ě me č ek, Z., and Šafránková, J. (2012). A new approach to magnetopause and bow shock modeling based on automated region identification. J. Geophys. Res.: Space Phys. , 117 (A5), A05208. https://doi.org/ 10.1029/2011JA017252
- Jensen, J. B., Raeder, J., Maynard, K., and Cramer, W. D. (2017). Particle precipitation effects on convection and the magnetic reconnection rate in earth's magnetosphere. J. Geophys. Res.: Space Phys. , 122 (11), 11413-11427. https://doi.org/10.1002/2017JA024030
- Je ř áb, M., N ě me č ek, Z., Šafránková, J., Jelínek, K., and M ě rka, J. (2005). Improved bow shock model with dependence on the IMF strength. Planet. Space Sci. , 53 (1-3), 85-93. https://doi.org/10.1016/j.pss.2004.09.032
- Jorgensen, A. M., Sun, T. R., Wang, C., Dai, L., Sembay, S., Wei, F., Guo, Y. H., and Xu, R. L. (2019). Boundary detection in three dimensions with application to the SMILE mission: the effect of photon noise. J. Geophys. Res.: Space Phys. , 124 (6), 4365-4383. https://doi.org/10.1029/2018JA025919
- Jung, J., Connor, H. K., Carter, J. A., Koutroumpa, D., Pagani, C., and Kuntz, K. D. (2022). Solar minimum exospheric neutral density near the subsolar magnetopause estimated from the XMM soft X-ray observations on 12 November 2008. J. Geophys. Res.: Space Phys. , 127 (3), e2021JA029676. https: //doi.org/10.1029/2021JA029676
- Karimabadi, H., Roytershteyn, V., Vu, H. X., Omelchenko, Y. A., Scudder, J., Daughton, W., Dimmock, A., Nykyri, K., Wan, M., … Geveci, B. (2014). The link between shocks, turbulence, and magnetic reconnection in collisionless plasmas. Phys. Plasmas , 21 (6), 062308. https://doi.org/10.1063/ 1.4882875
- Kavosi, S., Spence, H. E., Fennell, J. F., Turner, D. L., Connor, H. K., and Raeder, J. (2018). MMS/FEEPS observations of electron microinjections due to kelvinHelmholtz waves and flux transfer events: a case study. J. Geophys. Res.: Space Phys. , 123 (7), 5364-5378. https://doi.org/10.1029/2018JA025244
- King, J. H., and Papitashvili, N. E. (2005). Solar wind spatial scales in and comparisons of hourly wind and ACE plasma and magnetic field data. J. Geophys. Res.: Space Phys. , 110 (A2), A02104. https://doi.org/10.1029/ 2004JA010649
- Kobel, E., and Flückiger, E. O. (1994). A model of the steady state magnetic field in the magnetosheath. J. Geophys. Res.: Space Phys. , 99 (A12), 23617-23622. https://doi.org/10.1029/94JA01778
- Kuntz, K. D. (2019). Solar wind charge exchange: an astrophysical nuisance. Astron. Astrophys. Rev. , 27 (1), 1. https://doi.org/10.1007/s00159-018-0114-0
- Kuznetsov, S. N., and Suvorova, A. V. (1998). An empirical model of the magnetopause for broad ranges of solar wind pressure and BZ IMF. In J. Moen, et al. (Eds.), Polar Cap Boundary Phenomena (pp. 51-61). Dordrecht: Springer. https://doi.org/10.1007/978-94-011-5214-3\_5
- Lin, R. L., Zhang, X. X., Liu, S. Q., Wang, Y. L., and Gong, J. C. (2010). A three-

- dimensional asymmetric magnetopause model. J. Geophys. Res.: Space Phys. , 115 (A4), A04207. https://doi.org/10.1029/2009JA014235
- Liu, Z. Q., Lu, J. Y., Wang, C., Kabin, K., Zhao, J. S., Wang, M., Han, J. P., Wang, J. Y., and Zhao, M. X. (2015). A three-dimensional high Mach number asymmetric magnetopause model from global MHD simulation. J. Geophys. Res.: Space Phys. , 120 (7), 5645-5666. https://doi.org/10.1002/2014JA020961
- Lu, J. Y., Liu, Z. Q., Kabin, K., Zhao, M. X., Liu, D. D., Zhou, Q., and Xiao, Y. (2011). Three dimensional shape of the magnetopause: global MHD results. J. Geophys. Res.: Space Phys. , 116 (A9), A09237. https://doi.org/10.1029/ 2010JA016418
- Lu, J. Y., Zhang, H. X., Wang, M., Gu, C. L., and Guan, H. Y. (2019a). Magnetosphere response to the IMF turning from north to south. Earth Planet. Phys. , 3 (1), 8-16. https://doi.org/10.26464/epp2019002
- Lu, J. Y., Zhou, Y., Ma, X., Wang, M., Kabin, K., and Yuan, H. Z. (2019b). Earth's bow shock: a new three-dimensional asymmetric model with dipole tilt effects. J. Geophys. Res.: Space Phys. , 124 (7), 5396-5407. https://doi.org/10. 1029/2018JA026144
- Merka, J., Szabo, A., Slavin, J. A., and Peredo, M. (2005). Three-dimensional position and shape of the bow shock and their variation with upstream Mach numbers and interplanetary magnetic field orientation. J. Geophys. Res.: Space Phys. , 110 (A4), A04202. https://doi.org/10.1029/2004JA010944
- N ě me č ek, Z., and Šafránková, J. (1991). The Earth's bow shock and magnetopause position as a result of the solar wind-magnetosphere interaction. J. Atmos. Terr. Phys. , 53 (11-12), 1049-1054. https://doi.org/10. 1016/0021-9169(91)90051-8
- Oliveira, D. M., and Raeder, J. (2015). Impact angle control of interplanetary shock geoeffectiveness: a statistical study. J. Geophys. Res.: Space Phys. , 120 (6), 4313-4323. https://doi.org/10.1002/2015JA021147
- Pepino, R., Kharchenko, V., Dalgarno, A., and Lallement, R. (2004). Spectra of the X-ray emission induced in the interaction between the solar wind and the heliospheric gas. Astrophys. J. , 617 (2), 1347-1352. https://doi.org/10.1086/ 425682
- Peredo, M., Slavin, J. A., Mazur, E., and Curtis, S. A. (1995). Three-dimensional position and shape of the bow shock and their variation with Alfvénic, sonic and magnetosonic Mach numbers and interplanetary magnetic field orientation. J. Geophys. Res.: Space Phys. , 100 (A5), 7907-7916. https://doi.org /10.1029/94JA02545
- Petrinec, S. M., and Russell, C. T. (1993). An empirical model of the size and shape of the near-Earth magnetotail. Geophys. Res. Lett. , 20 (23), 2695-2698. https://doi.org/10.1029/93GL02847
- Petrinec, S. M., and Russell, C. T. (1996). Near-Earth magnetotail shape and size as determined from the magnetopause flaring angle. J. Geophys. Res.: Space Phys. , 101 (A1), 137-152. https://doi.org/10.1029/95JA02834
- Qin, J. Q., and Waldrop, L. (2016). Non-thermal hydrogen atoms in the terrestrial upper thermosphere. Nat. Commun. , 7 (1), 13655. https://doi.org/10.1038/ ncomms13655
- Qu, B. H., Lu, J. Y., Wang, M., Yuan, H. Z., Zhou, Y., and Zhang, H. X. (2021). Formation of the bow shock indentation: MHD simulation results. Earth Planet. Phys. , 5 (3), 259-269. https://doi.org/10.26464/epp2021033
- Raeder, J., McPherron, R. L., Frank, L. A., Kokubun, S., Lu, G., Mukai, T., Paterson, W. R., Sigwarth, J. B., Singer, H. J., and Slavin, J. A. (2001). Global simulation of the geospace environment modeling substorm challenge event. J. Geophys. Res.: Space Phys. , 106 (A1), 381-395. https://doi.org/10.1029/ 2000JA000605
- Raeder, J., Larson, D., Li, W. H., Kepko, E. L., and Fuller-Rowell, T. (2008). OpenGGCM simulations for the THEMIS mission. Space Sci. Rev. , 141 (1), 535-555. https://doi.org/10.1007/s11214-008-9421-5
- Robertson, I. P., and Cravens, T. E. (2003). X-ray emission from the terrestrial magnetosheath. Geophys. Res. Lett. , 30 (8), 1439. https://doi.org/10.1029/ 2002GL016740
- Roelof, E. C., and Sibeck, D. G. (1993). Magnetopause shape as a bivariate function of interplanetary magnetic field Bz and solar wind dynamic pressure. J. Geophys. Res.: Space Phys. , 98 (A12), 21421-21450. https://doi.org /10.1029/93JA02362
- Romashets, E. P., and Vandas, M. (2019). Analytic modeling of magnetic field in the magnetosheath and outer magnetosphere. J. Geophys. Res.: Space Phys. ,

124 (4), 2697-2710. https://doi.org/10.1029/2018JA026006

- Samsonov, A., Sembay, S., Read, A., Carter, J. A., Branduardi-Raymont, G., Sibeck, D., and Escoubet, P. (2022). Finding magnetopause standoff distance using a soft X-ray imager: 2. methods to analyze 2-D X-ray images. J. Geophys. Res.: Space Phys. , 127 (12), e2022JA030850. https://doi.org/10.1029/ 2022JA030850
- Samsonov, A. A., Gordeev, E., Tsyganenko, N. A., Šafránková, J., N ě me č ek, Z., Šim ů nek, J., Sibeck, D. G., Tóth, G., Merkin, V. G., and Raeder, J. (2016). Do we know the actual magnetopause position for typical solar wind conditions. . J. Geophys. Res.: Space Phys. , 121 (7), 6493-6508. https://doi.org/10.1002/ 2016JA022471
- Schwadron, N. A., and Cravens, T. E. (2000). Implications of solar wind composition for cometary X-rays. Astrophys. J. , 544 (1), 558-566. https://doi. org/10.1086/317176
- Seiff, A. (1962). Recent information on hypersonic flow fields. In Gas Dynamics in Space Explorations . Washington: NASA.
- Shi, Y., Zesta, E., Connor, H. K., Su, Y. J., Sutton, E. K., Huang, C. Y., Ober, D. M., Christodoulou, C., Delay, S., and Oliveira, D. M. (2017). High-latitude thermosphere neutral density response to solar wind dynamic pressure enhancement. J. Geophys. Res.: Space Phys. , 122 (11), 11559-11578. https:// doi.org/10.1002/2017JA023889
- Shue, J. H., Chao, J. K., Fu, H. C., Russell, C. T., Song, P., Khurana, K. K., and Singer, H. J. (1997). A new functional form to study the solar wind control of the magnetopause size and shape. J. Geophys. Res.: Space Phys. , 102 (A5), 9497-9511. https://doi.org/10.1029/97JA00196
- Shue, J. H., Song, P., Russell, C. T., Steinberg, J. T., Chao, J. K., Zastenker, G., Vaisberg, O. L., Kokubun, S., Singer, H. J., … Kawano, H. (1998). Magnetopause location under extreme solar wind conditions. J. Geophys. Res.: Space Phys. , 103 (A8), 17691-17700. https://doi.org/10.1029/98JA01103
- Sibeck, D. G., Lopez, R. E., and Roelof, E. C. (1991). Solar wind control of the magnetopause shape, location, and motion. J. Geophys. Res.: Space Phys. , 96 (A4), 5489-5495. https://doi.org/10.1029/90JA02464
- Sibeck, D. G., Allen, R., Aryan, H., Bodewits, D., Brandt, P., Branduardi-Raymont, G., Brown, G., Carter, J. A., Collado-Vega, Y. M., … Wing, S. (2018). Imaging plasma density structures in the soft X-rays generated by solar wind charge exchange with neutrals. Space Sci. Rev. , 214 (4), 79. https://doi.org/10.1007/ s11214-018-0504-7
- Sivadas, N., and Sibeck, D. G. (2022). Regression bias in using solar wind measurements. Front. Astron. Space Sci. , 9 , 924976. https://doi.org/10.3389/ fspas.2022.924976
- Soucek, J., and Escoubet, C. P. (2012). Predictive model of magnetosheath plasma flow and its validation against cluster and THEMIS data. Ann. Geophys. , 30 (6), 973-982. https://doi.org/10.5194/angeo-30-973-2012
- Soucek, J., Escoubet, C. P., and Grison, B. (2015). Magnetosheath plasma stability and ULF wave occurrence as a function of location in the magnetosheath and upstream bow shock parameters. J. Geophys. Res.: Space Phys. , 120 (4), 2838-2850. https://doi.org/10.1002/2015JA021087
- Spreiter, J. R., Summers, A. L., and Alksne, A. Y. (1966). Hydromagnetic flow around the magnetosphere. Planet. Space Sci. , 14 (3), 223-253. https://doi. org/10.1016/0032-0633(66)90124-3
- Stahara, S. S. (2002). Adventures in the magnetosheath: two decades of modeling and planetary applications of the Spreiter magnetosheath model. Planet. Space Sci. , 50 (5-6), 421-442. https://doi.org/10.1016/S00320633(02)00023-5
- Sun, T. R., Wang, C., Sembay, S. F., Lopez, R. E., Escoubet, C. P., BranduardiRaymont, G., Zheng, J. H., Yu, X. Z., Guo, X. C., … Guo, Y. H. (2019). Soft X-ray imaging of the magnetosheath and cusps under different solar wind conditions: MHD simulations. J. Geophys. Res.: Space Phys. , 124 (4), 2435-2450. https://doi.org/10.1029/2018JA026093
- Tóth, G., Sokolov, I. V., Gombosi, T. I., Chesney, D. R., Clauer, C. R., De Zeeuw, D. L., Hansen, K. C., Kane, K. J., Manchester, W. B., … Kóta, J. (2005). Space weather modeling framework: a new tool for the space science community. J. Geophys. Res.: Space Phys. , 110 (A12), A12226. https://doi.org/10.1029/ 2005JA011126
- Vandas, M., N ě me č ek, Z., Šafránková, J., Romashets, E. P., and Hajoš, M. (2020). Comparison of observed and modeled magnetic fields in the Earth's

magnetosheath. J. Geophys. Res.: Space Phys. , 125 (3), e2019JA027705. https: //doi.org/10.1029/2019JA027705

- Verigin, M. I., Kotova, G. A., Slavin, J., Szabo, A., Kessel, M., Safrankova, J., Nemecek, Z., Gombosi, T. I., Kabin, K., … Kalinchenko, A. (2001). Analysis of the 3-D shape of the terrestrial bow shock by interball/magion 4 observations. Adv. Space Res. , 28 (6), 857-862. https://doi.org/10.1016/S02731177(01)00502-6

Verigin, M. I., Tátrallyay, M., Erd ő s, G., and Kotova, G. A. (2006). Magnetosheathinterplanetary medium reference frame: application for a statistical study of mirror type waves in the terrestrial plasma environment. Adv. Space Res. , 37 (3), 515-521. https://doi.org/10.1016/j.asr.2005.03.042

- Walsh, B. M., Collier, M. R., Kuntz, K. D., Porter, F. S., Sibeck, D. G., Snowden, S. L., Carter, J. A., Collado-Vega, Y., Connor, H. K., … Thomas, N. E. (2016). Wide field-of-view soft X-ray imaging for solar wind-magnetosphere interactions.

J. Geophys. Res.: Space Phys. , 121 (4), 3353-3361. https://doi.org/10.1002/ 2016JA022348

Wang, M., Lu, J. Y., Kabin, K., Yuan, H. Z., Liu, Z. Q., Zhao, J. S., and Li, G. (2018).

- The influence of IMF By on the bow shock: observation result. J. Geophys. Res.: Space Phys. , 123 (3), 1915-1926. https://doi.org/10.1002/2017JA024750
- Whittaker, I. C., and Sembay, S. (2016). A comparison of empirical and experimental O 7+ , O 8+ , and O/H values, with applications to terrestrial solar wind charge exchange. Geophys. Res. Lett. , 43 (14), 7328-7337. https://doi. org/10.1002/2016GL069914

Zoennchen, J. H., Connor, H. K., Jung, J., Nass, U., and Fahr, H. J. (2022). Terrestrial exospheric dayside H-density profile at 3-15 R E from UVIS/HDAC and TWINS Lymanα data combined. Ann. Geophys. , 40 (3), 271-279. https:// doi.org/10.5194/angeo-40-271-2022