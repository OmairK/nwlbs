import socket as sc

HOST = '127.0.0.1'
PORT = 1234

with sc.socket(sc.AF_INET, sc.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by',addr)
        while True:
            data = conn.recv(1024)
            print(f'{data}')
            server_message = input("Send to client: ")
            conn.sendall(server_message.encode())
            if not data:
                break
            
