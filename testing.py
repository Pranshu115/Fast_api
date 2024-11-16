import requests

# Define the store numbers dynamically
store_numbers = [1, 2, 3, 4]  # You can change this list anytime

# Function to create the payload based on store numbers
def create_payload(store_numbers):
    payload = []
    for store in store_numbers:
        # Create a request payload for each store
        payload.append({
            "Store": store,
            "Holiday_Flag": 0,  # Set any values you want
            "Temperature": 75.0,  # Example value
            "Fuel_Price": 2.50,   # Example value
            "CPI": 211.0,         # Example value
            "Unemployment": 7.5   # Example value
        })
    return payload

# Create the payload dynamically based on store numbers
payload = create_payload(store_numbers)

# Make the API request
url = "http://127.0.0.1:8000/predict"
response = requests.post(url, json=payload)

# Print the response (predictions)
print(response.json())



