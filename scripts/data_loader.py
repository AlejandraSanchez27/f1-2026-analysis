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
# URL de la API para pilotos 2026
DRIVERS_URL = "https://api.jolpi.ca/ergast/f1"
SEASON = 2026 # Temporada que se va a consultar

def get_drivers():
    url = f"{DRIVERS_URL}/{SEASON}/drivers.json"

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
    # Obtiene los datos crudos desde la API
    data = get_schedule()

    # Procesa y organiza la informacion
    schedule = parse_schedule(data)

    # Convierte la lista en un DataFrame de pandas
    df = pd.DataFrame(schedule)
    df.to_csv("data/schedule_2026.csv", index=False)
    print("Guardado!")
    # Refleja el dataframe completo
    #print(df)

    #Filtra el dataframe por carreras por país
    #print(df["country"].value_counts())

    #filtra el dataframe info de un solo país (USA)
    #print(df[df["country"] == "USA"])

    #filtra trae la info segun el round seleccionado
    #print(df[df["round"] == "1"])

    # Recorre e imprime cada carrera individualmente
    """
    for race in schedule:
        print(race["round"], race["name"], race["date"], race["country"])
    """

    # Otra forma de acceder a los datos originales de la API
    """
    races = data["MRData"]["RaceTable"]["Races"]

    # Imprime el total de carreras de la temporada
    print(f"Total de carreras: {len(races)}")
    #print(data)
    
    # Recorre e imprime ronda, nombre y fecha
    for race in races:
        print(race["round"], race["raceName"], race["date"])
    """