import streamlit as st


def BI():
    st.title('🧮Bmi calculate✨')
    st.info('''📍 BMI, or Body Mass Index, is a commonly used method for assessing whether a person's weight is in a healthy 
        range for their height. It is calculated by dividing a person's weight in kilograms by the square of their height in meters.💭''')
    height = st.number_input('Height❕(cm)', 60, 250, 170)
    weight = st.number_input('Weight 🥓  (kg)', 1, 150, 75)
    calb = st.button('✧Calculate✧')
    if calb:
        BMI = (weight / (height / 100) ** 2)
        st.markdown(f'## BMI = {BMI:.2f}')