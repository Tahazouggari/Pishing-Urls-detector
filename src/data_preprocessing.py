# src/data_preprocessing.py

import pandas as pd
from sklearn.model_selection import train_test_split
def load_and_preprocess_data():
    """
    Loads the dataset, maps the labels, performs URL feature extraction, and splits the data.
    
    Returns:
        X_train, X_test, y_train, y_test: Preprocessed data splits with numeric features.
    """
    # Load the datasets
    data0 = pd.read_csv('data/phishing_site_urls.csv')
    data1 = pd.read_csv('data/new_data_urls.csv')

    # Debug: Check column names
    print("Colonnes dans data0 :", data0.columns.tolist())
    print("Colonnes dans data1 :", data1.columns.tolist())

    # Ensure consistent column names
    if 'url' in data0.columns:
        data0 = data0.rename(columns={'url': 'URL'})
    if 'url' in data1.columns:
        data1 = data1.rename(columns={'url': 'URL'})
    if 'label' in data0.columns:
        data0 = data0.rename(columns={'label': 'Label'})
    if 'label' in data1.columns:
        data1 = data1.rename(columns={'label': 'Label'})

    # Add default labels if missing
    if 'Label' not in data0.columns:
        data0['Label'] = 0
    if 'Label' not in data1.columns:
        data1['Label'] = 0

    # Handle missing values
    data0 = data0.dropna()
    data1 = data1.dropna()
    
    # Map labels: "bad" -> 1 (phishing), "good" -> 0 (legitimate)
    data0['Label'] = data0['Label'].map({'bad': 1, 'good': 0})
    
    # Map labels for data1: ensure they are integers
    data1['Label'] = data1['Label'].astype(str).map({'0': 0, '1': 1})

    # Combine datasets and remove duplicates based on 'URL'
    data = pd.concat([data0, data1], ignore_index=True)
    data = data.drop_duplicates(subset=['URL'])

    # Extract numeric features from URL
    X = extract_url_features(data[['URL']])
    y = data['Label']
    
    # Debug: Print columns retained after feature extraction
    print("Columns retained in X after feature extraction:", X.columns.tolist())

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test
