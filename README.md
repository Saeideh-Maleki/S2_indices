README: Sentinel-2 Indices Calculation Script
Overview
This script processes Sentinel-2 (S2) imagery data to calculate various spectral indices. These indices are used for remote sensing applications and vegetation analysis. The script performs the following tasks:

Loads the Sentinel-2 dataset.
Extracts relevant spectral bands from the dataset.
Calculates several spectral indices, such as NDVI, LSWI, and EVI.
Saves the processed data to a new file.

Requirements
Python 
NumPy
Data

The script expects the input data in a .npz file format with the following structure:

S2: A NumPy array of shape (number of parcels, number of dates, number of bands) representing the Sentinel-2 bands.
y: The target values associated with each parcel.
id_parcels_S2: Identifiers for each parcel.
dates_S2: Dates corresponding to each observation in the dataset.
