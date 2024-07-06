import requests
from bs4 import BeautifulSoup
from googlesearch import search
from time import sleep

def get_page_title_and_description(url):
    try:
        # Fazendo a requisição para a URL
        response = requests.get(url)
        response.raise_for_status()  # Verificando se a requisição foi bem-sucedida

        # Parseando o conteúdo HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Obtendo o título da página
        title = soup.title.string if soup.title else 'No title found'

        # Obtendo a descrição da página
        description_tag = soup.find('meta', attrs={'name': 'description'})
        description = description_tag['content'] if description_tag else 'No description found'

        return title, description
    except requests.RequestException as e:
        return f'Error fetching the URL: {e}', None

class SearchEngine:

    def __init__(self, person) -> None:
        self.person = person

    def standard(self, num):
        websites = list(search(f'intext:{self.person}', tld="com", start=0, stop=num, pause=2))
        documents = list(search(f'{self.person} filetype:pdf', tld="com", start=0, stop=num, pause=2))
        
        # Adicionando título e descrição às URLs
        websites_info = [(url, *get_page_title_and_description(url)) for url in websites]
        documents_info = [(url, *get_page_title_and_description(url)) for url in documents]

        social_networks = {
            "instagram": list(search(f'{self.person} site:instagram.com', tld="com", start=0, stop=1, pause=2)),
            "facebook": list(search(f'{self.person} site:facebook.com', tld="com", start=0, stop=1, pause=2)),
            "twitter X": list(search(f'{self.person} site:x.com', tld="com", start=0, stop=1, pause=2)),
            "tiktok": list(search(f'{self.person} site:tiktok.com', tld="com", start=0, stop=1, pause=2)),
            "youtube": list(search(f'{self.person} site:youtube.com inurl:channel', tld="com", start=0, stop=1, pause=2)),
            "linkedin": list(search(f'{self.person} site:linkedin.com', tld="com", start=0, stop=1, pause=2)),
            "pinterest": list(search(f'{self.person} site:pinterest.com', tld="com", start=0, stop=1, pause=2)),
            "reddit": list(search(f'{self.person} site:reddit.com', tld="com", start=0, stop=1, pause=2))
        }

        return {
            'websites': websites_info,
            'documents': documents_info,
            'social networks': social_networks
        }

    def advanced(self, num, keyword):
        websites = list(search(f'intext:{self.person} + {keyword}', tld="com", start=0, stop=num, pause=2))
        documents = list(search(f'{self.person} + {keyword} filetype:pdf', tld="com", start=0, stop=num, pause=2))
        
        # Adicionando título e descrição às URLs
        websites_info = [(url, *get_page_title_and_description(url)) for url in websites]
        documents_info = [(url, *get_page_title_and_description(url)) for url in documents]

        social_networks = {
            "instagram": list(search(f'{self.person} + {keyword} site:instagram.com', tld="com", start=0, stop=1, pause=2)),
            "facebook": list(search(f'{self.person} + {keyword} site:facebook.com', tld="com", start=0, stop=1, pause=2)),
            "twitter X": list(search(f'{self.person} + {keyword} site:x.com', tld="com", start=0, stop=1, pause=2)),
            "tiktok": list(search(f'{self.person} + {keyword} site:tiktok.com', tld="com", start=0, stop=1, pause=2)),
            "youtube": list(search(f'{self.person} + {keyword} site:youtube.com inurl:channel', tld="com", start=0, stop=1, pause=2)),
            "linkedin": list(search(f'{self.person} + {keyword} site:linkedin.com', tld="com", start=0, stop=1, pause=2)),
            "pinterest": list(search(f'{self.person} + {keyword} site:pinterest.com', tld="com", start=0, stop=1, pause=2)),
            "reddit": list(search(f'{self.person} + {keyword} site:reddit.com', tld="com", start=0, stop=1, pause=2))
        }

        return {
            'websites': websites_info,
            'documents': documents_info,
            'social networks': social_networks
        }
