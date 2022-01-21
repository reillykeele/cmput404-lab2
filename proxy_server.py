import sys
import socket
import errno

try:
    HOST = ''
    PORT = 8001

    with socket.create_server((HOST, PORT), backlog=5, reuse_port=True) as clientSock:        
        while True:
            clientConn, addr = clientSock.accept()
            with clientConn: 
                print("Connected to client", addr)
                clientReq = clientConn.recv(1024)

                googleSock = socket.create_connection(("www.google.com", 80), timeout=60)

                googleSock.sendall(clientReq)
                googleResponse = googleSock.recv(8192)      
                googleSock.close()              

                clientConn.sendall(googleResponse)
except socket.error as e:
    if e.errno == errno.EPIPE:        
        print("Remote disconnected.")
