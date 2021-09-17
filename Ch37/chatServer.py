import socket

host = socket.gethostname()
port = 2255
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()
print('Server: Waiting...')
conn, addr = s.accept()
print(f'Server: Connected, IP: {addr}')
msg = conn.recv(1024).decode()

while msg != 'bye':
    if msg:
        print(f'Receive content: {msg}')
    mydata = input('Enter message: ')
    conn.send((mydata.encode()))
    if mydata == 'bye':
        break
    print('Server waiting...')
    msg = conn.recv(1024).decode()

conn.close()
s.close()