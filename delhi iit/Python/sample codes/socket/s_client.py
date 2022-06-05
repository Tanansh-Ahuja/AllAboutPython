import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = '192.168.129.108' # Get local machine name
port = 1234                # Reserve a port for your service.

s.connect((host, port))
s.send("hello")
print s.recv(1024)
s.close                     # Close the socket when done
