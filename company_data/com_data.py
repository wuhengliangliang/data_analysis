import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame,Series

plt.rcParams['font.sans-serif']=['SimHei']
df = pd.read_csv("dataAnalyst_sql.csv",engine="python")
# print(df)

#计算函数
def countS(a,b):
    return s.loc[(df["secondType"] == a) & (df["education"] == b)].count()

s = df[["secondType","education"]]
s1 = countS("数据开发","本科")

s11 = s.loc[(df["secondType"]=="数据开发")&(df["education"]=="硕士")].count()
s2 = s.loc[(df["secondType"]=="数据分析")&(df["education"]=="本科")].count()
s22 = s.loc[(df["secondType"]=="数据分析")&(df["education"]=="硕士")].count()
s3 = s.loc[(df["secondType"]=="后端开发")&(df["education"]=="本科")].count()
s33 = s.loc[(df["secondType"]=="后端开发")&(df["education"]=="硕士")].count()

print(s1,+s11,s2,s22,s3,s33)