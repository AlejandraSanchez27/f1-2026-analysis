import requests

BASE_URL = "https://api.jolpi.ca/ergast/f1"
SEASON = 2026

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