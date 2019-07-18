import argparse
import threading
from threading import * 
import socket
from socket import *

screenLock = Semaphore(value=1)

def connScan(host,port):

    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        banner = s.recv(1024)

        screenLock.acquire()
        
        print(f'Port {port} Open')
        print(banner)
    except Exception as err:
        screenLock.acquire()
        print(f'Port {port} Closed')
    finally:
        screenLock.release()
        s.close()

    print("\n")

def portScan(host,ports):
    try:
        host_ip = gethostbyname(host)
    except expression as identifier:
        print(f"Cannot resolve: {host}")
    
    setdefaulttimeout(2)

    for port in ports:
        t = threading.Thread(target=connScan,args=[host,int(port)])
        t.start()

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


