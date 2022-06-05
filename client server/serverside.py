import socket

def decrypt(text,key):
     final = ''
     j=0
     for i in text:
         final = final + chr((ord(i) - key[j % 5] - 97) % 26 + 97)
         j = j + 1
     return final



s = socket.socket()
print('Socket Created')
k= 'point'
key=list(map(ord,list(k)))
s.bind(('localhost', 9000))
s.listen(3)
while True:
    c, addr = s.accept()
    msg = c.recv(1024).decode()
    decrypted=decrypt(msg, key)
    print("Decrypted message is: ",decrypted )
