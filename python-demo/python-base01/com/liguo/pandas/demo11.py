# import pandas as pd
# import numpy as np
#
# df_excel = pd.read_excel("波士顿房价.xlsx", sheet_name="Sheet1"
#                         )
# df_excel.dropna(axis=0, how="all")
# df_excel.columns = df_excel.columns.str.replace('\n', '', regex=True)
# df = df_excel.round(6)
#
# df.to_csv('out2.csv', mode='w', encoding="utf-8", index=False)



import random
import pandas as pd
import numpy as np
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
from pandas import Series,DataFrame
#用随机数产生一个二维数组。分别是年龄的性别。
df = pd.DataFrame({'Age': np.random.randint(0, 70, 100),
                   'Sex': np.random.choice(['M', 'F'], 100),
                })
#用cut函数对于年龄进行分段分组，用bins来对年龄进行分段，左开右闭
age_groups=pd.cut(df['Age'], 5)

print(age_groups.value_counts().to_dict())
# for key, value in age_groups.value_counts(sort=False).to_dict().items():
#     print(key.left)
#     print(key.right)
#     print(value)
# print(df.groupby(age_groups).count())


# var_f = 124.3242343;

#
# print(np.floor(var_f))
tt = [1,3,252,4534,35345]
print(tt)



def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]


print(find_nearest(tt, 54))

