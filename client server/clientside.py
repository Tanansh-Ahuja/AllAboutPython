import socket

def encrypt(txt, s):
    result = ""
    result += chr((ord(txt) + s - 97) % 26 + 97)
    return result



so = socket.socket()
so.connect(('localhost', 9000))

message = input('Enter the text: ')
k= 'point'
k=list(map(ord,list(k)))
i=0
final=''
for j in range(0,len(message),1):
    s=encrypt(message[j], k[i])
    final=final+s
    i=(i+1)%len(k)
print (final)
so.send(bytes(final, 'utf-8'))
