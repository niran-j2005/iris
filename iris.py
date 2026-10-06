import numpy as np
import pandas as pd
import streamlit as st
import pickle
import sklearn

model=pickle.load(open('iris_model.pk1', 'rb'))

st.title("Iris Flower Prediction")

sepal_length = st.slider("Sepal Length", 0.0, 10.0, 5.0)
sepal_width = st.slider("Sepal Width", 0.0, 10.0, 3.0)
petal_length = st.slider("Petal Length", 0.0, 10.0, 1.0)    
petal_width = st.slider("Petal Width", 0.0, 10.0, 0.2)

predict=st.button("Predict species")

if predict:
    input_data = np.array([[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]])

    prediction = model.predict(input_data)

    species = ["Setosa", "Versicolor", "Virginica"]

    st.success(f"Predicted species: {species[prediction[0]]}")