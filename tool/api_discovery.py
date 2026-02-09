import requests
import sys

endpoints = ['/api/v1/', '/api/', '/v1/', '/v2/']

for endpoint in endpoints:
    url = sys.argv[1] + endpoint
    r = requests.get(url)
    if r.status_code == 200:
        print(f'[+] Found API endpoint: {url}')
