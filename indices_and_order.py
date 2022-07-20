import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def insert_all_indices(index_data):

    # Plastic Index (PI)
    index_data['PI'] = index_data['B8']/(index_data['B8']+index_data['B4'])

    # Normalised Difference Water Index (NDWI)
    index_data['NDWI'] = (index_data['B3']-index_data['B8'])/(index_data['B8']+index_data['B3'])

    # Water Ratio Index (WRI)
    index_data['WRI'] = (index_data['B3']+index_data['B4'])/(index_data['B8']+index_data['B12'])

    # Automated Water Extraction Index (AWEI)
    index_data['AWEI'] = 4*(index_data['B3']+index_data['B12'])-(0.25*index_data['B8']+2.75*index_data['B11'])

    # Modified Normalization Difference Water Index (MNDWI)
    index_data['MNDWI'] = (index_data['B3']-index_data['B12'])/(index_data['B4']+index_data['B12'])

    # Simple Ratio (SR)
    index_data['SR'] = index_data['B8']/index_data['B4']

    # Reversed Normalised Difference Vegetation Index (RNDVI)
    index_data['RNDVI'] = (index_data['B4']-index_data['B8'])/(index_data['B4']+index_data['B8'])

    # Anthocyanin Reflectance Index (ARI)
    index_data['ARI'] = (1/index_data['B3'])-(1/index_data['B5'])

    # Modified Anthocyanin Reflectance Index (MARI)
    index_data['MARI'] = ((1/index_data['B3'])-(1/index_data['B5']))*index_data['B7']

    # Chlorophyll Red-Edge (CHL_RedEdge)
    index_data['CHL_RedEdge'] = index_data['B8']/index_data['B5']-1

    # Red Edge Position Index (REPI)
    index_data['REPI'] = 700+40*(((index_data['B4']+index_data['B7'])/2)-index_data['B5'])/(index_data['B6']-index_data['B5'])

    # Enhanced Vegetation Index (EVI)
    index_data['EVI'] = 2.5*(index_data['B8']-index_data['B4'])/(index_data['B8']+6*index_data['B4']-7.5*index_data['B2']+1)

    # Enhanced Vegetation Index 2 (EVI2)
    index_data['EVI2'] = 2.4*(index_data['B8']-index_data['B4'])/(index_data['B8']+index_data['B4']+1)

    # Green Normalised Difference Vegetation Index
    index_data['GNDVI'] = (index_data['B8']-index_data['B3'])/(index_data['B3']+index_data['B8'])

    # Modified Chlorophyll Absorption in Reflectance Index (MCARI)
    index_data['MCARI'] = (index_data['B5']-index_data['B4'])-0.2*(index_data['B5']-index_data['B3'])*(index_data['B5']/index_data['B4'])

    # Moisture Index (MSI)
    index_data['MSI'] = index_data['B11']/index_data['B8']

    # Normalised Difference Moisture Index (NDMI)
    index_data['NDMI'] = (index_data['B8']-index_data['B11'])/(index_data['B8']+index_data['B11'])

    # Normalized Burn Ratio (NBR)
    index_data['NBR'] = (index_data['B8']-index_data['B12'])/(index_data['B8']+index_data['B12'])

    # Normalised Difference Snow Index (NDSI)
    index_data['NDSI'] = (index_data['B3']-index_data['B11'])/(index_data['B3']+index_data['B11'])

    # Soil Adjusted Vegetation Index (SAVI) (L=0.5)
    index_data['SAVI'] = ((index_data['B8']-index_data['B4'])/(index_data['B8']+index_data['B4']+0.5))*(1.5)

    # Oil Spill Index (OSI)
    index_data['OSI'] = (index_data['B3']+index_data['B4'])/(index_data['B2'])

    # Pan Normalised Difference Vegetation Index (PNDVI)
    index_data['PNDVI'] = (index_data['B8']-(index_data['B2']+index_data['B3']+index_data['B4']))/(index_data['B8']+(index_data['B2']+index_data['B3']+index_data['B4']))

    return index_data

path = input("Insert the dataset's path: ")
df = pd.read_csv(path, header=0)

df = insert_all_indices(df)

df = df[['Location', 'Date', 'Sentinel-2', 'Longitude', 'Latitude',
       'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B8A', 'B11', 'B12',
       'NDVI', 'FDI', 'PI', 'NDWI', 'WRI', 'AWEI', 'MNDWI', 'SR',
       'RNDVI', 'ARI', 'MARI', 'CHL_RedEdge', 'REPI', 'EVI', 'EVI2', 'GNDVI',
       'MCARI', 'MSI', 'NDMI', 'NBR', 'NDSI', 'SAVI', 'OSI', 'PNDVI', 'label']]

df = df.sort_values(by=['label'])
df = df.reset_index(drop=True)
df = df.drop(['index', 'level_0'], axis=1, errors='ignore')

df.to_csv(path, index=False)