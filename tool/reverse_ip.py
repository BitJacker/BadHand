import requests
import sys

print(requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={sys.argv[1]}').text)
