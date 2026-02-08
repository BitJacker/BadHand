import dns.resolver
import sys

def subdomain_enum(domain, wordlist):
    with open(wordlist, 'r') as file:
        for line in file:
            subdomain = line.strip() + "." + domain
            try:
                dns.resolver.resolve(subdomain, 'A')
                print(f"Found subdomain: {subdomain}")
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
                pass

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python subdomain_enum.py <domain> <wordlist>")
        sys.exit(1)

    domain = sys.argv[1]
    wordlist = sys.argv[2]
    subdomain_enum(domain, wordlist)
