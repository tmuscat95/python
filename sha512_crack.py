import hashlib
import os

def bruteForce(passes,words,phash,uname = ""):
    #salt = phash[0:2]
    plaintext_pass = ""
    for word in words:
        sha = hashlib.sha512()
        sha.update(word.strip("\n").encode("UTF-8"))
        whash = sha.hexdigest()
        if(whash==phash):
            plaintext_pass = word
            break
    
    if(plaintext_pass == ""):
        return ""
    else:
        return uname + ": " + plaintext_pass

#def main():

try:
    passes = open("./pass.txt","r").readlines()
    words = open("./words.txt","r").readlines() 

    for p in passes:
        p = p.strip("\n").strip(" ")
        plaintext = ""
        if(":" in p):
            plaintext = bruteForce(passes,words,p.split(":")[1],p.split(":")[0])
        else:
            plaintext = bruteForce(passes,words,p)

        if(plaintext == ""):
            print("No dictionary match for: " + p)
        else:
            print(p + "|" + plaintext)

except OSError as err:
    print(err)
