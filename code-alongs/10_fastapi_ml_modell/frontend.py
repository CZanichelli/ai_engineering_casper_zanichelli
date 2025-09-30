import streamlit as st
from helpers import read_api_endpoint, post_api_endpoint
import pandas as pd

iris_data = read_api_endpoint(endpoint="/api/")
df = pd.DataFrame(iris_data.json())



        

def layout():
    st.markdown("# Iris Flower Prediction App")
    with st.form("iris_data"):
        sepal_length = st.number_input(
            "Sepal Length (cm)", min_value=4.01, max_value=8.49, value=6.0, step=0.01
        )
        sepal_width = st.number_input(
            "Sepal Width (cm)", min_value=2.0, max_value=4.5, value=3.0, step=0.01
        )
        petal_length = st.number_input(
            "Petal Length (cm)", min_value=4.01, max_value=8.49, value=6.0, step=0.01
        )
        petal_width = st.number_input(
            "Petal Width (cm)", min_value=1.0, max_value=2.5, value=1.5, step=0.01
        )

        submitted = st.form_submit_button("Predict flower")

    if submitted:
        payload = {
            "SepalLengthCm": sepal_length,
            "SepalWidthCm": sepal_width,
            "PetalLengthCm": petal_length,
            "PetalWidthCm": petal_width,
        }
        
        response = post_api_endpoint(payload=payload, endpoint="/api/predict")
        predicted_flower = response.json().get("predicted_flower")

        st.markdown(f"Predicted flower: {predicted_flower}")

    print(f"{sepal_length = }")
    print(f"{submitted = }")

    st.markdown("## Raw data")
    st.dataframe(df)


if __name__ == "__main__":
    layout()
