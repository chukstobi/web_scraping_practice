from bs4 import BeautifulSoup
from csv import DictWriter
import requests
import random

BASE_URL = "http://quotes.toscrape.com"

# def scrape_quotes():
#     all_quotes = []
#     url = '/page/1'
#     while url:
#         res = requests.get(f"{BASE_URL}{url}")
#         print(f"Now Scraping {BASE_URL}{url}.....")
#         soup = BeautifulSoup(res.text, 'html.parser')
#         quotes = soup.find_all(class_='quote')
#         for quote in quotes:
#             all_quotes.append({
#                 'text':quote.find(class_='text').get_text(),
#                 'author':quote.find(class_="author").get_text(),
#                 'bio-link':quote.find('a')['href']
#             })

#         next_btn = soup.find(class_='next')
#         url = next_btn.find('a')['href'] if next_btn else None
#         return all_quotes

# def write_quotes(quotes):
#     with open("all_quotes.csv", "w") as file:
#         headers = ["text", "author", "bio-link"]
#         csv_writer = DictWriter(file, fieldnames=headers)
#         csv_writer.writeheader()
#         for quote in quotes:
#             csv_writer.writerow(quote)

all_quotes = []
url = '/page/1'
while url:
    res = requests.get(f"{BASE_URL}{url}")
    print(f"Now Scraping {BASE_URL}{url}.....")
    soup = BeautifulSoup(res.text, 'html.parser')
    quotes = soup.find_all(class_='quote')
    for quote in quotes:
        all_quotes.append({
            'text':quote.find(class_='text').get_text(),
            'author':quote.find(class_="author").get_text(),
            'bio-link':quote.find('a')['href']
        })

    next_btn = soup.find(class_='next')
    url = next_btn.find('a')['href'] if next_btn else None

with open("all_quotes.csv", "w") as file:
    headers = ["text", "author", "bio-link"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for quote in quotes:
        csv_writer.writerow(all_quotes[0])

# quotes = scrape_quotes()
# quotes
# write_quotes(quotes)