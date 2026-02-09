import requests
import sys

url = sys.argv[1]
for i in range(1, 20):
    if requests.get(f'{url}/?author={i}').status_code == 200:
        print(f'[+] User found: ID {i}')
