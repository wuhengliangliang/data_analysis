import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from pandas import DataFrame,Series
#设置显示的最大列、宽等参数，消掉打印不完全中间的省略号
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
df = pd.read_csv("log_movie.txt",sep=',',error_bad_lines=False)
plt.rcParams['font.sans-serif']=['SimHei']

# bool = df["text"].str.contains('烈火英雄')
# print(type(bool))
# filter_data = df[bool]
# filter_data.to_csv("烈火英雄")
# print('filter data : \n', filter_data)
D_F = df.drop_duplicates(subset=None, keep='first', inplace=False)
