# Import the required libraries
import streamlit as st
import pickle
import numpy as np
import pandas as pd

import subprocess
import sys
def install (package):
    subprocess.check_call([sys.executable, "-r", "pip", "install", "sklearn"])

# Load the saved model
filename = 'project_heart_disease_prediction_model.pkl'
loaded_model = pickle.load(open(filename, 'rb'))

def chd_prediction(gender, age, cpd, bpm, ps, ph, tc, sbp, bmi, glu):
    X = pd.DataFrame([[gender, age, cpd, bpm, ps, ph, tc, sbp, bmi, glu]])
    prediction = loaded_model.predict(X)
    return prediction
            
# Design the app
st.title('CSU Heart Disease Prediction App')
st.markdown("This project was developed by Babatunde Olayinka")
st.header("Heart Disease Prediction")
st.markdown("The framinghan dataset contains comprises of health records of various patients. The health record will be used to predict if a patient will have cardiovascular heart disease in Ten Years time.")

# Get data from user
st.header('User Input Features')
selected_gender = st.selectbox('Gender', list(('Male', 'Female')))
if selected_gender == 'Male':
    gender = 1
elif selected_gender == 'Female':
    gender = 0
age = st.slider("Age of the patient", min_value= 1, max_value= 120, value= 50)
cpd = st.slider("Number of cigarettes per day", min_value= 0, max_value= 30, value= 10)
selected_bpm = st.selectbox('Does the patient take blood pressure medications', list(('Yes', 'No')))
if selected_bpm == 'Yes':
    bpm = 1
elif selected_bpm == 'No':
    bpm = 0
selected_ps = st.selectbox('Does the patient have prevalent stroke', list(('Yes', 'No')))
if selected_ps == 'Yes':
    ps = 1
elif selected_ps == 'No':
    ps = 0
selected_ph = st.selectbox('Does the patient have prevalent hypertension', list(('Yes', 'No')))
if selected_ph == 'Yes':
    ph = 1
elif selected_ph == 'No':
    ph = 0
tc = st.slider("Total cholesterol of the patient", min_value= 100.0, max_value= 696.0, value= 120.0)
sbp = st.slider("Systolic blood pressure of the patient", min_value= 40.0, max_value= 300.0, value= 100.0)
bmi = st.slider("Body mass index of the patient", min_value= 5.0, max_value= 60.0, value= 25.5)
glu = st.slider("Glucose level of the patient", min_value= 40.0, max_value= 400.0, value= 45.0)
                      
# Creating the button for prediction
st.header('Get Prediction')
if st.button("Cardiovascular Heart Disease Prediction"):
    prediction = chd_prediction(gender, age, cpd, bpm, ps, ph, tc, sbp, bmi, glu)
    if (prediction[0] == 1):
         st.success('Patient is predicted to have Cardiovascular heart disease in Ten years time')
    elif (prediction[0] == 0):
         st.success('Patient is predicted not to have Cardiovascular heart disease in Ten years time')
    



                                     
