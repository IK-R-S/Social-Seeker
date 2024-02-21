from engine import SearchEngine
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
    print(results)
else:
    Components.clearConsole()
    print(f'Searching for {person} on the web...')
    engine = SearchEngine(person=person)
    results = engine.standard(2)
    print(results)
    