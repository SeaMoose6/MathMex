import requests
from bs4 import BeautifulSoup

def language(lang):
    math_link = "https://en.wikipedia.org/wiki/Pythagorean_theorem"
    response = requests.get(math_link)
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.find('p')
    print(text.txt)

language("spanish")

