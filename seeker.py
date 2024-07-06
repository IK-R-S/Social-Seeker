from engine import SearchEngine, get_page_title_and_description
from components import *
from time import sleep
import argparse

parser = argparse.ArgumentParser(prog='seeker.py', description='Find all about someone on internet')

parser.add_argument('-k', '--keyword', dest='keyword', help='Add a keyword to search about the person')
parser.add_argument('-p', '--person', dest='person', help='Person to search')

args = parser.parse_args()

person = args.person

if args.keyword:
    keyword = args.keyword
    Components.clearConsole()
    print(f'Searching for {keyword} related to {person} on the web...')
    engine = SearchEngine(person=person)
    results = engine.advanced(2, keyword=keyword)
else:
    Components.clearConsole()
    print(f'Searching for {person} on the web...')
    engine = SearchEngine(person=person)
    results = engine.standard(2)

# Printando resultados com título e descrição
for category, items in results.items():
    print(f"\n{category.capitalize()}:")
    if isinstance(items, dict):  # Social networks
        for network, urls in items.items():
            print(f"\n{network.capitalize()}:")
            for url in urls:
                title, description = get_page_title_and_description(url)
                print(f"URL: {url}\nTitle: {title}\nDescription: {description}\n")
    else:
        for url, title, description in items:
            print(f"URL: {url}\nTitle: {title}\nDescription: {description}\n")
