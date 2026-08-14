import pandas as pd



def convert_customer_input(data):

    """
    Convert business input
    into model raw features
    """


    df = pd.DataFrame([data])


    # ==========================
    # Calculate credit utilization
    # ==========================

    df["RevolvingUtilizationOfUnsecuredLines"] = (

        df["used_credit"]

        /

        df["total_credit"]

    )


    df["RevolvingUtilizationOfUnsecuredLines"] = (

        df["RevolvingUtilizationOfUnsecuredLines"]
        .fillna(0)
        .clip(0, 10)

    )



    # ==========================
    # Calculate debt ratio
    # ==========================

    df["DebtRatio"] = (

        df["total_debt"]

        /

        (
            df["MonthlyIncome"] * 12
            +
            1
        )

    )



    # ==========================
    # Generate model input
    # ==========================


    model_df = pd.DataFrame({

        "RevolvingUtilizationOfUnsecuredLines":
            df["RevolvingUtilizationOfUnsecuredLines"],


        "age":
            df["age"],


        "NumberOfTime30-59DaysPastDueNotWorse":
            df["late_30_59"],


        "DebtRatio":
            df["DebtRatio"],


        "MonthlyIncome":
            df["MonthlyIncome"],


        "NumberOfOpenCreditLinesAndLoans":
            df["credit_lines"],


        "NumberOfTimes90DaysLate":
            df["late_90"],


        "NumberRealEstateLoansOrLines":
            df["real_estate_loans"],


        "NumberOfTime60-89DaysPastDueNotWorse":
            df["late_60_89"],


        "NumberOfDependents":
            df["dependents"]

    })


    return model_df