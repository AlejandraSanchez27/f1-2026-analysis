import pandas as pd

df_races = pd.read_csv("../data/all_results_2026.csv")
df_sprints = pd.read_csv("../data/sprints_results_2026.csv")

df_all = pd.concat([df_races, df_sprints], ignore_index=True)

#print(f"Carreras: {len(df_races)} filas")
#print(f"Sprints: {len(df_sprints)} filas")
#print(f"Total combinado: {len(df_all)} filas")

championship = df_all.groupby(["driver_code", "constructor"])["points"]\
    .sum()\
    .reset_index()\
    .sort_values(by="points", ascending=False)\
    .reset_index(drop=True)

championship.index = championship.index + 1
championship.index.name = "position"

print(championship)
championship.to_excel("../excel/championship_2026.xlsx", index=False)

constructors = df_all.groupby("constructor")["points"]\
    .sum()\
    .reset_index()\
    .sort_values(by="points", ascending=False)\
    .reset_index(drop=True)

print(constructors)
constructors.to_excel("../excel/constructors_2026.xlsx", index=False)


