import streamlit as st
import pandas as pd
import numpy as np

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Credit Card Default Predictor",
    layout="centered"
)

# -----------------------------
# Title & Description
# -----------------------------
st.title("💳 Credit Card Default Prediction")
st.subheader("Machine Learning based Risk Classification")

st.write(
    """
    This application demonstrates a **credit card default prediction model**
    built using **Logistic Regression** and **Classification Tree** techniques.
    
    The final model focuses on **interpretability, stability, and business usability**
    for proactive credit risk management.
    """
)

# -----------------------------
# Business Problem
# -----------------------------
st.markdown("### 📌 Business Problem")
st.write(
    """
    Credit card defaults result in financial losses and increased operational costs
    for banks. Identifying high-risk customers early allows institutions to:
    - Reduce credit losses
    - Prioritize customer interventions
    - Improve portfolio health
    """
)

# -----------------------------
# Model Summary
# -----------------------------
st.markdown("### 🧠 Model Overview")

model_summary = pd.DataFrame({
    "Model": ["Logistic Regression", "Classification Tree"],
    "AUC": [0.772, 0.760],
    "Precision": ["58%", "60%"],
    "Sensitivity": ["62%", "50%"],
    "F1 Score": [0.542, 0.530]
})

st.table(model_summary)

st.success(
    "Logistic Regression was selected as the final model due to its "
    "strong performance, interpretability, and suitability for financial decision-making."
)

# -----------------------------
# Key Drivers
# -----------------------------
st.markdown("### 🔍 Key Drivers of Default Risk")
st.write(
    """
    The most influential predictors of default are:
    - Recent repayment delays (PAY_0, PAY_2)
    - Low payment amounts relative to bill amounts
    - High outstanding balances
    - Lower credit limits combined with rising balances

    Demographic variables such as age and education have a relatively smaller impact.
    """
)

# -----------------------------
# Risk Segmentation
# -----------------------------
st.markdown("### 🚦 Risk Segmentation Strategy")

risk_table = pd.DataFrame({
    "Risk Level": ["High Risk", "Medium Risk", "Low Risk"],
    "Probability Range": [">= 0.26", "0.18 – 0.26", "< 0.18"],
    "Recommended Action": [
        "Immediate outreach, limit review, payment plans",
        "Monitor closely, reminders, auto-pay nudges",
        "Standard servicing"
    ]
})

st.table(risk_table)

# -----------------------------
# Business Impact
# -----------------------------
st.markdown("### 💡 Business Impact")
st.write(
    """
    Using this model enables banks to:
    - Identify high-risk customers before default occurs
    - Allocate collections and customer service resources efficiently
    - Reduce unnecessary interventions for low-risk customers
    - Make data-driven credit policy decisions
    """
)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Credit Card Default Prediction | Machine Learning Project")
