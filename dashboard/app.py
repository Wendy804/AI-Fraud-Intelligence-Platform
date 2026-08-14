import sys
import os


# ==========================
# Project Path
# ==========================

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.insert(
    0,
    PROJECT_ROOT
)



import streamlit as st
import pandas as pd
import plotly.express as px


from src.pipeline import RiskPipeline



# ==========================
# Page Config
# ==========================

st.set_page_config(
    page_title="AI Credit Risk Platform",
    layout="wide"
)



# ==========================
# Title
# ==========================

st.title(
    "AI Credit Risk Strategy Platform"
)


st.markdown(
    """
Machine Learning Based Credit Risk Decision System

Pipeline:

Raw Customer Data
→ Feature Engineering
→ XGBoost Risk Model
→ Risk Score
→ Strategy Decision
"""
)



# ==========================
# Upload
# ==========================

uploaded_file = st.file_uploader(
    "Upload Customer CSV",
    type=["csv"]
)



if uploaded_file is not None:


    # ==========================
    # Load Data
    # ==========================

    df = pd.read_csv(
        uploaded_file
    )


    st.subheader(
        "Customer Data"
    )


    st.dataframe(
        df,
        use_container_width=True
    )



    # ==========================
    # Run Pipeline
    # ==========================


    pipeline = RiskPipeline()


    result_df = pipeline.run(
        df
    )


    # ==========================
    # Remove duplicated columns
    # ==========================

    result_df = (
        result_df
        .loc[
            :,
            ~result_df.columns.duplicated()
        ]
    )



    # ==========================
    # Risk Overview
    # ==========================


    st.subheader(
        "Risk Overview"
    )


    total_customers = len(
        result_df
    )


    if "risk_level" in result_df.columns:


        high_risk = (
            result_df["risk_level"]
            .astype(str)
            .str.contains(
                "HIGH",
                case=False
            )
            .sum()
        )


    else:

        high_risk = 0



    if "decision" in result_df.columns:


        approval_rate = (

            (
                result_df["decision"]
                .astype(str)
                .str.contains(
                    "Approve",
                    case=False
                )
            )
            .mean()
            *
            100

        )

    else:

        approval_rate = 0



    col1,col2,col3 = st.columns(3)


    with col1:

        st.metric(
            "Total Customers",
            total_customers
        )


    with col2:

        st.metric(
            "High Risk Customers",
            int(high_risk)
        )


    with col3:

        st.metric(
            "Approval Rate",
            f"{approval_rate:.1f}%"
        )




    # ==========================
    # Risk Result
    # ==========================


    st.subheader(
        "Customer Risk Assessment"
    )


    show_columns = []


    for c in [
        "fraud_probability",
        "risk_level",
        "decision"
    ]:

        if c in result_df.columns:

            show_columns.append(c)



    st.dataframe(
        result_df[
            show_columns
        ],
        use_container_width=True
    )



    # ==========================
    # Risk Distribution
    # ==========================


    if "risk_level" in result_df.columns:


        st.subheader(
            "Risk Distribution"
        )


        risk_count = (
            result_df["risk_level"]
            .value_counts()
            .reset_index()
        )


        risk_count.columns = [
            "Risk Level",
            "Count"
        ]


        fig = px.pie(
            risk_count,
            names="Risk Level",
            values="Count"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )



    # ==========================
    # Explanation
    # ==========================


    st.subheader(
        "Model Explanation"
    )


    explanation_columns = []


    for c in [
        "customer_id",
        "risk_factors",
        "feature",
        "impact"
    ]:

        if c in result_df.columns:

            explanation_columns.append(c)



    if explanation_columns:


        st.dataframe(
            result_df[
                explanation_columns
            ],
            use_container_width=True
        )


    else:


        st.info(
            "No explanation available"
        )



else:


    st.info(
        "Please upload customer data file"
    )