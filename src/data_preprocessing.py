# src/data_preprocessing.py

import pandas as pd
from sklearn.model_selection import train_test_split

def extract_url_features(data):
    """
    Extracts additional features from the URL column for better phishing detection.
    
    Args:
        data (pd.DataFrame): Original dataset with a 'URL' column.
        
    Returns:
        pd.DataFrame: Dataset with extracted numeric features.
    """
    # URL Length
    data['url_length'] = data['URL'].apply(len)
    
    # Number of dots in the URL
    data['num_dots'] = data['URL'].apply(lambda x: x.count('.'))
    
    # Presence of "https" in the URL (binary feature)
    data['has_https'] = data['URL'].apply(lambda x: 1 if 'https' in x.lower() else 0)

    # Number of special characters in the URL (such as @, -, _, =)
    data['num_special_chars'] = data['URL'].apply(lambda x: sum([x.count(c) for c in ['@', '-', '_', '=', '%']]))
    
    # Check if the URL contains an IP address
    data['has_ip_address'] = data['URL'].apply(lambda x: 1 if any(part.isdigit() for part in x.split('.')) else 0)
    
    # Number of subdomains
    data['num_subdomains'] = data['URL'].apply(lambda x: x.count('.') - 1)
    
    # Presence of keywords often used in phishing URLs
    phishing_keywords = ['login', 'secure', 'account', 'verify', 'update']
    for keyword in phishing_keywords:
        data[f'has_{keyword}_keyword'] = data['URL'].apply(lambda x: 1 if keyword in x.lower() else 0)
    
    # Drop the original URL column after feature extraction
    data = data.drop(columns=['URL'])
    
    return data

def load_and_preprocess_data():
    """
    Loads the dataset, maps the labels, performs URL feature extraction, and splits the data.
    
    Returns:
        X_train, X_test, y_train, y_test: Preprocessed data splits with numeric features.
    """
    # Load the datasets
    data0 = pd.read_csv('data/phishing_site_urls.csv')
    data1 = pd.read_csv('new_data_urls.csv')

    # Ensure consistent column names
    if 'url' in data0.columns:
        data0 = data0.rename(columns={'url': 'URL'})
    if 'url' in data1.columns:
        data1 = data1.rename(columns={'url': 'URL'})

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
