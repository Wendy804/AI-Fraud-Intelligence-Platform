import pandas as pd

from src.explain import RiskExplainer



df = pd.read_csv(
    "data/cs-training.csv"
)



sample = df.head(1)



explainer = RiskExplainer()


result = explainer.explain(
    sample
)


print(result)