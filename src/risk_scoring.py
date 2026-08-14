import joblib
import pandas as pd

from src.feature_engineering import create_features



class RiskScorer:


    def __init__(self):


        self.model = joblib.load(
            "models/best_model.pkl"
        )


        self.threshold = joblib.load(
            "models/best_threshold.pkl"
        )


        self.features = joblib.load(
            "models/features.pkl"
        )



    def preprocess(self, df):


        """
        Feature engineering
        and feature alignment
        """


        df = create_features(df)



        # remove target if exists

        if "SeriousDlqin2yrs" in df.columns:

            df = df.drop(
                columns=[
                    "SeriousDlqin2yrs"
                ]
            )



        # 保证和训练一致

        df = df[
            self.features
        ]


        return df



    def predict_probability(self, df):


        X = self.preprocess(df)


        probability = (
            self.model
            .predict_proba(X)[:,1]
        )


        return probability



    def predict(self, df):


        probability = (
            self.predict_probability(df)
        )


        risk = []


        for p in probability:


            if p >= self.threshold:

                level = "HIGH RISK"

            elif p >= 0.3:

                level = "MEDIUM RISK"

            else:

                level = "LOW RISK"



            risk.append(level)



        result = pd.DataFrame({

            "fraud_probability":
                probability,

            "risk_level":
                risk

        })


        return result