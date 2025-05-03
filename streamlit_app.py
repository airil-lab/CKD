import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("best_rf_model.pkl")  # Ensure the model file is in the same directory

# Function to make predictions
def predict(input_data):
    prediction = model.predict([input_data])
    return prediction[0]  # Return the single prediction value

# Streamlit app code
st.title("NefroAi: A Real-Time Framework for Predicting Chronic Kidney Disease")

st.markdown("""
This app predicts ckd disease. 
Fill in the fields below and click *Predict*.
""")

# Input fields for user data
hemo = st.number_input("Hemoglobin", min_value=3.1, max_value=17.8, step=1.1, value=10.1)
pcv = st.number_input("Packed Cell Volume / Hematocrit", min_value=9, max_value=54, value=30, step=1)
rc = st.number_input("Red Cells / RBC Count", min_value=2.1, max_value=8, value=6.1, step=1.1)
sc = st.number_input("Serum Creatinine", min_value=0.4, max_value=76, step=1.1, value=35.1)
sg = st.number_input("Specific Gravity of Urine", min_value=1, max_value=1.2, step=0.1, value=1.1)
bgr = st.number_input("Blood Glucose Random", min_value=22, max_value=490, step=1, value=250)
al = st.number_input("Albumin", min_value=0, max_value=5.1, step=0.1, value=2.5)
sod = st.number_input("Sodium - Na⁺", min_value=104, max_value=163, step=1, value=130)
pot = st.number_input("Potassium - K⁺", min_value=2.5, max_value=47, step=1.1, value=30.1)
bu = st.number_input("Blood Urea", min_value=1.5, max_value=391, step=1.1, value=150.1)


# Collect all inputs in a list
input_data = [
    hemo, pcv, rc, sc, sg, bgr, al, sod, pot, bu ]

# Prediction button
if st.button("Predict"):
    prediction = predict(input_data)
    
    # Display the prediction result
    if prediction == 1:
        st.error("Machine predict You May be Chronic Kidney Disease , Please meet doctor soon")
    else:
        st.success("Machine predict, you are safe")
