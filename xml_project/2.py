#引入parse的包
from xml.dom.minidom import parse

doc=parse("1.xml")                   #先把xml文件加载进来
root=doc.documentElement                #获取元素的根节点
print(root)
Events=root.getElementsByTagName('Event') #找到子节点，得到的是一个数组
print(Events)
count = 0
for Event in Events:                       #把所有的事件子节点进行遍
    # count = count + 1
    # print("事件：------------------"+str(count))
    if len(Event.getElementsByTagName("Participant")) :
        bookname=Event.getElementsByTagName("Participant")[0]  #根据标签名找到，并且输出第一个元素
        print("参与者：%s"%bookname.childNodes[0].data, end=''+" ")      #输出标签名的子节点的第一个值，并转为data类型
    if  len(Event.getElementsByTagName("Time")):
        bookname=Event.getElementsByTagName("Time")[0]  #根据标签名找到，并且输出第一个元素
        print("时间：%s"%bookname.childNodes[0].data, end=''+" ")      #输出标签名的子节点的第一个值，并转为data类型
    if len(Event.getElementsByTagName("Location")):
        author=Event.getElementsByTagName("Location")[0]
        print("地点：%s"%author.childNodes[0].data, end=''+" ")
    if len(Event.getElementsByTagName("Object")):
        author=Event.getElementsByTagName("Object")[0]
        print("对象：%s"%author.childNodes[0].data, end=''+" ")
    price=Event.getElementsByTagName("Denoter")[0]
    print("动作：%s"%price.childNodes[0].data+" ")