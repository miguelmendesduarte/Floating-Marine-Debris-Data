import pandas as pd


def add_indices(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds spectral indices to the dataframe given as input (with spectral bands) and returns the new dataframe.

        Parameters:
            df (pd.DataFrame): A "pandas" dataframe
        
        Returns:
            df (pd.DataFrame): Updated "pandas" dataframe with spectral indices
    """

    # Plastic Index (PI)
    df["PI"] = df["B8"]/(df["B8"]+df["B4"])

    # Normalised Difference Water Index (NDWI)
    df["NDWI"] = (df["B3"]-df["B8"])/(df["B8"]+df["B3"])

    # Water Ratio Index (WRI)
    df["WRI"] = (df["B3"]+df["B4"])/(df["B8"]+df["B12"])

    # Automated Water Extraction Index (AWEI)
    df["AWEI"] = 4*(df["B3"]+df["B12"])-(0.25*df["B8"]+2.75*df["B11"])

    # Modified Normalization Difference Water Index (MNDWI)
    df["MNDWI"] = (df["B3"]-df["B12"])/(df["B4"]+df["B12"])

    # Simple Ratio (SR)
    df["SR"] = df["B8"]/df["B4"]

    # Reversed Normalised Difference Vegetation Index (RNDVI)
    df["RNDVI"] = (df["B4"]-df["B8"])/(df["B4"]+df["B8"])

    # Anthocyanin Reflectance Index (ARI)
    df["ARI"] = (1/df["B3"])-(1/df["B5"])

    # Modified Anthocyanin Reflectance Index (MARI)
    df["MARI"] = ((1/df["B3"])-(1/df["B5"]))*df["B7"]

    # Chlorophyll Red-Edge (CHL_RedEdge)
    df["CHL_RedEdge"] = df["B8"]/df["B5"]-1

    # Red Edge Position Index (REPI)
    df["REPI"] = 700+40*(((df["B4"]+df["B7"])/2)-df["B5"])/(df["B6"]-df["B5"])

    # Enhanced Vegetation Index (EVI)
    df["EVI"] = 2.5*(df["B8"]-df["B4"])/(df["B8"]+6*df["B4"]-7.5*df["B2"]+1)

    # Enhanced Vegetation Index 2 (EVI2)
    df["EVI2"] = 2.4*(df["B8"]-df["B4"])/(df["B8"]+df["B4"]+1)

    # Green Normalised Difference Vegetation Index
    df["GNDVI"] = (df["B8"]-df["B3"])/(df["B3"]+df["B8"])

    # Modified Chlorophyll Absorption in Reflectance Index (MCARI)
    df["MCARI"] = (df["B5"]-df["B4"])-0.2*(df["B5"]-df["B3"])*(df["B5"]/df["B4"])

    # Moisture Index (MSI)
    df["MSI"] = df["B11"]/df["B8"]

    # Normalised Difference Moisture Index (NDMI)
    df["NDMI"] = (df["B8"]-df["B11"])/(df["B8"]+df["B11"])

    # Normalized Burn Ratio (NBR)
    df["NBR"] = (df["B8"]-df["B12"])/(df["B8"]+df["B12"])

    # Normalised Difference Snow Index (NDSI)
    df["NDSI"] = (df["B3"]-df["B11"])/(df["B3"]+df["B11"])

    # Soil Adjusted Vegetation Index (SAVI) (L=0.5)
    df["SAVI"] = ((df["B8"]-df["B4"])/(df["B8"]+df["B4"]+0.5))*(1.5)

    # Oil Spill Index (OSI)
    df["OSI"] = (df["B3"]+df["B4"])/(df["B2"])

    # Pan Normalised Difference Vegetation Index (PNDVI)
    df["PNDVI"] = (df["B8"]-(df["B2"]+df["B3"]+df["B4"]))/(df["B8"]+(df["B2"]+df["B3"]+df["B4"]))

    # Normalised Difference Vegetation Index (NDVI)
    df["NDVI"] = (df["B8"]-df["B4"])/(df["B8"]+df["B4"])

    # Floating Debris Index (FDI)
    if df["Sentinel-2"][0] == "A":
        df["FDI"] = df["B8"]-(df["B6"]+(df["B11"]-df["B6"])*((833-665)/(1610.4-665))*10)
    else:
        df["FDI"] = df["B8"]-(df["B6"]+(df["B11"]-df["B6"])*((832.8-664.6)/(1613.7-664.6))*10)

    return df
