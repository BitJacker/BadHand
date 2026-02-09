from scapy.all import ARP, Ether, srp
import sys

ans, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=sys.argv[1]+'/24'), timeout=2, verbose=0)
for s, r in ans:
    print(f'IP: {r.psrc} MAC: {r.hwsrc}')
