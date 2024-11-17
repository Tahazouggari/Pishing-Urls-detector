# src/model_training.py

import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

def train_and_evaluate(X_train, X_test, y_train, y_test):
    """
    Trains a RandomForest model, evaluates it, and saves the model.
    
    Args:
        X_train, X_test, y_train, y_test: Training and testing data splits.
    """
    # Check and convert data to numpy arrays
    if isinstance(X_train, pd.DataFrame):
        X_train = X_train.values
        X_test = X_test.values
    if isinstance(y_train, pd.Series):
        y_train = y_train.values
        y_test = y_test.values

    print("Training the model...")
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Predictions and evaluation
    print("Evaluating the model...")
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, target_names=['bad', 'good'])
    print("Classification Report:\n", report)

    # Ensure the 'models' directory exists
    os.makedirs('models', exist_ok=True)

    # Save the trained model
    model_path = 'models/random_forest_model.pkl'
    joblib.dump(model, model_path)
    print(f"Model saved successfully at {model_path}!")
