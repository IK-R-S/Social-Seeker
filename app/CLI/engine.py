from googlesearch import search
from time import sleep

# Search engines
class SearchEngine_STANDARD:
    def __init__(self, person) -> None:
        self.response = []
        self.person = person
    
    def websites(self, num):
        self.response = []
        for url in search(f'intext:{self.person}', tld="com", lang="en", start=0, stop=num, pause=2):
            self.response.append(url)
        return self.response

    def documents(self, num):
        self.response = []
        for url in search(f'{self.person} filetype:pdf', tld="com", lang="en", start=0, stop=num, pause=2):
            self.response.append(url)
        return self.response

    def instagram(self, num):
        self.response = []
        for url in search(f'{self.person} site:instagram.com', tld="com", lang="en", start=0, stop=num, pause=2):
            self.response.append(url)
        return self.response

class SearchEngine_ADVANCED:
    def __init__(self, person, keyword) -> None:
        self.response = []
        self.person = person
        self.keyword = keyword
    
    def websites(self, num):
        self.response = []
        for url in search(f'intext:{self.person} + {self.keyword}', tld="com", lang="en", start=0, stop=num, pause=2):
            self.response.append(url)
        return self.response

    def documents(self, num):
        self.response = []
        for url in search(f'{self.person} + {self.keyword} filetype:pdf', tld="com", lang="en", start=0, stop=num, pause=2):
            self.response.append(url)
        return self.response

    def instagram(self, num):
        self.response = []
        for url in search(f'{self.person} + {self.keyword} site:instagram.com', tld="com", lang="en", start=0, stop=num, pause=2):
            self.response.append(url)
        return self.response
