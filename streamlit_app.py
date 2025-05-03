import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("best_rf_model.pkl")  # Ensure this file is in the same directory

# Function to make predictions
def predict(input_data):
    prediction = model.predict([input_data])
    probability = model.predict_proba([input_data])  # Optional: probability estimate
    return prediction[0], probability[0][1]  # Return label and probability of CKD

# Streamlit app code
st.set_page_config(page_title="NefroAi: CKD Predictor", layout="centered")
st.title("🩺 NefroAi: A Real-Time Framework for Predicting Chronic Kidney Disease")

st.markdown("""
Welcome to **NefroAi**, an intelligent system to help predict the risk of **Chronic Kidney Disease (CKD)** using clinical values.  
Please fill in your health parameters and click **Predict** to see the results.
""")

# Use columns for better layout
col1, col2 = st.columns(2)

with col1:
    hemo = st.number_input("Hemoglobin (g/dL)", min_value=3.1, max_value=17.8, step=0.1, value=10.1)
    pcv = st.number_input("Packed Cell Volume (%)", min_value=9, max_value=54, step=1, value=30)
    rc = st.number_input("Red Blood Cell Count (million cells/uL)", min_value=2.0, max_value=8.0, step=0.1, value=4.5)
    sc = st.number_input("Serum Creatinine (mg/dL)", min_value=0.4, max_value=76.1, step=0.1, value=1.2)
    sg = st.number_input("Urine Specific Gravity", min_value=1.005, max_value=1.025, step=0.005, value=1.015)

with col2:
    bgr = st.number_input("Blood Glucose Random (mg/dL)", min_value=22, max_value=490, step=1, value=110)
    al = st.number_input("Albumin (g/dL)", min_value=0.0, max_value=5.0, step=0.1, value=2.5)
    sod = st.number_input("Sodium - Na⁺ (mEq/L)", min_value=104, max_value=163, step=1, value=135)
    pot = st.number_input("Potassium - K⁺ (mEq/L)", min_value=2.5, max_value=7.0, step=0.1, value=4.5)
    bu = st.number_input("Blood Urea (mg/dL)", min_value=1.5, max_value=391.1, step=1.0, value=45.0)

# Collect all inputs
input_data = [hemo, pcv, rc, sc, sg, bgr, al, sod, pot, bu]

# Predict button
if st.button("🔍 Predict"):
    prediction, probability = predict(input_data)

    if prediction == 1:
        st.error("⚠️ You may have Chronic Kidney Disease. Please consult a healthcare provider.")
        st.write(f"Model Confidence: **{probability * 100:.2f}%** chance of CKD.")
    else:
        st.success("✅ You are safe from CKD based on the current data.")
        st.write(f"Model Confidence: **{(1 - probability) * 100:.2f}%** chance of being healthy.")
