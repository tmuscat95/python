import argparse
import socket
from socket import *

def connScan(host,port):
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        print(f'Port {port} Open')
    except Exception as err:
        print(f'Port {port} Closed')
        pass
    try:
        banner = s.recv(128)
        print(banner)
        s.close()
    except timeout as err:
        print(f"Timed out grabbing banner from port: {port}")
        pass
    print("\n")

def portScan(host,ports):
    try:
        host_ip = gethostbyname(host)
    except expression as identifier:
        print(f"Cannot resolve: {host}")
    
    setdefaulttimeout(2)

    for port in ports:
        connScan(host,int(port))


parser = argparse.ArgumentParser()
parser.add_argument("host",type=str,help="Hostname")
parser.add_argument("-p","--ports",type=str,help="Port Numbers ()")
args = parser.parse_args() 

ports = []
if(not args.ports):
    ports = range(1,65535)
else:
    ports = args.ports.split(",")

portScan(args.host,ports)


