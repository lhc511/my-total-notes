import getpass
import hashlib  # 转换加密

# pwd = getpass.getpass()  # 这个函数只能在终端上调用 在输入时可以隐藏输入 和input一样
pwd = getpass.getpass("PW")  # 这个函数只能在终端上调用 在输入时可以隐藏输入 和input一样
print(pwd)
# hash对象
# hash = hashlib.md5()

#算法加盐
hash = hashlib.md5("#$%^87".encode())#在原本的密码与新添的字符串拼接在加密

hash.update(pwd.encode())  # 加密处理

pwd = hash.hexdigest()  # 提取加密后的密码
print(pwd)
