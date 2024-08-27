import streamlit as st
import pandas as pd
st.title("Insurance Premium Predictor")
st.header("By: Prithvi S Krishnan")
st.subheader("This is the best way to learn about your insurance premium costs after a procedure!  ")


st.image('insured.jpg')

from joblib import load
import numpy as np

model = load("model.joblib")

def get_user_input():
    age= st.selectbox('Age', ["Elder(50+)", "Middle(34-49)", "Young(18-33)"])
    bmi= st.slider('Bmi', min_value=10, max_value=50)
    sex= st.select_slider('Slide to select', options=['Male','Female'])
    children= st.slider('children', min_value=0, max_value=7)
    smoker=st.selectbox('Smoker', ['Yes', 'No'])
    region=st.radio('Region:', ['Northeast', 'Northwest','Southeast', 'Southwest']) 
    age_encoded = {"Elder(50+)": 0, "Middle(34-49)": 1, "Young(18-33)": 2}[age]
    sex_encoded = 0 if sex == 'Male' else 1
    smoker_encoded = 1 if smoker == 'Yes' else 0
    region_encoded = {"Northeast": 0, "Northwest": 1, "Southeast": 2, "Southwest": 3}[region]
    
    
    input_features = [age_encoded, bmi, sex_encoded, children, smoker_encoded, region_encoded]
    
    return np.array(input_features).reshape(1, -1)

def make_prediction(model, input) :
    return model.predict(input)

input_features=get_user_input()
prediction = make_prediction(model, input_features)
st.write(f"The insurance premium is: {prediction}")
