import socket

host = "127.0.0.1"                                      # 主機的IP
port = 2255                                             # 連接port編號
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 建立socket物件
s.connect((host, port))

data = input('Enter: ')
s.send(data.encode())

receive_data = s.recv(1024).decode()
print(f'Receive data {receive_data}')

s.close()