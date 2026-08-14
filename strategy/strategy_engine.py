class StrategyEngine:


    def __init__(self):
        pass


    def apply_strategy(self, fraud_probability):


        if fraud_probability >= 0.7:

            return {

                "risk_level":
                    "High Risk",

                "decision":
                    "Reject"

            }


        elif fraud_probability >= 0.3:

            return {

                "risk_level":
                    "Medium Risk",

                "decision":
                    "Manual Review"

            }


        else:

            return {

                "risk_level":
                    "Low Risk",

                "decision":
                    "Approve"

            }