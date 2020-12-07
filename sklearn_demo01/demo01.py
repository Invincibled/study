from sklearn import tree
from sklearn.datasets import  load_wine
from sklearn.model_selection import  train_test_split

#  分类树.
wine = load_wine()

import pandas as pd

pd.concat([wine.data], [wine.target], axis=1)