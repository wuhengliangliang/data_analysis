#到"""之前这一段是打开spyder的界面就会自动添加的内容，一般不用去动。
#这一句是告诉电脑解码方式是UTF-8码，我们可以简单地理解为可以在代码里加中文，建议每次编程都加上。
# -*- coding: utf-8 -*-

#用（"""      """）包起来的这一部分电脑也是忽略掉的，主要是给人看的部分，分别是代码首次编写时间和作者，属于可写可不写的部分。
"""
Created on Sun Jul 24 23:11:55 2016

@author: 检
"""


#这里是导入模块，以下模块分别用于抓取网页、数据处理保存、时间、正则表达式
import requests as req
import pandas as pd
import time
import re

#这是刚才我们通过F12查找到的网页
# url='http://wenshu.court.gov.cn/List/ListContent'
url = 'http://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=65192ef535b85f94a539ec5acc1a84ef&s8=02http://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=65192ef535b85f94a539ec5acc1a84ef&s8=02'
#这是页数、程序休息时间的定义和三个空的列表用来装筛选后的数据。
Index=1
SleepNum = 3
dates=[]
titles=[]
nums=[]

#循环模块，因为有很多页，当小于这个数时，不断地传数据，相当于点下一页的功能。最后一句的意思是每执行一次，index加1，就是翻到下一页。具体页数也可以用变量实现。
while Index < 123:

    #这是请求头，伪装成浏览器访问网站，以免被网站屏蔽
    my_headers={'User-Agent':'User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.95 Safari/537.36 Core/1.50.1280.400',}

    #这一行就是我们搞定的搜索条件，可以按自己要求设置，比如：“法院名称:北京市人   民法院,案件类型:执行案件,裁判日期:2016-01-01 TO 2016-10-08”。
    #如果实在不会设置，可以在文书网上搜索好，再通过F12查看到的内容复制粘贴到代码中加红的区域即可。
    data={'Param':'全文检索：执行', 'Index': Index,'Page':'20','Order':'裁判日期','Direction':'asc'}

    #将网址、请求头、搜索条件等数据上传并取得内容
    r=req.post(url, headers=my_headers, data = data)

    #用 json解码取得的网页内容
    raw=r.json()

#用正则表达式将我们需要的内容提取出来，正则表达式真的很有用，要想真正用好westlaw等数据库，这一关也得过
#大意是定义筛选标准，把（“裁判日期”：）后，（'）前的内容截取出来。
    pattern1 = re.compile('"裁判日期":"(.*?)"', re.S)
    date = re.findall(pattern1,raw)
    pattern2 = re.compile('"案号":"(.*?)"', re.S)
    num = re.findall(pattern2,raw)
    pattern3 = re.compile('"案件名称":"(.*?)"', re.S)
    title = re.findall(pattern3,raw)

#把筛选出的数据添加到开始的三个空列表里
    dates+=date
    titles+=title
    nums+=num

#这一行是让程序休息，做事留点余地比较好。通过网页编码可知，文书网是有验证码功能的，如果你抓的太狠中招莫怪。
    time.sleep(SleepNum)
    Index += 1
#这里我们可以看到，从while开始到此，所有的代码都缩进了四个空格。这是因为要告诉电脑，这一段代码构成一个相对独立的组，当index小于123时，不断地从这个组第一句代码执行到最后一句代码，而不涉及到本文涉及的其他代码。

#这里代码又是顶格写。
#用pandas模块将筛选出的内容转成dataframe格式，并保存到Excel。
df=pd.DataFrame({'时间':dates,'案号':nums, '案件名称':titles})
df.to_excel('C:\\result.xlsx')