import pickle
import numpy as np
import os
import json
import numpy as np
# import pandas as pd
# list = ['ak47', 'binoculars', 'boom-box', 'calculator', 'cannon', 'computer-keyboard', 'computer-monitor', 'computer-mouse', 'doorknob', 'dumb-bell', 'flashlight', 'head-phones', 'joy-stick', 'palm-pilot', 'video-projector', 'washing-machine']
# new_fo = open('newTest.txt', 'w+',encoding='UTF-8')
# def readfile():
#     with open("Test.txt", 'r', encoding="utf-8")as file:
#         for line in file:
#             for i in range(16):
#                 if(line.__contains__(list[i])):
#                     line = line.rstrip('\n')
#                     line = line + "\t" + str(i)
#             new_fo.write(line+"\n")
#             print(line)
#
# readfile()
# new_fo.close()
list = {}
def unpickle():
    with open("newTest.txt", 'r',encoding="utf-8") as file1:
        for line1 in file1:
            #data/data9657/Images/ak47
            #"head-phones/101_0118.jpg"
            line1 = line1.strip('\n')
            key = line1.split("\t")
            key[0] ="/home/aistudio/data/data9657/Images/"+key[0]
            print(key[0])
            list[key[0]] = key[1]
    return list
unpickle()

json_str = json.dumps(list)
with open('test_data.json', 'w') as json_file:
    json_file.write(json_str)
print(list.keys())
print(list.values())

def test_mapper(sample):
    img, label = sample
    #将img数组进行进行归一化处理，得到0到1之间的数值
    img= img.flatten().astype('float32')/255.0
    return img, label

def train_mapper(sample):
    img, label = sample
    #将img数组进行进行归一化处理，得到0到1之间的数值
    img= img.flatten().astype('float32')/255.0
    return img, label
#
#
def train_r(buffered_size=1024):
    def reader():
        xs = []
        ys = []
        train_dict = unpickle()
        xs.append(train_dict.keys())
        ys.append(train_dict.values())

