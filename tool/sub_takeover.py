import requests
import sys

subdomains = ['www', 'dev', 'api', 'blog', 'test']

for sub in subdomains:
    d = f'{sub}.{sys.argv[1]}'
    try:
        r = requests.get(f'http://{d}')
        if r.status_code == 200:
            print(f'[+] Subdomain Takeover possible: {d}')
    except:
        pass
