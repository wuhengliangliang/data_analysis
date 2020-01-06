import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#需求：
#用户第一次消费（首购）
# 用户最后一次消费
# 新老客户消费比
#    多少用户仅消费一次？
#    每月新客户比？
# 用户分层
#     RFM
#     新、老、活跃、回流、流失
# 用户购买周期（按订单）
#     用户消费周期描述
#     用户消费周期分布
# 用户生命周期
#     用户生命周期描述
#     用户生命周期分布
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



#按照用户进行分组，然后对用户id进行求和描述
#用户首购距离日期最远第一次，先对所有用户聚合
grouped_user = df.groupby('usr_id')

#设置图像形状
plt.style.use('ggplot')
#然后求出最小的时间，也就是距离现在最遥远的时间
grouped_user.min().order_dt.value_counts().plot()

plt.savefig('用户首购距离最远.jpg')
plt.show()
#分析：用户在第一次购买分布，集中在前三个月，其中，在2月11日至2月25日有一次剧烈的波动




#用户首购距离日期最近第一次，也就是最后一次消费，先对所有用户聚合
grouped_user = df.groupby('usr_id')

#设置图像形状
plt.style.use('ggplot')
#然后求出最小的时间，也就是距离现在最遥远的时间
grouped_user.max().order_dt.value_counts().plot()
plt.savefig('用户首购距离最近.jpg')
plt.show()
#图像分析：用户最后一次购买的分布比在第一次分布广
# 大部分最后一次购买，集中在前三个月，说明有很多用户购买了一次后就不在进行购买
#随着时间的递增，最后一次购买数也在递增，消费呈现流失上升的状况



# 新老客户消费比
user_life = grouped_user.order_dt.agg(['min','max'])
print(user_life.head())

#如果用户最后一次消费和最后一次消费日期相等，那么就说明用户只消费了一次
rate = (user_life['min']==user_life['max']).value_counts()
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
labels = ['只消费一次用户','多次消费用户']
plt.axis('equal') # 保证长宽相等
plt.pie(rate,explode=(0,0.15),labels=labels,autopct='%2.1f%%',startangle=90,colors=['r','orange'],radius=1.5)
plt.savefig("消费比")
#看看true和false谁更多

#用户分层：
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
grouped_user.max().order_dt.value_counts().plot()
plt.savefig("用户分成")
plt.show()
#利用透视分层
rfm = df.pivot_table(index = 'usr_id',
                     values = ['order_products','order_amount','order_dt'],
                     aggfunc={'order_dt':'max',
                              'order_amount':'sum',
                              'order_products':'sum'
                     })
print(rfm.head())
rfm['R'] = -(rfm.order_dt - rfm.order_dt.max()) / np.timedelta64(1,'D')
#对字段进行重命名
rfm.rename(columns = {'order_products':'F','order_amount':'M'},inplace=True)
print(rfm.head())


#定义函数把其中的数字转换成对应的信息
# 负数是小于的   正式大于的
# R：离最近一次购买的天数   F：产品数（消费次数） M：消费金额   与均值的对比
def rfm_func(x):
    level = x.apply(lambda x:'1' if x>= 0 else '0')
    # 字符串拼接
    #  111，R>0,是距离平均消费时间要久，R越大 说明没有消费时间越久  ，F >0 M>0,消费次数和金额也是较高的，重要价值客户，依次类推
    label = level.R + level.F + level.M
    d = {
        '111':'重要价值客户',
        '011':'重要保持客户',
        '101':'重要挽留客户',
        '001':'重要发展客户',
        '110':'一般价值客户',
        '010':'一般保持客户',
        '100':'一般挽留客户',
        '000':'一般发展客户'
    }
    result = d[label]
    return result
# x - x.mean() （具体真实情况可以修改，不一定需要用均值）   切比雪夫也可以 > 200 极值人工处理掉
rfm['label'] = rfm[['R','F','M']].apply(lambda x:x-x.mean()).apply(rfm_func,axis=1)
print(rfm)

#重要占比
print(rfm.groupby('label').sum())
print(rfm.groupby('label').count())


# 各类类型用户占比
use_c = rfm.groupby('label').count()
plt.axis('equal')
labels = ['一般价值客户','一般保持客户','一般发展客户','一般挽留客户','重要价值客户','重要保持客户','重要发展客户','重要挽留客户']
plt.pie(use_c['M'],
       autopct='%3.1f%%',
       labels = labels,
       pctdistance=0.9,
       labeldistance = 1.2,
       radius=3,
       startangle = 15)
pivoted_counts = df.pivot_table(index = 'usr_id',
                                  columns = 'month',
                                  values = 'order_dt',
                                  aggfunc = 'count').fillna(0)
# pivoted_counts.head()
print(pivoted_counts.head())
# 按月份进行对比，1月份哪些是购买的，再去对比二月份哪些是购买的
df_purchase = pivoted_counts.applymap(lambda x : 1 if x> 0 else 0)
print(df_purchase.tail())
def active_status(data):
    status = []
    for i in range(18):

        # 若本月没有消费
        if data[i] == 0:
            if len(status) > 0:
                if status[i - 1] == 'unreg':
                    status.append('unreg')
                else:
                    status.append('unactive')
            else:
                status.append('unreg')
                # 若本月消费
        else:
            if len(status) == 0:
                status.append('new')
            else:
                if status[i - 1] == 'unactive':
                    status.append('return')
                elif status[i - 1] == 'unreg':
                    status.append('new')
                else:
                    status.append('active')
# 这里需要对返回的值进行转换，将列表转为Series
    return status
purchase_status = df_purchase.apply(active_status,axis = 1)
print(purchase_status.head())
purchase_status_ct = purchase_status.replace('unreg',np.NaN).apply(lambda x:pd.value_counts(x))
print(purchase_status_ct)
purchase_status_ct.fillna(0).T.plot().area()
plt.savefig("用户面积")
plt.show()