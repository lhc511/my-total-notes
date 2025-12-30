from package01.module_a import fun01  # 通过包访问模块来调用函数
from package01.package02.module_b import fun02
fun01()
fun02()

import  package01.module_a as pm
pm.fun01()