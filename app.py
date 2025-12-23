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
# Header (subtle color only here)
# -----------------------------
st.markdown(
    "<h1 style='color:#2C3E50;'>Credit Card Default Prediction</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h4 style='color:#4F6D7A;'>Machine Learning based Risk Classification</h4>",
    unsafe_allow_html=True
)

st.write(
    """
    This app summarizes a credit card default prediction project using Logistic Regression
    and Classification Tree models. The final model selection emphasizes interpretability,
    stable validation performance, and business usability.
    """
)

# -----------------------------
# Business Problem
# -----------------------------
st.markdown("### Business Problem")
st.write(
    """
    Credit card defaults create financial losses and higher operational costs for banks.
    Predictive modeling enables early identification of at-risk customers so institutions
    can take proactive measures to reduce defaults.
    """
)

# -----------------------------
# Model Performance Table
# -----------------------------
st.markdown(
    "<h3 style='color:#2C3E50;'>Model Performance Comparison</h3>",
    unsafe_allow_html=True
)

model_summary = pd.DataFrame({
    "Model": ["Logistic Regression", "Classification Tree"],
    "AUC": [0.772, 0.760],
    "Precision (%)": [58, 60],
    "Sensitivity (%)": [62, 50],
    "F1 Score": [0.542, 0.530],
    "Final Model": ["Yes", "No"]
})

st.dataframe(
    model_summary,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Model": st.column_config.TextColumn(width="large"),
        "AUC": st.column_config.NumberColumn(format="%.3f"),
        "Precision (%)": st.column_config.NumberColumn(format="%d"),
        "Sensitivity (%)": st.column_config.NumberColumn(format="%d"),
        "F1 Score": st.column_config.NumberColumn(format="%.3f"),
        "Final Model": st.column_config.TextColumn()
    }
)

st.info(
    "Logistic Regression was selected as the final model due to the best balance of "
    "predictive performance and interpretability."
)

# -----------------------------
# Key Drivers
# -----------------------------
st.markdown(
    "<h3 style='color:#2C3E50;'>Key Drivers of Default Risk</h3>",
    unsafe_allow_html=True
)

st.write(
    """
    The strongest predictors of default are repayment behavior variables rather than
    demographic characteristics.

    Key drivers include:
    - Recent payment delays (PAY_0, PAY_2)
    - Low payment amounts relative to outstanding bills
    - High outstanding balances
    - Lower credit limits combined with rising balances
    """
)

# -----------------------------
# Risk Segmentation Table
# -----------------------------
st.markdown(
    "<h3 style='color:#2C3E50;'>Risk Segmentation and Action Strategy</h3>",
    unsafe_allow_html=True
)

risk_table = pd.DataFrame({
    "Risk Level": ["High Risk", "Medium Risk", "Low Risk"],
    "Default Probability": ["≥ 0.26", "0.18 to 0.26", "< 0.18"],
    "Recommended Action": [
        "Immediate outreach, credit limit review, payment plans",
        "Close monitoring, reminders, auto-pay nudges",
        "Standard servicing, no intervention"
    ]
})

st.dataframe(
    risk_table,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Risk Level": st.column_config.TextColumn(width="medium"),
        "Default Probability": st.column_config.TextColumn(width="small"),
        "Recommended Action": st.column_config.TextColumn(width="large")
    }
)

# -----------------------------
# Business Impact
# -----------------------------
st.markdown(
    "<h3 style='color:#2C3E50;'>Business Impact</h3>",
    unsafe_allow_html=True
)

st.write(
    """
    This model enables banks to:
    - Identify high-risk customers before default occurs
    - Prioritize interventions efficiently
    - Reduce unnecessary actions for low-risk customers
    - Support data-driven credit policy and collections decisions
    """
)

# -----------------------------
# Project Learnings
# -----------------------------
st.markdown(
    "<h3 style='color:#2C3E50;'>Project Learnings</h3>",
    unsafe_allow_html=True
)

st.write(
    """
    - Accuracy alone is insufficient for imbalanced datasets; AUC and F1 are more informative.
    - Cutoff tuning is critical to balance missed defaulters and false positives.
    - Repayment behavior consistently outperforms demographic variables.
    - Interpretable models are essential in regulated financial environments.
    """
)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Credit Card Default Prediction | Machine Learning Project")
