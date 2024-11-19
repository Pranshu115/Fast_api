import requests
import json

# URL for the API endpoint
url = "http://127.0.0.1:8000/predict"

# Data to send with the POST request
payload = [
    {
        "Store": 1,
        "Holiday_Flag": 0,
        "Temperature": 75.0,
        "Fuel_Price": 2.50,
        "CPI": 211.0,
        "Unemployment": 7.5
    },
    {
        "Store": 2,
        "Holiday_Flag": 1,
        "Temperature": 60.0,
        "Fuel_Price": 2.70,
        "CPI": 220.0,
        "Unemployment": 6.0
    }
]

# Send the POST request to the FastAPI server
response = requests.post(url, json=payload)

# Check the response status and print the response
if response.status_code == 200:
    print("Predictions:", response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)
