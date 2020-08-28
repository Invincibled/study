import pandas as pd

pd.set_option('display.max_columns', None)

with open("4exam_item.csv") as file:
    mapping = pd.read_csv(file, index_col="id")
    print(mapping)
