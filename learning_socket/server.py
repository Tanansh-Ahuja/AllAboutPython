import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)


while True:
    clientsocket, address = s.accept()
    print("connection from ",address," has been extablished")
    clientsocket.send(bytes("welcome to the server","utf-8"))
    
