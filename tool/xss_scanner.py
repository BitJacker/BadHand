import requests
import sys

def scan_xss(url):
    payloads = ["<script>alert(1)</script>", "<img src='x' onerror='alert(1)'>"]
    for payload in payloads:
        response = requests.get(url + payload)
        if payload in response.text:
            print(f"XSS vulnerability found at: {url}")
            return
    print("No XSS vulnerabilities found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python xss_scanner.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    scan_xss(url)
