import dpkt
import socket
import geoIP_locate
from geoIP_locate import printGeoIP

f = open("./network_analysis/geotest.pcap","rb")

pcap = dpkt.pcap.Reader(f)

for (timestamp,buf) in pcap:
    eth = dpkt.ethernet.Ethernet(buf)

    if(not isinstance(eth.data,dpkt.ip.IP)):
        continue
    
    src = socket.inet_ntoa(eth.data.src)
    dst = socket.inet_ntoa(eth.data.dst)

    print("Source: ")
    printGeoIP(src)
    print("Destination: ")
    printGeoIP(src)
    print("\n")


