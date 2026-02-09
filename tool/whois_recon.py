import requests
import sys

r = requests.get(f'https://www.whoisxmlapi.com/whoisserver/WhoisService?domainName={sys.argv[1]}')
print(r.text)
