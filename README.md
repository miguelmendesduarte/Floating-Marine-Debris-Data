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
	literature <b>[1]</b>, <b>[4]</b>, and the ones that did not meet the requirements were rejected. Therefore, many pixels identified as suspected
	plastic in scientific reports were discarded. From the 206 pixels, 102 were taken from Sentinel-2A images and 107 from Sentinel-2B imagery.
	Around 42% of the data, corresponding to 88 pixels, are from artificial plastic targets deployed in the ocean in the Gulf of Gera <b>[5]</b>, 
	Tsamakia beach <b>[6]</b>, <b>[7]</b>, and Limassol <b>[8]</b>. The remaining 58% result from 
	observations and reports of plastic floating in the marine environment. On the 23$^{rd}$ of April 2019, substantial quantities of plastic covered
	the Durban harbour, in South Africa, after a flood event. The debris eventually washed out to the sea, and a Sentinel-2 image
	from the following day allowed the detection of 72 pixels with spectral reflectance similar to plastic. The remaining pixels result from the work
	of Kikaki et al. <b>[9]</b> and their observations over the Bay Islands and Gulf of Honduras.
	
<p align=center> <img src="https://user-images.githubusercontent.com/106109897/176547565-494e5e0d-adc4-4cc2-9e1d-92d6400a1162.png" width="550"> </p>
<p align=center> <b> Figure 3: </b> Spectral reflectance (mean - line, and standard deviation - shaded area) of plastic pixels after atmospheric correction.
	
<p align=justify> The spectral signature of plastic is characterized by two reflectance peaks, one centred at <b>B3</b> and the other at <b>B8</b>, and one absorption peak centred at the fifth Sentinel-2 spectral band (<b>B5</b>). It is also clear that plastic has higher reflectance values in all spectral bands compared to the water spectral signature.
	
- **Driftwood**

<p align=justify> Driftwood is wood that has been washed into the ocean through the action of natural occurrences such as winds or flooding, or because of logging. Its study is of great interest in many research fields. For example, in geomorphology, knowing the accumulation rates of wood in rivers may help in creating measures concerning the maintenance of watercourses and assist in risk management. However, it is challenging to find these pixels in Sentinel-2 images since it is not common to exist significant accumulations of driftwood. 
	
<p align=center> <img src="https://user-images.githubusercontent.com/106109897/176548225-dc41767e-bc94-4729-98c1-30e23225703d.png" width="550"> </p>
<p align=center> <b> Figure 4: </b> Spectral reflectance (mean - line, and standard deviation - shaded area) of pixels of driftwood after atmospheric correction.
	
<p align=justify> PLP 2021 <b>[5]</b> allowed the collection of 62 pixels of driftwood on thirteen different days since they deployed a wooden target that simulates natural driftwood. Around 55% of these pixels were taken from Sentinel-2A images and the remaining from Sentinel-2B. Driftwood shows substantially more reflectance when compared to water or plastic, and it has two reflectance peaks in the fourth (<b>B4</b>) and eighth (<b>B8</b>) Sentinel-2 spectral bands.
	
- **Seaweed**
	
<p align=justify> Seaweed is the common name for countless species of marine plants and algae that grow in the ocean. There are several types of seaweed, but the most prevalent is the Sargassum or brown algae, which floats in large masses and even inspired the name of a region in the Atlantic Ocean, the Sargasso Sea. Its presence in the ocean is essential since it provides nutrients and shelter for many marine organisms, but too much seaweed can be harmful. Substantial accumulations of seaweed may block sunlight, preventing the seagrass below from growing and, when decomposing, its organic matter removes oxygen from the water. This work does not focus on differentiating the distinct species of seaweed, as its goal is to discriminate floating debris, and considerable variations in the various seaweed reflectance are not expected. One Sentinel-2B image from October 2018 was used to collect 150 pixels of seaweed in the coastal waters of Accra, Ghana. The seaweed's spectral signature coincides with the literature <b>[1]</b>, <b>[4]</b> since it presents a sharp increase in reflectance in the fourth Sentinel-2 spectral band (<b>B4</b>), followed by a fall in the band <b>8A</b>, being very distinct from the spectral responses of water, plastic and driftwood. Also, the standard deviation reveals that there is not much dispersion in the data relative to the mean before the reflection peak.
	
<p align=center> <img src="https://user-images.githubusercontent.com/106109897/176548273-9c0736bf-9789-4099-8c86-b34f73d35d67.png" width="550"> </p>
<p align=center> <b> Figure 5: </b> Spectral reflectance (mean - line, and standard deviation - shaded area) of pixels of seaweed after atmospheric correction.
	
<p align=justify> 
	
- **Pumice**
	
<p align=justify> Pumice is a light-coloured volcanic rock with a foamy appearance. It is formed when super-heated and highly pressurized molten rock, magma, is powerfully ejected from a volcano and rapidly cools down, which commonly happens in underwater eruptions. Pumice is so light that it may float on water for years, potentially forming gigantic floating islands (pumice rafts). These pumice rafts are considered a danger to navigation since they can cause damage to cargo vessels and mess up with radar signals. For example, tankers carry thousands of tonnes of oil and, if damaged from a collision, can provoke a massive environmental disaster. Hence, information on the location and course of pumice rafts can be valuable for the shipping industry.
	
<p align=center> <img src="https://user-images.githubusercontent.com/106109897/176548351-9c14f5d6-976d-4bd3-b65a-2633c8397388.png" width="550"> </p>
<p align=center> <b> Figure 6: </b> Spectral reflectance (mean - line, and standard deviation - shaded area) of pixels of pumice and plastic after atmospheric correction.
	
<p align=justify> In October 2021, a large underwater volcanic eruption spewed massive amounts of floating pumice stones that littered coastlines in Okinawa, Japan, damaging dozens of fishing vessels and forcing a large percentage to remain stuck at ports. A Sentinel-2A image from 26 October 2021 reveals thousands of bright pixels containing floating pumice stone and was used to collect 31098 pixels of this floating material. Pumice's reflectance values are close to the plastic mean spectral signature. However, plastic presents an absorption peak in the fifth spectral band (<b>B5</b>), which does not happen with pumice. Pumice's standard deviation reveals a lot of dispersion relative to the mean reflectance, which may be a consequence of different floating depths in different pixels. Pixels where pumice floats on the ocean's surface will have higher reflectance values than ones where pumice is slightly submerged.
	
- **Sea Snot**
	
<p align=justify> Marine mucilage, also known as sea snot, is a thick slimy organic substance that floats on the ocean. It forms when algae are overloaded with nutrients because of global warming and water pollution that results from industrial waste dumped into the seas. Warmer and slower-moving waters also increase the production of sea snot and allow its accumulation. Marine mucilage surge poses severe threats to public health since it contains bacteria, transports diseases, and has adverse economic and environmental consequences. This substance harshly affects the fishing industry as it clogs fishing nets, removes oxygen from the water and limits sunlight from reaching marine ecosystems, killing sea creatures. There are several reports of sea snot outbreaks in the last few years, however, none of them reaches the level of the one in the Marmara Sea, Turkey, in 2021. Short-term countermeasures include laying barriers on the sea surface and collecting the substance. On the other hand, long-term countermeasures comprise improving wastewater treatment and imposing fines on companies that dump industrial waste in the ocean. 
	
<p align=center> <img src="https://user-images.githubusercontent.com/106109897/176548391-de3c86e2-b49f-46fd-9d4a-98019925baa1.png" width="550"> </p>
<p align=center> <b> Figure 7: </b> Spectral reflectance (mean - line, and standard deviation - shaded area) of pixels of sea snot and plastic after atmospheric correction.
	
<p align=justify> One Sentinel-2B image from the Marmara Sea, on the 6$^{th}$ of June 2021, showed thousands of pixels containing sea snot. From those, 26403 pixels were selected. By examining Figure 7, it is clear why Hu et al. <b>[10]</b> concluded that remote differentiation of sea snots and marine debris using multi-band sensors is problematic. The two classes show a similar mean spectral reflectance, except in the eighth Sentinel-2 spectral band (<b>B8</b>), where plastics have a reflectance peak. In contrast to plastic, sea snot's standard deviation reveals a lot of dispersion, which probably results from different floating depths in different pixels, just like pumice.
	
- **Sea Foam**
	
<p align=justify> The model from Biermann et al. <b>[1]</b> showed some difficulties in distinguishing plastic from sea foam, bubbles, and froth, so this group of substances was included in this study. A Sentinel-2A image from Vigo Ria in Galicia, Spain, was used to gather 2735 pixels and study sea foam's spectral behaviour. Sea foam presents a small reflectance peak in the early spectral bands and another one in the eighth Sentinel-2 band (<b>B8</b>), just like the plastic mean spectral signature. These features, adding to the relatively high standard deviation, suggest that sea foam might be confused with plastic.
	
<p align=center> <img src="https://user-images.githubusercontent.com/106109897/176548420-cba2b7ce-3aed-475a-941f-9ef46d67bab6.png" width="550"> </p>
<p align=center> <b> Figure 8: </b> Spectral reflectance (mean - line, and standard deviation - shaded area) of pixels of sea foam and plastic after atmospheric correction.
	
### Summary
	
<p align=justify> With all data gathered from common floating classes such as seaweed, sea foam and driftwood, and from substances that, despite not being so common, can provoke harmful environmental consequences such as sea snot and pumice, it is possible to compare all spectral signatures to plastic. Both driftwood and seaweed have very high reflectance in the eighth Sentinel-2 spectral band, making them distinguishable from all other materials. Driftwood has a reflectance peak where seaweed has an absorption peak, so they are also distinct from each other. As expected, water has lower reflectance than all other classes thanks to its high heat capacity. On the other hand, separating plastic from pumice, sea snot, and sea foam based on spectral responses is challenging. Therefore, using spectral indices, which are mathematical equations that combine values from two or more wavelengths enhancing spectral features that were not visible initially, is appropriate.
	
<p align=center> <img src="https://user-images.githubusercontent.com/106109897/176548705-ef6f5da1-1339-466a-9a01-aecb4f4f0106.png" width="650"> </p>
<p align=center> <b> Figure 9: </b> Spectral signatures derived from the mean reflectance of all data after atmospheric correction.
	
## Synthetic Data

<p align=justify> Despite the efforts in gathering public domain samples of the different floating materials, the number of samples obtained is relatively small for automatic classification algorithms. A usual procedure to overcome this limitation is applying data augmentation methods. Data augmentation methods enable the classification models to learn from a variety of data that could not be gathered in the data acquisition step, making them more robust, and reducing the time-consuming process of collecting and labelling data. In this work, making minor changes in the original data, such as rotating, cropping, zooming or grayscaling is not possible, and slightly changing the values of the spectral bands may create spectral responses that do not represent any floating class. We used of a Wasserstein Generative Adversarial Network (WGAN) <b>[11]</b> to generate <b>1434 synthetic pixels from each class</b> that replicate patterns and features of the actual data, and to assess if artificial data sets are a solution for the lack of floating plastic data.
	
<p align=center> <img src="https://user-images.githubusercontent.com/106109897/176710844-a90f1229-e1ec-4603-90df-31a4fb7fff93.png" width="650"> </p>
<p align=center> <b> Figure 10: </b> Comparison between mean (lines) and standard deviation (shaded areas) of the spectral reflectance values from every class of real pixels and synthetic pixels generated from a WGAN (in red).
	
## Data Sets
<p align=center> Label = 1 (<b>WATER</b>), 2 (<b>PLASTIC</b>), 3 (<b>DRIFTWOOD</b>), 4 (<b>SEAWEED</b>), 5 (<b>PUMICE</b>), 6 (<b>SEA_SNOT</b>), 7 (<b>SEA_FOAM</b>).
	
 > ALL_data.csv
	
	Data set that contains every pixel collected.
	
 > BALANCED_data.csv
	
	Balanced data set that contains pixels from ALL_data.

 > Train_data.csv
	
	Data set used to train the models in the testing phase.
	
 > Test_data.csv
	
	Data set used to test the models in the testing phase.
	
 > balanced_quality_data.csv
	
	1434 synthetic pixels from each class, generated from a WGAN.

### References
<p align=justify> <b>[1]</b> L. Biermann, D. Clewley, V. Martinez-Vicente, and K. Topouzelis, “Finding Plastic Patches in Coastal Waters using Optical Satellite Data,” 
	Scientific Reports, vol. 10, p. 1–10, 2020.
	
<p align=justify> <b>[2]</b> B. Basu, S. Sannigrahi, A. Sarkar Basu, and F. Pilla, “Development of Novel Classification Algorithms for Detection of Floating Plastic Debris in Coastal Waterbodies Using Multispectral Sentinel-2 Remote Sensing Imagery,” Remote Sensing, vol. 13, no. 8, 2021.
	
<p align=justify> <b>[3]</b> Q. Vanhellemont, K. Ruddick, "Atmospheric correction of metre-scale optical satellite data for inland and coastal water applications," 
	Remote Sensing of Environment, vol. 216, pp. 586-597, 2018.
	
<p align=justify> <b>[4]</b> P. Tasseron, T. van Emmerik, J. Peller, L. Schreyers, and L. Biermann, "Advancing Floating Macroplastic Detection from Space Using Experimental Hyperspectral Imagery," Remote Sensing, vol. 13, no. 2335, 2021.

<p align=justify> <b>[5]</b> Marine Remote Sensing Group, "Plastic Litter Project 2021," http://plp.aegean.gr/plastic-litter-project-2021/.
	
<p align=justify> <b>[6]</b> K. Topouzelis, A. Papakonstantinou, and S. P. Garaba, "Detection of floating plastics from satellite and unmanned aerial systems (Plastic Litter Project 2018)," International Journal of Applied Earth Observation and Geoinformation, vol. 79, pp. 175-183, 2019.
	
<p align=justify> <b>[7]</b> K. Topouzelis, D. Papageorgiou, A. Karagaitanakis, A. Papakonstantinou, and M. Arias Ballesteros, "Remote Sensing of Sea Surface Artificial Floating Plastic Targets with Sentinel-2 and Unmanned Aerial Systems (Plastic Litter Project 2019)," Remote Sensing, vol. 12, no. 2013, 2020.
	
<p align=justify> <b>[8]</b> K. Themistocleous, C. Papoutsa, S. Michaelides, and D. Hadjimitsis, "Investigating Detection of Floating Plastic Litter from Space Using Sentinel-2 Imagery," Remote Sensing, vol. 12, no. 2648, 2020.
	
<p align=justify> <b>[9]</b> A. Kikaki, K. Karantzalos, C. A. Power, and D. E. Raitsos, "Remotely Sensing the Source and Transport of Marine Plastic Debris in Bay Islands of Honduras (Caribbean Sea)," Remote Sensing, vol. 12, no. 1727, 2020.
	
<p align=justify> <b>[10]</b> C. Hu, L. Qi, Y. Xie, S. Zhang, and B. B. Barnes, "Spectral characteristics of sea snot reflectance observed from satellites: Implications for remote sensing of marine debris," Remote Sensing of Environment, vol. 269, 2022.
	
<p align=justify> <b>[11]</b> M. Arjovsky, S. Chintala, and L. Bottou, “Wasserstein GAN,” 2017.

<p align=right> <i><b>Authors</b>: Miguel M. Duarte and Leonardo Azevedo.</i>
