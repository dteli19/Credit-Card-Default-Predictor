import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Credit Card Default Predictor",
    layout="centered"
)

# -----------------------------
# Header
# -----------------------------
st.title("Credit Card Default Prediction")
st.subheader("Machine Learning based Risk Classification")

st.write(
    """
    This application summarizes a credit card default prediction project using
    Logistic Regression and Classification Tree models. The final model selection
    prioritizes interpretability, stability, and business usability.
    """
)

# -----------------------------
# Business Problem
# -----------------------------
st.markdown("### Business Problem")
st.write(
    """
    Credit card defaults lead to financial losses and higher operational costs for banks.
    Predictive modeling helps institutions identify risky customers early and take
    proactive actions to reduce default rates.
    """
)

# -----------------------------
# Model Performance Table (FIXED)
# -----------------------------
st.markdown("### Model Performance Comparison")

model_summary = pd.DataFrame({
    "Model": ["Logistic Regression", "Classification Tree"],
    "AUC": [0.772, 0.760],
    "Precision (%)": [58, 60],
    "Sensitivity (%)": [62, 50],
    "F1 Score": [0.542, 0.530]
})

styled_model_summary = (
    model_summary.style
    .format({"AUC": "{:.3f}", "F1 Score": "{:.3f}"})
    .background_gradient(subset=["AUC", "F1 Score"], cmap="Blues")
)

st.write(styled_model_summary)

st.success(
    "Final Model Selected: Logistic Regression due to its superior balance of performance and interpretability."
)

# -----------------------------
# Key Risk Drivers
# -----------------------------
st.markdown("### Key Drivers of Default Risk")
st.write(
    """
    The strongest indicators of default are related to repayment behavior rather than demographics.

    Key drivers include:
    - Recent payment delays (PAY_0, PAY_2)
    - Low payment amounts relative to outstanding bills
    - High outstanding balances
    - Lower credit limits combined with rising balances
    """
)

# -----------------------------
# Risk Segmentation Table (FIXED)
# -----------------------------
st.markdown("### Risk Segmentation and Action Strategy")

risk_table = pd.DataFrame({
    "Risk Level": ["High Risk", "Medium Risk", "Low Risk"],
    "Default Probability": ["≥ 0.26", "0.18 to 0.26", "< 0.18"],
    "Recommended Action": [
        "Immediate outreach, credit limit review, payment plans",
        "Close monitoring, reminders, auto-pay nudges",
        "Standard servicing, no intervention"
    ]
})

styled_risk_table = (
    risk_table.style
    .set_properties(**{"text-align": "left"})
    .applymap(
        lambda x: "font-weight: bold;" if x == "High Risk" else "",
        subset=["Risk Level"]
    )
)

st.write(styled_risk_table)

# -----------------------------
# Business Impact
# -----------------------------
st.markdown("### Business Impact")
st.write(
    """
    This model enables banks to:
    - Identify high-risk customers before default occurs
    - Prioritize interventions more efficiently
    - Reduce unnecessary actions for low-risk customers
    - Support data-driven credit policy decisions
    """
)

# -----------------------------
# Project Learnings
# -----------------------------
st.markdown("### Project Learnings")
st.write(
    """
    - Evaluation metrics like AUC and F1 are critical for imbalanced datasets
    - Cutoff tuning significantly impacts business outcomes
    - Repayment behavior consistently outperforms demographic variables
    - Interpretable models are preferred in regulated financial environments
    """
)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Credit Card Default Prediction | Machine Learning Project")
