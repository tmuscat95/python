import sys
import hashlib

if(len(sys.argv) == 1):
    exit(0)
else:
    sha = hashlib.sha512() 
    sha.update(sys.argv[1].encode("UTF-8"))
    _hash = sha.hexdigest()
    print(_hash)
