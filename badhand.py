import os
import subprocess
import sys
import shlex

# Base directory configuration for tools
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tool")

class Colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    CYAN = '\033[36m'
    MAGENTA = '\033[35m'
    END = '\033[0m'

# Menu Configuration (Expanded to 30 Tools)
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
    "11": ("DNS LOOKUP/ENUM", "dns_lookup.py"),
    "12": ("PORT SCANNER (Nmap-like)", "port_scanner.py"),
    "13": ("WHOIS RECON", "whois_recon.py"),
    "14": ("REVERSE IP LOOKUP", "reverse_ip.py"),
    "15": ("CMS DETECTOR", "cms_detector.py"),
    "16": ("HEADER SECURITY CHECK", "header_check.py"),
    "17": ("ROBOTS.TXT ANALYZER", "robots_analyzer.py"),
    "18": ("CLOUD BUCKET FINDER", "cloud_finder.py"),
    "19": ("WP-SCAN LITE", "wp_scan.py"),
    "20": ("BRUTEFORCE SSH", "ssh_brute.py"),
    "21": ("BRUTEFORCE FTP", "ftp_brute.py"),
    "22": ("HONEYPOT DETECTOR", "honeypot_det.py"),
    "23": ("PARAM MINER (URL Params)", "param_miner.py"),
    "24": ("CLICKJACKING TEST", "clickjacking_test.py"),
    "25": ("IP GEOLOCATION", "ip_geo.py"),
    "26": ("MAIL SPOOF CHECKER", "mail_spoof.py"),
    "27": ("JS FILES EXTRACTOR", "js_extractor.py"),
    "28": ("API ENDPOINT DISCOVERY", "api_discovery.py"),
    "29": ("SUBDOMAIN TAKEOVER", "sub_takeover.py"),
    "30": ("HASH IDENTIFIER", "hash_id.py"),
    "0": ("Exit", None)
}

# Description for each tool
TOOL_DESCRIPTIONS = {
    "1": "This script performs a UDP Flood attack, aimed at overloading a target server with UDP packets, consuming its bandwidth and causing a Denial of Service (DoS).",
    "2": "WiFi deauthentication attack allows disconnecting a device from a wireless network by forcing disconnection between client and access point via deauthentication packets.",
    "3": "This tool performs a network scan to detect active devices and open ports on the network, revealing services running on connected devices.",
    "4": "Scans a website for Cross-Site Scripting (XSS) vulnerabilities, a technique that allows an attacker to inject malicious JavaScript code into a web application.",
    "5": "This scanner looks for SQL Injection vulnerabilities, where an attacker can inject malicious SQL commands to interact with a web application's database.",
    "6": "Performs directory brute forcing to find undocumented pages on a website.",
    "7": "Verifies and analyzes a website's SSL/TLS configuration to identify vulnerabilities in encrypted traffic protection.",
    "8": "Performs a Remote Code Execution (RCE) test on a web application to identify arbitrary code execution vulnerabilities.",
    "9": "This tool performs a Credential Stuffing attack, attempting to gain access to a system with usernames and passwords stolen from a data breach.",
    "10": "Performs subdomain enumeration on a specified domain to discover other resources linked to the domain.",
    "11": "Tool for DNS analysis and enumeration to find subdomains, configuration information, or DNS configuration errors.",
    "12": "An Nmap-like port scanner that performs a port scan of a host to determine which are open and what services are running on them.",
    "13": "Gathers information about a specific domain, such as IP address, registrar, WHOIS information, etc.",
    "14": "Allows performing a reverse IP lookup to identify domains associated with a specific IP address.",
    "15": "Detects if a website uses a Content Management System (CMS) such as WordPress, Joomla, Drupal, etc.",
    "16": "Verifies the security of a website's HTTP headers to identify weak configurations.",
    "17": "Analyzes a website's robots.txt file to look for configuration errors or to identify hidden resources.",
    "18": "Finds unprotected cloud storage buckets that may contain sensitive or vulnerable data.",
    "19": "A WordPress vulnerability scanner designed to detect common security issues on a WordPress site.",
    "20": "Brute force tool for SSH, designed to attempt to guess login credentials for an SSH machine.",
    "21": "Brute force tool for FTP, designed to attempt to guess login credentials for an FTP server.",
    "22": "A honeypot detector that analyzes a website to see if a honeypot has been configured to trap attackers.",
    "23": "Analyzes URLs to determine exposed parameters, with the goal of finding vulnerabilities such as SQL Injection, XSS, etc.",
    "24": "Tests for clickjacking vulnerabilities on a website, which allows users to perform actions on other sites without their consent.",
    "25": "Verifies the geolocation of an IP address to determine the geographic location associated with that particular address.",
    "26": "Checks if an email has been spoofed to detect potential phishing attempts.",
    "27": "Extracts JavaScript files from a website to analyze them for vulnerabilities, malware, or other sensitive information.",
    "28": "Discovers and maps API endpoints of a web application.",
    "29": "Detects subdomain takeover vulnerabilities on a domain.",
    "30": "Identifies the type of hash provided, such as MD5, SHA1, SHA256, etc.",
}

# Function to handle input securely
def sanitize_input(input_string):
    return shlex.quote(input_string)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print(f"""{Colors.CYAN}
 ██████╗  █████╗ ██████╗     ██╗  ██╗ █████╗ ███╗   ██╗██████╗ 
 ██╔══██╗██╔══██╗██╔══██╗    ██║  ██║██╔══██╗████╗  ██║██╔══██╗
 ██████╔╝███████║██║  ██║    ███████║███████║██╔██╗ ██║██║  ██║
 ██╔══██╗██╔══██║██║  ██║    ██╔══██║██╔══██║██║╚██╗██║██║  ██║
 ██████╔╝██║  ██║██████╔╝    ██║  ██║██║  ██║██║ ╚████║██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝{Colors.END}""")

def get_input(prompt):
    return input(f"{Colors.YELLOW}{prompt} > {Colors.END}").strip()

def display_menu():
    """Displays the main menu with all available tools"""
    print(f"{Colors.YELLOW}{'='*67}")
    print(f"            Ethical Hacking Lab - Created by BitJacker             ")
    print(f"{'='*67}{Colors.END}")
    
    # Menu items in two-column format
    menu_items = [
        ("1", "DDOS (UDP Flood)", "16", "HEADER SECURITY CHECK"),
        ("2", "DEAUTHER (WiFi)", "17", "ROBOTS.TXT ANALYZER"),
        ("3", "NETWORK SCAN", "18", "CLOUD BUCKET FINDER"),
        ("4", "XSS SCANNER", "19", "WP-SCAN LITE"),
        ("5", "SQL INJECTION SCANNER", "20", "BRUTEFORCE SSH"),
        ("6", "DIRECTORY BRUTEFORCE", "21", "BRUTEFORCE FTP"),
        ("7", "SSL/TLS CHECKER", "22", "HONEYPOT DETECTOR"),
        ("8", "RCE TEST", "23", "PARAM MINER (URL Params)"),
        ("9", "CREDENTIAL STUFFING", "24", "CLICKJACKING TEST"),
        ("10", "SUBDOMAIN ENUM", "25", "IP GEOLOCATION"),
        ("11", "DNS LOOKUP/ENUM", "26", "MAIL SPOOF CHECKER"),
        ("12", "PORT SCANNER", "27", "JS FILES EXTRACTOR"),
        ("13", "WHOIS RECON", "28", "API ENDPOINT DISCOVERY"),
        ("14", "REVERSE IP LOOKUP", "29", "SUBDOMAIN TAKEOVER"),
        ("15", "CMS DETECTOR", "30", "HASH IDENTIFIER"),
    ]
    
    for left_num, left_name, right_num, right_name in menu_items:
        print(f" {Colors.GREEN}[{left_num:>2}]{Colors.END} {left_name:<28} | {Colors.GREEN}[{right_num:>2}]{Colors.END} {right_name:<28}")
    
    print(f"\n {Colors.RED}[0]{Colors.END}  Exit")
    print(f"{Colors.YELLOW}{'='*67}{Colors.END}")

def show_tool_description(choice):
    """Shows the description of a specific tool"""
    if choice in TOOL_DESCRIPTIONS:
        print(f"\n{Colors.BLUE}{'='*60}")
        print(f"Tool Description:")
        print(f"{'='*60}{Colors.END}")
        print(f"{Colors.YELLOW}{TOOL_DESCRIPTIONS[choice]}{Colors.END}")
        print(f"{Colors.BLUE}{'='*60}{Colors.END}\n")

def run_script(script_name):
    script_path = os.path.join(BASE_DIR, script_name)

    if not os.path.isfile(script_path):
        print(f"{Colors.RED}Error: {script_name} not found in {BASE_DIR}{Colors.END}")
        input("Press ENTER to continue...")
        return

    cmd = ""

    # --- DATA ACQUISITION LOGIC ---

    # 1. DDOS (UDP Flood)
    if script_name == "udp_attak.py":
        ip = get_input("Target IP")
        port = get_input("Port")
        method = get_input("Method (UDP-Mix/UDP-Power)")
        if ip and port and method:
            cmd = f"python3 {script_path} {sanitize_input(ip)} {sanitize_input(port)} {sanitize_input(method)}"

    # 2. DEAUTHER (WiFi)
    elif script_name == "deauther.py":
        target = get_input("Target MAC")
        gateway = get_input("Gateway MAC")
        iface = get_input("Interface (e.g. wlan0mon)")
        if target and gateway and iface: 
            cmd = f"sudo python3 {script_path} {sanitize_input(target)} {sanitize_input(gateway)} {sanitize_input(iface)}"

    # 3. NETWORK SCAN
    elif script_name == "scan.py":
        target = get_input("Target URL/IP")
        if target: 
            cmd = f"python3 {script_path} {sanitize_input(target)}"

    # 4. XSS SCANNER
    elif script_name == "xss_scanner.py":
        target = get_input("Target URL/IP")
        if target: 
            cmd = f"python3 {script_path} {sanitize_input(target)}"

    # 5. SQL INJECTION SCANNER
    elif script_name == "sqli_scanner.py":
        target = get_input("Target URL/IP")
        if target: 
            cmd = f"python3 {script_path} {sanitize_input(target)}"

    # 6. DIRECTORY BRUTEFORCE
    elif script_name == "dir_bruteforce.py":
        url = get_input("Target Domain/URL")
        wlist = get_input("Wordlist Path")
        if url and wlist: 
            cmd = f"python3 {script_path} {sanitize_input(url)} {sanitize_input(wlist)}"

    # 7. SSL/TLS CHECKER
    elif script_name == "ssl_checker.py":
        target = get_input("Target URL")
        if target: 
            cmd = f"python3 {script_path} {sanitize_input(target)}"

    # 8. RCE TEST
    elif script_name == "rce_test.py":
        target = get_input("Target URL/IP")
        if target: 
            cmd = f"python3 {script_path} {sanitize_input(target)}"

    # 9. CREDENTIAL STUFFING
    elif script_name == "credential_stuffing.py":
        ip = get_input("Target IP/URL")
        user = get_input("Username")
        wlist = get_input("Wordlist")
        if ip and user and wlist: 
            cmd = f"python3 {script_path} {sanitize_input(ip)} {sanitize_input(user)} {sanitize_input(wlist)}"

    # 10. SUBDOMAIN ENUM
    elif script_name == "subdomain_enum.py":
        url = get_input("Target Domain/URL")
        wlist = get_input("Wordlist Path")
        if url and wlist: 
            cmd = f"python3 {script_path} {sanitize_input(url)} {sanitize_input(wlist)}"

    # 11. DNS LOOKUP/ENUM
    elif script_name == "dns_lookup.py":
        domain = get_input("Enter Domain Name")
        if domain: 
            cmd = f"python3 {script_path} {sanitize_input(domain)}"

    # 12. PORT SCANNER (Nmap-like)
    elif script_name == "port_scanner.py":
        target = get_input("Target IP/URL")
        ports = get_input("Ports (comma separated)")
        if target and ports: 
            cmd = f"python3 {script_path} {sanitize_input(target)} {sanitize_input(ports)}"

    # 13. WHOIS RECON
    elif script_name == "whois_recon.py":
        target = get_input("Target Domain")
        if target: 
            cmd = f"python3 {script_path} {sanitize_input(target)}"

    # 14. REVERSE IP LOOKUP
    elif script_name == "reverse_ip.py":
        ip = get_input("Target IP")
        if ip: 
            cmd = f"python3 {script_path} {sanitize_input(ip)}"

    # 15. CMS DETECTOR
    elif script_name == "cms_detector.py":
        target = get_input("Target URL")
        if target: 
            cmd = f"python3 {script_path} {sanitize_input(target)}"

    # 16. HEADER SECURITY CHECK
    elif script_name == "header_check.py":
        target = get_input("Target URL")
        if target: 
            cmd = f"python3 {script_path} {sanitize_input(target)}"

    # 17. ROBOTS.TXT ANALYZER
    elif script_name == "robots_analyzer.py":
        target = get_input("Target URL")
        if target: 
            cmd = f"python3 {script_path} {sanitize_input(target)}"

    # 18. CLOUD BUCKET FINDER
    elif script_name == "cloud_finder.py":
        domain = get_input("Enter Domain Name")
        if domain: 
            cmd = f"python3 {script_path} {sanitize_input(domain)}"

    # 19. WP-SCAN LITE
    elif script_name == "wp_scan.py":
        url = get_input("Target WordPress URL")
        if url: 
            cmd = f"python3 {script_path} {sanitize_input(url)}"

    # 20. BRUTEFORCE SSH
    elif script_name == "ssh_brute.py":
        ip = get_input("Target IP/URL")
        user = get_input("Username")
        wlist = get_input("Wordlist")
        if ip and user and wlist: 
            cmd = f"python3 {script_path} {sanitize_input(ip)} {sanitize_input(user)} {sanitize_input(wlist)}"

    # 21. BRUTEFORCE FTP
    elif script_name == "ftp_brute.py":
        ip = get_input("Target IP/URL")
        user = get_input("Username")
        wlist = get_input("Wordlist")
        if ip and user and wlist: 
            cmd = f"python3 {script_path} {sanitize_input(ip)} {sanitize_input(user)} {sanitize_input(wlist)}"

    # 22. HONEYPOT DETECTOR
    elif script_name == "honeypot_det.py":
        target = get_input("Target URL/IP")
        if target: 
            cmd = f"python3 {script_path} {sanitize_input(target)}"

    # 23. PARAM MINER (URL Params)
    elif script_name == "param_miner.py":
        url = get_input("Target URL")
        if url: 
            cmd = f"python3 {script_path} {sanitize_input(url)}"

    # 24. CLICKJACKING TEST
    elif script_name == "clickjacking_test.py":
        target = get_input("Target URL")
        if target: 
            cmd = f"python3 {script_path} {sanitize_input(target)}"

    # 25. IP GEOLOCATION
    elif script_name == "ip_geo.py":
        ip = get_input("Target IP")
        if ip: 
            cmd = f"python3 {script_path} {sanitize_input(ip)}"

    # 26. MAIL SPOOF CHECKER
    elif script_name == "mail_spoof.py":
        email = get_input("Enter Email Address")
        if email: 
            cmd = f"python3 {script_path} {sanitize_input(email)}"

    # 27. JS FILES EXTRACTOR
    elif script_name == "js_extractor.py":
        target = get_input("Target URL")
        if target: 
            cmd = f"python3 {script_path} {sanitize_input(target)}"

    # 28. API ENDPOINT DISCOVERY
    elif script_name == "api_discovery.py":
        url = get_input("Target URL")
        if url: 
            cmd = f"python3 {script_path} {sanitize_input(url)}"

    # 29. SUBDOMAIN TAKEOVER
    elif script_name == "sub_takeover.py":
        domain = get_input("Enter Target Domain")
        if domain: 
            cmd = f"python3 {script_path} {sanitize_input(domain)}"

    # 30. HASH IDENTIFIER
    elif script_name == "hash_id.py":
        hash_val = get_input("Enter Hash to Identify")
        if hash_val: 
            cmd = f"python3 {script_path} {sanitize_input(hash_val)}"

    # Execute the command
    if cmd:
        print(f"{Colors.GREEN}Executing: {cmd}{Colors.END}")
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"{Colors.RED}Error executing command: {e}{Colors.END}")
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Operation interrupted by user{Colors.END}")
        input(f"{Colors.YELLOW}Press ENTER to return to menu...{Colors.END}")
    else:
        print(f"{Colors.RED}No valid command provided. Returning to menu...{Colors.END}")
        input(f"{Colors.YELLOW}Press ENTER to return to menu...{Colors.END}")

def main():
    """Main program function"""
    # Create tool directory if it doesn't exist
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)
        print(f"{Colors.YELLOW}'tool' directory created at: {BASE_DIR}{Colors.END}")
    
    while True:
        try:
            clear()
            banner()
            display_menu()
            
            choice = get_input("\nSelect a tool")
            
            if choice == "0":
                clear()
                print(f"{Colors.CYAN}")
                print("╔═══════════════════════════════════════╗")
                print("║                                       ║")
                print("║      Thank you for using              ║")
                print("║      Ethical Hacking Lab              ║")
                print("║                                       ║")
                print("║      Created by BitJacker             ║")
                print("║                                       ║")
                print("║      Stay Safe, Stay Legal!           ║")
                print("║                                       ║")
                print("╚═══════════════════════════════════════╝")
                print(f"{Colors.END}")
                sys.exit(0)
            
            if choice in MENU and choice != "0":
                tool_name, script_name = MENU[choice]
                clear()
                banner()
                print(f"\n{Colors.CYAN}Selected Tool: {tool_name}{Colors.END}")
                show_tool_description(choice)
                
                confirm = get_input("Do you want to proceed with this tool? (y/n)").lower()
                if confirm == 'y' or confirm == 'yes':
                    run_script(script_name)
                else:
                    print(f"{Colors.YELLOW}Operation cancelled{Colors.END}")
                    input("Press ENTER to return to menu...")
            else:
                print(f"{Colors.RED}Invalid choice! Select a number between 0 and 30{Colors.END}")
                input("Press ENTER to continue...")
        
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Program interrupted by user{Colors.END}")
            sys.exit(0)
        except Exception as e:
            print(f"{Colors.RED}Error: {str(e)}{Colors.END}")
            input("Press ENTER to continue...")

if __name__ == "__main__":
    main()
