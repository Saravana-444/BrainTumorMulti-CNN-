import streamlit as st
import pickle
import gdown
import os
import numpy as np

# -----------------------------
# Google Drive file details
# -----------------------------
FILE_ID = "PASTE_YOUR_FILE_ID_HERE"
MODEL_PATH = "model.pkl"

# -----------------------------
# Download model if not exists
# -----------------------------
if not os.path.exists(MODEL_PATH):
    url = f"https://drive.google.com/uc?id=14zaQHuHJ0lleXvXNRfFSsnHUZfTFbmHk"
    gdown.download(url, MODEL_PATH, quiet=False)

# -----------------------------
# Load model
# -----------------------------
with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🏠 House Price Prediction App")

st.write("Enter the details below:")

sqft_living = st.number_input("Square Footage", min_value=100)
bedrooms = st.number_input("Bedrooms", min_value=0)
bathrooms = st.number_input("Bathrooms", min_value=0.0)
yr_built = st.number_input("Year Built", min_value=1800)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Price"):
    input_data = np.array([[sqft_living, bedrooms, bathrooms, yr_built]])
    prediction = model.predict(input_data)
    st.success(f"Predicted House Price: ₹ {prediction[0]:,.2f}")
