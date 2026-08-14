import pandas as pd

from src.risk_scoring import RiskScorer
from src.explain import RiskExplainer
from strategy.strategy_engine import StrategyEngine



class RiskPipeline:


    def __init__(self):

        self.scorer = RiskScorer()

        self.strategy = StrategyEngine()

        self.explainer = RiskExplainer()



    def run(self, df):


        # 保存原始数据给 explanation

        raw_df = df.copy()


        if "Unnamed: 0" in raw_df.columns:

            raw_df = raw_df.drop(
                columns=["Unnamed: 0"]
            )



        # =====================
        # 1. Model prediction
        # =====================
        # 注意：
        # RiskScorer内部已经做feature engineering

        risk_df = self.scorer.predict(
            raw_df
        )



        # =====================
        # 2. Strategy
        # =====================

        decisions = []


        for prob in risk_df["fraud_probability"]:

            decisions.append(

                self.strategy.apply_strategy(
                    prob
                )

            )


        decision_df = pd.DataFrame(
            decisions
        )



        # =====================
        # 3. Explanation
        # =====================

        explain_df = self.explainer.explain(
            raw_df
        )



        # =====================
        # 4. Merge
        # =====================

        result = pd.concat(

            [

                risk_df.reset_index(drop=True),

                decision_df.reset_index(drop=True),

                explain_df.reset_index(drop=True)

            ],

            axis=1

        )


        return result