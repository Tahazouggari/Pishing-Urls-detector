# src/utils.py

import pandas as pd
import joblib

def load_model(model_path='models/random_forest_model.pkl'):
    """Loads a trained model from the specified path."""
    return joblib.load(model_path)

def extract_features_from_url(url):
    """
    Extracts features from a single URL for prediction.
    
    Args:
        url (str): The URL to analyze.
    
    Returns:
        pd.DataFrame: A DataFrame containing the extracted features.
    """
    features = {
        'url_length': len(url),
        'num_dots': url.count('.'),
        'has_https': 1 if 'https' in url.lower() else 0,
        'num_special_chars': sum([url.count(c) for c in ['@', '-', '_', '=', '%']]),
        'has_ip_address': 1 if any(part.isdigit() for part in url.split('.')) else 0,
        'num_subdomains': url.count('.') - 1,
        'has_login_keyword': 1 if 'login' in url.lower() else 0,
        'has_secure_keyword': 1 if 'secure' in url.lower() else 0,
        'has_account_keyword': 1 if 'account' in url.lower() else 0,
        'has_verify_keyword': 1 if 'verify' in url.lower() else 0,
        'has_update_keyword': 1 if 'update' in url.lower() else 0
    }
    return pd.DataFrame([features])

def predict_url(url, model_path='models/random_forest_model.pkl'):
    """
    Predicts if a given URL is phishing or legitimate.
    
    Args:
        url (str): The URL to check.
        model_path (str): Path to the saved model.
        
    Returns:
        str: 'Phishing' if URL is phishing, 'Legitimate' otherwise.
    """
    # Load the trained model
    model = load_model(model_path)
    
    # Extract features from the input URL
    url_features = extract_features_from_url(url)
    
    # Make a prediction
    prediction = model.predict(url_features)[0]
    
    # Interpret the result
    return 'Phishing' if prediction == 1 else 'Legitimate'
