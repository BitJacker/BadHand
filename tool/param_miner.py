import requests
import sys

params = ['id', 'user', 'file', 'p', 'url']

for p in params:
    if requests.get(sys.argv[1], params={p: 'test'}).status_code == 200:
        print(f'Found Param: {p}')
