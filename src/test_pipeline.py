import pandas as pd

from src.pipeline import RiskPipeline



data = {


"RevolvingUtilizationOfUnsecuredLines":[0.8],

"age":[35],

"NumberOfTime30-59DaysPastDueNotWorse":[2],

"DebtRatio":[0.6],

"MonthlyIncome":[3000],

"NumberOfOpenCreditLinesAndLoans":[10],

"NumberOfTimes90DaysLate":[1],

"NumberRealEstateLoansOrLines":[2],

"NumberOfTime60-89DaysPastDueNotWorse":[1],

"NumberOfDependents":[3]

}



df = pd.DataFrame(data)



pipeline = RiskPipeline()



result = pipeline.run(df)



print(result)