import socket
import os
import sys

#server vm ip
hostip = "192.168.56.104"

#socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8888

#connect socket 
serverSocket.connect((hostip, PORT))

print("------FILE STORAGE APPLICATION------")
print("--Welcome!Send files you wish to send to server--\n")
sendFile = input(">>Enter name of file that you wish to send to server: ")
#print("File name: " + sendFile)

file = open(sendFile, "rb")
sendData = file.read(1024)

serverSocket.send(sendFile.encode("utf-8"))

while sendData:
	print("[+]Message received!\n", serverSocket.recv(1024).decode("utf-8"))
	print("File name: " + sendFile)
	serverSocket.send(sendData)
	sendData = file.read(1024)

#close socket
serverSocket.close()
