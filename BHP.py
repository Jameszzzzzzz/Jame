import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib


def load_data():
    return pd.read_csv('500_Person_Gender_Height_Weight_Index.csv')


def save_model(model):
    joblib.dump(model, 'model.joblib')


def load_model():
    return joblib.load('model.joblib')


def BP():
    st.title('💪🏻Body Health Prediction')
    df = pd.read_csv('500_Person_Gender_Height_Weight_Index.csv')
    df.Gender = df.Gender.replace({'Male': int(1)})
    df.Gender = df.Gender.replace({'Female': int(0)})
    X = df[['Gender', 'Height', 'Weight']]
    y = df['Index']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=40)
    model.fit(X_train, y_train)
    save_model(model)

    gender = st.selectbox('Gender🧏🧏‍♀️', ['Male🧏‍', 'Female🧏‍♀️'])
    height = st.number_input('Height❕ (cm)', 60, 250, 170)
    weight = st.number_input('Weight🥓 (kg)', 1, 150, 75)
    gender_num = 1 if gender == 'Male' else 0
    predb = st.button('Predict')
    if predb:
        model = load_model()
        predict = model.predict([[gender_num, height, weight]])
        if predict[0] == 0:
            st.warning('### Your body health is :orange[Extremely Weak🤏]')
        elif predict[0] == 1:
            st.warning('### Your body health is :orange[Weak]😿')
        elif predict[0] == 2:
            st.success('### Your body health is :green[Normal👏]')
        elif predict[0] == 3:
            st.error('### Your body health is :red[Overweight🥲]')
        elif predict[0] == 4:
            st.error('### Your body health is :red[Obesity😢]')
        else:
            st.error('### Your body health is :red[Extremely Obesity😭]')
