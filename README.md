# Netflix Films Web Scraping Dataset

## Project Overview
This project collects data about Netflix original films from Wikipedia using Python web scraping techniques. The script extracts information from tables on the webpage and saves it as a structured CSV dataset.

## Data Source
Wikipedia page containing Netflix original films released since 2025.

## Tools and Technologies
- Python
- Requests
- BeautifulSoup (bs4)
- CSV
- Git & GitHub

## Project Structure

netflix-web-scraper/
│
├── scripts/
│   └── scrape_netflix.py
│
├── scraped_data/
│   └── netflix_films_YYYY-MM-DD.csv
│
├── requirements.txt
└── README.md

## Installation

Install required libraries:

pip install -r requirements.txt

## How to Run

Run the script:

python scripts/scrape_netflix.py

The dataset will automatically be saved in the `scraped_data` folder.

## Output Dataset Columns

- Title
- Release Date
- Genre
- Language
- Notes

## Purpose

This project demonstrates:
- Web scraping
- Data extraction from HTML tables
- Dataset generation using Python
- Basic data pipeline workflow
