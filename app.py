import streamlit as st
import pandas as pd
import pickle

# Page title
st.set_page_config(page_title="Churn Predictor", layout="wide")
st.title("Customer Churn Prediction System")

# Load model
@st.cache_resource
def load_model():
    with open("best_churn_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()
st.success("Model loaded successfully!")

# Input fields
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", ["No", "Yes"])

with col2:
    tenure = st.slider("Tenure", 0, 72, 12)
    charges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)

# Prediction
if st.button("Predict Churn"):
    data = {
        "gender": gender,
        "SeniorCitizen": 1 if senior == "Yes" else 0,
        "tenure": tenure,
        "MonthlyCharges": charges
    }

    df = pd.DataFrame([data])
    df = pd.get_dummies(df)

    prediction = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1] * 100

    if prediction == 1:
        st.error(f"HIGH RISK: {prob:.1f}% chance of churn")
    else:
        st.success(f"LOW RISK: {100-prob:.1f}% chance of staying")