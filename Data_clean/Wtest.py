import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from  pandas import DataFrame,Series
from pyecharts import Line
import seaborn as sns
from matplotlib.pyplot import MultipleLocator
sns.set_style(style="whitegrid")

line=Line("折线图示列")  # title
# df = pd.read_csv("Data.csv")
# print(type(df))#查一下类型
# #指定获取某一列的两种方式
# print(df['comment_num'])
# print(df.role)
# #生成新的一列
# df_new = DataFrame(df,columns=['title','rating_num', 'comment_num','index'])
# #为某一列不存在的值赋值
# df_new['index'] = range(0,250)
# print(df_new['index'])
#
# #指定其中的列的值的改变，比如某个值为空值,下面这句话的意思就是，把index这列的索引为1和2的赋值为100,200，其他的行默认为pandas填充
# df_new['index'] = pd.Series([100,200],index=[1,2])
# print(df_new['index'])
#
#
# #按照新生成的列其中的某个列的值进行排序，这里是电影的评分
# print(df_new.sort_values(by='rating_num',ascending=False).head(20))
# columns=['date' 'weather'   'high'    'low'  'win'    '  ']
# df = pd.read_csv("word.txt")
# print(type(df["date"]))
#
# df_new = df.loc[df['date']>"2018-9-0"]
# df_new1 = DataFrame(df_new)
# df_new1.to_csv("cleanWeather.csv")
df = pd.read_csv("cleanWeather.csv")
print(df['date'])
print(df['high'])



# delay_group=df_new.groupby([x,y])
# df_delay=delay_group.size().unstack() #转换为DataFrame  然后进行数据可视化
# df_delay.plot()


# plt.xticks(rotation=45)
plt.xlabel("counts",fontsize=14) #设置X轴的
plt.ylabel("temperature")#设置y轴
plt.title("nine mounth")
#加上标注在坐标下面有值
# plt.xticks(np.arange(len(df["high"].value_counts())),df["high"].value_counts().index)
# #设置范围
plt.axis([0,30,0,35])
#设置轴的间隔
#ax为两条坐标轴的实例
ax=plt.gca()
#把x轴的刻度间隔设置为5，并存在变量里
x_major_locator=MultipleLocator(1)
#把x轴的主刻度设置为5的倍数
ax.xaxis.set_major_locator(x_major_locator)

sns.set_context(context="poster",font_scale=0.1)
# plt.bar(np.arange(len(df["high"].value_counts()))+0.5,df["high"].value_counts(),width=0.8)
plt.plot(df["date"],df["high"],c='green')
for x,y in zip(np.arange(len(df["date"].value_counts())),df["high"].value_counts()):
    plt.text(x,y,y,ha="center",va="bottom")
plt.savefig("weather.jpg")
plt.show()

sns.pointplot(df["date"],df["high"])
sns.set_context(context="poster",font_scale=0.1)
plt.savefig("2.jpg")
plt.show()

line.add("气温",df["date"],df["high"],ymbol_size=2,is_step=False,is_label_show=df['date'])
line.render("zhexian.html")   #生成对于的HTML文件
# print(df_new.head(10))



