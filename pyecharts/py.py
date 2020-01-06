from pyecharts import  Bar,Line,Pie         # 用于图形数据的添加以及展现   Bar Line Pie 分别是柱状图 折线图 饼图
import pandas as pd  #读取文件的库
df=pd.read_csv("./Data.csv")  # 读取css文件的操作
# v2=df["Data"]
v1=df["city"]  # 读取文件中的某一列的字段
# print(df["Age"].value_counts())
# v1 = [2.0,4.9,5.0,6.0,7.0,8.0,4.5,8.6,9.6,5.4,7.6,8.5]
# v2 = [2.8,4.1,8.0,7.0,9.0,4.0,2.5,9.6,7.6,3.4,9.6,4.5]
bar=Bar("柱状图示例")  # title
line=Line("折线图示列")  # title
pie=Pie("饼图示例")         # title
# print(df["Data"].value_counts())
# bar.add("济南是房屋出租",df["city"],df["avg"])
bar.add("济南市房屋出租",df["city"],df["avg"],bar_category_gap="50%",mark_line=["average"],mark_point=["max","min"],is_label_show=df['city']) # bar_category_gap="50%"加上柱子的大小的百分比
# bar.add("降水量",df["city"].value_counts().index,df["city"].value_counts(),mark_line=["average"],mark_point=["max","min"])
line.add("济南市房屋出租",df["city"],df["avg"],ymbol_size=2,is_step=False,is_label_show=df['city'])    # 可以直接点按住ctrl 鼠标放到add上  点击进去可以看里面的注释 更详细
pie.add("济南市房屋出租",df["city"],df["avg"],is_label_show=df['city'])
bar.show_config()
bar.render("ss.html")           #生成对于的HTML文件
line.render("zhexian.html")   #生成对于的HTML文件
pie.render("bintu.html")        #生成对于的HTML文件
