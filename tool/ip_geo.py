import requests
import sys

print(requests.get(f'http://ip-api.com/json/{sys.argv[1]}').json())
