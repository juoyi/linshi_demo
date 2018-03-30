# coding=utf-8

# import time
# from functools import wraps


# def timefunc(func):
#     """统计一个函数的运行时间--装饰器函数"""
#     # @wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         res = func(*args, **kwargs)  # 调用被装饰函数
#         end_time = time.time()
#         print("function %s runtime is %s" % (func.__name__, end_time - start_time))
#         print(res)
#     return wrapper


# @timefunc
# def fib(n):
#     """递归法求fibonacci数列"""
#     def _fib(n):
#         # if not isinstance(n, int) or n < 0:
#         #     raise ValueError('请输入正整数!')
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return _fib(n-1) + _fib(n-2)
#     return _fib(n)


# @timefunc
# def fibloop(n):
#     """利用循环求fibonacci数列"""
#     fib1, fib2 = 0, 1
#     for i in range(n-1):
#         fib1, fib2 = fib2, fib1 + fib2
#     return fib2


# if __name__ == '__main__':
#     fib(30)
#     fibloop(30)

def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

for index, x in enumerate(fib()):
    if index == 10:
        break
    print("%s" % x)