import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(page_title="Credit Card Default Predictor", layout="centered")

# -----------------------------
# Header
# -----------------------------
st.title("Credit Card Default Prediction")
st.subheader("Machine Learning based Risk Classification")

st.write(
    """
    This application summarizes a credit card default prediction project using
    Logistic Regression and Classification Tree models. The final selection focuses on
    interpretability, stability, and business usability for proactive credit risk management.
    """
)

# -----------------------------
# Business Problem
# -----------------------------
st.markdown("### Business Problem")
st.write(
    """
    Credit card defaults lead to financial losses and increased operational costs for banks.
    Predicting default risk helps institutions reduce credit losses, prioritize interventions,
    and improve overall portfolio health.
    """
)

# -----------------------------
# Model Comparison Table (Styled)
# -----------------------------
st.markdown("### Model Performance Comparison")

model_summary = pd.DataFrame({
    "Model": ["Logistic Regression", "Classification Tree"],
    "AUC": [0.772, 0.760],
    "Precision (%)": [58, 60],
    "Sensitivity (%)": [62, 50],
    "F1 Score": [0.542, 0.530]
})

st.dataframe(
    model_summary.style
        .format({"AUC": "{:.3f}", "F1 Score": "{:.3f}"})
        .background_gradient(subset=["AUC", "F1 Score"], cmap="Blues"),
    use_container_width=True
)

st.success(
    "Final Model Selected: Logistic Regression. It provides the best balance of performance and interpretability."
)

# -----------------------------
# Key Drivers
# -----------------------------
st.markdown("### Key Drivers of Default Risk")
st.write(
    """
    The strongest signals of default risk come from repayment behavior, especially recent payment delays
    and low payments relative to billed amounts.
    
    Most influential drivers:
    - Recent repayment delays (PAY_0, PAY_2)
    - Low payment amounts compared to outstanding bills
    - High outstanding balances
    - Lower credit limits combined with rising balances
    """
)

# -----------------------------
# Risk Segmentation Table (Styled)
# -----------------------------
st.markdown("### Risk Segmentation and Action Strategy")

risk_table = pd.DataFrame({
    "Risk Level": ["High Risk", "Medium Risk", "Low Risk"],
    "Default Probability": ["≥ 0.26", "0.18 to 0.26", "< 0.18"],
    "Business Action": [
        "Immediate outreach, credit limit review, payment plans",
        "Close monitoring, reminders, auto-pay nudges",
        "Standard servicing, no intervention"
    ]
})

st.dataframe(
    risk_table.style
        .set_properties(**{"text-align": "left"})
        .applymap(lambda x: "font-weight: bold;" if x == "High Risk" else "", subset=["Risk Level"]),
    use_container_width=True
)

# -----------------------------
# Business Impact
# -----------------------------
st.markdown("### Business Impact")
st.write(
    """
    This model supports banks in:
    - Identifying high-risk customers before default occurs
    - Allocating collections and customer support resources efficiently
    - Reducing unnecessary interventions for low-risk customers
    - Supporting smarter, data-driven credit policy decisions
    """
)

# -----------------------------
# Project Learnings
# -----------------------------
st.markdown("### Project Learnings")
st.write(
    """
    Key learnings from this project:
    - Accuracy alone is not sufficient for imbalanced datasets, AUC and F1 are more meaningful.
    - Cutoff tuning is critical to balance missed defaulters and false positives.
    - Repayment behavior consistently outperforms demographic variables in predicting default.
    - Interpretable models are valuable in financial settings for decision-making and compliance.
    """
)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Credit Card Default Prediction | ML Project")
