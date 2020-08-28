#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

import sys 

# try :
#     f = open('myfile.txt')
#     s =f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("os error: {0}".format(err))
# except ValueError:
#     print("could not convert data to an integer")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     # 抛出异常.
#     raise 

# for arg in sys.argv[1:]:
#     try :
#         f = open(arg,'r')
#     except IOError:
#         print("cannot open", arg)
#     else :
#         print(arg,'has', len(f.readlines()),'lines')
#         f.close()


# def this_fails():
#     x = 1/0
# 
# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print("handing run-time error:", err)

# try:
#     raise NameError("HiThrear")
# except NameError:
#     print("an exception flew by!")
#     raise

class MyError(Exception):
    def __init__(self, value):
        self.value = value 
    def __str__(self):
        return repr(self.value)
try:
    raise MyError(2*2)
except MyError as e:
    print("My Exception occurred, value:", e.value)
    