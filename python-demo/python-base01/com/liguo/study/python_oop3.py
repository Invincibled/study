#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

class People:
    name = ''
    age = 0 
    __weight = 0
    
    def __init__(self, n, a, w):
        self.nae = n
        self.age = a
        self.__weight =w
    def speack(self):
        print("")

if __name__ == '__main__':
    p = People(1,2,3)
    print(p.age)