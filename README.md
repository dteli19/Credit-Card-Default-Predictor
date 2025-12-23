# 💳 Credit Card Default Prediction using Machine Learning

## 📌 Project Overview
Credit card default is a major source of financial risk for banks and lending institutions. Accurately identifying customers who are likely to default enables proactive risk management, reduces losses, and supports better credit policy decisions.

This project builds and evaluates machine learning models to predict whether a customer will default on their credit card payment in the next billing cycle. Using customer demographic information, credit limits, billing behavior, and repayment history, the analysis compares multiple models and selects the most effective and business-friendly approach.

🔗 [Live Streamlit App](https://credit-card-default-predictor-8bv37sjw2hfxnn4q6jdaip.streamlit.app/)


## 🎯 Business Objectives
- Identify customers most likely to default on their credit card payments
- Understand the key behavioral and financial drivers of default risk
- Compare predictive models and select the best-performing model
- Provide actionable recommendations for early intervention and credit risk management

---

## 📊 Dataset
- Source: UCI Credit Card Default Dataset
- Sample Size: 10,000 randomly selected customers
- Target Variable: Default (Yes / No)

### Key Features
- **Demographics:** Age, Education, Marriage Status, Gender  
- **Credit Capacity:** Credit Limit (LIMIT_BAL)  
- **Repayment Behavior:** Recent payment status (PAY_0, PAY_2)  
- **Financial Trends:** Bill amounts and payment amounts from recent months  

Outliers were retained, as they represent real customer behavior and are meaningful for credit risk modeling.

---

## 🧠 Models Implemented
### 1. Logistic Regression
- Used as the primary baseline model due to interpretability and regulatory suitability
- Feature selection applied using stepwise elimination
- Cutoff optimized to balance precision and recall

### 2. Classification Tree
- Captures nonlinear relationships and interaction effects
- Multiple tree configurations tested with pruning
- Final model selected based on validation AUC and lift performance

---

## 🏆 Best Model Selection
After comparing model performance across AUC, precision, sensitivity, and F1 score:

| Model | AUC | Precision | Sensitivity | F1 Score |
|------|-----|-----------|-------------|----------|
| Logistic Regression | 0.772 | 58% | 62% | 0.542 |
| Classification Tree | 0.760 | 60% | 50% | 0.530 |

**Final Model Chosen: Logistic Regression**

### Why Logistic Regression?
- Highest overall AUC and F1 score
- Strong balance between identifying defaulters and controlling false positives
- Highly interpretable and suitable for financial decision-making and compliance
- Stable performance across training and validation data

---

## 📈 Model Performance (Logistic Regression)
- Training AUC: 0.760
- Validation AUC: 0.772
- Optimized Cutoff: **0.26**

Customers with predicted default probability ≥ 0.26 are classified as high-risk.

---

## 🔍 Key Insights
- **Repayment behavior is the strongest predictor of default**, especially recent payment delays (PAY_0 and PAY_2)
- Customers with repeated late payments and low repayment amounts face significantly higher default risk
- Demographic variables have relatively minor impact compared to behavioral variables
- Feature selection improves interpretability but does not materially improve predictive accuracy

---

## 💡 Business Recommendations
1. **Proactively engage high-risk customers**
   - Customers with risk scores ≥ 0.26 should receive early outreach
   - Actions include payment reminders, payment plans, or temporary credit limit reviews

2. **Closely monitor medium-risk customers**
   - Risk scores between 0.18 and 0.26 indicate emerging stress
   - Encourage auto-pay enrollment and provide financial education

3. **Maintain standard servicing for low-risk customers**
   - Customers below 0.18 show stable repayment behavior and require no intervention

4. **Integrate the model into credit management workflows**
   - Support credit limit adjustments
   - Improve collections prioritization
   - Allocate customer service resources more effectively

---

## 📘 Project Learnings
- Learned how different ML models behave on imbalanced financial datasets
- Understood the importance of evaluation metrics beyond accuracy, such as AUC and F1 score
- Gained experience tuning probability cutoffs to reflect real business costs
- Reinforced the value of interpretable models in regulated industries
- Developed the ability to translate technical outputs into actionable business insights

---

## 🛠 Tools & Technologies
- Python
- Excel / XLMiner
- Logistic Regression
- Classification Trees
- ROC, Lift, and Decile Analysis
