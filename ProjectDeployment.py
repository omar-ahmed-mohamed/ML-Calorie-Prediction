import pickle
import streamlit as st 
import pandas as pd


model = pickle.load(open("model.sav","rb"))


st.title('Predict Calorie Expenditure')
st.info('Predict Calorie Expenditure: Easily estimate calories burned based on your activity, duration, and personal stats. Stay on track with your fitness goals!')

st.sidebar.header('Feature Selection')

# Use a radio button for Sex and map to numeric as expected by the model
sex_label = st.radio('Sex', options=['Male', 'Female'], index=0, horizontal=True)
Sex = 1 if sex_label == 'Male' else 0
Age = st.number_input('Age', min_value=0, max_value=100)
Height = st.number_input('Height', min_value=0, max_value=250)
Weight = st.number_input('Weight', min_value=0, max_value=200)
Duration = st.number_input('Duration "(in minutes)"', min_value=0, max_value=1000)
Heart_Rate = st.number_input('Heart_Rate', min_value=0, max_value=200)
Body_Temp = st.number_input('Body_Temp', min_value=0, max_value=50)

df = pd.DataFrame({
    'Sex': [Sex],
    'Age': [Age],
    'Height': [Height],
    'Weight': [Weight],
    'Duration': [Duration],
    'Heart_Rate': [Heart_Rate],
    'Body_Temp': [Body_Temp]
})

conf = st.sidebar.button('Confirm')
st.sidebar.header('Total calories you burned')

if conf:
    result = model.predict(df)
    st.sidebar.success(f"🔥 You burned: {result[0]:.2f} calories")
