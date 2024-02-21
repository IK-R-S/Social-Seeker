# DUCKGO SEARCH ENGINE - Beta

from components import *
from bs4 import BeautifulSoup
import requests

# https://duckduckgo.com/?q= {PESQUISA}
# https://duckduckgo.com/?q= {PESQUISA} &ia=web
# https://duckduckgo.com/?t=h_&q= {PESQUISA} &ia=web

query =  'python'
url = f'https://duckduckgo.com/?q={query}'

req = requests.get(url)

soup = BeautifulSoup(req.text, 'html.parser')

print(soup)