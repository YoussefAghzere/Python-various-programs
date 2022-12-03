import socket

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_DGRAM for UDP

tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpSocket.bind(("0.0.0.0", 8000))  # (ip address that the socket will listen to, specific port number)

tcpSocket.listen(2)

print("Waiting for a client ...")

(client, (ip, sock)) = tcpSocket.accept()  # client = client's socket

print("Client Writing ...")
# print(client)
# print(ip)
# print(sock)
client.send("I am client 1".encode("ascii"))

# data = client.recv(2048)
# print( "data = ",data)


data = 'dummy'
while len(data):
    data = client.recv(20)
    print("Client sent : ", data)
    client.send(data)






