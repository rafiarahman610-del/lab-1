import streamlit as st
import pandas as pd
import numpy as np
import pickle
st.set_page_config(
    page_title='Customer Churn Predictor',
    layout='wide'
)

st.title('Customer Churn Prediction System')
@st.cache_resource
def load_model():
    with open('best_churn_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()
st.success('Model loaded successfully!')
col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox('Gender', ['Male', 'Female'])
    senior_citizen = st.selectbox('Senior Citizen', ['No', 'Yes'])
with col2:
    tenure = st.slider('Tenure', 0, 72, 12)
    monthly_charges = st.number_input('Monthly Charges', 0.0, 200.0, 70.0)
    if st.button('Predict Churn'):
        input_data = {
    'gender': gender,
    'SeniorCitizen': 1 if senior_citizen == 'Yes' else 0,
    'tenure': tenure,
    'MonthlyCharges': monthly_charges
}

input_df = pd.DataFrame([input_data])
input_encoded = pd.get_dummies(input_df)

prediction = model.predict(input_encoded)[0]
probability = model.predict_proba(input_encoded)[0]

churn_prob = probability[1] * 100
if prediction == 1:
    st.error('HIGH RISK: Customer likely to churn')
    st.metric('Churn Probability', f'{churn_prob:.1f}%')
else:
    st.success('LOW RISK: Customer will stay')
    st.metric('Retention Probability', f'{100-churn_prob:.1f}%')
git init
git add .
git commit -m "churn app"
git push


  

 

    
