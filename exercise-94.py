# Exercise 94 — Program that displays coronavirus case counts for a country
# Uses the disease.sh public API (no key required).
# ─────────────────────────────────────────────────────────────────────────────

import urllib.request
import json

API_URL = "https://disease.sh/v3/covid-19/countries/"

def get_covid_data(country: str) -> dict:
    url = API_URL + country
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read())

def main():
    country = input("Enter a country name (e.g. France, Morocco): ").strip()
    try:
        data = get_covid_data(country)
        print(f"\n=== COVID-19 Stats: {data['country']} ===")
        print(f"Total Cases    : {data['cases']:,}")
        print(f"Deaths         : {data['deaths']:,}")
        print(f"Recovered      : {data['recovered']:,}")
        print(f"Active Cases   : {data['active']:,}")
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    main()
