class A:

    def m01(self):
        print("A-m01")


class B(A):

    def m01(self):
        print("B-m01")


class C(A):

    def m01(self):
        print("C-m01")


class D(B, C):

    def m02(self):
        self.m01()


d01 = D()
d01.m02()

print(D.mro())  # mro() 打印出该子类在调用父类
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
