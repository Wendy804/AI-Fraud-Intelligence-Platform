import numpy as np
import pandas as pd



def create_features(df):

    """
    Feature Engineering
    Credit Risk Modeling
    """


    df = df.copy()


    # =========================
    # Missing value indicators
    # =========================


    df["MonthlyIncome_missing"] = (
        df["MonthlyIncome"]
        .isnull()
        .astype(int)
    )


    df["Dependents_missing"] = (
        df["NumberOfDependents"]
        .isnull()
        .astype(int)
    )



    # =========================
    # Fill missing values
    # =========================


    df["MonthlyIncome"] = (
        df["MonthlyIncome"]
        .fillna(
            df["MonthlyIncome"].median()
        )
    )


    df["NumberOfDependents"] = (
        df["NumberOfDependents"]
        .fillna(0)
    )



    # =========================
    # Credit utilization
    # =========================


    df["credit_utilization_level"] = (
        df["RevolvingUtilizationOfUnsecuredLines"]
    )



    # =========================
    # Past due risk score
    # =========================


    df["past_due_score"] = (

        df["NumberOfTime30-59DaysPastDueNotWorse"]

        +

        2 *
        df["NumberOfTime60-89DaysPastDueNotWorse"]

        +

        3 *
        df["NumberOfTimes90DaysLate"]

    )



    # =========================
    # Serious delay flag
    # =========================


    df["serious_delay_flag"] = (

        (
        df["NumberOfTimes90DaysLate"] > 0
        )

        |

        (
        df["NumberOfTime60-89DaysPastDueNotWorse"] > 0
        )

    ).astype(int)



    # =========================
    # Credit lines
    # =========================


    df["credit_line_total"] = (

        df["NumberOfOpenCreditLinesAndLoans"]

        +

        df["NumberRealEstateLoansOrLines"]

    )



    # =========================
    # Income features
    # =========================


    df["income_per_dependent"] = (

        df["MonthlyIncome"]

        /

        (
            df["NumberOfDependents"] + 1
        )

    )



    # =========================
    # Age group
    # =========================


    df["age_group"] = pd.cut(

        df["age"],

        bins=[
            0,
            25,
            35,
            50,
            65,
            100
        ],

        labels=False

    )


    # 防止category/int问题
    df["age_group"] = (
        df["age_group"]
        .fillna(0)
        .astype(int)
    )



    # =========================
    # Debt income ratio
    # =========================


    df["debt_income_ratio"] = (

        df["DebtRatio"]

        /

        (
            df["MonthlyIncome"]
            + 1
        )

    )



    return df