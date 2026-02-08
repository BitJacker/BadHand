import requests
import sys

def brute_force_directories(url, wordlist):
    with open(wordlist, 'r') as file:
        for line in file:
            directory = line.strip()
            response = requests.get(url + "/" + directory)
            if response.status_code == 200:
                print(f"Found directory: {url}/{directory}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python dir_bruteforce.py <url> <wordlist>")
        sys.exit(1)

    url = sys.argv[1]
    wordlist = sys.argv[2]
    brute_force_directories(url, wordlist)
