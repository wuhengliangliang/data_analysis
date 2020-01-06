import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import scipy.stats as ss


from pandas import DataFrame,Series

df = pd.read_csv("./skip_Data/HR.csv")
#我想要看各个部门的离职分布
#通过 indices 拿到分组后的索引
df_index = df.groupby(by="department").indices
#拿到销售部门的离职值
sales_values = df['left'].iloc[df_index['sales']].values
technical_values = df['left'].iloc[df_index['technical']].values
#在python3中所有的keys加上一个list,然后才能转换为数组
dp_keys = list(df_index.keys())
#初始化一个矩阵
df_t_mat = np.zeros([len(dp_keys),len(dp_keys)])
for i in range(len(dp_keys)):
    for j in range(len(dp_keys)):
        p_value = ss.ttest_ind(df['left'].iloc[df_index[dp_keys[i]]].values,\
                  df['left'].iloc[df_index[dp_keys[j]]].values)[1]
        #对矩阵进行赋值
        if p_value<0.05:
            df_t_mat[i][j] = -1
        else :
            df_t_mat[i][j] = p_value
sns.heatmap(df_t_mat,xticklabels=dp_keys,yticklabels=dp_keys)
plt.savefig("1.jpg")
plt.show()
