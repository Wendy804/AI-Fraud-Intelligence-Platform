import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


import streamlit as st
import pandas as pd
import joblib


from src.feature_engineering import preprocess_data
from src.explainer import explain_prediction



# =========================
# Page Config
# =========================

st.set_page_config(
    page_title="AI Fraud Intelligence Platform",
    layout="centered"
)



# =========================
# Load Model
# =========================


model = joblib.load(
    "models/fraud_xgb.pkl"
)


threshold = joblib.load(
    "models/threshold.pkl"
)



# =========================
# Title
# =========================


st.title(
    "AI Fraud Intelligence Platform"
)


st.write(
    """
AI-powered transaction fraud risk analysis system.
"""
)



st.divider()



# =========================
# Input
# =========================


st.subheader(
    "Transaction Information"
)



type_options = [

    "PAYMENT",

    "TRANSFER",

    "CASH_OUT",

    "DEBIT"

]



transaction_type = st.selectbox(

    "Transaction Type",

    type_options,

    help=
    """
Transaction category.

TRANSFER and CASH_OUT
usually have higher fraud risk.
"""

)



amount = st.number_input(

    "Transaction Amount",

    min_value=0.0,

    value=1000.0,

    help=
    """
Money transferred in this transaction.
Unit: currency amount.
"""

)



oldbalanceOrg = st.number_input(

    "Sender Balance Before Transaction",

    min_value=0.0,

    value=5000.0,

    help=
    """
Sender account balance before transaction.
"""

)



newbalanceOrig = st.number_input(

    "Sender Balance After Transaction",

    min_value=0.0,

    value=4000.0,

    help=
    """
Sender account balance after transaction.
"""

)



oldbalanceDest = st.number_input(

    "Receiver Balance Before Transaction",

    min_value=0.0,

    value=1000.0,

    help=
    """
Receiver account balance before receiving money.
"""

)



newbalanceDest = st.number_input(

    "Receiver Balance After Transaction",

    min_value=0.0,

    value=2000.0,

    help=
    """
Receiver account balance after transaction.
"""

)



st.divider()



# =========================
# Prediction
# =========================


if st.button(
    "Analyze Fraud Risk"
):


    # create raw dataframe

    input_df = pd.DataFrame(

        [{

        "step":1,

        "type":transaction_type,

        "amount":amount,

        "oldbalanceOrg":oldbalanceOrg,

        "newbalanceOrig":newbalanceOrig,

        "oldbalanceDest":oldbalanceDest,

        "newbalanceDest":newbalanceDest


        }]

    )



    # Feature engineering

    X,_ = preprocess_data(

        input_df,

        training=False

    )



    # Prediction probability


    probability = model.predict_proba(

        X

    )[0][1]



    prediction = int(

        probability >= threshold

    )



    risk_score = int(

        probability * 100

    )



    # =========================
    # Dashboard
    # =========================


    st.divider()


    st.subheader(
        "Fraud Risk Assessment"
    )



    st.metric(

        "Fraud Probability",

        f"{risk_score}%"

    )



    if prediction == 1:


        st.error(

            "🔴 HIGH RISK FRAUD DETECTED"

        )


    else:


        st.success(

            "🟢 LOW RISK TRANSACTION"

        )



    # =========================
    # Explanation
    # =========================


    st.divider()


    st.subheader(

        "AI Explanation"

    )



    explanation = explain_prediction(

        X

    )


    st.dataframe(

        explanation,

        use_container_width=True

    )