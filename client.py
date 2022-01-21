import socket

try :
    sock = socket.create_connection(("www.google.com", 80))
    
    sock.sendall(b"GET / HTTP/1.0\r\n\r\n")
    print(sock.recv(4096))
finally:
    sock.close()