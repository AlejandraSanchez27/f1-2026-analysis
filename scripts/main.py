from drivers import get_drivers, parse_drivers
from schedule import get_schedule, parse_schedule
from constructors import get_constructors, parse_constructors
from results import get_race_results, parse_race_results

import pandas as pd

def main():
    # PILOTOS
    drivers_data = get_drivers()
    drivers = parse_drivers(drivers_data)
    drivers_df = pd.DataFrame(drivers)
    print("\n===== PILOTOS =====")
    print(drivers_df)


    # CALENDARIO F1 2026
    schedule_data = get_schedule()
    schedule = parse_schedule(schedule_data)
    schedule_df = pd.DataFrame(schedule)
    print("\n===== CALENDARIO 2026 =====")
    print(schedule_df)

    # Guarda en CSV (opcional)
    # schedule_df.to_csv("data/schedule_2026.csv", index=False)
    # print("Archivo guardado correctamente")

    # CONSTRUCTORES
    constructors_data = get_constructors()
    constructors = parse_constructors(constructors_data)
    constructors_df = pd.DataFrame(constructors)
    print("\n===== CONSTRUCTORES =====")
    print(constructors_df)

    # RESULTADOS DE CARRERA
    results_data = get_race_results(1)
    race_results = parse_race_results(results_data)
    results_df = pd.DataFrame(race_results)
    print("\n===== RESULTADOS DE CARRERA =====")
    print(results_df)

# Ejecuta el programa
if __name__ == "__main__":
    main()