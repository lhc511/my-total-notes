import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ADDR=('127.0.0.1',8888)
while True:
    data=input("msg:")
    if not data:
        break
    s.sendto(data.encode(),ADDR)
    data,addr=s.recvfrom(1024)
    print(data.decode())
s.close()