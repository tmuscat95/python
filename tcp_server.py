import socket
import threading

ip = "127.0.0.1"
port = 9999
n = 5 #max connections

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((ip,port))
server.listen(n)

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(request)
    client_socket.send("ACK")

    client_socket.close()


while True:
    print("Listening on " + str(port))
    (client,addr) = server.accept()

    print(addr[0])
    print(addr[1])

    client_handler = threading.Thread(target=handle_client,args=(client))
    client_handler.start()