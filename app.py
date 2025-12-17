import streamlit as st
import numpy as np

st.title("Iris Species Classifier")


input_list = st.text_input("Enter 4 numbers (Sepal Length, Sepal Width, Petal Length, Petal Width) , "")

def classify_iris(features):
    sl, sw, pl, pw = features
    # Simple multi-feature rule
    if pl < 2.5 and pw < 1.0:
        return 'setosa'
    elif pl < 5.0 and pw < 1.8:
        return 'versicolor'
    else:
        return 'virginica'

if st.button("Classify"):
    try:

        features = [float(x.strip()) for x in input_list.split(",")]
        if len(features) != 4:
            st.error("Please enter exactly 4 numbers!")
        else:
            species = classify_iris(features)
            st.success(f"Predicted Species: {species}")
    except:
        st.error("Invalid input! Make sure to enter numbers separated by commas.")


