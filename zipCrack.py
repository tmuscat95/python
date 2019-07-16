import zipfile
import sys
words = open("words.txt","r").readlines()

if(len(sys.argv)==1):
    exit(0)

_zip = zipfile.ZipFile(sys.argv[1])

for word in words:
    try:
        _zip.extractall(pwd=word.strip("\n"))
        print(word)
        exit(0)
    except Exception as err:
        pass

    




