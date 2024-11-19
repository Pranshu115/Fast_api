# prediction.py
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression

MODEL_PATH = "walmart_sales_model.pkl"

# Load the saved model
def load_model():
    with open(MODEL_PATH, "rb") as model_file:
        model = pickle.load(model_file)
    return model

# Function to predict using the loaded model
def predict(input_data):
    model = load_model()
    predictions = model.predict(input_data)
    return predictions
