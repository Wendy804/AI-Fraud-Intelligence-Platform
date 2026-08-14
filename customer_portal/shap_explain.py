import pandas as pd



def generate_risk_factors(df):


    factors = []



    row = df.iloc[0]



    # =====================
    # Debt
    # =====================


    if "DebtRatio" in df.columns:


        if row["DebtRatio"] > 0.5:

            factors.append(
                "High debt ratio 高负债率"
            )



    # =====================
    # Credit utilization
    # =====================


    if "RevolvingUtilizationOfUnsecuredLines" in df.columns:


        if row[
            "RevolvingUtilizationOfUnsecuredLines"
        ] > 0.5:


            factors.append(
                "High credit utilization 高信用使用率"
            )



    # =====================
    # Payment history
    # =====================


    late_cols = [

        "NumberOfTime30-59DaysPastDueNotWorse",

        "NumberOfTime60-89DaysPastDueNotWorse",

        "NumberOfTimes90DaysLate"

    ]



    late_count = 0



    for col in late_cols:


        if col in df.columns:


            late_count += row[col]



    if late_count > 0:


        factors.append(

            "Past payment delay history 历史逾期记录"

        )



    # =====================
    # Income
    # =====================


    if "MonthlyIncome" in df.columns:


        if row["MonthlyIncome"] < 5000:


            factors.append(

                "Low income level 低收入水平"

            )



    # =====================
    # Fallback
    # =====================


    if len(factors)==0:


        factors.append(

            "Model detected combined risk pattern 模型综合特征判断风险"

        )



    return factors