from pandas import DataFrame,Series
import pandas as pd
#设置显示的最大列、宽等参数，消掉打印不完全中间的省略号
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
df = pd.read_csv("dns_log.txt",sep='|',error_bad_lines=False)
print(df['ip'].value_counts().head(3))

