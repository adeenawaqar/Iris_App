import streamlit as st
import numpy as np

st.title("🌼Iris Species Classifier")

# Input features
sepal_length = st.number_input('Sepal Length', min_value=0.0, value=5.1)
sepal_width  = st.number_input('Sepal Width', min_value=0.0, value=3.5)
petal_length = st.number_input('Petal Length', min_value=0.0, value=1.4)
petal_width  = st.number_input('Petal Width', min_value=0.0, value=0.2)

def classify_iris(sl, sw, pl, pw):
    if pl < 2.5:
        return 'setosa'
    elif pl < 5.0:
        return 'versicolor'
    else:
        return 'virginica'

if st.button('Classify'):
    species = classify_iris(sepal_length, sepal_width, petal_length, petal_width)
    st.success(f"Predicted Species: {species}")

