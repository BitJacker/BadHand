import ssl
import socket
import sys

c = ssl.create_default_context()

with socket.create_connection((sys.argv[1], 443)) as s:
    with c.wrap_socket(s, server_hostname=sys.argv[1]) as ss:
        print(ss.version(), ss.cipher())
