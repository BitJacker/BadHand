import dns.resolver
import sys

for r in ['A', 'MX', 'NS', 'TXT']:
    try:
        [print(f'{r}: {i}') for i in dns.resolver.resolve(sys.argv[1], r)]
    except:
        pass
