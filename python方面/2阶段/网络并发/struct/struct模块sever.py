from socket import *
import struct

st = struct.Struct('i10sif')
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('192.168.129.130', 8889))

# 接收发送测试1
# data, addr = s.recvfrom(1024)
# print(st.unpack(data))
# s.sendto(b'received', addr)

while True:
    data, addr = s.recvfrom(1024)
    if not st.unpack(data):
        break
    s.sendto(b'received', addr)
    stu_info = str(st.unpack(data))  # 进行二进制的解码，即转变为字符串
    with open('info_stu', 'a+') as info_fill:
        info_fill.write(stu_info)
        info_fill.write('\n')
s.close()