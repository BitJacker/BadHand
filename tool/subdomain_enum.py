import socket
import sys

for s in open(sys.argv[2]):
    d = f'{s.strip()}.{sys.argv[1]}'
    try:
        print(f'[+] {d}: {socket.gethostbyname(d)}')
    except:
        pass
