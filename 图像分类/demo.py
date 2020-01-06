with open('newTest.txt','r',encoding='utf-8') as f:
         dic=[]
         for line in f.readlines():
            line=line.strip('\n') #去掉换行符\n
            b=line.split("\t") #将每一行以空格为分隔符转换成列表
            dic.append(b)
dic=dict(dic)
for i in dic.keys():
    print(i)