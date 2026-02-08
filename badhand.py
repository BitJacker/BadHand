import os
import subprocess
import sys

# Imposta BASE_DIR per puntare alla cartella 'tool'
# Assicurati che i file .py siano dentro una cartella chiamata 'tool' nella stessa posizione di questo script
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tool")

class Colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    CYAN = '\033[36m'
    END = '\033[0m'

# Configurazione Menu
MENU = {
    "1": ("DDOS (UDP Flood)", "udp_attak.py"),
    "2": ("DEAUTHER (WiFi)", "deauther.py"),
    "3": ("NETWORK SCAN", "scan.py"),
    "4": ("XSS SCANNER", "xss_scanner.py"),
    "5": ("SQL INJECTION SCANNER", "sqli_scanner.py"),
    "6": ("DIRECTORY BRUTEFORCE", "dir_bruteforce.py"),
    "7": ("SSL/TLS CHECKER", "ssl_checker.py"),
    "8": ("RCE TEST", "rce_test.py"),
    "9": ("CREDENTIAL STUFFING", "credential_stuffing.py"),
    "10": ("SUBDOMAIN ENUM", "subdomain_enum.py"),
    "0": ("Exit", None)
}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print(f"""{Colors.CYAN}
██████╗  █████╗ ██████╗     ██╗  ██╗ █████╗ ███╗   ██╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗    ██║  ██║██╔══██╗████╗  ██║██╔══██╗
██████╔╝███████║██║  ██║    ███████║███████║██╔██╗ ██║██║  ██║
██╔══██╗██╔══██║██║  ██║    ██╔══██║██╔══██║██║╚██╗██║██║  ██║
██████╔╝██║  ██║██████╔╝    ██║  ██║██║  ██║██║ ╚████║██████╔╝
╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝
{Colors.END}""")

def run_script(script_name):
    script_path = os.path.join(BASE_DIR, script_name)

    if not os.path.isfile(script_path):
        print(f"{Colors.RED}Errore: {script_name} non trovato in {BASE_DIR}{Colors.END}")
        input("Premi ENTER per continuare...")
        return

    cmd = ""

    # --- LOGICA ACQUISIZIONE DATI ---
    if script_name == "udp_attak.py":
        ip = input(f"{Colors.YELLOW}IP Target > {Colors.END}").strip()
        porta = input(f"{Colors.YELLOW}Porta > {Colors.END}").strip()
        metodo = input(f"{Colors.YELLOW}Metodo (UDP-Mix / UDP-Power) > {Colors.END}").strip()
        if ip and porta and metodo:
            cmd = f"python3 {script_path} {ip} {porta} {metodo}"

    elif script_name == "scan.py":
        ip = input(f"{Colors.YELLOW}IP da scansionare > {Colors.END}").strip()
        if ip: cmd = f"python3 {script_path} {ip}"

    elif script_name == "xss_scanner.py":
        url = input(f"{Colors.YELLOW}URL target > {Colors.END}").strip()
        if url: cmd = f"python3 {script_path} {url}"

    elif script_name == "sqli_scanner.py":
        url = input(f"{Colors.YELLOW}URL target > {Colors.END}").strip()
        if url: cmd = f"python3 {script_path} {url}"

    elif script_name == "dir_bruteforce.py":
        url = input(f"{Colors.YELLOW}URL target > {Colors.END}").strip()
        wordlist = input(f"{Colors.YELLOW}Percorso wordlist > {Colors.END}").strip()
        if url and wordlist: cmd = f"python3 {script_path} {url} {wordlist}"

    elif script_name == "ssl_checker.py":
        domain = input(f"{Colors.YELLOW}Dominio > {Colors.END}").strip()
        if domain: cmd = f"python3 {script_path} {domain}"

    elif script_name == "rce_test.py":
        url = input(f"{Colors.YELLOW}URL target > {Colors.END}").strip()
        if url: cmd = f"python3 {script_path} {url}"

    elif script_name == "credential_stuffing.py":
        url = input(f"{Colors.YELLOW}URL login > {Colors.END}").strip()
        user = input(f"{Colors.YELLOW}Username > {Colors.END}").strip()
        wlist = input(f"{Colors.YELLOW}Wordlist > {Colors.END}").strip()
        if url and user and wlist: cmd = f"python3 {script_path} {url} {user} {wlist}"

    elif script_name == "subdomain_enum.py":
        domain = input(f"{Colors.YELLOW}Dominio > {Colors.END}").strip()
        wlist = input(f"{Colors.YELLOW}Wordlist > {Colors.END}").strip()
        if domain and wlist: cmd = f"python3 {script_path} {domain} {wlist}"

    elif script_name == "deauther.py":
        target = input(f"{Colors.YELLOW}MAC Target > {Colors.END}").strip()
        gateway = input(f"{Colors.YELLOW}MAC Gateway > {Colors.END}").strip()
        iface = input(f"{Colors.YELLOW}Interfaccia (es. wlan0mon) > {Colors.END}").strip()
        if target and gateway and iface:
            cmd = f"sudo python3 {script_path} {target} {gateway} {iface}"

    # --- ESECUZIONE ---
    if not cmd:
        print(f"{Colors.RED}Dati insufficienti. Riprova.{Colors.END}")
        input("Premi ENTER per tornare al menu...")
        return

    try:
        # Prova ad aprire xfce4-terminal (tipico di Kali/Parrot)
        subprocess.Popen(["xfce4-terminal", "--hold", "-e", cmd])
        print(f"{Colors.GREEN}Script avviato in una nuova finestra.{Colors.END}")
    except FileNotFoundError:
        # Se xfce4 non c'è, esegue nel terminale attuale
        print(f"{Colors.CYAN}Terminale esterno non trovato. Avvio locale...{Colors.END}")
        print(f"{Colors.BLUE}Esecuzione: {cmd}{Colors.END}\n")
        os.system(cmd)
    
    input(f"\n{Colors.GREEN}Sessione terminata. Premi ENTER per il menu...{Colors.END}")

def menu_display():
    print(f"{Colors.BLUE}{'='*55}{Colors.END}")
    print(f"{Colors.YELLOW}{'Created by BitJacker':^55}{Colors.END}")
    print(f"{Colors.CYAN}{'Cybersecurity Network Testing Lab v2.0':^55}{Colors.END}")
    print(f"{Colors.BLUE}{'='*55}{Colors.END}\n")

    for key, value in MENU.items():
        print(f" {Colors.GREEN}[{key}]{Colors.END} {value[0]}")

def main():
    while True:
        clear()
        banner()
        menu_display()

        choice = input(f"\n{Colors.YELLOW}BadHand > {Colors.END}").strip()

        if choice == "0":
            print(f"{Colors.BLUE}Chiusura in corso...{Colors.END}")
            break
        elif choice in MENU and MENU[choice][1]:
            run_script(MENU[choice][1])
        else:
            print(f"{Colors.RED}Opzione non valida.{Colors.END}")
            input("Premi ENTER per riprovare...")

if __name__ == "__main__":
    main()
