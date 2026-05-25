import requests

BASE_URL = "https://api.jolpi.ca/ergast/f1"
SEASON = 2026

def get_results_sprints():
    url = f"{BASE_URL}/{SEASON}/sprint.json?limit=600"
    response = requests.get(url, timeout=10)
    data = response.json()
    return data

def parse_results_sprints(data):
    sprints = data["MRData"]["RaceTable"]["Races"]
    result = []
    for sprint in sprints:
        for sprint_result in sprint["SprintResults"]:
            result.append({
                "round": sprint["round"],
                "raceName": sprint["raceName"],
                "date": sprint["date"],
                "position": sprint_result["position"],
                "grid": sprint_result["grid"],
                "points": sprint_result["points"],
                "status": sprint_result["status"],
                "driver_code": sprint_result["Driver"]["code"],
                "constructor": sprint_result["Constructor"]["name"]
            })
    return result
