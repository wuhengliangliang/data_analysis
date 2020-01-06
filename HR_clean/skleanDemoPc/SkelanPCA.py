import pandas as pd
import numpy as np
#如果取不到，默认取很大的维度
def  myPCA(data,n_components = 100000000):
    # data的均值，axis是每个属性的均值
    mean_vals = np.mean(data,axis=0)
    mid = data - mean_vals
    #求斜方差
    #rowvar = False,如果不指定False那么会对行进行斜方差计算，
    # 而这里我需要对列进行斜方差进行计算
    cov_mat = np.cov(mid,rowvar=False)
    #引入线性计算的包
    from scipy import linalg
    #求斜方差的特征值和特征向量
    eig_vals,eig_vects = linalg.eig(np.mat(cov_mat))
    #取出最大值所对应的特征向量,得到排序后的索引
    eig_val_index = np.argsort(eig_vals)
    #取最大的
    eig_val_index = eig_val_index[:-(n_components+1):-1]
    #取出特征向量
    eig_vects = eig_vects[:,eig_val_index]
    #利用矩阵乘法
    low_dim_mat = np.dot(mid,eig_vects)
    #返回转换后的矩阵转换后的特征值
    return low_dim_mat,eig_vals

data = np.array([np.array([2.5,0.5,2.2,1.9,3.1,2.3,2,1,1.5,1.1]),np.array([2.4,0.7,2.9,2.2,3.0,2.7,1.6,1.1,1.6,0.9])]).T
print(myPCA(data,n_components=1))