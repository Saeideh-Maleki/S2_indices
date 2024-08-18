#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

region = 'Tarbes'
year = 2021

# Load the dataset
dataset = np.load(f'F:/Project/{region}{year}/S2_important.npz', allow_pickle=True)

# Extract the relevant data
y, S2 = dataset["y"], dataset["S2"]
id_parcels_S2, dates_S2 = dataset["id_parcels_S2"], dataset["dates_S2"]

# Extract the bands from S2.
Blue = S2[..., 1]  # B2
Green = S2[..., 2]  # B3
Red = S2[..., 3]  # B4
Rededge1 = S2[..., 4]  # B5
Rededge2 = S2[..., 5]  # B6
Rededge3 = S2[..., 6]  # B7
NIR = S2[..., 7]  # B8
SWIR1 = S2[..., 10]  # B11
SWIR2 = S2[..., 11]  # B12

# Calculate the indices
LSWI = (NIR - SWIR1) / (NIR + SWIR1)
NBR2 = (NIR - SWIR2) / (NIR + SWIR2)
NDRE = (Rededge2 - Rededge1) / (Rededge2 + Rededge1)
RESI = (Rededge3 + Rededge2 - Rededge1) / (Rededge3 + Rededge2 + Rededge1)
NDSVI = (SWIR1 - Red) / (SWIR1 + Red)
MODCRC = (SWIR1 - Green) / (SWIR1 + Green)
CIgreen = (NIR / Green) - 1
CI_red_edge = (NIR / Rededge3) - 1
NDWI = (Green - NIR) / (Green + NIR)
RENDVI = (NIR - Rededge2) / (NIR + Rededge2)
GNDVI = (NIR - Green) / (NIR + Green)
EVI = 2.5 * ((NIR - Red) / ((NIR + 6 * Red - 7.5 * Blue) + 1))
MSAVI = 0.5 * ((2 * NIR + 1) - np.sqrt((2 * NIR + 1) ** 2 - 8 * (NIR - Red)))


# Stack the indices
indices = np.stack((LSWI, NBR2, NDRE, RESI, NDSVI, MODCRC, CIgreen, CI_red_edge, NDWI, RENDVI, GNDVI, EVI, MSAVI), axis=-1)


# Save the cleaned data
np.savez(
    f'F:/Project/{region}{year}/S2_indices',
    S2=S2, y=y, id_parcels_S2=id_parcels_S2, 
    dates_S2=dates_S2, S2_ind=indices
)

print('Finished processing and saving data.')


# In[ ]:




