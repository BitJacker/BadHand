import dns.resolver
import sys

try:
    r = dns.resolver.resolve(sys.argv[1], 'TXT')
    print('SPF Records:', [x.to_text() for x in r if 'spf' in x.to_text().lower()])
except:
    print('No SPF found!')
