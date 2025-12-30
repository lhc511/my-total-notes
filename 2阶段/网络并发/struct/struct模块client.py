from socket import *
import struct

st=struct.Struct('i10sif')
def input_info():
    id = int(input("请输入编号："))
    if id=="":
        return
    name = input("请输入姓名：").encode()
    age = int(input("请输入年龄："))
    score = float(input("请输入分数："))
    data = st.pack(id, name, age, score)  # 以二进制形式打包
    return data


s = socket(AF_INET, SOCK_DGRAM)
ADDR = ('192.168.129.130', 8889)
while True:
    info=input_info()
    if not info:
        break
    s.sendto(info,ADDR)
    data,addr=s.recvfrom(1024)
    print(data.decode())

s.close()