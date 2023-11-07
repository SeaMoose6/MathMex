import requests
import wikipediaapi
from bs4 import BeautifulSoup
from googletrans import Translator

def language(lang):
    english_name = "Pythagorean_theorem"
    spanish_name = "Teorema_de_Pitágoras"
    fr_name = "héorème_de_Pythagore"
    zh_name = "勾股定理"
    if lang == "en":
      name = english_name
    elif lang == "es":
      name = spanish_name
    elif lang == "fr":
      name = fr_name
    elif lang == "zh":
      name = zh_name
    english_name = "Pythagorean_theorem"
    spanish_name = "Teorema_de_Pitágoras"
    math_link = f"https://{lang}.wikipedia.org/wiki/{name}"
    response = requests.get(math_link)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.find_all('p')
    print(text[1:2])

#language("en")
language("es")
