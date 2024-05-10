# import streamlit as st
# import firebase_admin
# from firebase_admin import credentials, db
# import time

# # Initialize Firebase Admin SDK
# cred = credentials.Certificate("key.json")  # Replace '/key.json' with your actual key file path (downloaded from Firebase Console
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://aquaalert2-6a2ac-default-rtdb.asia-southeast1.firebasedatabase.app/'
# })

# # Function to fetch real-time data from Firebase
# def fetch_data():
#     ref = db.reference('/your-data-node')  # Replace 'your-data-node' with your actual node path
#     data = ref.get()
#     return data

# # Main function to create the Streamlit app
# def main():
#     st.title('Real-time Data Meter')
    
#     # Get Firebase API keys and other essentials from user
#     firebase_config = st.text_input('Paste your Firebase API keys and other essentials here:')
    
#     # Check if Firebase config is provided
#     if firebase_config:
#         # Connect to Firebase Realtime Database
#         cred = credentials.Certificate(firebase_config)
#         firebase_admin.initialize_app(cred, {
#             'databaseURL': 'https://aquaalert2-6a2ac-default-rtdb.asia-southeast1.firebasedatabase.app/'
#         })
        
#         # Display real-time data meter
#         st.write('Real-time Data Meter:')
#         while True:
#             data = fetch_data()  # Fetch real-time data
#             if data:
#                 # Display data as meter (example)
#                 value = data['value']  # Assuming 'value' is the key for your data
#                 st.write(f'Meter Value: {value}')
#             else:
#                 st.write('No data available')
#             time.sleep(1)  # Update every 1 second

# # Run the app
# if __name__ == '__main__':
#     main()
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import streamlit as st

# Initialize Firebase Admin SDK
cred = credentials.Certificate("key2.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://careurplant-default-rtdb.firebaseio.com/'
})

# Create a Streamlit app
st.title("Real-time Data from Firebase RTDB")

# Function to listen for real-time updates from Firebase
@st.cache(allow_output_mutation=True)
def listen_to_firebase():
    ref = db.reference('/tds_value')  # Reference to the data in your Firebase RTDB
    return ref

ref = listen_to_firebase()

# Function to display real-time updates
def display_realtime_data(ref):
    snapshot = ref.get()
    if snapshot is not None:
        st.write("Real-time data:")
        st.write(snapshot)

# Display real-time updates
while True:
    display_realtime_data(ref)
