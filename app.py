
import streamlit as st
import pandas as pd
import pickle
import os

st.title("Customer Churn Prediction")

# ✅ Load model safely
def load_model():
    try:
        if not os.path.exists("model.pkl"):
            st.error("model.pkl file nahi mili ❌")
            return None

        with open("model.pkl", "rb") as f:
            model = pickle.load(f)
        return model

    except Exception as e:
        st.error("Model load error ❌")
        st.write(e)
        return None

model = load_model()

# Stop if model not loaded
if model is None:
    st.stop()

st.success("Model loaded successfully ✅")

# ✅ Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", ["No", "Yes"])
tenure = st.slider("Tenure", 0, 72, 12)
monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)

# ✅ Predict
if st.button("Predict"):

    # 🔥 SAME FORMAT as model expected
    data = {
        "gender_Male": 1 if gender == "Male" else 0,
        "SeniorCitizen": 1 if senior == "Yes" else 0,
        "tenure": tenure,
        "MonthlyCharges": monthly
    }

    df = pd.DataFrame([data])

    try:
        pred = model.predict(df)[0]
        prob = model.predict_proba(df)[0][1] * 100

        if pred == 1:
            st.error(f"🔴 High Risk: Customer will churn ({prob:.1f}%)")
        else:
            st.success(f"🟢 Low Risk: Customer will stay ({100 - prob:.1f}%)")

    except Exception as e:
        st.error("❌ Feature mismatch ya model issue")
        st.write(e)

 

    
