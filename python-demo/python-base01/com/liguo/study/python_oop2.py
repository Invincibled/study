#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

class People:
    name = ''
    age = 0 
    __weight = 0 
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁"%(self.name, self.age))
        
# p = People('runoob', 10, 30)
# p.speak()
# p.name

class Student(People):
    grade = ''
    def __init__(self, n, a, w, g):
        People.__init__(self, n, a, w)
        self.grade = g
    def speak(self):
        print("%s 说: 我 %d 岁了, 我在读 %d年级"%(self.name, self.age, self.grade))

# s = Student('ken',10,32,5)
# s.speak()
class Speaker():
    topics = ''
    name =''
    def __init__(self, n ,t):
        self.topicss = t
        self.name =  n 
    def speak(self):
        print("我叫 %s, 我是一个演说家,我讲的主题是%s" %(self.name, self.topics))    
class Sample(Speaker, Student):
    a = ''
    def __init__(self,n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)

test = Sample("tim",23,244,4, "Python")
test.speak()