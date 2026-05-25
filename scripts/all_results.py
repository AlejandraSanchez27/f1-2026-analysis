import requests

BASE_URL = "https://api.jolpi.ca/ergast/f1"
SEASON = 2026

def get_all_results():
    url = f"{BASE_URL}/{SEASON}/results.json?limit=600"
    response = requests.get(url, timeout=10)
    data = response.json()
    return data

def parse_all_results(data):
    races = data["MRData"]["RaceTable"]["Races"]
    result = []
    for race in races:
        for race_result in race["Results"]:
            result.append({
                "round": race["round"],
                "race_name": race["raceName"],
                "date": race["date"],
                "position": race_result["position"],
                "grid": race_result["grid"],
                "points": race_result["points"],
                "status": race_result["status"],
                "driver_code": race_result["Driver"]["code"],
                "constructor": race_result["Constructor"]["name"]
            })
    return result

