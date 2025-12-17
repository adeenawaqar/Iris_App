# iris_streamlit_multi_feature_examples.py
import streamlit as st
import pandas as pd

st.title("🌼 Iris Species Classifier (Multi-feature)")

# Input features using number_input
sepal_length = st.number_input('Sepal Length (cm)', min_value=0.0, value=5.1)
sepal_width  = st.number_input('Sepal Width (cm)', min_value=0.0, value=3.5)
petal_length = st.number_input('Petal Length (cm)', min_value=0.0, value=1.4)
petal_width  = st.number_input('Petal Width (cm)', min_value=0.0, value=0.2)

# Multi-feature rule-based classification
def classify_iris(sl, sw, pl, pw):
    if pl < 2.5 and pw < 1.0:
        return 'setosa'
    elif pl < 5.0 and pw < 1.8:
        return 'versicolor'
    else:
        return 'virginica'

# Classify button
if st.button('Classify'):
    species = classify_iris(sepal_length, sepal_width, petal_length, petal_width)
    st.success(f"Predicted Species: {species}")

# Example table
st.subheader("🌸 Example Feature Values and Predicted Species")

data = {
    "Sepal Length": [4.3, 4.8, 5.1, 5.5, 6.0, 6.7, 7.0],
    "Sepal Width":  [2.0, 2.5, 3.0, 3.2, 3.5, 3.8, 4.0],
    "Petal Length": [0.1, 0.5, 1.0, 1.4, 2.0, 4.5, 5.0, 6.0, 6.9],
    "Petal Width":  [0.1, 0.2, 0.4, 0.6, 1.0, 1.5, 2.0, 2.5]
}

# Create all combinations of features
import itertools
combinations = list(itertools.product(data["Sepal Length"], data["Sepal Width"],
                                      data["Petal Length"], data["Petal Width"]))

# Build table with predicted species
table = []
for sl, sw, pl, pw in combinations:
    species = classify_iris(sl, sw, pl, pw)
    table.append([sl, sw, pl, pw, species])

df = pd.DataFrame(table, columns=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Predicted Species"])

# Show first 20 rows for example
st.dataframe(df.head(20))
st.write("✅ Table shows first 20 combinations. Full table has all feature combinations.")
