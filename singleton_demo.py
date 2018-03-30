"""单例模式的几种实现方式"""


# 使用__new__
class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance


s1 = Singleton()
print(id(s1))
s2 = Singleton()
print(id(s2))


# python 中的模块就是天然的单例模式,模块第一次被导入时会创建.pyc文件,第二次导入时会直接加载.pyc文件
# 不会执行模块中的代码

# 装饰器实现
