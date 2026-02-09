import requests
import sys

if 'X-Frame-Options' not in requests.get(sys.argv[1]).headers:
    print('VULNERABLE')
