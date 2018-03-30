"""
深拷贝,浅拷贝问题
以下代码执行后会修改a的值,请修改test()函数实现在不影响源代码逻辑的情况下调用前后a的值不受影响
"""

# def test(a = {}):
# 	b = a
# 	b['a'] = 1
# 	return b
# a = {'a':2}
# test(a)
# print(a)


import copy


def test(a={}):
    b = copy.deepcopy(a)
    b['a'] = 1
    return b


a = {'a': 2}
test(a)
print(a)
