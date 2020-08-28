import pandas as pd

pd.set_option('display.max_columns', None)
# test1 = pd.ExcelFile('test.xlsx')
# print(test1.sheet_names)
#
# for sheet in test1.sheet_names:
#     df = pd.read_excel('test.xlsx', sheet_name=sheet, )
#     df.dropna(axis=0, how="all")
#     df.to_hdf(sheet + ".h5", 'data', format="table", append=True)

##########

test2 = pd.read_hdf("4T条各种条件的数据.h5")

print(test2)
# print(test2)
# column2 = test2.columns.str.strip('a')
#
# test2.columns = column2
# print(column2)
# print(test2)

print(test2.loc[:,'姓名'].value_counts().size)
############
# test3 = pd.read_hdf("晓丹数据.h5")
# # print(test3)
# column3 = test3.columns.values
# print(column3)
# #################
#
# test4 = pd.read_hdf("科学计数.h5")
# # print(test4)
# column4 = test4.columns.values
#
# print(test4.shape == test3.shape)
# print(test4.shape)
# print(test3.shape)


#print(True in test)
#
#
# df = pd.concat([test2, test3], axis=0, ignore_index=True)
# print(df)
# print(type(df))
#test3.to_hdf("4T条各种条件的数据.h5", 'data', format="table", append=True, index=False)
# hdf2 = pd.HDFStore("4T条各种条件的数据.hdf", 'w', complevel=4, complib='blosc', append=True)
# hdf2.put(key='data', value=test3)
# hdf2.close()

# test4 = pd.HDFStore('4T条各种条件的数据.h5', mode="w")
# test4.append("data", df, index=False)
# # print(test4.get('data'))
# # print(test4.keys())
# test4.close()
# print(pd.read_hdf('4T条各种条件的数据.h5'))
