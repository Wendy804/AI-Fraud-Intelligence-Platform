import pandas as pd

from src.risk_scoring import RiskScorer



data = {


"RevolvingUtilizationOfUnsecuredLines":[0.5],

"age":[45],

"NumberOfTime30-59DaysPastDueNotWorse":[1],

"DebtRatio":[0.3],

"MonthlyIncome":[5000],

"NumberOfOpenCreditLinesAndLoans":[5],

"NumberOfTimes90DaysLate":[0],

"NumberRealEstateLoansOrLines":[1],

"NumberOfTime60-89DaysPastDueNotWorse":[0],

"NumberOfDependents":[2]

}



df = pd.DataFrame(data)



scorer = RiskScorer()



result = scorer.predict(df)



print(result)