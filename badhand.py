import os
import subprocess
import sys

# Imposta BASE_DIR per puntare alla cartella 'tool'
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tool")

class Colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    CYAN = '\033[36m'
    END = '\033[0m'

# Definisci il menu con le opzioni e gli script da eseguire
MENU = {
    "1": ("DDOS", "udp_attak.py"),
    "2": ("DEAUTHER", "deauther.py"),
    "3": ("SCAN", "scan.py"),
    "4": ("XSS SCANNER", "xss_scanner.py"),
    "5": ("SQL INJECTION SCANNER", "sqli_scanner.py"),
    "6": ("DIRECTORY BRUTEFORCE", "dir_bruteforce.py"),
    "7": ("SSL/TLS CERTIFICATE CHECKER", "ssl_checker.py"),
    "8": ("RCE TEST", "rce_test.py"),
    "9": ("CREDENTIAL STUFFING", "credential_stuffing.py"),
    "10": ("SUBDOMAIN ENUMERATION", "subdomain_enum.py"),
    "0": ("Exit", None)
}

def clear():
    os.system("clear")

def banner():
    print("""
██████╗  █████╗ ██████╗     ██╗  ██╗ █████╗ ███╗   ██╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗    ██║  ██║██╔══██╗████╗  ██║██╔══██╗
██████╔╝███████║██║  ██║    ███████║███████║██╔██╗ ██║██║  ██║
██╔══██╗██╔══██║██║  ██║    ██╔══██║██╔══██║██║╚██╗██║██║  ██║
██████╔╝██║  ██║██████╔╝    ██║  ██║██║  ██║██║ ╚████║██████╔╝
╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝
""")
    print("\n")

def run_script(script_name):
    script_path = os.path.join(BASE_DIR, script_name)

    if not os.path.isfile(script_path):
        print(f"{Colors.RED}Errore: Il file {script_name} non è stato trovato!{Colors.END}")
        return

    if script_name == "udp_attak.py":
        ip = input(f"{Colors.YELLOW}Inserisci l'IP di destinazione > {Colors.END}").strip()
        porta = input(f"{Colors.YELLOW}Inserisci la porta > {Colors.END}").strip()
        metodo = input(f"{Colors.YELLOW}Inserisci il metodo (es. 'UDP-Mix') > {Colors.END}").strip()

        if not ip or not porta or not metodo:
            print(f"{Colors.RED}Utilizzo: python udp_attak.py <IP> <PORTA> <METODO>{Colors.END}")
            return

        cmd = f"python3 {script_path} {ip} {porta} {metodo}"

    elif script_name == "scan.py":
        ip = input(f"{Colors.YELLOW}Inserisci l'IP da scansionare > {Colors.END}").strip()

        if not ip:
            print(f"{Colors.RED}Utilizzo: python scan.py <IP>{Colors.END}")
            return

        cmd = f"python3 {script_path} {ip}"

    elif script_name == "xss_scanner.py":
        url = input(f"{Colors.YELLOW}Inserisci l'URL da testare per XSS > {Colors.END}").strip()
        cmd = f"python3 {script_path} {url}"

    elif script_name == "sqli_scanner.py":
        url = input(f"{Colors.YELLOW}Inserisci l'URL da testare per SQL Injection > {Colors.END}").strip()
        cmd = f"python3 {script_path} {url}"

    elif script_name == "dir_bruteforce.py":
        url = input(f"{Colors.YELLOW}Inserisci l'URL da testare per Directory Brute Force > {Colors.END}").strip()
        wordlist = input(f"{Colors.YELLOW}Inserisci il percorso della wordlist > {Colors.END}").strip()
        cmd = f"python3 {script_path} {url} {wordlist}"

    elif script_name == "ssl_checker.py":
        domain = input(f"{Colors.YELLOW}Inserisci il dominio per il controllo SSL > {Colors.END}").strip()
        cmd = f"python3 {script_path} {domain}"

    elif script_name == "rce_test.py":
        url = input(f"{Colors.YELLOW}Inserisci l'URL da testare per RCE > {Colors.END}").strip()
        cmd = f"python3 {script_path} {url}"

    elif script_name == "credential_stuffing.py":
        url = input(f"{Colors.YELLOW}Inserisci l'URL per il Credential Stuffing > {Colors.END}").strip()
        username = input(f"{Colors.YELLOW}Inserisci il nome utente > {Colors.END}").strip()
        wordlist = input(f"{Colors.YELLOW}Inserisci il percorso della wordlist > {Colors.END}").strip()
        cmd = f"python3 {script_path} {url} {username} {wordlist}"

    elif script_name == "subdomain_enum.py":
        domain = input(f"{Colors.YELLOW}Inserisci il dominio per la Subdomain Enumeration > {Colors.END}").strip()
        wordlist = input(f"{Colors.YELLOW}Inserisci il percorso della wordlist > {Colors.END}").strip()
        cmd = f"python3 {script_path} {domain} {wordlist}"

    elif script_name == "deauther.py":
        target_mac = input(f"{Colors.YELLOW}Inserisci l'indirizzo MAC del target > {Colors.END}").strip()
        gateway_mac = input(f"{Colors.YELLOW}Inserisci l'indirizzo MAC del gateway > {Colors.END}").strip()
        interface = input(f"{Colors.YELLOW}Inserisci l'interfaccia di rete (es. wlan0) > {Colors.END}").strip()

        if not target_mac or not gateway_mac or not interface:
            print(f"{Colors.RED}Utilizzo: python deauther.py <target_mac> <gateway_mac> <interface>{Colors.END}")
            return

        cmd = f"sudo python3 {script_path} {target_mac} {gateway_mac} {interface}"

    # Esegui lo script in un nuovo terminale
    try:
        subprocess.Popen(["xfce4-terminal", "--hold", "--command", cmd])
    except FileNotFoundError:
        os.system(f"python3 {script_path} {cmd}")

def menu():
    print(f"{Colors.BLUE}{'='*50}{Colors.END}")
    print(f"{Colors.YELLOW}{'Created by BitJacker':^50}{Colors.END}")
    print(f"{Colors.CYAN}{'Cybersecurity Network Testing Lab':^50}{Colors.END}")
    print(f"{Colors.BLUE}{'='*50}{Colors.END}\n")

    for key, value in MENU.items():
        print(f"{Colors.GREEN}{key}. {value[0]}{Colors.END}")

def main():
    while True:
        clear()
        banner()
        menu()

        choice = input(f"\n{Colors.YELLOW}Seleziona un'opzione > {Colors.END}").strip()

        if choice == "0":
            print(f"{Colors.BLUE}Uscita...{Colors.END}")
            sys.exit(0)

        elif choice in MENU and MENU[choice][1]:
            run_script(MENU[choice][1])

        else:
            input(f"{Colors.RED}Scelta non valida. PREMI ENTER per riprovare{Colors.END}")

if __name__ == "__main__":
    main()
