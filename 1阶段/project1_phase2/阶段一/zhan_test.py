"""逆波兰表达式"""
from sstack import *

st = SStack()
"""mine"""
while True:
    str_input=input()
    list_str=str_input.split(" ")
    for item in list_str:
        if item not in ["+"]:
            st.push(item)
        if item is ["+"]:
            x=st.pop()
            y=st.pop()
            print(x+y)
        if item is ["p"]:
            print(st.top())
            

"""teacher"""
# while True:
#     exp = input()
#     tmp = exp.split(" ")  # 按空格切割金print(tmp)
#     print(tmp)
#     for i in tmp:
#         if i not in ["+", "-", "*", "/", "p"]:
#             st.push(float(i))
#         elif i == "+":
#             y = st.pop()
#             x = st.pop()
#             st.push(x + y)
#         elif i == "p":
#             print(st.top())
