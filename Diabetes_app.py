# -*- coding: utf-8 -*-
"""
Created on Mon May  6 09:27:17 2024

@author: HP
"""

import pickle
import streamlit as st
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import base64



def set_background(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover;
         }}
         .st-emotion-cache-15ndg0s{{
             background: None}}
         </style>
         """,
         unsafe_allow_html=True
     )

set_background('health.jpg') 


# Loading the saved models

diabetes_model = pickle.load(open('diabetes_project.pkl', 'rb'))


    
# page title
st.title('Diabetes Prediction App')



age = st.number_input('Age : ', step = 1, value = None, placeholder = "Input your age")

if age:
    
    if age > 18 and age <= 40:
    
        age_group_young = 1
    
    else:
    
        age_group_young = 0
    
    if age > 60:
    
        age_group_senior = 1
    
    else:
    
        age_group_senior = 0
        
    if age > 40 and age <= 60:
        
        age_group_middle_aged = 1
        
    else:
        
        age_group_middle_aged = 0

hypertension = st.selectbox('Hypertension', ['Yes', 'No'])

if hypertension == 'Yes':
    
    hypertension = 1
    
else:
    hypertension = 0
    
heart_disease = st.selectbox('Heart disease', ['Yes', 'No'])

if heart_disease == 'Yes':
    
    heart_disease = 1
    
else:
    heart_disease = 0
    
bmi = st.number_input('Body Mass Index : ', step = 0.1, value = None, placeholder = "Input your Body Mass Index")

if bmi:

    if bmi > 18 and bmi <= 25:
        
        bmi_category_healthy = 1
        
    else:
        
        bmi_category_healthy = 0
        
    if bmi > 25 and bmi <= 30:
        
        bmi_category_over_weight = 1
        
    else:
        
        bmi_category_over_weight = 0
        
    if bmi > 30.0:
        
        bmi_category_obese = 1
        
    else:
        
        bmi_category_obese = 0
    
HbA1c_level = st.number_input('HbA1c Level : ', step = 0.1,value = None, placeholder = "Input your current Glycated Haemoglobin level or HbA1c level")

blood_glucose_level = st.number_input('Blood Glucose Level : ', step = 1, value = None, placeholder = "Input your Blood Glucose Level")

if blood_glucose_level:
    
    if blood_glucose_level > 70 and blood_glucose_level <= 140:
    
        glucose_category_normal = 1
    
    else:
    
        glucose_category_normal = 0
        
    if blood_glucose_level > 140 and blood_glucose_level < 200:
        
        glucose_category_high = 1
    
    else:
    
        glucose_category_high = 0
    
    if blood_glucose_level > 200:
    
        glucose_category_risky = 1
        
    else:
        
        glucose_category_risky = 0
        
smoke = st.selectbox('Are you a Smoker ? : ', ['Current', 'Ever', 'Not Current', 'Former', 'No'])


if smoke.lower() == 'no':
    
    smoking_history_never = 1
    
else:
    
    smoking_history_never = 0
    
if smoke.lower() == 'current':
    
    smoking_history_current = 1
    
else:
    
    smoking_history_current = 0
    
if smoke.lower() == 'ever':
    
    smoking_history_ever = 1
    
else:
    
    smoking_history_ever = 0
    
if smoke.lower() == 'not current':
    
    smoking_history_not_current = 1
    
else:
    
    smoking_history_not_current = 0
    
if smoke.lower() == 'former':
    
    smoking_history_former = 1
    
else:
    
    smoking_history_former = 0

gender = st.selectbox('Gender', ['Male', 'Female', 'Choose not to disclose'])

if gender == 'Male':
    gender_Male = 1
else:
    gender_Male = 0

if gender == 'Choose not to disclose':
    gender_Other = 1
else:
    gender_Other = 0

    
diab_diagnosis = ''

if st.button('Diabetes Test Result : '):
    
    try:
    
        labels = [age, hypertension, heart_disease, bmi, HbA1c_level,
                  
           blood_glucose_level, age_group_young, age_group_middle_aged,
           
           age_group_senior, glucose_category_normal, glucose_category_high,
           
           glucose_category_risky, bmi_category_healthy,
           
           bmi_category_over_weight, bmi_category_obese,
           
           smoking_history_current, smoking_history_ever,
           
           smoking_history_former, smoking_history_never,
           
           smoking_history_not_current, gender_Male, gender_Other]
        
        diab_prediction = diabetes_model.predict(pd.DataFrame(labels).T)
    
    except NameError:
        
        st.error('Missing or Null Inputs')
        
        st.stop()
    
    if diab_prediction == 1:
        
        diagnosis = 'This patient has a high risk of diabetes. Please visit a doctor today'
    
        st.error('**Diagnosis : :red[{}]**'.format(diagnosis), icon='🚨')
        
        
    else:
        diagnosis = 'This patient has a low risk of diabetes'
        
        st.success('**Diagnosis: :green[{}]**'.format(diagnosis), icon='✅')
        
        
    
    
