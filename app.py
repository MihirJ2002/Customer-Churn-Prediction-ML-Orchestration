
import joblib
from pathlib import Path

# Importing Necessary Libraries
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# Dashboard Title
st.title("Customer Churn Prediction")
st.subheader("Machine Learning Orchestration Project")

st.write(
    "Predict customer churn using a trained "
    "machine learning model."
)

# Customer Information
tenure = st.number_input(
    "Customer Tenure (Months)",
    min_value=0,
    max_value=100,
    value=24
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=75.0
)

contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

if st.button("Predict Customer Churn"):
    st.info(
        "Interface is working. Model prediction "
        "will be connected in the next step."
    )