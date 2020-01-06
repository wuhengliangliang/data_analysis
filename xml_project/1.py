#-*-coding: utf-8-*-
#修改文件编码格式
import codecs
import re
import codecs
import re
def replaceXmlEncoding(filepath):
    f = open(filepath, mode='r',encoding="utf-8")
    content = f.read()#文本方式读入
    content = re.sub("GB2312", "UTF-8", content)#替换encoding头
    f.close()
    f = open(filepath, 'w')#写入
    f.write(content)
    f.close()
    f = codecs.open(filepath, 'rb', 'mbcs')#二进制方式读入
    text = f.read().encode("utf-8")#使用utf-8方式编码
    f.close()
    f = open(filepath, 'wb')#二进制方式写入
    f.write(text)
    f.close()

replaceXmlEncoding("3.xml")

from xml.dom.minidom import parse
import xml.dom.minidom
replaceXmlEncoding("3.xml")
#dom解析xml
DOMTree = xml.dom.minidom.parse("3.xml")
#返回文档的根节点
root1 = DOMTree.documentElement
#观察新闻发现，内容都在Event元素下
ContentNodes = root1.getElementsByTagName("Event")
#定义一个字符串，保存解析出的数据
# content = ""
#遍历所有的Event
# 获取属性对应的值
for i in range(len(ContentNodes)):
    #获取第i个Event下的子节点
    SonNodes = ContentNodes[i].childNodes
    #遍历Event下的所有子节点
    content = ""
    for j in range(len(SonNodes)):
        #print(SonNodes[j].nodeName)
         #获取所有Event下的所有子节点名字 #text是内容 要去掉，
        if(SonNodes[j].nodeName!="#text"):
           content += " "+SonNodes[j].firstChild.data
        #获取所有Event下的值，不包含在Event子节点的值
        if(ContentNodes[i].childNodes[j].nodeValue!=None):
            content+= " "+ContentNodes[i].childNodes[j].nodeValue
            content = content.replace("，", "")
            content = content.replace("。", "")
        if(content.startswith(" ")):
            content = content.lstrip()
    print(content)
