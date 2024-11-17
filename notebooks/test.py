# data_exploration.py

import pandas as pd

# Load the dataset
data = pd.read_csv('../data/phishing_site_urls.csv')

# Explore data
print("First 5 rows of the data:")
print(data.head())

print("\nData Information:")
print(data.info())

print("\nData Description:")
print(data.describe())
