# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from prediction import predict  # Import the prediction function

app = FastAPI()

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
def get_predictions(data: list[PredictionRequest]):
    try:
        # Convert input JSON to a pandas DataFrame
        input_df = pd.DataFrame([item.dict() for item in data])
        
        # Make predictions using the imported prediction module
        predictions = predict(input_df)
        
        # Return predictions as a JSON response
        return {"predictions": predictions.tolist()}
    except Exception as e:
        print(f"Error during prediction: {e}")  # Add more detailed logging here
        raise HTTPException(status_code=500, detail=str(e))
