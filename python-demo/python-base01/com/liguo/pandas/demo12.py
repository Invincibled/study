import pandas as pd
import numpy as np
import random


data = np.zeros((1000,1000),dtype=int)
for i in range(len(data)):#这里速度比较慢，因为随机给1000*1000的数组赋值
    for j in range(len(data[0])):
        data[i][j] = random.randint(1,20)#赋值的范围是1-20中的任意一个

#首先构造数据，这里注意构造的是一维数组可以使用pandas中的Series，如果是二维数组使用DataFrame。
data_m = pd.DataFrame(data)
data_m = data_m[1].value_counts()#注意value_counts函数统计一个series上的数据情况
data_m = data_m.sort_index()#给统计后的数据排序
# print(data_m)

#随后开始画直方图
# import matplotlib.pyplot as plt
#
# fig = plt.figure(figsize=(15, 7))
# # test = plt.hist(data[0])
# #
# # plt.show()
#
#
# test2 = plt.hist(data[0], bins=20)
# print(test2)
# plt.xticks(test2[1])
# for i in test2[2]:
#     print(i)
    # print(i.width())
# plt.show()
# plt.show()

import time

import random

import rpy2.robjects as robjects


def random_int_list(start, stop, length):
  start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
  length = int(abs(length)) if length else 0
  random_list = []
  for i in range(length):
   random_list.append(random.randint(start, stop))
  return random_list

list1 = random_int_list(1,100,100)
print(list1)

# pic = robjects.r('pic <- hist('+data_m[0]+', breaks=10)')
now = time.time()

v = robjects.FloatVector(list1)
pic2 = robjects.r['hist'](v, breaks=25)

ll = time.time()
# print(ll - now)
breaks = list(pic2[0])
counts = list(pic2[1])
print(list(pic2[0]))
print(list(pic2[1]))
sumlist = len(pic2[1])

for i in range(0, len(breaks)-1):
    print(f"{breaks[i]}--{breaks[i+1]}---{counts[i]}----{ '%.2f' % ( counts[i] * 100 / sumlist) }")


# creat an R function，自定义R函数
# robjects.r('''
#            ht <- function(arr, bin){
#              pic <- hist(arr, breaks=bin)
#              r <- list(one=pic$breaks, two=pic$counts)
#              return (r)
#            }
#     ''')
#
# t3=robjects.r['ht'](v, 25)
# print(t3)
# print(t3["one"])
# print(t3[2])
# for i in pic2:
#     print(type(i))
#     for t in i:
#         print(t)
#print(pic2)


