import ssl
import socket
import sys

def check_ssl(domain):
    context = ssl.create_default_context()
    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            print(f"SSL/TLS Certificate for {domain} is valid!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ssl_checker.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    check_ssl(domain)
