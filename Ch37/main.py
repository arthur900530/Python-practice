import socket

host = '127.0.0.1'
port = 2255
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
print(f'Server 在{host}:{port}')
print('waiting for connection...')
while True:
    conn, addr = s.accept()
    print(f'目前連線網址{addr}')
    data = conn.recv(1024)
    print(data)
    conn.sendall(b"HTTP/1.1 200 OK \r\n\r\n Welcome to Deepmind")
    conn.close()