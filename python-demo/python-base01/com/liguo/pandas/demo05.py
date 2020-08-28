import pandas as pd
import numpy as np
from itertools import groupby
from operator import itemgetter


# list= [1,2,3,4,56,7,7]
# print(np.mean(list))
# print(np.std(list,ddof=1))
list2 =[]
dict1 = {"name": "测试1", "category": "Test1"}
dict2 = {"name": "测试2", "category": "Test1"}
dict3 = {"name": "测试3", "category": "Test2"}
dict4 = {"name": "测试4", "category": "Test2"}

if "name" in dict1.keys():
    print("Test1")
# list2.append(dict1)
# list2.append(dict2)
# list2.append(dict3)
# list2.append(dict4)
# print(list2)
# list3 = []
# grouper = itemgetter("category")
# for key, value in groupby(list2, grouper):
#     print("k---%s, v----%s", key, dict(value))
#     dict5 = {"category": key, "list": zip(value)}
#     list3.append(dict5)
#
# print(list3)

# list1 = ['2019-02-03', '2019-01-11', '2020-02-22', '2019-11-11']
# print(list1.min())
# print(list1.max())



# list2 =[[1.2343],[3423],[3423],[234231],[13242765], [7.135]]
# # l = pd.Series(list2)
# # print(l)
#
# pt = np.quantile(list2, 0.5)
# pt2 = np.quantile(list2, 0.95)
# print(pt)
# print(pt2)


