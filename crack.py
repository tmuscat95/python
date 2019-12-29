import crypt
import os

def bruteForce(passes,words,phash,uname = ""):
    salt = phash[0:1]
    plaintext_pass = ""
    for word in words:
        if(crypt.crypt(word.strip("\n"),salt)==phash):
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
        p = p.strip("\n")
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

#main()

