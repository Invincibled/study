class MyClass:
    i = "xxxx"

    def f(self, name, age):
        self.name = name
        self.__age = age
        return "测试"

class Employee:

    pass


if __name__ == '__main__':
    MyClass.f
    MyClass.i
    my = MyClass()
    my.f("xxxx",22)
    my.name

    john = Employee()
    john.name = "xxxxx"
    john.dept = "yyy"
    print(john.name)
    #my.__age
    #MyClass.__init__()
    for key in {'one': 1, 'two': 2}.values():
        #print(key)
        print(key)
    s = "abc"
    it = iter(s)
    it.__next__()
    next(it)