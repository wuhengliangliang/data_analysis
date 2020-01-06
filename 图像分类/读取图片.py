import numpy as np
import json

from PIL import Image
import numpy as np
# i = Image.open("001_0001.jpg")
# I_array = np.array(i)
# Xtr = np.concatenate(i)
# print(Xtr)
list = {}
def unpickle1():
    with open("newTest.txt", 'r',encoding="utf-8") as file1:
        for line1 in file1:
            img, lable = line1.split("\t")
            print(img)
            line1 = line1.strip('\n')
            key = line1.split("\t")
            key[0] ="C:\\Users\\User\\PycharmProjects\\data_analysis\\图像分类\\home\\aistudio\\data\\data9657\\Images\\"+key[0]
            list[key[0]] = key[1]
    return list
unpickle1()

# json_str = json.dumps(list)
# with open('train_data.json', 'w') as json_file:
#     json_file.write(json_str)
# print(list.keys())
# print(list.values())
xs = []
ys = []
train_dict = unpickle1()
for i in train_dict.keys():
    # xs.append(i)
    xs.append(Image.open(i))
# xs = np.mat(xs)

# print(Ytr)

# for j in train_dict.values():
#     ys.append(np.array(j))
# Ytr = np.concatenate(ys)
# print(Ytr)

# for (x, y) in zip(Xtr, Ytr):
#     yield x, int(y)





# def train_reader(buffered_size=1024):
#     def reader():
#         X = []
#         Y = []
#         train_dict = unpickle1()
#         for i in test_dict.keys():
#             xs.append(np.array(Image.open(i)))
#         # Xtr = np.concatenate(xs)
#         for j in test_dict.values():
#             ys.append(np.array(j))
#         # Ytr = np.concatenate(ys)
#         # print(Xtr)
#         # print(Ytr)
#         for (x, y) in zip(, ys):
#             yield x, int(y)

# def unpickle(file):
#     import pickle
#     with open(file, 'rb') as fo:
#         dict = pickle.load(fo, encoding='bytes')
#     return dict
# print(unpickle(r"D:\home\aistudio\data\data9657\Images\ak47"))








# def train_reader(train_list):
#
#     def reader():
#
#         with open(train_list, 'r') as f:
#
#             lines = [line.strip() for line in f.readlines()]
#
#             print ("len of train dataset=",len(lines))
#
#             for line in lines:
#
#                 img_path, lab = line.strip().split('\t')
#
#                 yield img_path, int(lab)
#
# train_reader("train_list")
    # return paddle.reader.xmap_readers(self.train_mapper, reader,cpu_count(), buffered_size)
with open("train_list_new", "w+") as fw:
    with open("train_list",'r') as f:
        for line in f.readlines():
            line ="\\home\\aistudio\\data\data9657\\Images\\"+line
            fw.write(line)
