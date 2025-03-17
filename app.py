import streamlit as st
import requests

# FastAPI backend URL
FASTAPI_URL = "http://fastapi:8000/predict/"  # Instead of 127.0.0.1

# Streamlit UI
st.title("📩 SMS Spam Classifier")
st.write("Enter an SMS message below to check if it's Spam or Not Spam.")

# User input text box
sms_text = st.text_area("Enter your SMS message:")

if st.button("Classify SMS"):
    if sms_text.strip():
        # Send request to FastAPI
        response = requests.post(FASTAPI_URL, json={"message": sms_text})
        
        if response.status_code == 200:
            result = response.json()
            prediction = result["prediction"]
            
            # Display the prediction result
            st.success(f"Prediction: {prediction}")
        else:
            st.error("Error: Could not get a response from the server.")
    else:
        st.warning("Please enter a valid SMS message.")
