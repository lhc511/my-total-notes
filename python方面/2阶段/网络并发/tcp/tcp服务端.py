import socket

s=socket.socket()
s.bind(('127.0.0.1',8888))
s.listen(8)
print("等待连接中...")

c,adr=s.accept()
print("connect from",adr)

file=open('saved.jpg', 'wb')
while True:
    data=c.recv(1024)
    if not data :
        break
    file.write(data)

c.send(b"received")



s.close()
c.close()
file.close()