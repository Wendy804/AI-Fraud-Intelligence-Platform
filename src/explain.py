import pandas as pd


class RiskExplainer:


    def explain(self, df):

        results = []


        for i,row in df.iterrows():

            reasons=[]


            if row["DebtRatio"] > 0.5:

                reasons.append(
                    "High debt ratio"
                )


            if row["RevolvingUtilizationOfUnsecuredLines"] > 0.7:

                reasons.append(
                    "High credit utilization"
                )


            if row["NumberOfTimes90DaysLate"] > 0:

                reasons.append(
                    "Past payment delay history"
                )


            if pd.isna(row["MonthlyIncome"]):

                reasons.append(
                    "Missing income information"
                )


            if len(reasons)==0:

                reasons.append(
                    "No major risk factor detected"
                )


            results.append(
                {
                    "customer_id": i+1,

                    "risk_factors":
                    ", ".join(reasons)
                }
            )


        return pd.DataFrame(results)