import requests

BASE_URL = "https://api.jolpi.ca/ergast/f1"
SEASON = 2026

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