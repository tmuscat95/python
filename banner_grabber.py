#Banner grabber.
#Connect to remote service and get the connection header in order to determine service running.

import socket
import sys
import os


def vulnerable(banner):
    for l in vulnlines:
        if(l.strip("\n") in banner):
            return True

def connect(ip,port):
    try:
        s = socket.socket()
        s.connect((ip,port))
        ans = s.recv(1024)
        print(str(port) + ": ")
        print(ans)

        if(vulnerable(ans)):
            print("VULNERABLE")
        
    except Exception as err:
        pass
        #print(str(port) + ": ")
        #print(err)
    finally:
        print("\n")

def main():
    
    socket.setdefaulttimeout(2) 
    ip = sys.argv[1]
    vulnlines = []
    try:
        
        if(len(sys.argv)==2):
            ip = sys.argv[1]
        elif(len(sys.argv)>=3):
            f = open(sys.argv[2],"r")
        else:
            f = open("vuln_banners.txt","r")

        vulnlines = f.readlines() 

    except OSError as err:
        print(err)

    for port in range(1,65535):
            connect(ip,port)
        
main()