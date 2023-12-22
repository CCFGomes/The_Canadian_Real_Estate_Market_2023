# Data Preparation
# Load required libraries

import numpy as np # data arrays
import pandas as pd # data analysis and data manipulation
import datetime as dt #date time
import glob #retrieving file paths
import os #to perform operations related to file and directory handling
import seaborn as sns  # Importing seaborn library for statistical data visualization
import matplotlib.pyplot as plt  # Importing matplotlib.pyplot for creating static visualizations
import matplotlib.ticker as ticker # To support user customized ticking

# List all files under the input directory
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Specify the directories for the two sets of data
provinces_directory = '/kaggle/input/canadian-re-data-ab-bc-sk-on-qc-and-national'
popular_cities_directory = '/kaggle/input/most-popular-cities-in-canada/'

# Create an empty dictionary to store DataFrames for central and prairies
provinces_dfs = {}

# Loop through the CSV files in the central and prairies directory
for dirname, _, filenames in os.walk(provinces_directory):
    for filename in filenames:
        # Create a key for the dictionary using the filename without extension
        key = os.path.splitext(filename)[0].lower()
        # Read the CSV file and store it in the dictionary
        provinces_dfs[key] = pd.read_csv(os.path.join(dirname, filename))

# Create an empty dictionary to store DataFrames for popular cities
popular_cities_dfs = {}

# Loop through the CSV files in the popular cities directory
for dirname, _, filenames in os.walk(popular_cities_directory):
    for filename in filenames:
        # Create a key for the dictionary using the filename without extension
        key = os.path.splitext(filename)[0].lower()
        # Read the CSV file and store it in the dictionary
        popular_cities_dfs[key] = pd.read_csv(os.path.join(dirname, filename))

# Print the keys from your dictionary
print(popular_cities_dfs.keys())
print(provinces_dfs.keys())
# Assign the corresponding DataFrames to their variables

yyz = popular_cities_dfs['toronto']
yyc = popular_cities_dfs['calgary']
yvr = popular_cities_dfs['vancouver'] 
yxe = popular_cities_dfs['saskatoon']
yul = popular_cities_dfs['montreal']
yqb = popular_cities_dfs['quebec']
yeg = popular_cities_dfs['edmonton']
yow = popular_cities_dfs['ottawa']
ywg = popular_cities_dfs['winnipeg']

AB = provinces_dfs['alberta']
SK = provinces_dfs['saskatchewan']
QC = provinces_dfs['quebec']
BC = provinces_dfs['british_columbia']
ON = provinces_dfs['ontario']
CAN = provinces_dfs['aggregate']

# Checking for missing values
for key, df in popular_cities_dfs.items():
    print(f"Missing values in {key}:")
    print(df.isnull().sum())
    print("\n")
for key, df in provinces_dfs.items():
    print(f"Missing values in {key}:")
    print(df.isnull().sum())
    print("\n")

# Checking for duplicates
for key, df in popular_cities_dfs.items():
    print(f"Duplicate values in {key}:")
    print(df.duplicated().any())
    print("\n")
for key, df in provinces_dfs.items():
    print(f"Duplicate values in {key}:")
    print(df.duplicated().any())
    print("\n")

# Creating new column 'City' with the respective city names on each data frame
yyz['City'] = 'Toronto'
yyc['City'] = 'Calgary'
yvr['City'] = 'Vancouver'
yxe['City'] = 'Saskatoon'
yul['City'] = 'Montreal'
yqb['City'] = 'Quebec'
yeg['City'] = 'Edmonton'
yow['City'] = 'Ottawa'
ywg['City'] = 'Winnipeg'

# Creating new column 'Province' with the respective Province names on each data frame
AB['Province'] = 'Alberta'
SK['Province'] = 'Saskatchewan'
QC['Province'] = 'Quebec'
BC['Province'] = 'British Columbia'
ON['Province'] = 'Ontario'
CAN['Province'] = 'Canada'
