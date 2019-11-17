import socket 

# HOST = '127.0.0.1'
HOST = '192.168.43.211'
PORT = 8001
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        client_message = input("Send message to the server: ") 
        s.send(client_message.encode())
        data = s.recv(1024).decode()
        print(f'Daniyal says: {data.strip()}')

print('Recieved', repr(data))