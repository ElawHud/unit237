import socket 

s = socket.socket()

port = 7777

s.connect(('172.17.0.1', port))

print (s.recv(1024).decode)

s.close
