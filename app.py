import streamlit as st
import pickle
import gdown
import os
import numpy as np

# -----------------------------
# Google Drive Model Download
# -----------------------------
FILE_ID = "PASTE_YOUR_FILE_ID_HERE"
MODEL_PATH = "alzheimer_model.pkl"

if not os.path.exists(MODEL_PATH):
    url = f"https://drive.google.com/uc?id=14zaQHuHJ0lleXvXNRfFSsnHUZfTFbmHk"
    gdown.download(url, MODEL_PATH, quiet=False)

# -----------------------------
# Load Model
# -----------------------------
with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Alzheimer Prediction", layout="centered")

st.title("🧠 Alzheimer Disease Prediction")
st.write("Enter patient details to predict Alzheimer condition.")

# -----------------------------
# Input Fields (EDIT IF NEEDED)
# -----------------------------
age = st.number_input("Age", min_value=1, max_value=120)
gender = st.selectbox("Gender", ["Male", "Female"])
mmse = st.number_input("MMSE Score", min_value=0.0, max_value=30.0)
cdr = st.number_input("CDR Score", min_value=0.0, max_value=3.0)
brain_volume = st.number_input("Brain Volume", min_value=0.0)

# Encode Gender
gender_encoded = 1 if gender == "Male" else 0

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict"):
    input_data = np.array([[age, gender_encoded, mmse, cdr, brain_volume]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("🧠 Alzheimer Detected")
    else:
        st.success("✅ No Alzheimer Detected")
