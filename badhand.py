import os
import subprocess
import sys

# Set BASE_DIR to point to the 'tool' folder
# Ensure that the .py files are inside a folder named 'tool' in the same location as this script
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tool")

class Colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    CYAN = '\033[36m'
    END = '\033[0m'

# Menu Configuration
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
        print(f"{Colors.RED}Error: {script_name} not found in {BASE_DIR}{Colors.END}")
        input("Press ENTER to continue...")
        return

    cmd = ""

    # --- DATA ACQUISITION LOGIC ---
    if script_name == "udp_attak.py":
        ip = input(f"{Colors.YELLOW}Target IP > {Colors.END}").strip()
        port = input(f"{Colors.YELLOW}Port > {Colors.END}").strip()
        method = input(f"{Colors.YELLOW}Method (UDP-Mix / UDP-Power) > {Colors.END}").strip()
        if ip and port and method:
            cmd = f"python3 {script_path} {ip} {port} {method}"

    elif script_name == "scan.py":
        ip = input(f"{Colors.YELLOW}IP to scan > {Colors.END}").strip()
        if ip: cmd = f"python3 {script_path} {ip}"

    elif script_name == "xss_scanner.py":
        url = input(f"{Colors.YELLOW}Target URL > {Colors.END}").strip()
        if url: cmd = f"python3 {script_path} {url}"

    elif script_name == "sqli_scanner.py":
        url = input(f"{Colors.YELLOW}Target URL > {Colors.END}").strip()
        if url: cmd = f"python3 {script_path} {url}"

    elif script_name == "dir_bruteforce.py":
        url = input(f"{Colors.YELLOW}Target URL > {Colors.END}").strip()
        wordlist = input(f"{Colors.YELLOW}Wordlist path > {Colors.END}").strip()
        if url and wordlist: cmd = f"python3 {script_path} {url} {wordlist}"

    elif script_name == "ssl_checker.py":
        domain = input(f"{Colors.YELLOW}Domain > {Colors.END}").strip()
        if domain: cmd = f"python3 {script_path} {domain}"

    elif script_name == "rce_test.py":
        url = input(f"{Colors.YELLOW}Target URL > {Colors.END}").strip()
        if url: cmd = f"python3 {script_path} {url}"

    elif script_name == "credential_stuffing.py":
        url = input(f"{Colors.YELLOW}Login URL > {Colors.END}").strip()
        user = input(f"{Colors.YELLOW}Username > {Colors.END}").strip()
        wlist = input(f"{Colors.YELLOW}Wordlist > {Colors.END}").strip()
        if url and user and wlist: cmd = f"python3 {script_path} {url} {user} {wlist}"

    elif script_name == "subdomain_enum.py":
        domain = input(f"{Colors.YELLOW}Domain > {Colors.END}").strip()
        wlist = input(f"{Colors.YELLOW}Wordlist > {Colors.END}").strip()
        if domain and wlist: cmd = f"python3 {script_path} {domain} {wlist}"

    elif script_name == "deauther.py":
        target = input(f"{Colors.YELLOW}Target MAC > {Colors.END}").strip()
        gateway = input(f"{Colors.YELLOW}Gateway MAC > {Colors.END}").strip()
        iface = input(f"{Colors.YELLOW}Interface (e.g., wlan0mon) > {Colors.END}").strip()
        if target and gateway and iface:
            cmd = f"sudo python3 {script_path} {target} {gateway} {iface}"

    # --- EXECUTION ---
    if not cmd:
        print(f"{Colors.RED}Insufficient data. Please try again.{Colors.END}")
        input("Press ENTER to return to menu...")
        return

    try:
        # Try to open xfce4-terminal (typical for Kali/Parrot)
        subprocess.Popen(["xfce4-terminal", "--hold", "-e", cmd])
        print(f"{Colors.GREEN}Script started in a new window.{Colors.END}")
    except FileNotFoundError:
        # If xfce4 is not present, execute in current terminal
        print(f"{Colors.CYAN}External terminal not found. Launching locally...{Colors.END}")
        print(f"{Colors.BLUE}Executing: {cmd}{Colors.END}\n")
        os.system(cmd)
    
    input(f"\n{Colors.GREEN}Session ended. Press ENTER for menu...{Colors.END}")

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
            print(f"{Colors.BLUE}Closing...{Colors.END}")
            break
        elif choice in MENU and MENU[choice][1]:
            run_script(MENU[choice][1])
        else:
            print(f"{Colors.RED}Invalid option.{Colors.END}")
            input("Press ENTER to try again...")

if __name__ == "__main__":
    main()
