import pandas as pd

from src.risk_scoring import RiskScorer
from strategy.strategy_engine import StrategyEngine

from customer_portal.shap_explain import (
    generate_risk_factors
)



class CustomerRiskPipeline:


    def __init__(self):

        self.scorer = RiskScorer()

        self.strategy = StrategyEngine()



    def run(self, df):


        # =====================
        # Prediction
        # =====================


        probability = (
            self.scorer.predict_probability(df)
        )[0]



        # =====================
        # Risk Level
        # =====================


        threshold = self.scorer.threshold



        if probability >= threshold:

            level = "HIGH RISK"


        elif probability >= 0.3:

            level = "MEDIUM RISK"


        else:

            level = "LOW RISK"




        # =====================
        # Decision
        # =====================


        decision = (

            self.strategy
            .apply_strategy(
                probability
            )

        )



        # =====================
        # Explanation
        # =====================


        factors = generate_risk_factors(
            df
        )



        return {


            "fraud_probability":

                float(probability),



            "risk_level":

                level,



            "decision":

                decision.get(
                    "decision",
                    ""
                ),



            "risk_factors":

                factors

        }