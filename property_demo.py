# 变量前加一个_表示私有属性或者私有方法,外界可以访问,但是不建议访问
# 变量前加两个__表示私有属性,外界无法直接访问

class Student(object):
    def __init__(self):
        self._score = None  # 变量前加一个_表示私有属性或者私有方法,外界可以访问,但是不建议访问

    @property
    def score(self):
        return self._score
        # raise AttributeError("非法读取")

    @score.setter
    def score(self, num):
        if 0 <= num <= 100:  # python不等式可以连写
            self._score = num
        else:
            raise ValueError("数字必须在0-100之间")

if __name__ == '__main__':
    student = Student()
    print(student.score)
    student.score = 100
    print(student.score)



