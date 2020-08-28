import pandas as pd
import numpy as np
# pd.set_option('display.max_columns', None)
#
# df_values = pd.read_csv("yw20200331-2_Sheet1.csv", dtype=np.str, keep_default_na=False)
#
# print(df_values)

# str = "tt"
# print(str+"测试")
from sklearn.preprocessing import minmax_scale

# test_array_numpy = [2.395,3423.132,91.00,2341.132, 15937.0]
test_array_numpy = [1668494936442, 1668491659643, 2129887299937, 2129887299937]
# test_array_numpy = np.array(test_array)
# your function
def normalize_list(list_normal):
    max_value = max(list_normal)
    min_value = min(list_normal)
    for i in range(len(list_normal)):
        list_normal[i] = (list_normal[i] - min_value) / (max_value - min_value)
    return list_normal

#Scikit learn version
def normalize_list_numpy(list_numpy):
    normalized_list = minmax_scale(list_numpy, copy=True)
    return normalized_list

# test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# test_array_numpy = np.array(test_array)

# print(normalize_list(test_array))
print(np.around((normalize_list_numpy(test_array_numpy)), 3))
print((normalize_list_numpy(test_array_numpy)))
