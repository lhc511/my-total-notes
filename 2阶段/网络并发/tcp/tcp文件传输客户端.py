import socket

file = open('/home/ubuntu/图片/img01.jpg', 'rb')

s = socket.socket()
s.connect(('127.0.0.1', 8888))

while True:
    data = file.read(1024)
    if not data:
        break
    s.send(data)

# data_rec = s.recv(1024)
# print(data.decode())
s.close()
file.close()