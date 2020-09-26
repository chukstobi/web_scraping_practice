from bs4 import BeautifulSoup
from csv import DictReader
import requests
import random

BASE_URL = "http://quotes.toscrape.com"

def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)

def start_game(quotes):
    quote = random.choice(quotes)
    remaining_guesses = 4
    new_game = print(f"Here's a quote\n{quote['text']}")
    print(quote['author'])
    guess = ''

    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote?\nGuesses remaining:{remaining_guesses}\n> ")
        if guess.lower() == quote["author"].lower():
            print("You win")
            new_game
        remaining_guesses -= 1
        if remaining_guesses == 3:
            res = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, 'html.parser')
            birth_date = soup.find(class_='author-born-date').get_text()
            birth_place =soup.find(class_='author-born-location').get_text()
            print(f"Here's a hint: The author was born on {birth_date} {birth_place}")
        elif remaining_guesses == 2:
            print(f"Here's a hint: The author first name starts with {quote['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print(f"Here's a hint: The author last name starts with {last_initial}")
        else:
            print(f"You Loss.\nAnswer: {quote['author']}")

    again = ""
    while again.lower() not in ("y", 'yes', 'n', "no"):
        again = input("Would you like to play again (y/n)? ")
    if again.lower() in ('yes', 'y'):
        return start_game(quotes)
    else:
        print("Goodbye")

quotes = read_quotes("all_quotes.csv")
start_game(quotes)
