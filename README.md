* N1 - Dantas_2023 and exoplanets catalogues match.ipynb
  
  Here we tried to crossmatch the catalogue studied in (reference to Dantas_202(3?)) with the exoplanet.eu catalogue. We wanted to check how many host stars in the exoplanet catalogue could be included in the first catalogue, which studied stars under migrating processes. This crossmatch ended in no coincidences between the samples. This is the reason why we started reproducing Dantas_2023 procedure with orbital dynamics calculation, but in this case the sample studied will include the host stars registered in the exoplanet.eu catalogue.
  
* N2 - Matching exoplanets and Gaia Stars (coordinates approach).ipynb
  
  
  This didn't take into account observation ephocs and proper motions, so we changed to a crossmatch based on source identifiers in N3.
  
* N3 - Matching Exoplanets and Gaia Stars (identifiers approach).ipynb
  
  We run here several queries in Gaia to get the parameters we will need for the orbital dynamics step. First, we do a search directly in SIMBAD through identifiers. Exoplanets' host stars are already registered in the exoplanet.eu catalogue, so there is no need to get the risk of some mismatches with coordinates in this case. In fact, there are a lot of different identifiers in this catalogue so we can check all of them and get a match easily. However, in some cases we cannot get a match, so we lose some stars in the sample. The reasons are several, but in general: naming issues.
  
* N4 - Star age cross-match with 2MASS and AIIWise.ipynb

  TOPCAT crossmatch and more Gaia crossmatches...

* N5 - Zero point corrections for parallaxes.ipynb

  ...

* N6 - Bayesian distances.ipynb

  Dantas_2023 R code applied to our sample to get distance estimations.
  ...
  ...

* N6.2 - Bayesian and Gaia distances comparison.ipynb

* N7 - 3D extinction.ipynb

  Dustmaps... Bayestar and Eidenhofer, at first...

* N8 - Unidam ages.ipynb

* N13 - Orbits_HTC_Condor.ipynb

* N13 - Orbits_HTC_Condor.ipynb
  
* catalogue_with_distances.csv:

  This is the whole exoplanet.eu catalogue with some extra columns. These include Gaia parameters brought from the Gaia Archive, magnitudes from 2MASS and AIIWise catalogues, parallax zero-point correction, Bayesian estimations for distances, UNIDAM estimates for ages and stellar orbital dynamics parameters.

  This catalogue will be temporaly 
