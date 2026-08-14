def generate_report(result):


    score = float(
        result["fraud_probability"]
    )



    level = str(
        result["risk_level"]
    )



    decision = str(
        result.get(
            "decision",
            ""
        )
    )



    factors = result.get(
        "risk_factors",
        []
    )



    if isinstance(
        factors,
        str
    ):

        factors = [
            factors
        ]



    if level == "HIGH RISK":


        recommendation = (

            "High risk detected. "
            "Manual review required."

        )


    elif level == "MEDIUM RISK":


        recommendation = (

            "Medium risk detected. "
            "Additional verification required."

        )


    else:


        recommendation = (

            "Low risk detected. "
            "Approval recommended."

        )



    return {


        "Risk Score":

            round(score,4),



        "Risk Level":

            level,



        "Decision":

            decision,



        "Risk Factors":

            factors,



        "Summary":

            (
                f"Risk assessment completed. "
                f"Risk score is {score:.4f} "
                f"and level is {level}."
            ),



        "Recommendation":

            recommendation

    }