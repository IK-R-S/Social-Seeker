from googlesearch import search
from time import sleep

# Search engine


class SearchEngine:

    def __init__(self, person) -> None:
        self.person = person
    
    def standard(self, num):

        websites = list(search(f'intext:{self.person}', tld="com", start=0, stop=num, pause=2))

        documents = list(search(f'{self.person} filetype:pdf', tld="com", start=0, stop=num, pause=2))
    
        social_networks = {
            "instagram": list(search(f'{self.person} site:instagram.com', tld="com", start=0, stop=1, pause=2)),
            "facebook": list(search(f'{self.person} site:facebook.com', tld="com", start=0, stop=1, pause=2)),
            "twitter X": list(search(f'{self.person} site:x.com', tld="com", start=0, stop=1, pause=2)),
            "tiktok": list(search(f'{self.person} site:tiktok.com', tld="com", start=0, stop=1, pause=2)),
            "youtube": list(search(f'{self.person} site:youtube.com inurl:channel', tld="com", start=0, stop=1, pause=2))
        }
        
        return {'websites': websites, 'documents': documents, 'social networks': social_networks}

    def advanced(self, num, keyword):
        
        websites = list(search(f'intext:{self.person} + {keyword}', tld="com", start=0, stop=num, pause=2))

        documents = list(search(f'{self.person} + {keyword} filetype:pdf', tld="com", start=0, stop=num, pause=2))

        social_networks = {
            "instagram": list(search(f'{self.person} + {keyword} site:instagram.com', tld="com", start=0, stop=1, pause=2)),
            "facebook": list(search(f'{self.person} + {keyword} site:facebook.com', tld="com", start=0, stop=1, pause=2)),
            "twitter X": list(search(f'{self.person} + {keyword} site:x.com', tld="com", start=0, stop=1, pause=2)),
            "tiktok": list(search(f'{self.person} + {keyword} site:tiktok.com', tld="com", start=0, stop=1, pause=2)),
            "youtube": list(search(f'{self.person} + {keyword} site:youtube.com inurl:channel', tld="com", start=0, stop=1, pause=2))
        }

        return {'websites': websites, 'documents': documents, 'social networks': social_networks}
