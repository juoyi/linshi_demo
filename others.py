# def factorial(x):
#     result = 1
#     for i in range(2, x + 1):
#         result *= i
#     return result
#
#
# if __name__ == '__main__':
#     res = factorial(10)
#     print(res)
#
#


# def runTime(func):
#     def wrapper(*args,**kwargs):
#         import time
#         t1 = time.time()
#         func(*args,**kwargs)
#         t2 = time.time()
#         print("%s run time: %.5f s" %(func.__name__,t2-t1))
#     return wrapper
#
#
# @runTime
# def fib(n):
#     def _fib(n):
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return _fib(n-1) + _fib(n-2)
#     return _fib(n)
#
# fib(30)


def fiblist(num1, num2, n):
    li = [num1, num2]
    for i in range(n-2):
        num1, num2 = num2, num1 + num2
        li.append(num2)
    return li

res = fiblist(num1=1, num2=2, n=10)
print(res)

