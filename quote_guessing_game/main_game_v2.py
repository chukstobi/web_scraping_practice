from bs4 import BeautifulSoup
from csv import DictReader,DictWriter
import requests
import random

BASE_URL = "http://quotes.toscrape.com"

class QuoteGuessingGame:
    main_player_score = 0
    def read_quotes(self, filename):
        with open(filename, "r") as file:
            csv_reader = DictReader(file)
            return list(csv_reader)  
        
    def main_game(self, quotes):
        self.main_player_score
        read_player_score = open('player_score.csv',"r")
        high_score = 0
        for score in read_player_score:
            high_score = int(score)
            
        quote = random.choice(quotes)
        remaining_guesses = 4

        print(f"Enter 'quit' to quit game\nHigh Score: {high_score}")
        print(f"Here's a quote\n{quote['text']}")
        print(quote['author'])
        
        guess = input(f"Who said this quote?\nGuesses remaining:{remaining_guesses}\n> ")
        if guess.lower() == quote["author"].lower() and remaining_guesses > 0:
            print("You win")
            self.main_player_score += 5
            print("Your score:",self.main_player_score)
            return self.main_game(quotes)

        elif guess.lower() == "quit".lower() and remaining_guesses > 0:
            print("Your score:",self.main_player_score)
        
        elif guess.lower() != quote["author"].lower() and remaining_guesses > 0:
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
                print(self.main_player_score)
            
        if self.main_player_score > high_score:
            print(f'New High Score: {self.main_player_score}')
            player_score = open('player_score.csv',"w")
            player_score.write(f"{self.main_player_score}")
        else:
            pass

    def begin(self):
        quotes = self.read_quotes("all_quotes.csv")
        self.main_game(quotes)

game = QuoteGuessingGame()
game.begin()

# filename = open("player_details.csv","r")
# for f in filename:
#     print(f)
# read_player_score = open('player_score.csv',"r")
# read_player_score
# for score in read_player_score:
#     print("score")
    
#     print(score)
