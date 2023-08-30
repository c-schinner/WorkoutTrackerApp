# Workout Tracker
The Workout Tracker is a Python program designed to help users track their workouts and nutritional information. This application interacts with external APIs to retrieve exercise data and nutritional information and then stores the collected data in a Google Sheets document for tracking and analysis.

# Features
Retrieves exercise data and nutritional information from the Nutritionix API.

Stores workout information, including exercise, duration, and calories burned, in a Google Sheets document using the Sheety API.

Utilizes environment variables to securely store API credentials.

Provides a command-line interface for input and output.

Automates the process of recording workout details for tracking purposes.

# Setup and Usage
1. Make sure you have Python installed on your system.

2. Create a virtual environment (recommended) and install the required packages using the following commands:

        python -m venv venv
        source venv/bin/activate  # For macOS/Linux
        venv\Scripts\activate     # For Windows

        pip install -r requirements.txt

3. Create a .env file in the same directory as your script and add your API credentials as follows:

        AUTH_HEADER=your_authorization_header
        WRKOUT_USERNAME=your_username
        WRKOUT_PASS=your_password
        WRKOUT_APP_ID=your_app_id
        WRKOUT_API_KEY=your_api_key
        NUTRITION_ENDPOINT=https://trackapi.nutritionix.com/v2/natural/exercise

4. Run the script using the following command:

        python workout_tracker.py


5. The script will prompt you to input the exercise you did today.

6. The application will retrieve nutritional information using the Nutritionix API and display the results.

7. The application will then add the exercise, duration, and calories burned to a Google Sheets document using the Sheety API.

# Note
This application is designed for educational purposes and serves as a demonstration of integrating APIs and automating data tracking.

Ensure that you exercise caution when storing sensitive information such as API credentials. Using environment variables and storing them in a .env file is a recommended practice to keep credentials secure.

The provided code does not cover all possible error scenarios and edge cases. In a production environment, you would want to implement proper error handling and validation to ensure the application functions correctly.

# Author
This Workout Tracker application was created by Chris Schinner.

Feel free to modify, enhance, and adapt the application to suit your needs. 

Enjoy tracking your workouts and nutritional data!
