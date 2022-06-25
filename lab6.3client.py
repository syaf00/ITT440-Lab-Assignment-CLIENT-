import socket
import signal
import sys

ClientSocket= socket.socket()
host= '192.168.56.104'    #server VM IP address
port= 8080                     

print('Waiting for incoming connection from client...')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response= ClientSocket.recv(1024)
print(Response.decode("utf-8"))
while True:
    Input= input('Enter <operation> <number>: ')

    if Input == 'E':
        break
    else:
        ClientSocket.send(str.encode(Input))
        Response= ClientSocket.recv(1024)
        print(Response.decode("utf-8"))

ClientSocket.close()
