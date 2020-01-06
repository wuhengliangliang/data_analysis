import pandas as pd
import  numpy as np
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.preprocessing import Normalizer
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import PCA
import pydotplus

#sl:satisfaction_level---False:MinMaxScaler;True:StandardScaler
#le:last_evaluation---False:MinMaxScaler;True:StandardScaler
#npr:number_project---False:MinMaxScaler;True:StandardScaler
#amh:average_monthly_hours--False:MinMaxScaler;True:StandardScaler
#tsc:time_spend_company--False:MinMaxScaler;True:StandardScaler
#wa:Work_accident--False:MinMaxScaler;True:StandardScaler
#pl5:promotion_last_5years--False:MinMaxScaler;True:StandardScaler
#dp:department--False:LabelEncoding;True:OneHotEncoding
#slr:salary--False:LabelEncoding;True:OneHotEncoding

#定义函数读入数据
def hr_preprocessing(sl=False,le=False,npr=False,amh=False,tsc=False,wa=False,pl5=False,dp=False,slr=False,lower_d=False,ld_n=1):
    df = pd.read_csv("./HR.csv")

    # 1、清洗数据
    df = df.dropna(subset=["satisfaction_level", "last_evaluation"])
    df = df[df["satisfaction_level"] <= 1][df["salary"] != "nme"]
    # 2、得到标注
    label = df["left"]
    df = df.drop("left", axis=1)
    # 3、特征选择
    # 4、特征处理
    scaler_lst = [sl, le, npr, amh, tsc, wa, pl5]
    column_lst = ["satisfaction_level", "last_evaluation", "number_project", \
                  "average_monthly_hours", "time_spend_company", "Work_accident", \
                  "promotion_last_5years"]
    for i in range(len(scaler_lst)):
        if not scaler_lst[i]:
            df[column_lst[i]] = \
                MinMaxScaler().fit_transform(df[column_lst[i]].values.reshape(-1, 1)).reshape(1, -1)[0]
        else:
            df[column_lst[i]] = \
                StandardScaler().fit_transform(df[column_lst[i]].values.reshape(-1, 1)).reshape(1, -1)[0]
    scaler_lst = [slr, dp]
    column_lst = ["salary", "department"]
    for i in range(len(scaler_lst)):
        if not scaler_lst[i]:
            if column_lst[i] == "salary":
                df[column_lst[i]] = [map_salary(s) for s in df["salary"].values]
            else:
                df[column_lst[i]] = LabelEncoder().fit_transform(df[column_lst[i]])
            df[column_lst[i]] = MinMaxScaler().fit_transform(df[column_lst[i]].values.reshape(-1, 1)).reshape(1, -1)[0]

        else:
            df = pd.get_dummies(df, columns=[column_lst[i]])
    if lower_d:
        return PCA(n_components=ld_n).fit_transform(df.values), label #PAC降维可以不使用标注
    return df, label


d = dict([("low", 0), ("medium", 1), ("high", 2)])

def hr_modeling(features,labe1):
#切分训练集和测试集
    from sklearn.model_selection import train_test_split
    f_v = features.values
    l_v = labe1.values
#   返回训练集，验证集，标注
    X_tt,X_validation,Y_tt,Y_validation = train_test_split(f_v,l_v,test_size=0.2)
    X_train,X_test,Y_train,Y_test = train_test_split(X_tt,Y_tt,test_size=0.2)
    print(len(X_train),len(X_validation),len(X_test))
#KNN算法实现:NearestNeighbors可以直接获得一点中最近的点
    from sklearn.neighbors import NearestNeighbors,KNeighborsClassifier
    knnclf = KNeighborsClassifier(n_neighbors=3)
    knnclf.fit(X_train,Y_train)
    Y_pred = knnclf.predict(X_validation)
    from sklearn.metrics import accuracy_score,recall_score,f1_score
    print("ACC:",accuracy_score(Y_validation,Y_pred))
    print("REC:",recall_score(Y_validation,Y_pred))
    print("F-Score:",f1_score(Y_validation,Y_pred))
# #存储训练模型
#     from sklearn.externals import joblib
#     joblib.dump(knnclf,"knnclf")
# #加载训练模型
#     joblib.load('knnclf')
def map_salary(s):
    return d.get(s,0)
def main():
    features,label = hr_preprocessing()
    # print(hr_preprocessing())
    hr_modeling(features,label)
if __name__ == '__main__':
    main()
