import crypt
import sys

hash = ""

if(len(sys.argv)<2):
    print("give password to hash")
elif(len(sys.argv)==2):
    hash = crypt.crypt(sys.argv[1],crypt.mksalt())
elif(len(sys.argv)==3):
    if(len(sys.argv[2])!=2):
        print("Hash Incorrect format")
        exit(1)
    else:
        hash = crypt.crypt(sys.argv[1],sys.argv[2])
        
print(hash)
    
