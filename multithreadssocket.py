import socket

mt_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM :: TCP  SOCK_DGRAM :: UDP
mt_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mt_sock.bind(("0.0.0.0", 8000))

mt_sock.listen(2)

print("Waiting for 2 clients")

clients_number = 2

clients = ["a", "b"]

for i in range(clients_number):
    clients[i] = mt_sock.accept()
    print("Client ", i, " is connected")

for i in range(clients_number):
    str = "hey i am a client "
    clients[i][0].send(str.encode("ascii"))

data1 = 'dummy'
data2 = 'dummy'

while 1:
    data1 = clients[0][0].recv(10)
    data2 = clients[1][0].recv(10)
    print("Client 1 is writing ...")
    print("Client 2 is writing ...")
    clients[0][0].send(data1)
    clients[1][0].send(data2)






