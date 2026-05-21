import requests
import pandas as pd

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
            "country": race["Circuit"]["Location"]["country"]
        })
    return result

if __name__ == "__main__":
    data = get_schedule()
    schedule = parse_schedule(data)
    df = pd.DataFrame(schedule)
    #print(df)
    print(df["country"].value_counts())
    print(df[df["country"] == "USA"])
    print(df[df["round"] == "1"])
    """for race in schedule:
        print(race["round"], race["name"], race["date"], race["country"])"""
    """
    races = data["MRData"]["RaceTable"]["Races"]
    print(f"Total de carreras: {len(races)}")
    #print(data)
    for race in races:
        print(race["round"], race["raceName"], race["date"])
    """