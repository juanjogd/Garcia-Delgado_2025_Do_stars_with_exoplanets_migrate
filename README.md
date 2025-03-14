* N1 - Malu's and exoplanets catalogues match
  
  Here we tried to crossmatch the catalogue studied in (reference to Dantas_202(3?)) with the exoplanet.eu catalogue. We wanted to check how many host stars in the exoplanet catalogue could be included in the first catalogue, which studied stars under migrating processes. This crossmatch ended in no coincidences between the samples. This is the reason why we started reproducing Dantas_2023 procedure with orbital dynamics calculation, but in this case the sample studied will include the host stars registered in the exoplanet.eu catalogue
  
* N2 - Matching exoplanets and Gaia Stars (coordinates approach)
  
  This didn't take into account observation ephocs, proper motions, etc, so we changed to a crossmatch based on source identifiers
  
* N3 - Matching Exoplanets and Gaia Stars (identifiers approach)
  
  We run here several queries in Gaia to get the parameters we will need for the orbital dynamics step. First, we do a search directly in SIMBAD through identifiers. Exoplanets' host stars are already registered in the exoplanet.eu catalogue, so there is no need to get the risk of some mismatches with coordinates in this case. In fact, there are a lot of different identifiers in this catalogue so we can check all of them and get a match easily. However, in some cases we cannot get a match, so we lose some stars in the sample. The reasons are several, but in general: naming issues.
  
* N4 - Star age cross-match with 2MASS and AIIWise...

  ...
  ...
  ...
  
* catalogue_with_distances.csv:

  This is the whole exoplanet.eu catalogue with some extra columns. These include Gaia parameters brought from the Gaia Archive, magnitudes from 2MASS and AIIWise catalogues, parallax zero-point correction and bayesian estimations for distances.
