# SOCIAL.SEEK - BUSCA ATIVA DE INFORMAÇÕES PESSOAIS

from googlesearch import search
from time import sleep

person = 'Neymar jr'
URLs = 3
response = []

class SearchEngine:
    def __init__(self) -> None:
        pass
    
    def Instagram():
        for url in search(f'{person} site:instagram.com', tld="com", lang="en", start=0, stop=URLs, pause=2):
            response.append(url)
            
        return response

thread = SearchEngine.Instagram()

print(thread)