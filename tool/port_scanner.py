import socket
import threading
import sys

def s(p):
    c = socket.socket()
    c.settimeout(1)
    if not c.connect_ex((sys.argv[1], p)):
        print(f'Port {p} OPEN')
    c.close()

[threading.Thread(target=s, args=(p,)).start() for p in range(1, 1025)]
