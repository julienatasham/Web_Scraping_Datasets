# Import libraries
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os

# Target webpage
url = "https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(since_2025)"
headers = {"User-Agent": "Mozilla/5.0"}

# Request webpage
response = requests.get(url, headers=headers)
response.raise_for_status()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

films = []

# Extract table data
for table in soup.find_all("table", {"class": "wikitable"}):
    for row in table.find_all("tr")[1:]:
        cols = row.find_all("td")

        title = cols[0].get_text(strip=True) if len(cols) > 0 else ""
        release_date = cols[1].get_text(strip=True) if len(cols) > 1 else ""
        genre = cols[2].get_text(strip=True) if len(cols) > 2 else ""
        language = cols[3].get_text(strip=True) if len(cols) > 3 else ""
        notes = cols[4].get_text(strip=True) if len(cols) > 4 else ""

        films.append([title, release_date, genre, language, notes])

# Create folder if it doesn't exist
os.makedirs("scraped_data", exist_ok=True)

# Save dataset
today = datetime.now().strftime("%Y-%m-%d")
filename = f"scraped_data/netflix_films_{today}.csv"

with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title","Release Date","Genre","Language","Notes"])
    writer.writerows(films)

print("Data successfully saved:", filename)