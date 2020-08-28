#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

class Person:
    name = 'asfasd'
    age = '23432'
    __fuck = "22222"
    def __init__(self, name, age, fuck):
        name = name
        self.age = age 
        __fuck = fuck
    @classmethod
    def speak(self):
        print("类方法....." + self.name)
         
        
    @staticmethod
    def eat():
        print("静态方法")
        return 
        
    def normal(self):
        print("普通方法")
        return 
        
print(Person.name)
print(Person.age)
p = Person("time", 113,"fadsf")
# print(Person.__fuck)
print(p.name)
print(p.age)

print("-----------------\n")

Person.speak()
Person.eat()
#print(Person.normal())