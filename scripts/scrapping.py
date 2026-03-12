import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import csv

# defining netflix wikipedia url
url = "https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(since_2025)"
headers = {"User-Agent": "Mozilla/5.0"}

# requesting webpage
response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Failed to retrieve webpage")
    exit()

# parse the webpage and locate tables
soup = BeautifulSoup(response.text, "lxml")
tables = soup.find_all("table", {"class": "wikitable"})

films = []

# extract first five columns
for table in tables:
    rows = table.find_all("tr")

    for row in rows[1:]:
        cols = row.find_all("td")

        title = cols[0].get_text(strip=True) if len(cols) > 0 else ""
        release_date = cols[1].get_text(strip=True) if len(cols) > 1 else ""
        genre = cols[2].get_text(strip=True) if len(cols) > 2 else ""
        runtime = cols[3].get_text(strip=True) if len(cols) > 3 else ""
        language = cols[4].get_text(strip=True) if len(cols) > 4 else ""

        films.append({
            "Title": title,
            "Release Date": release_date,
            "Genre": genre,
            "Runtime": runtime,
            "Language": language
        })

# save dataset
today = datetime.now().strftime("%Y-%m-%d")

filename = f"scraped_data/netflix_films_5cols_{today}.csv"

with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["Title", "Release Date", "Genre", "Runtime", "Language"]
    )
    writer.writeheader()
    writer.writerows(films)

print("Dataset saved:", filename)

#scrapping exploding topics data generated per day
# Path to your HTML file
# --- Import libraries ---
today = datetime.now().strftime("%Y-%m-%d")

# =========================================================
# SCRAPER 1: Projected Data Explosion Table
# =========================================================
# Load local HTML file
data_path = r"C:\Users\USER\OneDrive\Desktop\projects\Web Scraping Datasets\data.HTML" # raw string to avoid backslash issues
with open(data_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

table = soup.find("table")
data_rows = []

for row in table.find_all("tr")[1:]:  # skip header
    cols = row.find_all("td")
    if len(cols) < 2:
        continue
    year = cols[0].get_text(strip=True)
    data_generated = cols[1].get_text(strip=True)
    change_absolute = cols[2].get_text(strip=True) if len(cols) > 2 else "-"
    change_percent = cols[3].get_text(strip=True) if len(cols) > 3 else "-"
    data_rows.append({
        "Year": year,
        "Data Generated": data_generated,
        "Change Over Previous Year": change_absolute,
        "Change Over Previous Year (%)": change_percent
    })

# Save CSV
filename = f"scraped_data/data_generated_{today}.csv"
with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["Year", "Data Generated", "Change Over Previous Year", "Change Over Previous Year (%)"]
    )
    writer.writeheader()
    writer.writerows(data_rows)

print(f"Projected data table saved: {filename}")