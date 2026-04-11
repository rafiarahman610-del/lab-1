# lab 1 - lab 4 Machine Learning Pipleline 
# Course Information

Course: Introduction to Applied Artificial Intelligence
Semester: BS 8th Semester
Project: Customer Churn Prediction
Author: Rafia Rahman
Date: 11-04-2026 

 # Customer Churn Prediction Using Machine Learning

1. Introduction

Customer churn means when customers stop using a company’s service. In the telecom industry, it is important to predict churn so companies can keep their customers.
This project uses machine learning models to predict whether a customer will leave the company or not.

 2. Dataset

The dataset used is the Telco Customer Churn dataset.
It contains information about telecom customers such as:

* Gender
* Tenure (how long the customer stayed)
* Monthly Charges
* Total Charges
* Internet Service
* Online Security
* Tech Support
* Contract type
* Payment Method

The target variable is Churn (Yes or No).

# Repository Structure

  Customer-Churn-Prediction/
│
├── app.py                      # Streamlit web app
├── best_churn_model.pkl        # Trained ML model
├── requirements.txt            # Dependencies
├── README.md                   # Documentation
│
├── week1_eda.ipynb             # Data exploration
├── week2_ml_models.ipynb       # ML models
├── week3_optimization.ipynb    # Model tuning


  # week 1 :Exploratory Data Analysis (EDA)
1.Data cleaning & preprocessing

2.Missing values handling

3.Customer behavior analysis

4.Key churn patterns identified

  # week 2 :Machine Learning Models

1. Logistic Regression

Accuracy: 0.803 (80.3%)

 2. Decision Tree

Accuracy: 0.794 (79.4%)

3. Random Forest
* Predict churn
* Evaluate performance

Accuracy: 0.807 (80.7%)

5. Model Comparison

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 0.803    |
| Decision Tree       | 0.794    |
| Random Forest       | 0.807    |


Key findings:

* Random Forest performed the best with **80.7% accuracy**
* Customer features like "tenure, monthly charges, and services" affect churn
* Machine learning can help telecom companies identify customers likely to leave
  
# Week 3: Model Optimization
  
optimize machine learning models for customer churn prediction by improving accuracy using different techniques

1.Import & Setup Code
2. Data Loading & Preprocessing
3. Baseline Model Code
4. Cross-Validation Code
5. XGBoost Model Code
6.Model Comparison Code

# Week 4: Deployment (Streamlit App)

1.Streamlit is used to deploy machine learning models as web apps easily.
2.It converts a trained ML model into an interactive interface using Python.
3.Users can give input data and get real-time predictions from the model.
4. The trained model (like `.pkl`) is loaded inside app.py for prediction
5. After deployment, the app gets a live link that anyone can use online
