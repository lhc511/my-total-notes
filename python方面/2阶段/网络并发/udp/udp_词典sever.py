from socket import *


def find_word(data):
    f = open('/home/ubuntu/桌面/dict.txt', 'r+')  # 要放在内部 或者用f.seek(0,0) 遍历之后文件偏移量会在末尾
    for line in f:
        w = line.split(" ")[0]
        if w == data.decode():
            f.close()
            return line
        elif w > data.decode():
            f.close()
            return "没找到"

    else:
        f.close()
        return "没找到"


ADDR = ('0.0.0.0', 8888)
s = socket(AF_INET, SOCK_DGRAM)
s.bind(ADDR)

while True:
    data, addr = s.recvfrom(1024)  # 发来的数据  发送方的地址
    result = find_word(data)
    s.sendto(result.encode(), addr)

s.close()
f.close()
