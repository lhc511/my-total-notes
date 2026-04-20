from time import sleep
from threading import Thread, Lock
"""
产生原因：在两个或多个线程均有锁的情况下，彼此线程在占用资源锁住的情况下需要彼此被占用的资源便会锁死

该案例：双方在借钱或者被借钱时账户会锁着，所以两方在同时使用账户时会让两条线程一直锁住
"""

# 交易类
class Account:
    def __init__(self, _id, balance, lock):
        self.id = _id  # 用户
        self.balance = balance  # 存款
        self.lock = lock  # 锁

    # 取钱
    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    # 查看余额
    def get_balance(self):
        return self.balance


# 产生两个账户
Tom = Account('Tom', 5000, Lock())
Alex = Account('A', 8000, Lock())


# 转账过程
def transfer(from_, to, amount):
    if from_.lock.acquire():  # 锁住自己账户
        from_.withdraw(amount)  # from账户减少
        sleep(0.5)
        if to.lock.acquire():  # 对方账户上锁
            to.deposit(amount)  # to账户加钱
            to.lock.release()  # to解锁
            from_.lock.release()  # from账户解锁
    print("%s给%s转账%d" % (from_.id, to.id, amount))
# transfer(Tom, Alex, 4000)
t1 = Thread(target=transfer, args=(Tom, Alex, 2000))
t2 = Thread(target=transfer, args=(Alex, Tom, 3500))
t1.start()
t2.start()
t1.join()
t2.join()
