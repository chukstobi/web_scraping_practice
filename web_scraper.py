from bs4 import BeautifulSoup
import requests
import csv

response = requests.get("https://www.rithmschool.com/blog")
print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all('article')

file = open("blog.csv","w")
file.write

for article in articles:
    title = article.find("a").get_text()
    link = article.find("a")["href"]
    date = article.find('time')['datetime']
    print(title, link, date, sep=",", file=file)

file.close

print('done')
