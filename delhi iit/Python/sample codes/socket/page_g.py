import socket
request = b"GET / HTTP/1.1\nHost: 192.168.0.100\n\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.google.com", 80))
s.send(request)
result = s.recv(10000)
while (len(result) > 0):
    print(result)
    result = s.recv(10000)   
