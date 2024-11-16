from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Initialize FastAPI app
app = FastAPI()

# Paths for dataset and model
DATASET_PATH = "walmart_sales.csv"  # Update this to your dataset file
MODEL_PATH = "walmart_sales_model.pkl"

# Ensure the model is trained and saved before running the API
def train_and_save_model():
    try:
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
    except Exception as e:
        print(f"Error training model: {e}")
        raise

# Train the model if it doesn't exist
try:
    with open(MODEL_PATH, "rb") as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    print(f"Model not found. Training a new model...")
    train_and_save_model()
    with open(MODEL_PATH, "rb") as model_file:
        model = pickle.load(model_file)

# Define a schema for input data
class PredictionRequest(BaseModel):
    Store: int
    Holiday_Flag: int
    Temperature: float
    Fuel_Price: float
    CPI: float
    Unemployment: float

# Define a POST endpoint for predictions
@app.post("/predict")
def predict(data: list[PredictionRequest]):
    try:
        # Convert input JSON to a pandas DataFrame
        input_df = pd.DataFrame([item.dict() for item in data])
        
        # Debugging: print the input DataFrame
        print(input_df)
        
        # Make predictions using the loaded model
        predictions = model.predict(input_df)
        
        # Return predictions as a JSON response
        return {"predictions": predictions.tolist()}
    except Exception as e:
        print(f"Error during prediction: {e}")  # Add more detailed logging here
        raise HTTPException(status_code=500, detail=str(e))



