import os
import numpy as np

import pandas as pd

pd.set_option('display.max_columns', None)
#
# test2 = pd.read_hdf("晓丹数据.h5", columns=['备注1'])
# print(test2)
# print(test2.shape)
# print(test2.count())
# print(test2.isna())

# 模拟数据
data = pd.DataFrame({'price': np.random.randn(1000),
                     'amount': 100*np.random.randn(1000)})

print(data)
# 等分价格为10个区间
quartiles = pd.cut(data.price, 10)
print(quartiles)
# 定义聚合函数
def get_stats(group):
    return {'amount': group.sum()}

# 分组统计
grouped = data.amount.groupby(quartiles)
price_bucket_amount = grouped.apply(get_stats).unstack()

print(grouped)
print(price_bucket_amount)
