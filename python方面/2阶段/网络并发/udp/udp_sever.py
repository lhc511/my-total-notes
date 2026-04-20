import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 方式不一样
#绑定地址
server_addr=('127.0.0.1',8888)
s.bind(server_addr)  
#循环收发消息 
while True: 
    data, addr = s.recvfrom(1024)#内容 发送方地址
    print("收到消息:",data.decode())
    s.sendto (b'Thanks',addr)
    break
#关闭套接字
s.close()