import gevent
from gevent import monkey

monkey.patch_socket()
from socket import *


def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        c.send(b'ok')


s = socket()
s.bind(('0.0.0.0', 8888))
s.listen(4)
while True:
    c, addr = s.accept()
    print('connect from', addr)
    handle(c)
    gevent.spawn(handle, c)
