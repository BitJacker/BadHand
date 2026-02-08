# 🛡️ Bad Hand v1.0
### *The Swiss Army Knife for Security Auditing*

**Bad Hand** is a modular Python-based framework designed for conducting penetration tests on local networks and web applications. It automates common scanning and testing processes, providing a straightforward command-line interface.

---

## 🚀 Toolkit Overview

The project is organized into independent modules to ensure speed, precision, and ease of maintenance:

| Category | Tool | Description |
| :--- | :--- | :--- |
| **Network** | `scan.py` | Active host discovery and network mapping. |
| **Network** | `deauther.py` | Wi-Fi client deauthentication (stability testing). |
| **Network** | `udp_attak.py` | Network stress testing via mass UDP packet flooding. |
| **Web** | `xss_scanner.py` | Detects malicious script injection in web forms. |
| **Web** | `sqli_scanner.py` | Tests for SQL database injection vulnerabilities. |
| **Web** | `rce_test.py` | Checks for Remote Code Execution (RCE) possibilities. |
| **OSINT** | `subdomain_enum.py`| Subdomain discovery for target perimeter expansion. |
| **Auth** | `credential_stuffing.py`| Tests login robustness against account takeover. |
| **Admin** | `ssl_checker.py` | Verifies SSL certificate expiration and chain of trust. |
| **Bruteforce**| `dir_bruteforce.py` | Automated scanning for hidden files and directories. |

---

## 🛠️ Installation

Ensure you are using a Linux environment (Kali Linux recommended) with Python 3.x installed.

1. **Clone the project**
   ```bash
   git clone [https://github.com/BitJacker/BadHand.git](https://github.com/BitJacker/BadHand.git)
   cd BadHand

2 Configure the environment
Install the required libraries via the package manager:
   pip install -r requirements.txt

🔌 Usage
The framework is managed by a central script that acts as a menu:
   python3 badhand.py

[!IMPORTANT]
For network-layer tools (e.g., deauther, scan), you must run the script with administrative privileges to allow raw packet injection:
   sudo python3 badhand.py


📁 Project Structure
   bad_hand/
├── badhand.py           # Main Script (Menu UI)
├── requirements.txt      # Python Dependencies
├── tool/                 # Directory containing all modules
│   ├── scan.py
│   ├── deauther.py
│   └── ... (other scripts)
└── README.md


Certainly! Here is the professional version of your README.md in English. It uses a clean structure, icons, and clear technical sections to make it stand out on GitHub.

Markdown

# 🛡️ Bad Hand v1.0
### *The Swiss Army Knife for Security Auditing*

**Bad Hand** is a modular Python-based framework designed for conducting penetration tests on local networks and web applications. It automates common scanning and testing processes, providing a straightforward command-line interface.

---

## 🚀 Toolkit Overview

The project is organized into independent modules to ensure speed, precision, and ease of maintenance:

| Category | Tool | Description |
| :--- | :--- | :--- |
| **Network** | `scan.py` | Active host discovery and network mapping. |
| **Network** | `deauther.py` | Wi-Fi client deauthentication (stability testing). |
| **Network** | `udp_attak.py` | Network stress testing via mass UDP packet flooding. |
| **Web** | `xss_scanner.py` | Detects malicious script injection in web forms. |
| **Web** | `sqli_scanner.py` | Tests for SQL database injection vulnerabilities. |
| **Web** | `rce_test.py` | Checks for Remote Code Execution (RCE) possibilities. |
| **OSINT** | `subdomain_enum.py`| Subdomain discovery for target perimeter expansion. |
| **Auth** | `credential_stuffing.py`| Tests login robustness against account takeover. |
| **Admin** | `ssl_checker.py` | Verifies SSL certificate expiration and chain of trust. |
| **Bruteforce**| `dir_bruteforce.py` | Automated scanning for hidden files and directories. |

---

## 🛠️ Installation

Ensure you are using a Linux environment (Kali Linux recommended) with Python 3.x installed.

1. **Clone the project**
   ```bash
   git clone [https://github.com/BitJacker/BadHand.git](https://github.com/BitJacker/BadHand.git)
   cd BadHand
Configure the environment
Install the required libraries via the package manager:

Bash

pip install -r requirements.txt
🔌 Usage
The framework is managed by a central script that acts as a menu:

Bash

python3 badhand.py
[!IMPORTANT]
For network-layer tools (e.g., deauther, scan), you must run the script with administrative privileges to allow raw packet injection:

Bash

sudo python3 badhand.py
📁 Project Structure
Plaintext

bad_hand/
├── badhand.py           # Main Script (Menu UI)
├── requirements.txt      # Python Dependencies
├── tool/                 # Directory containing all modules
│   ├── scan.py
│   ├── deauther.py
│   └── ... (other scripts)
└── README.md


⚠️ Legal Disclaimer
The use of Bad Hand for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. The developer, BitJacker, assumes no liability and is not responsible for any misuse or damage caused by this toolkit   
