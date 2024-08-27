import streamlit as st
import pandas as pd
st.title("Insurance Premium Predictor")
st.header("By: Prithvi S Krishnan")
st.subheader("This is the best way to learn about your insurance premium costs after a procedure!  ")
st.caption("This is an example of how your predicted charges are calculated ")
st.slider('Slide me', min_value=0, max_value=10)
st.latex(r''' 1126*1331=1,500,000 ''')
bar = st.progress(12)
bar.progress(100)
st.radio('Region:', ['North','South', 'East', 'West'])
st.write("THE GRAPH")
df = pd.DataFrame({
    'column 1' : [0,1,2,3,4,5,6],
    'column 2' : [50,100,150,200,250,300,350],
 })
st.line_chart(df)
st.multiselect('Multiselect', [1,2,3])
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")
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
