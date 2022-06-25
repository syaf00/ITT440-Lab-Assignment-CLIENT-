import socket

msgFromClient= "Hi, saya client. Terima Kasih!"
bytesToSend= str.encode(msgFromClient)
serverPort= ("192.168.56.104", 20001)
buffer= 1024

# Create UDP socket at client side
UDPClient_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClient_sock.sendto(bytesToSend, serverPort)

msgFromServer = UDPClient_sock.recvfrom(buffer)

msg = "{}".format(msgFromServer[0])
print(msg)
