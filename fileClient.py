import socket
import sys
import os
a = sys.argv[1]

# HOST = '127.0.0.1'
HOST = '192.168.43.211'
PORT = 8004
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    with open(a,'r') as f:
        
        print("Sending file to the server:........../") 
        size = os.path.getsize(f.name)
        s.send(str(size).encode())
        # print(size)
        s.send(f.read().encode())
        s.send(str(sys.argv[1]).encode())
        data = s.recv(1024).decode()
        print(f'Daniyal says: {data.strip()}')

print('Recieved', repr(data))