import pandas as pd
import numpy as np
df = pd.read_csv("../HR.csv")
df_new = df["last_evaluation"]
print(df_new[df_new.isnull()])
#求均值 观察数据
print(df_new.mean())
#标准差
print(df_new.std())
#中位数
print(df_new.median())
print(df_new.max())
print(df_new[df_new>1])
#下次分位数
q_low=df_new.quantile(q=0.25)
q_high = df_new.quantile(q=0.75)
#四分位间距

q_interval = q_high-q_low
k=1.5
#满足条件的数据
df_new = df_new[df_new<q_high+k*q_interval][df_new>q_low-k*q_interval]
print(df_new)
print(len(df_new))