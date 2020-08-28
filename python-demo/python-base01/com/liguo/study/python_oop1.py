#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

class Test:
    i = 12424
    def __init__(self, i):
        self.i = i
        print(self)
        print(self.__class__)
    def f(self):
        return "hello world"

x = Test(2)

print(x.f())
print(x.i)
print(x)