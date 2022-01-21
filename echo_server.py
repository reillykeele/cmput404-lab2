import socket

HOST = ''
PORT = 8001
with socket.create_server((HOST, PORT), backlog=5, reuse_port=True) as sock: 
    while True:        
        conn, addr = sock.accept()
        with conn: 
            print("Connected by", addr)
            data = conn.recv(1024)            
            # print(data)        
            
            conn.sendall(data)            