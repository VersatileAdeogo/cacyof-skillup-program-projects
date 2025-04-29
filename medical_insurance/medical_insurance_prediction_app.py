# Import the required libraries
import streamlit as st
import pandas as pd
import pickle
import numpy as np

import subprocess
import sys
def install (package):
    subprocess.check_call([sys.executable, "-r", "pip", "install", "scikit-learn"])

# Load the saved model
filename = 'project_medical_insurance_prediction_model.pkl'
loaded_model = pickle.load(open(filename, 'rb'))


# Define the prediction function
def mi_prediction(age, bmi, children, sex_n, smoker_n, region_n):
    X = pd.DataFrame([[age, bmi, children, sex_n, smoker_n, region_n]])
    prediction = loaded_model.predict(X)
    return prediction
    
# Design the app
st.title('CSU Medical Insurance Prediction App')
st.markdown("This project was developed by Babatunde Olayinka")
st.header("Medical Insurance Prediction")
st.markdown("The insurance dataset contains comprises of various variables considered in charging an individual for medical insurance. These variables will be used to predict the price charged for medical insurance.")

# Get data from user
st.header('User Input Features')
age = st.slider("Age of the customer", min_value= 1, max_value= 120, value= 50)
bmi = st.slider("Body mass index of the customer", min_value= 5.00, max_value= 70.00, value= 30.50)
children = st.slider("Number of children the customer has", min_value= 0, max_value= 15, value= 4)
selected_gender = st.selectbox('Gender', list(('Male', 'Female')))
if selected_gender == 'Male':
    sex_n = 1
elif selected_gender == 'Female':
    sex_n = 0
selected_smoker = st.selectbox('Smoker', list(('Yes', 'No')))
if selected_smoker == 'Yes':
    smoker_n = 1
elif selected_smoker == 'No':
    smoker_n = 0
selected_region = st.selectbox('Region', list(('North East', 'North West', 'South East', 'South West')))
if selected_region == 'North East':
    region_n = 0
elif selected_region == 'North West':
    region_n = 1
elif selected_region == 'South East':
    region_n = 2
elif selected_region == 'South West':
    region_n = 3
    
# Creating the button for prediction
st.header('Get Prediction')
if st.button("Medical Insurance Prediction"):
    prediction = mi_prediction(age, bmi, children, sex_n, smoker_n, region_n)
    round_pred = "$" + str(round(prediction[0], 2))
    st.success(round_pred)
    
    
    
