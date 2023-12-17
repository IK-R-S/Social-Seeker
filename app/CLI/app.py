from engine import SearchEngine_STANDARD, SearchEngine_ADVANCED
from components import *
from time import sleep

person = 'Jaqueline'
keyword = 'fazenda' 

class Application:
    def __init__(self) -> None:
        pass
    
    def start_STANDARD(self):
        # Defining a new standard search
        newSearch = SearchEngine_STANDARD(person=person)
        # Searching by modules
        websites = newSearch.websites(5)
        documents = newSearch.documents(3)
        instagram = newSearch.instagram(1)
        return {'websites': websites, 'documents': documents, 'instagram': instagram}
    
    def start_ADVANCED(self):
        # Defining a new advanced search
        newSearch = SearchEngine_ADVANCED(person=person, keyword=keyword)
        # Searching by modules
        websites = newSearch.websites(5)
        documents = newSearch.documents(3)
        instagram = newSearch.instagram(1)
        return websites, documents, instagram
