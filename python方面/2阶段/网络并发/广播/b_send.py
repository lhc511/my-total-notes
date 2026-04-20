from socket import *
from time import sleep
 #广播地址
dest=('192.168.129.130',9999)
s=socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
data="""
****************** 
北京7.4 
盛夏温度:38.6 
状态:没有四块五的妞
*******************
"""

while True:
    sleep(2)
    s.sendto(data.encode(),dest)#目标地址三广播地