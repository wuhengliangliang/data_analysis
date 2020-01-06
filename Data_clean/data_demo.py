# import codecs

import pandas as pd
# df_index = pd.read_csv("shuju.csv",header=None,names=['num','','direcor','role','init_year','area','genre','rating_num','comment_num','comment','url'])#加索引

# df = df_index.to_csv("Data.csv",sep=',')#把有索引的重新写入一个文件中
df = pd.read_csv("Data.csv")#读取我刚刚转换有索引的数据

#print(df[["num","area","rating_num","genre"]].to_csv("newData.csv"))#再拿到我的三个索引的数据，事实上比赛结果只要2个索引数据我弄多了，不过都一样的
#df = pd.read_csv("newData.csv")#读取我指定索引的数据
print(df[["num","area","rating_num","genre"]].sort_values(by='rating_num', ascending=False, na_position='first').head(10)) #按照题目要求对评论次数进行排序
# -*-coding:utf-8 -*-

#设置文件的utf8的格式
# f = codecs.open('top250_f1.txt','r','utf-8')
# s = f.readlines()
# f.close()
# for line in s:
#     line.encode('utf-8')
# import csv #导入csv模块
# with open('shuju.csv', 'w+', newline='',encoding='utf-8') as csvfile:
#     spamwriter = csv.writer(csvfile,dialect="excel")#delimiter= ','修改为自己想要的分割符号
#     # 读要转换的txt文件，文件每行各词间以字符分隔
#     with open('top250_f1.txt', 'r', encoding='utf-8') as filein:
#         for line in filein:
#             line_list = line.strip('\n').split('\t')   #我这里的数据之间是以 ; 这里我的数据是以tab分割的
#             spamwriter.writerow(line_list) #按照每一行进行写入




