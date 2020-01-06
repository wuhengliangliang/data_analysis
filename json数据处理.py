import numpy as np

import pandas as pd

pd.set_option('display.max_columns', 1000)

pd.set_option('display.width', 1000)

pd.set_option('display.max_colwidth', 1000)
df = pd.read_json("地震预处理好的.json",encoding="utf8")
# print(df["no"])
# for i in range(62):
    # print(i)
    # for j in range(i):
x = df["no"][0]
        # if df["no"][j]== "eid":
print(len(x))
# print(x[0])
if "eid" in x[0]:
    a = str(x[0]).replace("eid","1")
    print(a)
    # print(df["no"][i])

    # i = i + 1