# --- STEP 1: Import libraries ---
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os

# --- STEP 2: Create data folder if it doesn't exist ---
if not os.path.exists("data"):
    os.makedirs("data")

today = datetime.now().strftime("%Y-%m-%d")

# --- FUNCTION: Scrape Netflix Wikipedia ---
def scrape_netflix():
    url = "https://en.wikipedia.org/wiki/List_of_Netflix_original_films_(since_2025)"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    films = []
    for table in soup.find_all("table", {"class": "wikitable"}):
        for row in table.find_all("tr")[1:]:
            cols = row.find_all("td")
            if len(cols) >= 5:
                films.append([
                    cols[0].get_text(strip=True),
                    cols[1].get_text(strip=True),
                    cols[2].get_text(strip=True),
                    cols[3].get_text(strip=True),
                    cols[4].get_text(strip=True)
                ])

    filename = f"data/netflix_films_{today}.csv"
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Release Date", "Genre", "Language", "Notes"])
        writer.writerows(films)

    print(f"Wikipedia Netflix data saved: {filename}")


# --- FUNCTION: Scrape Exploding Topics ---
def scrape_exploding():
    url = "https://explodingtopics.com/blog/data-generated-per-day"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table")
    if not table:
        raise Exception("Could not find the table on Exploding Topics page.")

    rows = table.find_all("tr")
    # Use first row for headers
    headers_list = [td.get_text(strip=True) for td in rows[0].find_all(["th", "td"])]

    data_rows = []
    for tr in rows[1:]:
        cells = tr.find_all("td")
        if cells:
            data_rows.append([td.get_text(strip=True) for td in cells])

    filename = f"data/exploding_topics_{today}.csv"
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers_list)
        writer.writerows(data_rows)

    print(f"Exploding Topics data saved: {filename}")


# --- MAIN ---
if __name__ == "__main__":
    scrape_netflix()
    scrape_exploding()