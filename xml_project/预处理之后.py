# coding=utf-8
#引入parse的包
from xml.dom.minidom import parse
import os.path

path = "D:\CEC2.3\地震"
files = os.listdir(path)  # 得到文件夹下所有文件名称
s = []
count = 0
for xmlFile in files:  # 遍历文件夹
    if not os.path.isdir(xmlFile):  # 判断是否是文件夹,不是文件夹才打开
        # xml文件读取操作
        # 将获取的xml文件名送入到dom解析
        doc = parse(os.path.join(path, xmlFile))  # 先把ml文件加载进来
        root = doc.documentElement  # 获取元素的根节点
        Events = root.getElementsByTagName('Event')  # 找到子节点，得到的是一个数组
        for Event in Events:  # 把所有的事件子节点进行遍
            count=count+1
            if len(Event.getElementsByTagName("Participant")):
                participant = Event.getElementsByTagName("Participant")[0]  # 根据标签名找到，并且输出第一个元素
                try:
                    print("%s" % participant.childNodes[0].data, end='' + " ")  # 输出标签名的子节点的第一个值，并转为data类型
                except:
                    print("null", end='' + " " )  # 输出标签名的子节点的第一个值，并转为data类型
            else:
                print("null", end='' + " ")
            if len(Event.getElementsByTagName("Time")):
                time = Event.getElementsByTagName("Time")[0]  # 根据标签名找到，并且输出第一个元素
                try:
                    print("%s" % time.childNodes[0].data, end='' + " ")  # 输出标签名的子节点的第一个值，并转为data类型
                except:
                    print("null",end='' + " ")
            else:
                print("null", end='' + " ")
            if len(Event.getElementsByTagName("Location")):
                location = Event.getElementsByTagName("Location")[0]
                try:
                    print("%s" % location.childNodes[0].data, end='' + " ")
                except:
                    print("null", end='' + " ")
            else:
                print("null", end='' + " ")
            if len(Event.getElementsByTagName("Object")):
                object = Event.getElementsByTagName("Object")[0]
                try:  # 判断是否有data这个属性有这个属性则输出
                    print("%s" % object.childNodes[0].data, end='' + " ")
                except:
                    print("null", end='' + " ")
            else:
                print("null",end='' + " ")
            if len(Event.getElementsByTagName("Denoter")):
                denoter = Event.getElementsByTagName("Denoter")[0]
                try:  # 判断是否有data这个属性有这个属性则输出
                    print("%s" % denoter.childNodes[0].data, end='' + " ")
                except:
                    print(" null",end='' + " ")
            else:
                print("null",end='' + " ")
            print("")
print("一个文件的事件总数："+str(count))