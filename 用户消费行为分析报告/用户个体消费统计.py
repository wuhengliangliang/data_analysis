import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#这份数据 分别是  用户的id  消费的日期 购买的产品数量，购买的金额
colums = ['usr_id','order_dt','order_products','order_amount']
#因为是txt的数据所以我用read_table
#这里的分割符是 多个空格
df = pd.read_table("CDNOW_master.txt",names=colums,sep='\s+')
#当我们看数据类型发现日期是 int类型，后期需要进行转换
print(df.info())
#转换日期的操作
df['order_dt'] = pd.to_datetime(df.order_dt,format="%Y%m%d")
#时间维度的转换 按照月份 ，values不能忘记加
df['month'] = df.order_dt.values.astype('datetime64[M]')
print(df.head())
#因为数据是按月的所以现在按照月份分组（聚合）
grouped_month = df.groupby('month')

# 一、用户消费金额、消费次数的描述统计
#按照用户进行分组，然后对用户id进行求和描述
grouped_user = df.groupby('usr_id')
print(grouped_user.sum().describe())
#利用散点图来观察
#用户消费金额、消费次数的描述统计可视化
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('ggplot')
plt.title("用户消费金额、消费次数的描述统计")
plt.ylabel("order_products")
plt.xlabel('order_amount')
#按照用户id进行每月的统计订单，都是一行
grouped_user.sum().query('order_amount < 4000').plot.scatter(x='order_amount',y='order_products')
plt.savefig('user_amount.jpg')
plt.show()
#使用分层的直方图来观看数据的趋势
grouped_user.sum().query("order_products<100").order_products.plot.hist(bins=40)
plt.savefig('order_amount_fencheng.jpg')
plt.show()

#用户消费金额的直方图
grouped_user.sum().query("order_amount<100").order_amount.plot.hist(bins=20)
plt.savefig('custome_amount.jpg')
plt.show()

#用户累计消费金额占比
#cumsum() 累加求和的函数
# user_cumsum = grouped_user.sum().sort_values('order_amount').cumsum()

user_cumsum = grouped_user.sum().sort_values('order_amount').apply(lambda x:x.cumsum()/x.sum())
print(user_cumsum)
#去除索引方便作图
user_cumsum.reset_index().order_amount.plot()
plt.savefig("用户消费累计比.jpg")