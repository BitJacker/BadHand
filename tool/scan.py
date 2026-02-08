import socket
import os
import sys

def scan_ip(ip):
    print(f"Scanning IP: {ip}")
    response = os.system(f"ping -c 1 {ip}")
    if response == 0:
        print(f"{ip} is up")
    else:
        print(f"{ip} is down")

def scan_ports(ip, port_range):
    print(f"Scanning ports on {ip}")
    for port in range(1, port_range+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python scan.py <ip> <port_range>")
        sys.exit(1)

    ip = sys.argv[1]
    port_range = int(sys.argv[2])

    scan_ip(ip)
    scan_ports(ip, port_range)
