import fastf1
import pandas as pd

fastf1.Cache.enable_cache("../data/cache")  # Habilitar caché para acelerar futuras ejecuciones

session = fastf1.get_session(2026, 1, "R")  # Obtener la sesión de clasificación de la primera carrera
session.load()  # Cargar los datos de la sesión
session1 = fastf1.get_session(2026, 2, "R")
session1.load()
session2 = fastf1.get_session(2026, 3, "R")
session2.load()
session3 = fastf1.get_session(2026, 4, "R")
session3.load()
session4 = fastf1.get_session(2026, 5, "R")
session4.load()
"""
print(session.name) # Imprimir el nombre de la sesión
print(session.date) # Imprimir la fecha de la sesión
print(session.laps) # Imprimir información sobre las vueltas de la sesión
print(session.results) # Imprimir los resultados de la sesión
"""
laps = session.laps
"""
ferrari_laps = laps.pick_drivers(["LEC", "HAM"])
print(ferrari_laps[["Driver", "LapNumber", "LapTime", "Compound", "TyreLife", "PitOutTime", "PitInTime"]].to_string())

mercedes_laps = laps.pick_drivers(["RUS", "ANT"])
print(mercedes_laps[["Driver", "LapNumber", "LapTime", "Compound", "TyreLife", "PitOutTime", "PitInTime"]].to_string())

mclaren_laps = laps.pick_drivers(["NOR", "PIA"])
print(mclaren_laps[["Driver", "LapNumber", "LapTime", "Compound", "TyreLife", "PitOutTime", "PitInTime"]].to_string())

redbull_laps = laps.pick_drivers(["VER", "HAD"])
print(redbull_laps[["Driver", "LapNumber", "LapTime", "Compound", "TyreLife", "PitOutTime", "PitInTime"]].to_string())
"""

pit_data = []

drivers_teams = {
    "LEC": "Ferrari",
    "HAM": "Ferrari",
    "RUS": "Mercedes",
    "ANT": "Mercedes",
    "NOR": "McLaren",
    "PIA": "McLaren",
    "VER": "Red Bull",
    "HAD": "Red Bull",
}

for driver, team in drivers_teams.items():
    driver_laps = laps.pick_drivers([driver])
    pits = driver_laps[driver_laps["PitInTime"].notna()][
        ["Driver", "LapNumber", "Compound", "TyreLife", "PitInTime"]
    ].copy()
    pits["Team"] = team
    pits["Race"] = "Australia"
    pits["Round"] = 1
    pit_data.append(pits)

df_strategy = pd.concat(pit_data, ignore_index=True)
print(df_strategy)
df_strategy.to_csv("../data/strategy_australia_2026.csv", index=False)

def get_pit_strategy(session, round_number, race_name, drivers_teams):
    laps = session.laps
    pit_data = []

    for driver, team in drivers_teams.items():
        driver_laps = laps.pick_drivers([driver])

        pits_in = driver_laps[driver_laps["PitInTime"].notna()][
            ["Driver", "LapNumber", "Compound", "TyreLife", "PitInTime"]
        ].copy()

        pits_out = driver_laps[driver_laps["PitOutTime"].notna()][
            ["LapNumber", "PitOutTime"]
        ].copy()
        pits_out["LapNumber"] = pits_out["LapNumber"] - 1

        pits = pits_in.merge(pits_out, on="LapNumber", how="left")
        pits["Team"] = team
        pits["Race"] = race_name
        pits["Round"] = round_number
        pit_data.append(pits)

    df = pd.concat(pit_data, ignore_index=True)
    df["PitInTime"] = df["PitInTime"].dt.total_seconds()
    df["PitOutTime"] = df["PitOutTime"].dt.total_seconds()
    df["PitDuration"] = df["PitOutTime"] - df["PitInTime"]

    return df


df = get_pit_strategy(session, 1, "Australia", drivers_teams)
print(df)
df1 = get_pit_strategy(session1, 2, "China", drivers_teams)
print(df1)
df2 = get_pit_strategy(session2, 3, "Japan", drivers_teams)
print(df2)
df3 = get_pit_strategy(session3, 4, "USA", drivers_teams)
print(df3)
df4 = get_pit_strategy(session4, 5, "Canada", drivers_teams)
print(df4)
"""
df_all = pd.concat([df, df1, df2, df3, df4], ignore_index=True)
df_all.to_csv("../data/strategy_all_races_2026.csv", index=False)
print(f"Total filas: {len(df_all)}")
"""

df_all = pd.concat([df, df1, df2, df3, df4], ignore_index=True)
df_all.to_excel("../excel/strategy_all_races_2026.xlsx", index=False)
print(f"Total filas: {len(df_all)}")


def get_lap_times(session, round_number, race_name, drivers_teams):
    laps = session.laps
    lap_data = []

    for driver, team in drivers_teams.items():
        driver_laps = laps.pick_drivers([driver])[
            ["Driver", "LapNumber", "LapTime", "Compound", "TyreLife", "IsAccurate"]
        ].copy()
        driver_laps["Team"] = team
        driver_laps["Race"] = race_name
        driver_laps["Round"] = round_number
        lap_data.append(driver_laps)

    return pd.concat(lap_data, ignore_index=True)

df = get_lap_times(session, 1, "Australia", drivers_teams)
print(df)
df1 = get_lap_times(session1, 2, "China", drivers_teams)
print(df1)
df2 = get_lap_times(session2, 3, "Japan", drivers_teams)
print(df2)
df3 = get_lap_times(session3, 4, "USA", drivers_teams)
print(df3)
df4 = get_lap_times(session4, 5, "Canada", drivers_teams)
print(df4)


df_all_lap_times = pd.concat([df, df1, df2, df3, df4], ignore_index=True)
df_all_lap_times["LapTimeSeconds"] = df_all_lap_times["LapTime"].dt.total_seconds()
df_clean = df_all_lap_times[df_all_lap_times["IsAccurate"] == True].copy()
df_clean = df_clean.drop(columns=["LapTime"])
df_clean.to_excel("../excel/lap_times_all_2026.xlsx", index=False)
print(f"Total filas: {len(df_clean)}")