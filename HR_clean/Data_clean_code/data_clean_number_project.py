import pandas as pd
import numpy as np
df = pd.read_csv("../HR.csv")
print(df)
#分析各个职员所做的工程数量
nn_s = df["number_project"]
print(nn_s)
#现在看看里面有没有空值
print(nn_s[nn_s.isnull()])
#平均值
print(nn_s.mean())
#标准差
print(nn_s.std())
#中位数
print(nn_s.median())
#最大值和最小值
print(nn_s.max())
print(nn_s.min())
#计算总数并且需要什么类型，也就是状态
print(nn_s.value_counts(normalize=True).sort_index())