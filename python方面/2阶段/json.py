import json5

"""python里面是json5"""
js = json5.dumps({'a': 1, 'b': "hello"})
print(js)

# 在终端里面输入
# In[1]:
# import json
#
# In[2]: js = json.dumps({'a': 1, 'b': "hello"})
#
# In[3]: js
# Out[3]: '{"a": 1, "b": "hello"}'#字典变成字符串
#
# In[4]: json.loads('{"a": 1, "b": "hello"}')#字符串变回字典
# Out[4]: {'a': 1, 'b': 'hello'}
