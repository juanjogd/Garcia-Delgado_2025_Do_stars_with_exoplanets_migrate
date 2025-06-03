* N1 - Dantas_2023 and exoplanets catalogues match.ipynb
  
  Crossmatch between the catalogue studied in (reference to Dantas_202(3?)) and the exoplanet.eu catalogue. We wanted to check how many host stars in the exoplanet catalogue could be included in the first catalogue, which studied stars under migrating processes. This crossmatch ended in no coincidences between the samples. This is the reason why we started reproducing Dantas_2023 procedure with orbital dynamics calculation, but in this case the sample studied will include the host stars registered in the exoplanet.eu catalogue.
  
* N2 - Matching exoplanets and Gaia Stars (coordinates approach).ipynb
  
  Crossmatch between the exoplanet.eu catalogue and Gaia DR3, based on coordinates. Proper motions not added, considering close ephocs.
  
* N3 - Matching Exoplanets and Gaia Stars (identifiers approach).ipynb

  Crossmatch between the exoplanet.eu catalogue and Gaia DR3, but with source identifiers. We run here several queries in Gaia to get the parameters we will need for the orbital dynamics step. First, we do a search directly in SIMBAD through identifiers. Some exoplanets' host stars are already registered in the exoplanet.eu catalogue.
  
* N4 - Star age cross-match with 2MASS and AIIWise.ipynb

  TOPCAT crossmatch and more Gaia crossmatches aiming to get more parameters (this could have been done more efficiently with just 1 crossmatch, but during the project some new needs arised)

* N5 - Zero point corrections for parallaxes.ipynb

  ...

* N6 - Bayesian distances.ipynb

  Dantas_2023 R code adapted and applied to our sample to get distance estimations.

* N6.2 - Bayesian and Gaia distances comparison.ipynb

  ...

* N7 - 3D extinction.ipynb

  Computing 3D extinctions with dustmaps (Bayestar and Edenhofer)

* N8 - Unidam ages.ipynb

  ...

* N13 - Orbits_HTC_Condor.ipynb

  Integration of the orbits using GALPY

* N13_2 - Orbits_HTC_Condor.py

  Similar code than N13 ipynb, but implemented in HTC cluster.
  
* garcia_delgado_catalogue.csv:

  This is the whole exoplanet.eu catalogue with some extra columns. These include Gaia parameters brought from the Gaia Archive, magnitudes from 2MASS and AIIWise catalogues, parallax zero-point correction, Bayesian estimations for distances, UNIDAM estimates for ages and stellar orbital dynamics parameters.

  This catalogue will be temporaly unavailable until the results are published
