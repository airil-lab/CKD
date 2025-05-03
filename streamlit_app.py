import streamlit as st
import joblib
import numpy as np

# Load the trained model (should support predict_proba)
@st.cache_resource
def load_model():
    return joblib.load("best_rf_model.pkl")

model = load_model()

# Function to make predictions and return confidence score
def predict(input_data):
    prediction = model.predict([input_data])[0]
    probability = model.predict_proba([input_data])[0]
    confidence_score = np.max(probability)  # Highest probability
    return prediction, confidence_score

# Streamlit app layout
st.title("🩺 NefroAI: CKD Prediction with Confidence Score")

st.markdown("""
This app predicts the likelihood of **Chronic Kidney Disease (CKD)** based on medical parameters.
Please input the normalized values and click **Predict** to see the result and confidence.
""")

# Input fields (normalized values)
hemo = st.number_input("Hemoglobin", min_value=-3.7158, max_value=1.7990, step=0.01, value=-3.7158)
pcv = st.number_input("Packed Cell Volume / Hematocrit", min_value=-3.9570, max_value=1.7527, step=0.01, value=-3.9570)
rc = st.number_input("Red Cells / RBC Count", min_value=-3.3546, max_value=3.9102, step=0.01, value=-3.3546)
sc = st.number_input("Serum Creatinine", min_value=-0.4402, max_value=14.4017, step=0.03, value=-0.4402)
sg = st.number_input("Specific Gravity of Urine", min_value=-2.5324, max_value=1.2364, step=0.01, value=-2.5324)
bgr = st.number_input("Blood Glucose Random", min_value=-1.7277, max_value=5.0802, step=0.01, value=-1.7277)
al = st.number_input("Albumin", min_value=-0.6726, max_value=2.4108, step=0.01, value=-0.6726)
sod = st.number_input("Sodium - Na⁺", min_value=-15.6624, max_value=2.8997, step=0.05, value=-15.6624)
pot = st.number_input("Potassium - K⁺", min_value=-0.8195, max_value=16.7834, step=0.05, value=-0.8195)
bu = st.number_input("Blood Urea", min_value=-1.1281, max_value=7.4688, step=0.02, value=-1.1281)

# Collect input
input_data = [hemo, pcv, rc, sc, sg, bgr, al, sod, pot, bu]

# Predict button
if st.button("Predict"):
    prediction, confidence = predict(input_data)
    confidence_percent = round(confidence * 100, 2)

    if prediction == 1:
        st.error(f"⚠️ Model predicts **CKD** with **{confidence_percent}%** confidence. Please consult a doctor.")
    else:
        st.success(f"✅ Model predicts **no CKD** with **{confidence_percent}%** confidence. You appear to be safe.")
