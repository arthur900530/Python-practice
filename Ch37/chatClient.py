import socket

host = socket.gethostname()
port = 2255
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print('Client connected')
msg = ''

while msg != 'bye':
    mydata = input('Enter message: ')
    s.send(mydata.encode())
    if mydata == 'bye':
        break
    print('Client waiting...')
    msg = s.recv(1024).decode()
    print(f'Receive: {msg}')

s.close()