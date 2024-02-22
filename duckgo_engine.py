# DUCKGO SEARCH ENGINE - Beta

from components import *
from bs4 import BeautifulSoup
import requests

# https://duckduckgo.com/?q= {PESQUISA}
# https://duckduckgo.com/?q= {PESQUISA} &ia=web
# https://duckduckgo.com/?t=h_&q= {PESQUISA} &ia=web

query = 'python'
url = f'https://duckduckgo.com/?q={query}&ia=web'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

req = requests.get(url, headers=headers)

soup = BeautifulSoup(req.text, 'html.parser')

elementos = soup.find_all("span", class_="EKtkFWMYpwzMKOYr0GYm LQVY1Jpkk8nyJ6HBWKAk")

print(soup)
