import sys
import os
import tempfile


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



from customer_portal.input_mapper import (
    convert_customer_input
)


from customer_portal.report import (
    generate_report
)


from customer_portal.pdf_report import (
    create_pdf
)


from src.customer_pipeline import (
    CustomerRiskPipeline
)




# ==========================
# Page Config
# ==========================


st.set_page_config(

    page_title="AI Credit Risk Assistant",

    layout="wide"

)




# ==========================
# Header
# ==========================


st.title(
    "AI Credit Risk Assistant"
)


st.markdown(
"""
### Intelligent Credit Risk Assessment System

Customer Raw Information  
↓  
Automatic Feature Calculation  
↓  
Machine Learning Risk Model  
↓  
Risk Decision & Credit Recommendation
"""
)



st.divider()




# ==========================
# Input Section
# ==========================


st.subheader(
    "Customer Information"
)



col1,col2 = st.columns(2)




with col1:


    age = st.number_input(
        "Age 年龄",
        min_value=18,
        max_value=100,
        value=40
    )


    income = st.number_input(
        "Monthly Income 月收入",
        min_value=0,
        value=8000
    )


    debt = st.number_input(
        "Total Debt 总负债",
        min_value=0,
        value=50000
    )


    credit = st.number_input(
        "Total Credit Limit 总信用额度",
        min_value=1,
        value=100000
    )


    used_credit = st.number_input(
        "Used Credit 已使用额度",
        min_value=0,
        value=50000
    )




with col2:


    dependents = st.number_input(
        "Dependents 家庭成员",
        min_value=0,
        value=2
    )


    late30 = st.number_input(
        "30-59 Days Past Due",
        min_value=0,
        value=0
    )


    late60 = st.number_input(
        "60-89 Days Past Due",
        min_value=0,
        value=0
    )


    late90 = st.number_input(
        "90+ Days Late",
        min_value=0,
        value=0
    )


    credit_lines = st.number_input(
        "Credit Lines 信用账户",
        min_value=0,
        value=5
    )


    real_estate = st.number_input(
        "Real Estate Loans 房贷数量",
        min_value=0,
        value=1
    )




st.divider()




# ==========================
# Prediction
# ==========================


if st.button(
    "Analyze Risk",
    type="primary"
):


    customer_data = {


        "age":
            age,


        "MonthlyIncome":
            income,


        "total_debt":
            debt,


        "total_credit":
            credit,


        "used_credit":
            used_credit,


        "dependents":
            dependents,


        "late_30_59":
            late30,


        "late_60_89":
            late60,


        "late_90":
            late90,


        "credit_lines":
            credit_lines,


        "real_estate_loans":
            real_estate

    }



    # Convert business input

    model_input = convert_customer_input(
        customer_data
    )



    # Run model

    pipeline = CustomerRiskPipeline()



    result = pipeline.run(
        model_input
    )



    report = generate_report(
        result
    )



    st.session_state["report"] = report



    st.session_state["result"] = result





# ==========================
# Display Result
# ==========================


if "report" in st.session_state:


    report = st.session_state["report"]


    result = st.session_state["result"]



    st.divider()



    st.subheader(
        "Risk Assessment Result"
    )



    c1,c2,c3 = st.columns(3)



    c1.metric(

        "Risk Score",

        report["Risk Score"]

    )



    c2.metric(

        "Risk Level",

        report["Risk Level"]

    )



    c3.metric(

        "Decision",

        report["Decision"]

    )




    st.divider()



    st.subheader(
        "Risk Factors"
    )



    for factor in report["Risk Factors"]:


        st.write(
            "•",
            factor
        )




    st.divider()



    st.subheader(
        "Recommendation"
    )



    st.info(
        report["Recommendation"]
    )




    st.divider()



    st.subheader(
        "Risk Summary"
    )



    st.write(
        report["Summary"]
    )




    # ==========================
    # PDF Report
    # ==========================


    st.divider()


    st.subheader(
        "Credit Risk Report"
    )



    if st.button(
        "Generate PDF Report"
    ):


        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        )



        create_pdf(

            report,

            temp_file.name

        )



        with open(
            temp_file.name,
            "rb"
        ) as pdf:


            st.download_button(

                label="Download PDF",

                data=pdf,

                file_name=
                "AI_Credit_Risk_Report.pdf",

                mime=
                "application/pdf"

            )




    # ==========================
    # Debug
    # ==========================


    with st.expander(
        "Model Output Details"
    ):


        st.dataframe(
            result,
            use_container_width=True
        )