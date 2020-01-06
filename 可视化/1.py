import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("DataAnalyst.csv",encoding='gbk')
print(df)
df['salary'].value_counts().sort_index().plot.bar()
plt.show()
#图像堆积的形式：bar(stacked=True)
df.pivot_table(index = 'city',columns='education',values='salary',aggfunc='count').plot.bar(stacked=True)
plt.show()
print(df.groupby('education').apply(lambda x:x))