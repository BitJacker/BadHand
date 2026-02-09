import socket
import sys

s = socket.socket()
s.settimeout(2)

try:
    s.connect((sys.argv[1], 80))
    print('Normal Server')
except:
    print('Possible Honeypot / Stealth Host')
