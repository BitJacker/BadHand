import requests
import sys

print(requests.get(sys.argv[1] + '/robots.txt').text)
