import streamlit as st
from helpers import read_api_endpoint, post_api_endpoint
import pandas as pd

iris_data = read_api_endpoint(endpoint="/api/")
df = pd.DataFrame(iris_data.json())


def layout():
    st.markdown("# Iris Flower Prediction App")
    with st.form("iris_data"):
        sepal_length = st.number_input(
            "Sepal Length (cm)", min_value=4.01, max_value=8.49, value=8.49
        )

        submitted = st.form_submit_button("Predict flower")

    print(f"{sepal_length = }")
    print(f"{submitted = }")

    st.markdown("## Raw data")
    st.dataframe(df)


if __name__ == "__main__":
    layout()
