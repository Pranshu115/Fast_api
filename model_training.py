# model_training.py
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Paths for dataset and model
DATASET_PATH = "C:/Users/prans/Downloads/Walmart_sales (1).csv"
MODEL_PATH = "walmart_sales_model.pkl"

def train_and_save_model():
    # Load the dataset
    data = pd.read_csv(DATASET_PATH)
    
    # Feature selection
    X = data[['Store', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']]
    y = data['Weekly_Sales']
    
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train a simple Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Save the model to a pickle file
    with open(MODEL_PATH, 'wb') as model_file:
        pickle.dump(model, model_file)
    
    print("Model trained and saved successfully!")

if __name__ == "__main__":
    train_and_save_model()
