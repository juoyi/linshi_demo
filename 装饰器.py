# """
# 装饰器的功能:
# 1.引入日志
# 2.函数执行时间的统计
# 3.执行函数前预备处理,如flask的请求钩子
# 4.执行函数后清理功能
# 5.权限校验等场景,如登陆验证装饰器
# 6.缓存
# """
#
import time
from functools import wraps
import math


def timefunc(func):
    """统计一个函数的运行时间"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)  # 调用被装饰函数
        end_time = time.time()
        print("function %s runtime is %s" % (func.__name__, end_time - start_time))
        print(res)
        # return res
    return wrapper


# @timefunc
# def factorial(num):
#     """计算一个正整数的阶乘"""
#     if num == 0 or num == 1:
#         return 1
#     elif num > 1:
#         return num * factorial(num-1)
#c
#     # math.factorial(num)  # 直接导库
#
#     result = 1
#     for i in range(1, num+1):
#         result *= i
#     return result
#
#
# if __name__ == '__main__':
#     res = factorial(10)
#     print(res)


# def clock(func):
#     def clocked(*args):
#         t0 = time.perf_counter()
#         result = func(*args)
#         elapsed = time.perf_counter() - t0
#         name = func.__name__
#         # arg_str = ', '.join(repr(arg) for arg in args)
#         # print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
#         print('[%0.8fs] %s -> %r' % (elapsed, name, result))
#         return result
#
#     return clocked


@timefunc
def factorial(n):
    def _factorial(n):
        return 1 if n < 2 else n * _factorial(n - 1)
    return _factorial(n)


@timefunc
def factorialloop(n):
    res = 1
    for i in range(2, n+1):
        res = res * i
    return res


if __name__ == '__main__':
    factorial(50)
    factorialloop(50)
