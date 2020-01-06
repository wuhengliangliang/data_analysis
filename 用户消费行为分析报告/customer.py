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
#现在形成了聚合好的对象
order_month_amount = grouped_month.order_amount.sum()
print(order_month_amount.head())
#现在对月份的金额的数据进行可视化
#下面两个参数设置，为了中文可以显示
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.style.use('ggplot')
plt.title("每月的金额总数趋势变化统计")
plt.xlabel("日期")
plt.ylabel("元")
order_month_amount.plot()
plt.savefig('amount.jpg')
plt.show()


#对每月订单数的统计进行可视化
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('ggplot')
plt.title("每月订单数量趋势变化")
plt.ylabel("订单数量")
#按照用户id进行每月的统计订单，都是一行
grouped_month.usr_id.count().plot()
plt.savefig('order.jpg')
plt.show()

#产品购买量可视化
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('ggplot')
plt.title("每月产品购买数量趋势变化")
plt.ylabel("产品购买数量")
#按照用户id进行每月的统计订单，都是一行
grouped_month.order_amount.count().plot()
plt.savefig('order_amount.jpg')
plt.show()

#按月的人数数据可视化，首先我们需要知道，一个在一个月份里面可能多次购买，这时候我们需要对数据进行人数的去重
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('ggplot')
plt.title("每月的人数趋势")
plt.ylabel("人数")
#对人数进行去重,人后去重过后直接统计人数：，去重x.drop_duplicates()
df.groupby('month').usr_id.apply(lambda x:len(x.drop_duplicates())).plot()
#去重数据的方法二：
# df.groupby(['month','usr_id']).count().reset_index()
plt.savefig('people_amount.jpg')
plt.show()
