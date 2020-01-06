# coding=utf-8
#引入parse的包
from xml.dom.minidom import parse
import os.path

path = "D:\CEC2.3\地震"
files = os.listdir(path)  # 得到文件夹下所有文件名称
s = []
#事件数目
count = 0
#文件数目
flag = 0
for xmlFile in files:  # 遍历文件夹
    if flag==0:
        print("[")
    flag = flag+1
    print("{"+"\"" + "第" + str(flag) + "文件开始" + "\"" + ":"+ "[")
    if not os.path.isdir(xmlFile):  # 判断是否是文件夹,不是文件夹才打开
        # xml文件读取操作
        # 将获取的xml文件名送入到dom解析
        doc = parse(os.path.join(path, xmlFile))  # 先把ml文件加载进来
        root = doc.documentElement  # 获取元素的根节点
        Events = root.getElementsByTagName('Event')  # 找到子节点，得到的是一个数组

        for Event in Events:  # 把所有的事件子节点进行遍
            # node_name = Event.hasAttribute("eid")
            count=count+1
            #打印事件的eid
            print("{"+"\""+"eid"+"\""+":"+"\""+ Event.getAttribute("eid")+"\"", end='' + ",")
            if len(Event.getElementsByTagName("Participant")):
                participant = Event.getElementsByTagName("Participant")[0]  # 根据标签名找到，并且输出第一个元素
                try:
                    print("\""+"参与者"+"\""+":"+"\""+"%s" % participant.childNodes[0].data+"\"", end='' + ",")  # 输出标签名的子节点的第一个值，并转为data类型
                except:
                    print("\""+"参与者+"+"\""+":"+"\""+"null"+"\"", end='' + "," )  # 输出标签名的子节点的第一个值，并转为data类型
            else:
                print("\""+"参与者"+"\""+":"+"\""+"null"+"\"", end='' + ",")
            if len(Event.getElementsByTagName("Time")):
                time = Event.getElementsByTagName("Time")[0]  # 根据标签名找到，并且输出第一个元素
                try:
                    print("\""+"时间"+"\""+":"+"\""+"%s" % time.childNodes[0].data+"\"",end=''+ ",")  # 输出标签名的子节点的第一个值，并转为data类型
                except:
                    print("\""+"时间"+"\""+":"+"\""+"null",end='' + ",")
            else:
                print("\""+"时间"+"\""+":"+"\""+"null"+"\"",end='' + ",")
            if len(Event.getElementsByTagName("Location")):
                location = Event.getElementsByTagName("Location")[0]
                try:
                    print("\""+"地点"+"\""+":"+"\""+"%s" % location.childNodes[0].data+"\"", end='' + ",")
                except:
                    print("\""+"地点"+"\""+":"+"\""+"null"+"\"",end=''+ ",")
            else:
                print("\""+"地点"+"\""+":"+"\""+"null"+"\"", end='' + ",")
            if len(Event.getElementsByTagName("Object")):
                object = Event.getElementsByTagName("Object")[0]
                try:  # 判断是否有data这个属性有这个属性则输出
                    print("\""+"对象"+"\""+":"+"\""+"%s"% object.childNodes[0].data+"\"", end='' + ",")
                except:
                    print("\""+"对象"+"\""+":"+"\""+"null", end='' + ",")
            else:
                print("\""+"对象"+"\""+":"+"\""+" null"+"\"",end='' + ",")
            if len(Event.getElementsByTagName("Denoter")):
                denoter = Event.getElementsByTagName("Denoter")[0]
                try:  # 判断是否有data这个属性有这个属性则输出
                    print("\""+"动作"+"\""+":"+"\""+"%s" % denoter.childNodes[0].data+"\"", end='')
                except:
                    print("\""+"动作"+"\""+":"+"\""+"null"+"\"",end='')
            else:
                print("\""+"动作"+"\""+":"+"\""+"null"+"\"",end='')
            print("}"+",")
        print("]"+",")
    eRelation = root.getElementsByTagName('eRelation')

    print("\"" + "relType" + "\"" + ":" + "[")
    for er in eRelation:
        if (er.hasAttribute("effect_eid")or er.hasAttribute("cause_eid") or er.hasAttribute("aevent_eid") or er.hasAttribute("bevent_eid")):
            print("{")
        # if(er.hasAttribute("thoughtcontent_eids")):
        #     print("thoughtcontent_eids: "+er.getAttribute("thoughtcontent_eids"),end=""+" ")
        # if (er.hasAttribute("thoughtevent_eid")):
        #     print("thoughtevent_eid: "+er.getAttribute("thoughtevent_eid"),end=""+" ")

        # if (er.hasAttribute("relType")):
        #     print(er.getAttribute("relType"),end=""+" ")
        # print("{")
        if (er.hasAttribute("effect_eid")):
            print("\""+"effect_eid"+"\""+":"+"\""+ er.getAttribute("effect_eid")+"\""+",", end="")
        if (er.hasAttribute("cause_eid")):
            print("\""+"cause_eid"+"\""+":"+"\""+ er.getAttribute("cause_eid")+"\"", end="")
        if (er.hasAttribute("aevent_eid")):
            print("\""+"aevent_eid"+"\""+":"+"\""+ er.getAttribute("aevent_eid")+"\""+",",end="")
        if (er.hasAttribute("bevent_eid")):
            print("\""+"bevent_eid"+"\""+":"+"\""+ er.getAttribute("bevent_eid")+"\"", end="")
        if (er.hasAttribute("effect_eid") or er.hasAttribute("cause_eid") or er.hasAttribute( "aevent_eid") or er.hasAttribute("bevent_eid")):
            print("}"+",")

    print("]"+ "}"+",")

print("]")
print("一个文件的事件总数："+str(count))