import requests

BASE_URL = "https://api.jolpi.ca/ergast/f1"
SEASON = 2026

def get_schedule():
    url = f"{BASE_URL}/{SEASON}.json"
    response = requests.get(url, timeout=10)
    data = response.json()
    return data
def parse_schedule(data):
    races = data["MRData"]["RaceTable"]["Races"]
    result = []
    for race in races:
        result.append({
            "round": race["round"],
            "name": race["raceName"],
            "date": race["date"],
            "country": race["Circuit"]["Location"]["country"],
            "sprint": race.get("Sprint", {}).get("date", "N/A")
        })
    return result