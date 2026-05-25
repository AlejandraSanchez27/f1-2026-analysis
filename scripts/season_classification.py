import pandas as pd

df = pd.read_csv("data/all_results_2026.csv")

championship = df.groupby(["driver_code", "constructor"])["points"].sum()
print(championship.sort_values(ascending=False))