import sys
import socket
import getopt
import threading
import subprocess

# define some global variables
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

def client_sender(buffer):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(target,port)

    client.send(buffer.encode("utf-8"))
    try:
        while True
        response = ""
        recv_len = 1

        while recv_len:
            data = client.recv(4096) #one block
            recv_len = len(data)
            response += data

            if recv_len < 4096:
                break

        print(response)
        buffer = input()
        buffer += "\n"
        client.send(buffer.encode("utf-8"))
    except :
        client.close()
    
def client_handler:
    
def server_loop():
    global target
    
    if not len(target):
        target = "0.0.0.0"

    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.bind((target,port))
    client.listen(5)

    while True:
        client_socket,client_addr = client.accept()

        client_handler_thread = threading.Thread(target=client_handler,args=(client_socket))
        client_handler_thread.start()


def usage():
    print("PyCat")
    print("\n")
    print("Usage: pycat.py -t target_host -p port")
    print("-l --listen - listen on [host]:[port] for incoming connections")
    print("-e --execute=file_to_run - execute the given file upon receiving a connection")
    print("-c --command - initialize a command shell")
    print("-u --upload=destination - upon receiving connection upload a file and write to [destination]")
    print("\n")
    print("\n")
    print("Examples: ")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -c")
    print( "bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"")
    print("echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135")
    sys.exit(0)

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target 
    #argument string -h -l -e
    optsShort = "hle:t:p:cu:"
    optsLong = ["help","listen","execute","target","port","command","upload"]
    
    if(len(sys.argv[1:])>0):
        try:
            opts,args = getopt.getopt(sys.argv[1:],optsShort,optsLong)

        except getopt.GetoptError as err:
            print  str(err)
            usage()
    else
        usage()

    for o,a in opts:
        if o in ("-h","--help"):
            usage()
        elif o in ("-l","--listen"):
            listen = True
        elif o in ("-e","--execute"):
            execute = True
        elif o in ("-t","--target"):
            target = a 
        elif o in ("-u","--upload"):
            upload_destination = a
        elif o in ("-p","--port"):
            port = a
        elif o in ("-c","--command"):
            command = c
        else:
            print("Invalid Option.")
            sys.exit()

#If Not listening, but target host specified 
if not listen and len(target) > 0 and port > 0:
    buffer = sys.stdin.read()
    client_sender(buffer)

if listen:
    server_loop()

main()

