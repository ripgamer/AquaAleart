import firebase_admin
from firebase_admin import credentials, db
import streamlit as st
import pandas as pd
import time

# Initialize Firebase Admin SDK
if not firebase_admin._apps:
    cred = credentials.Certificate("key2.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://careurplant-default-rtdb.firebaseio.com/'
    })

# Function to retrieve data from Firebase and convert it to DataFrame
def get_data_from_firebase():
    try:
        ref = db.reference('/previous_tds_value')  # Reference to the data in your Firebase RTDB
        data = ref.get()
        if isinstance(data, dict):
            # Parse data into lists
            keys = list(data.keys())
            values = [int(value) for value in data.values()]  # Convert values to integers
            # Create DataFrame
            df = pd.DataFrame({"ID": keys, "Value": values})
            return df
        else:
            print("Data retrieved from Firebase is not in expected format.")
            print("Make sure the specified path exists and contains data in JSON format.")
            return None
    except Exception as e:
        print("Error retrieving data from Firebase:", e)
        return None
# Function to retrieve temperature values from Firebase and convert it to DataFrame
def get_temperature_from_firebase():
    try:
        ref = db.reference('/previous_temp_value')  # Reference to the temperature data in your Firebase RTDB
        temperature_data = ref.get()
        if isinstance(temperature_data, dict):
            # Parse data into lists
            keys = list(temperature_data.keys())
            values = [float(value) for value in temperature_data.values()]  # Convert values to integers
            # Create DataFrame
            df = pd.DataFrame({"ID": keys, "Value": values})
            return df
        else:
            print("Temperature data retrieved from Firebase is not in expected format.")
            print("Make sure the specified path exists and contains temperature data in JSON format.")
            return None
    except Exception as e:
        print("Error retrieving temperature data from Firebase:", e)
        return None

# Create a Streamlit app
st.title("AquaAleart - Water Quality Monitoring System")

# Retrieve data from Firebase and display it
firebase_data = get_data_from_firebase()
temperature_data = get_temperature_from_firebase()
if firebase_data is not None:
    st.write("TDS Graph:")
    st.write(firebase_data)
    # Reset index to use sequential indices as x-axis labels
    firebase_data_reset_index = firebase_data.reset_index(drop=True)

    # Display data in a line chart
    st.line_chart(firebase_data.set_index("ID"), use_container_width=True)
# Display section for temperature values
if temperature_data is not None:
    st.header("Temperature Values")
    st.write(temperature_data)
    st.line_chart(temperature_data.set_index("ID"), use_container_width=True)