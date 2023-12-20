import streamlit as st

st.title("BMI Calculator")


def bmi_calc(height, weight):
    bmi = weight / (height ** 2)
    return bmi

col1,col2= st.columns(2)

with col1:
    height = st.number_input("Height (in m)")
with col2:
    weight  = st.number_input("Weight (in kg)")

submit = st.button("Calculate BMI")
if submit:
    bmi = bmi_calc(height, weight)
    st.write("Your BMI is: ", bmi)
    if bmi < 18.5:
        st.warning("You are Underweight")
    elif bmi >= 18.5 and bmi < 25:
        st.success("You are Healthy")
    elif bmi >= 25 and bmi < 30:
        st.warning("You are Overweight")
    elif bmi >=30:
        st.error("You are Obese")
