"""with.py 使用w i t h 语句打开文件"""
with open('dayQ2') as f:#生成文件对象
    data =f.read()
    print(data)
 # with语句块结束 f对象被自动销毁