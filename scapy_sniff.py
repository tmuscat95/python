#Python 2
from scapy.all import *


def testTTL(pkt):
    try:
        if(pkt.haslayer(IP)):
            ip = pkt.getlayer(IP)
            ttl = str(ip.ttl)
            print ip.src + " --> " + ip.dst + " TTL: " + ttl 
    except expression as Exception:
        pass

def main():
    sniff(prn=testTTL,store =0)
    
if __name__ == "__main__":
    main()
