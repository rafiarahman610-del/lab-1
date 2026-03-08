# lab-1 & lab 2: EDA + Machine Learning Models
Course Information

Course: Introduction to Applied Artificial Intelligence
Semester: BS 8th Semester
Project: Customer Churn Prediction
Author: Rafia Rahman
Date: 08-03-2026 

 Customer Churn Prediction Using Machine Learning

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

 3. Data Preprocessing

Before training the models, the data was cleaned and prepared.

Steps performed:

1. Load dataset
2. Check missing values
3. Convert `TotalCharges` to numeric values
4. Encode categorical variables using dummy encoding
5. Convert Churn into binary values
    Yes = 1
    No = 0
6. Remove unnecessary columns like customerID
7. Split dataset into:

   * 80% Training data**
   * 20% Testing data**
     
4. Machine Learning Models Used

1. Logistic Regression

Logistic Regression is a classification algorithm used to predict binary outcomes.

Steps:

* Train model using training data
* Predict churn on testing data
* Evaluate accuracy
* Display confusion matrix and classification report

Accuracy: 0.803 (80.3%)

 2. Decision Tree

Decision Tree creates a tree structure where decisions are made based on feature values.

Steps:

* Train decision tree model
* Predict churn
* Calculate accuracy
* Analyze feature importance

Accuracy: 0.794 (79.4%)

3. Random Forest

Random Forest is an ensemble method that combines multiple decision trees to improve prediction.

Steps:

* Train random forest with 100 trees
* Predict churn
* Evaluate performance

Accuracy: 0.807 (80.7%)

5. Model Comparison

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 0.803    |
| Decision Tree       | 0.794    |
| Random Forest       | 0.807    |

The results show that Random Forest achieved the highest accuracy.

 6. Visualization

The project also includes:

* Confusion Matrix to show prediction results
* Feature Importance to identify important factors
* Model Comparison Bar Chart to compare accuracy



7. Feature Engineering

A new feature was created:

TotalRevenue = tenure × MonthlyCharges

This helps the model understand how much revenue each customer generates.

8. Conclusion

In this project, different machine learning models were used to predict customer churn.

Key findings:

* Random Forest performed the best with **80.7% accuracy**
* Customer features like "tenure, monthly charges, and services" affect churn
* Machine learning can help telecom companies identify customers likely to leave

