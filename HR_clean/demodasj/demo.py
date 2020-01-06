import pandas as pd
import numpy as np
df = pd.read_csv("训练集.csv")
df_index = pd.read_csv("训练集.csv",header=None,names=['USER_ID','FLOW','FLOW_LAST_ONE','FLOW_LAST_TWO','MONTH_FEE','MONTHS_3AVG','BINDEXP_DATE','PHONE_CHANGE','AGE','OPEN_DATE','REMOVE_TAG',','])#加索引
print(df_index["USER_ID"])
