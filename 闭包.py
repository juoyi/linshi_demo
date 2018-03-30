"""
闭包就是调用函数A的时候,该函数返回了一个函数B给你,这个返回的函数B就是闭包
你在调用函数A的时候传递的参数就是自由变量
"""


def count(start=0):
    def inner():
        # nonlocal与global的区别在于nonlocal语句会搜寻本地变量与全局变量之间的变量
        # 会优先寻找层级关系与闭包作用域最近的外部变量
        nonlocal start
        start += 1
        return start
    return inner


f1 = count(10)
f2 = count(20)
print(f1())
print(f1())
print(f1())
print(f1())
print(f1())

print("***"*20)

print(f2())
print(f2())
print(f2())
print(f2())
print(f2())
