import requests

BASE_URL = "https://api.jolpi.ca/ergast/f1"
SEASON = 2026


def get_race_results(round_number):
    url = f"{BASE_URL}/{SEASON}/{round_number}/results.json"
    response = requests.get(url, timeout=10)
    data = response.json()
    return data

def parse_race_results(data):
    races = data["MRData"]["RaceTable"]["Races"][0]["Results"]
    result = []
    for race in races:
        result.append({         
            "position": race["position"],
            "grid": race["grid"],
            "points": race["points"],
            "status": race["status"],

            "driver_code": race["Driver"]["code"],
            "driver_name": race["Driver"]["familyName"],

            "constructor": race["Constructor"]["name"]
        })
    return result