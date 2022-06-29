<p align=center> <img src="https://user-images.githubusercontent.com/106109897/176538014-233c50c4-3c7d-43ea-87f1-e343f96c8a77.jpg"> </p>

# [*Data*] Automatic Detection of Floating Marine Debris Using Multi-Spectral Satellite Imagery
<p align=justify> Plastic pollution represents a major environmental threat to the maritime environment. Floating plastic debris drift autonomously in our oceans 
	endangering ecosystems and marine life. Therefore, there is the need to develop and implement efficient tools to detect, capture and remove floating plastic 
	debris from our oceans.

<p align=justify> Earth observation data have shown early promising results to detect marine plastic debris accumulations (e.g. <b>[1]</b>, <b>[2]</b>). 
	Satellites are a reliable data source thanks to their spatial and temporal resolution, efficiency in covering extensive areas without human interaction 
	and their effectiveness. However, the automatic classification of floating plastic debris from satellite data is not straightforward. Every study highlights 
	the need for more plastic data collected globally, since the best results were achieved by supervised classification methods (highly dependent on the training
	samples).

<p align=justify> The data acquisition process in this work (through the literature, news articles, and social media posts) allowed the collection of the 
	<b>largest data set related to floating plastic debris in satellite (Sentinel-2) imagery that is freely available</b>. Besides floating plastic debris 
	and water data, we collected data from five other classes of floating debris: driftwood, seaweed, pumice, sea snot, and sea foam. Our work proves that 
	plastic is detectable and distinguishable from every class in the data set.

## Table of contents
- [Satellite](#satellite)
- [Data Pre-processing](#data-pre-processing)
- [Data Overview](#data-overview) 
- [Synthetic Data](#synthetic-data)
- [Data Sets](#data-sets)
- [References](#references)
	
## Satellite
<p align=justify> This work uses freely available satellite data products from the Sentinel-2 mission, which comprises a constellation of two identical satellites, 
	Sentinel-2A and Sentinel-2B, developed and operated by the European Space Agency under the Copernicus Programme. It provides <b>systematic coverage</b> (5 days at 
	the equator and 2 to 3 days at mid-latitudes) over all coastal waters up to 20 km from the shore. Each satellite has a multi-spectral instrument aboard that works 
	passively (i.e., it measures the sunlight reflected from the Earth). Its optical data is of <b>high spatial resolution</b> (10 m, 20 m, or 60 m, depending
	on the spectral band). To detect floating plastic, the most crucial feature of the instrument besides the spatial resolution is its <b>radiometric resolution</b>,
	which is the instrument's capacity to distinguish differences in light intensity or reflectance and typically ranges from 8 to 16 bits. The greater the 
	total number of discrete signals that the sensor can record (spectral bands), the greater the radiometric resolution and the more accurate the image is.
	Sentinel-2 has 13 spectral bands that range from the visible and near-infrared (NIR) to the short-wave infrared (SWIR), shown in Table 1, allowing for a 12-bit 
	radiometric resolution and enabling the image to be acquired over a range of 0 to 4095 potential light intensity values. 
	All these features, as well as being used by most studies whose goal is to detect and monitor floating debris, make <b>Sentinel-2 a preferential 
	option for acquiring multi-spectral floating plastic data</b>.
	
<p align=center> <b> Table 1: </b> Sentinel-2 spectral bands, their central wavelengths and spatial resolutions.
<p align=center> <img src="https://user-images.githubusercontent.com/106109897/176535767-ac53970f-eb30-469a-9cd2-f97ca1c0f3b2.PNG" width="650"> </p>
	
## Data Pre-processing
<p align=justify> Unlike UAVs data, where the atmospheric effects are not considered because of the negligible path from the sensor to the observation sensor, 
	satellite images require a correction method to remove the contribution of the atmosphere from the multi-spectral instrument's measurements. 
	To perform the atmospheric correction of the Sentinel-2 images we applied the Dark Spectrum Fitting algorithm (DSF) from the Atmospheric Correction for 
	OLI ’lite’ (<b>ACOLITE</b>) <b>v.20210802.0</b> software <b>[3]</b>. This method assumes that the atmosphere is homogeneous, and that the scene contains pixels 
	with zero or very close to zero surface reflectance in at least one of the sensor bands (i.e., dark pixels). The spectral signature of the dark pixels, 
	or dark spectrum, is then used to determine the best fitting combination of the spectral band and aerosol model for the atmospheric correction. 
	With the most appropriate combination selected, the parameters required for the ”path-corrected” reflectance computation are then chosen from a look-up table. 
	Due to low atmospheric transmittance, band 9 (<b>B9</b>) and band 10 (<b>B10</b>) are excluded from the outputs.
	
## Data Overview
	
	
- **Water**

<p align=justify> Every day, the Sentinel-2 constellation gathers millions of pixels of ocean water. In this work, 150 pixels of ocean water were collected equally
	from two distinct locations: the Caribbean Sea and the Gulf of Gera, in fifteen different days. From the 150 pixels, 121 are from the Sentinel-2A
	and the remaining from the Sentinel-2B. Also, 25% of the water data, corresponding to 30 pixels, are from waters where the bottom of the ocean is
	visible, resulting in brighter pixels. This suggests that different water depths match different spectral reflectance. Waters closer to land usually 
	have shallower depth, so the ocean floor reflects sunlight, in contrast to waters far from the shore, where most of the light is absorbed. 
	Figure 1 confirms the assumption since shallower waters exhibit higher reflectance in all spectral bands. 

<p align=center> <img src="https://user-images.githubusercontent.com/106109897/176547429-0e87e65a-3dc0-42bd-8ed0-70457429c6cb.png" width="550"> </p>
<p align=center> <b> Figure 1: </b> Spectral reflectance (mean - line, and standard deviation - shaded area) of Sentinel-2 water pixels of different depths after atmospheric correction.
	
<p align=justify> Overall, the spectral signatures are identical except in the third band, where shallow depth water reflectance doubles the one from the deep water.
	By comparing these spectral signatures with the ones in <b>[1]</b>, it is safe to assume that the reflectance of shallower waters is not high 
	enough for it to be mistaken for another material, and it is not so different from the deeper waters' reflectance. Therefore, there is no need to
	create two distinct categories and all the data are grouped into a single class (water) with a spectral signature shown in Figure 2.

<p align=center> <img src="https://user-images.githubusercontent.com/106109897/176540867-f9cf8994-1b4b-4062-a9c6-6d6907028b9f.png" width="550"> </p>
<p align=center> <b> Figure 2: </b> Spectral reflectance (mean - line, and standard deviation - shaded area) of all water pixels after atmospheric correction.

- **Plastic**
<p align=justify> Floating plastic debris data are scarce. We gathered 206 pixels of plastic that are confirmed by scientific reports, news articles or pictures on
	social media posts (in situ data). Every pixel's spectral response was manually inspected and compared to the expected spectral signature in the
	literature \cite{thirty,thirty_seven}, and the ones that did not meet the requirements were rejected. Therefore, many pixels identified as suspected
	plastic in scientific reports were discarded. From the 206 pixels, 102 were taken from Sentinel-2A images and 107 from Sentinel-2B imagery.
	Around 42% of the data, corresponding to 88 pixels, are from artificial plastic targets deployed in the ocean in the Gulf of Gera \cite{twenty_seven}, 
	Tsamakia beach \cite{twenty_five,twenty_six}, and Limassol \cite{twenty_eight}. The remaining 58% result from 
	observations and reports of plastic floating in the marine environment. On the 23$^{rd}$ of April 2019, substantial quantities of plastic covered
	the Durban harbour, in South Africa, after a flood event \cite{thirty_eight}. The debris eventually washed out to the sea, and a Sentinel-2 image
	from the following day allowed the detection of 72 pixels with spectral reflectance similar to plastic. The remaining pixels result from the work
	of Kikaki et al. \cite{twenty_nine} and their observations over the Bay Islands and Gulf of Honduras.
	
<p align=center> <img src="https://user-images.githubusercontent.com/106109897/176547565-494e5e0d-adc4-4cc2-9e1d-92d6400a1162.png" width="550"> </p>
<p align=center> <b> Figure 3: </b> Spectral reflectance (mean - line, and standard deviation - shaded area) of plastic pixels after atmospheric correction.
	
- **Driftwood**
	
<p align=center> <img src="https://user-images.githubusercontent.com/106109897/176548225-dc41767e-bc94-4729-98c1-30e23225703d.png" width="550"> </p>
<p align=center> <b> Figure 4: </b> Spectral reflectance (mean - line, and standard deviation - shaded area) of pixels of driftwood after atmospheric correction.
	
- **Seaweed**
	
<p align=center> <img src="https://user-images.githubusercontent.com/106109897/176548273-9c0736bf-9789-4099-8c86-b34f73d35d67.png" width="550"> </p>
<p align=center> <b> Figure 5: </b> Spectral reflectance (mean - line, and standard deviation - shaded area) of pixels of seaweed after atmospheric correction.
	
- **Pumice**
	
<p align=center> <img src="https://user-images.githubusercontent.com/106109897/176548351-9c14f5d6-976d-4bd3-b65a-2633c8397388.png" width="550"> </p>
<p align=center> <b> Figure 6: </b> Spectral reflectance (mean - line, and standard deviation - shaded area) of pixels of pumice and plastic after atmospheric correction.
	
- **Sea Snot**
	
<p align=center> <img src="https://user-images.githubusercontent.com/106109897/176548391-de3c86e2-b49f-46fd-9d4a-98019925baa1.png" width="550"> </p>
<p align=center> <b> Figure 7: </b> Spectral reflectance (mean - line, and standard deviation - shaded area) of pixels of sea snot and plastic after atmospheric correction.
	
- **Sea Foam**
	
<p align=center> <img src="https://user-images.githubusercontent.com/106109897/176548420-cba2b7ce-3aed-475a-941f-9ef46d67bab6.png" width="550"> </p>
<p align=center> <b> Figure 8: </b> Spectral reflectance (mean - line, and standard deviation - shaded area) of pixels of sea foam and plastic after atmospheric correction.
	
### Summary
	
<p align=center> <img src="https://user-images.githubusercontent.com/106109897/176548705-ef6f5da1-1339-466a-9a01-aecb4f4f0106.png" width="650"> </p>
<p align=center> <b> Figure 9: </b> Spectral signatures derived from the mean reflectance of all data after atmospheric correction.
	
## Synthetic Data
	
## Data Sets
	

### References
**[1]** L. Biermann, D. Clewley, V. Martinez-Vicente, and K. Topouzelis, “Finding Plastic Patches in Coastal Waters using Optical Satellite Data,” 
	Scientific Reports, vol. 10, p. 1–10, 2020.
	
**[2]** B. Basu, S. Sannigrahi, A. Sarkar Basu, and F. Pilla, “Development of Novel Classification Algorithms for Detection of Floating Plastic Debris 
	in Coastal Waterbodies Using Multispectral Sentinel-2 Remote Sensing Imagery,” Remote Sensing, vol. 13, no. 8, 2021.
	
**[3]** Quinten Vanhellemont, Kevin Ruddick, "Atmospheric correction of metre-scale optical satellite data for inland and coastal water applications," 
	Remote Sensing of Environment, vol. 216, pp. 586-597, 2018.
	
**[4]** 
	
**[5]** 
	
**[6]** 
	
**[7]** 
	
**[8]** 
	
<p align=right> <i><b>Authors</b>: Miguel M. Duarte and Leonardo Azevedo.</i>
