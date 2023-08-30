import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv


load_dotenv()

# Go to Sheety and sign in to locate our exel sheet!

# These are the requirements to access my sheets documentation
AUTHORIZATION_HEADER = os.getenv("AUTH_HEADER")
USERNAME = os.getenv("WRKOUT_USERNAME")
PASSWORD = os.getenv("WRKOUT_PASS")
basic = HTTPBasicAuth(username=USERNAME, password=PASSWORD)

# These are for the Nutritionix requests, to get the correct data online
APP_ID = os.getenv("WRKOUT_APP_ID")
API_KEY = os.getenv("WRKOUT_API_KEY")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

nutrition_data = {
    "query": input("What exercise did you do today? "),
    "gender": "male",
    "weight_kg": 81.6,
    "height_cm": 180.34,
    "age": 36
}

nutrition_endpoint = os.getenv("NUTRITION_ENDPOINT")

# This is my request to get my workout and calories, from my API request it will return the info in json format
response = requests.post(url=nutrition_endpoint, json=nutrition_data, headers=headers)
results = response.json()
print(results)


# These lines of code are pulling the information from my API request above, and using the data received,
# to fill out my Google Docs spreadsheet with the correct information
today = datetime.now()

workout_endpoint = "https://api.sheety.co/7ed92b0ff16619ab76ca93a2eef2b032/copyOfMyWorkouts/workouts"

workout_parameters = {
    "workout": {
        "date": today.strftime("%m/%d/%Y"),
        "time": today.strftime("%X"),
        "exercise": results["exercises"][0]["user_input"].title(),
        "duration": results["exercises"][0]["duration_min"],
        "calories": results["exercises"][0]["nf_calories"],
    }
}

workout_response = requests.post(url=workout_endpoint, json=workout_parameters, auth=basic)
workout_results = workout_response.json()
