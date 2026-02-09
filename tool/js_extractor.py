from bs4 import BeautifulSoup
import requests
import sys

s = BeautifulSoup(requests.get(sys.argv[1]).text, 'html.parser')
for j in s.find_all('script'):
    print(j.get('src'))
