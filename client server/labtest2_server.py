import socket

keyMatrix = [[0] * 3 for i in range(3)]
messageVector = [[0] for i in range(3)]
cipherMatrix = [[0] for i in range(3)]


def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1


def encrypt(messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] * messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def HillCipher(message, key):
    
    getKeyMatrix(key)
    final=''
    for x in range(0,len(message),3):
        something=message[x]+message[x+1]+message[x+2]
        for i in range(3):
            messageVector[i][0] = ord(something[i]) % 65
        encrypt(messageVector)
        CipherText = []
        for i in range(3):
            CipherText.append(chr(cipherMatrix[i][0] + 65))
        ciphered= "".join(CipherText)
        final=final+ciphered
        CipherText.clear()
    return final



#main
s = socket.socket()
print('Socket Created')
s.bind(('localhost', 9990))
s.listen(3)
print('Waiting for connections')
while True:
    c, addr = s.accept()
    msg = c.recv(1024).decode()
    print('connected with', addr)
    key='TANANSHAH'
    cipher=HillCipher(msg,key)
    c.send(bytes(cipher, 'utf-8'))
