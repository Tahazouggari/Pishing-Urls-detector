# main.py

from src.data_preprocessing import load_and_preprocess_data
from src.utils import predict_url
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os

def train_and_evaluate(X_train, X_test, y_train, y_test):
    """
    Trains a RandomForest model, evaluates it, and saves the model.
    
    Args:
        X_train, X_test, y_train, y_test: Training and testing data splits.
    """
    # Initialize the model with balanced class weights
    model = RandomForestClassifier(class_weight='balanced')
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, target_names=['Legitimate', 'Phishing'])
    print("Classification Report:\n", report)

    # Ensure the 'models' directory exists
    os.makedirs('models', exist_ok=True)

    # Save the trained model
    joblib.dump(model, 'models/random_forest_model.pkl')
    print("Model saved successfully!")

def main():
    # Step 1: Load and preprocess data
    print("Loading and preprocessing data...")
    X_train, X_test, y_train, y_test = load_and_preprocess_data()
    print("Data loaded and preprocessed successfully.")

    # Step 2: Train and evaluate the model
    print("Training and evaluating model...")
    train_and_evaluate(X_train, X_test, y_train, y_test)
    print("Model training and evaluation completed.")

    # Step 3: Test a sample URL
    url_to_check = "https://leetcode.com/"
    result = predict_url(url_to_check)
    print(f"The URL '{url_to_check}' is classified as: {result}")

if __name__ == "__main__":
    main()
