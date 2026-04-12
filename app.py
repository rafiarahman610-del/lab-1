

       
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# Page config
st.set_page_config(page_title="Customer Churn Predictor", layout="wide")

st.title("📊 Customer Churn Prediction System")

# ✅ Load model safely
@st.cache_resource
def load_model():
    if not os.path.exists("model.pkl"):
        st.error("❌ model.pkl file missing hai! Folder check karo.")
        return None
    try:
        with open("model.pkl", "rb") as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f"❌ Model load error: {e}")
        return None

model = load_model()

# ✅ Run only if model loaded
if model:

    st.success("✅ Model successfully loaded!")

    # Layout
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        senior = st.selectbox("Senior Citizen", ["No", "Yes"])

    with col2:
        tenure = st.slider("Tenure (months)", 0, 72, 12)
        monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)

    # ✅ Predict button
    if st.button("🔍 Predict Churn"):

        # Input dictionary
        data = {
            "SeniorCitizen": 1 if senior == "Yes" else 0,
            "tenure": tenure,
            "MonthlyCharges": monthly,
            "gender_Male": 1 if gender == "Male" else 0,
            "gender_Female": 1 if gender == "Female" else 0
        }

        df = pd.DataFrame([data])

        try:
            prediction = model.predict(df)[0]
            prob = model.predict_proba(df)[0][1] * 100

            st.subheader("📈 Result")

            if prediction == 1:
                st.error("🔴 HIGH RISK: Customer will churn")
                st.metric("Churn Probability", f"{prob:.2f}%")
            else:
                st.success("🟢 LOW RISK: Customer will stay")
                st.metric("Retention Probability", f"{100 - prob:.2f}%")

        except Exception as e:
            st.error("❌ Feature mismatch ya model issue hai")
            st.write(e)

else:
    st.warning("⚠️ Model load nahi hua. Pehle model fix karo.")A

  

 

    
