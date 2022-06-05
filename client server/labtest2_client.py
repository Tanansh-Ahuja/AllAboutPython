import socket

c = socket.socket()
c.connect(('localhost', 9990))

#msg = input('Enter the text: ')
msg = 'HELLOWORL'

c.send(bytes(msg, 'utf-8'))
print('Ciphered text: ', c.recv(1024).decode())
