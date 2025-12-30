"""用range生成数时，无论怎样按索引（正负的大小位置）方向来，从小到大为正，从大到小为负"""
for item in range(-3, -1, 1):
    print(item)  # -3 -2
for item in range(-1, -3, -1):
    print(item)  # -1 -2

for item in range(3, 1, -1):
    print(item)  # 3,2

for item in range(1, 3, 1):
    print(item)  # 1 2
