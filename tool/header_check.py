import requests
import sys

headers = requests.get(sys.argv[1]).headers
for x in ['Content-Security-Policy', 'X-Frame-Options', 'Strict-Transport-Security']:
    print(f'{x}: {headers.get(x, "MISSING")}')
