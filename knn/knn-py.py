import numpy as np
from math import sqrt
from collections import Counter

# k 指的 参数大小 ，训练集，x:预测的特征向量
def KNN_classify(k,X_train,Y_train,x):
    #必须保证k的合法性，k<训练集中样本的数量
    assert 1<=k <=X_train.shape[0],"K must be valid"
    #其次保证x_tarin的样本数量和y中的label数量相等
    assert X_train.shape[0]==Y_train.shape[0],\
    "the size of X_train must equal to the size of y_train"
    #x的特征数量和训练集中的样本数量相等
    assert X_train.shape[1]==x.shape[0],\
    "the feature number of x must be equal to X_traib"
    #对预测的值，进行四周的距离的计算
    distances = [sqrt(np.sum((x_train-x)**2)) for x_train in X_train]
    #对距离进行排序
    nearest = np.argsort(distances)
    topK_y = [Y_train[i] for i in nearest[:k]]
    votes = Counter(topK_y)
    return votes.most_common(1)[0][0]
