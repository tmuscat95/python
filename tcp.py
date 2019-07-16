import socket;

target_host = "http://www.google.com"
target_port = 80

#create socket         #ipv4            #TCP
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect
client.connect((target_host,target_port))

#send get request
client.send(buffer.encode("utf-8"))

#receive response
response_len = 1
response = ""

while :
    data = client.recv(4096)
    response_len = len(data)
    response += data

    if response_len < 4096:
        break

print(response)


print(response)