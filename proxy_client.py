import socket
import errno

try :
    sock = socket.create_connection(("127.0.0.1", 8001))
    
    sock.sendall(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")
    print(sock.recv(8192))
except socket.error as e:
    if e.errno == errno.EPIPE:        
        print("proxy_server disconnected.")
finally:
    sock.close()