"""
Proyecto: Explorador del calendario de Fórmula 1 2026
Autor: Johana Alejandra Sánchez Vega

Descripción:
Este script consume la API Ergast/Jolpica de Fórmula 1 para
obtener el calendario oficial de la temporada 2026.
Posteriormente organiza la información en un DataFrame
para realizar análisis y filtros básicos con pandas.
"""

#importacion de librerias
import requests
import pandas as pd

# URL base de la API de Fórmula 1 (Ergast)
BASE_URL = "https://api.jolpi.ca/ergast/f1"
SEASON = 2026 # Temporada que se va a consultar
# Funcion->Data Escuderias
def get_constructors():
    url = f"{BASE_URL}/{SEASON}/constructors.json"
    response = requests.get(url, timeout=10)
    data = response.json()
    return data

def parse_constructors(data):
    constructors = data["MRData"]["ConstructorTable"]["Constructors"]
    result = []
    for constructor in constructors:
        result.append({
            "constructorId": constructor["constructorId"],
            "name": constructor["name"],
            "nationality": constructor.get("nationality", "N/A")
        })
    return result
# Funcion->Data pilotos
def get_drivers():
    url = f"{BASE_URL}/{SEASON}/drivers.json"
    response = requests.get(url, timeout=10)
    data = response.json()
    return data

def parse_drivers(data):
    drivers = data ["MRData"]["DriverTable"]["Drivers"]
    result = []
    for driver in drivers:
        result.append({
            "permanentNumber": driver.get("permanentNumber", "N/A"),
            "code": driver.get ("code", "N/A"),
            "givenName": driver ["givenName"],
            "familyName": driver ["familyName"],
            "dateOfBirth": driver.get("dateOfBirth", "N/A"),
            "nationality": driver.get("nationality", "N/A")
        })
    return result

# Funcion para obtener los datos del calendario desde la API
def get_schedule():
    # Construye la URL completa con la temporada
    url = f"{BASE_URL}/{SEASON}.json"
    # Hace la peticion GET a la API
    response = requests.get(url, timeout=10)
    # Convierte la respuesta JSON en diccionario de Python
    data = response.json()
    # Retorna los datos obtenidos
    return data

# Funcion para organizar y extraer la informacion importante
def parse_schedule(data):
    # Accede a la lista de carreras dentro del JSON
    races = data["MRData"]["RaceTable"]["Races"]
    # Estructura donde se almacenará la información procesada
    result = []
    # Ciclo que recorre cada carrera del calendario
    for race in races:
        result.append({
            "round": race["round"],
            "name": race["raceName"],
            "date": race["date"],
            "country": race["Circuit"]["Location"]["country"]
        })
    # Retorna la lista procesada
    return result
# Punto de entrada principal del programa
if __name__ == "__main__":
    import pandas as pd

def main():

    # =========================
    # PILOTOS
    # =========================
    
    # Obtiene datos de pilotos desde la API
    drivers_data = get_drivers()

    # Procesa los datos
    drivers = parse_drivers(drivers_data)

    # Convierte a DataFrame
    drivers_df = pd.DataFrame(drivers)

    # Muestra resultados
    print("\n===== PILOTOS =====")
    print(drivers_df)


    # =========================
    # CALENDARIO F1 2026
    # =========================

    # Obtiene calendario desde la API
    schedule_data = get_schedule()

    # Procesa los datos
    schedule = parse_schedule(schedule_data)

    # Convierte a DataFrame
    schedule_df = pd.DataFrame(schedule)

    # Muestra resultados
    print("\n===== CALENDARIO 2026 =====")
    print(schedule_df)

    # Guarda en CSV (opcional)
    # schedule_df.to_csv("data/schedule_2026.csv", index=False)
    # print("Archivo guardado correctamente")


    # =========================
    # CONSTRUCTORES
    # =========================

    # Obtiene datos de constructores
    constructors_data = get_constructors()

    # Procesa los datos
    constructors = parse_constructors(constructors_data)

    # Convierte a DataFrame
    constructors_df = pd.DataFrame(constructors)

    # Muestra resultados
    print("\n===== CONSTRUCTORES =====")
    print(constructors_df)


    # =========================
    # FILTROS Y ANALISIS
    # =========================

    # Carreras por país
    # print(schedule_df["country"].value_counts())

    # Información de carreras en USA
    # print(schedule_df[schedule_df["country"] == "USA"])

    # Información según ronda
    # print(schedule_df[schedule_df["round"] == "1"])


    # =========================
    # RECORRER CARRERAS
    # =========================

    """
    for race in schedule:
        print(
            race["round"],
            race["name"],
            race["date"],
            race["country"]
        )
    """


    # =========================
    # DATOS ORIGINALES DE LA API
    # =========================

    """
    races = schedule_data["MRData"]["RaceTable"]["Races"]

    print(f"Total de carreras: {len(races)}")

    for race in races:
        print(
            race["round"],
            race["raceName"],
            race["date"]
        )
    """


# Ejecuta el programa
if __name__ == "__main__":
    main()