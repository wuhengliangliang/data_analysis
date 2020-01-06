import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, recall_score, f1_score
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.preprocessing import Normalizer
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import PCA
import os
# import pydotplus
# os.environ["PATH"]+=os.pathsep+"D:/Program/Graphviz/bin/"
#sl:satisfaction_level---False:MinMaxScaler;True:StandardScaler
#le:last_evaluation---False:MinMaxScaler;True:StandardScaler
#npr:number_project---False:MinMaxScaler;True:StandardScaler
#amh:average_monthly_hours--False:MinMaxScaler;True:StandardScaler
#tsc:time_spend_company--False:MinMaxScaler;True:StandardScaler
#wa:Work_accident--False:MinMaxScaler;True:StandardScaler
#pl5:promotion_last_5years--False:MinMaxScaler;True:StandardScaler
#dp:department--False:LabelEncoding;True:OneHotEncoding
#slr:salary--False:LabelEncoding;True:OneHotEncoding
def hr_preprocessing(sl=False,le=False,npr=False,amh=False,tsc=False,wa=False,pl5=False,dp=False,slr=False,lower_d=False,ld_n=1):
    df=pd.read_csv("HR.csv")

    #1、清洗数据
    df=df.dropna(subset=["satisfaction_level","last_evaluation"])
    df=df[df["satisfaction_level"]<=1][df["salary"]!="nme"]
    #2、得到标注
    label = df["left"]
    df = df.drop("left", axis=1)
    #3、特征选择
    #4、特征处理
    scaler_lst=[sl,le,npr,amh,tsc,wa,pl5]
    column_lst=["satisfaction_level","last_evaluation","number_project",\
                "average_monthly_hours","time_spend_company","Work_accident",\
                "promotion_last_5years"]
    for i in range(len(scaler_lst)):
        if not scaler_lst[i]:
            df[column_lst[i]]=\
                MinMaxScaler().fit_transform(df[column_lst[i]].values.reshape(-1,1)).reshape(1,-1)[0]
        else:
            df[column_lst[i]]=\
                StandardScaler().fit_transform(df[column_lst[i]].values.reshape(-1,1)).reshape(1,-1)[0]
    scaler_lst=[slr,dp]
    column_lst=["salary","department"]
    for i in range(len(scaler_lst)):
        if not scaler_lst[i]:
            if column_lst[i]=="salary":
                df[column_lst[i]]=[map_salary(s) for s in df["salary"].values]
            else:
                df[column_lst[i]]=LabelEncoder().fit_transform(df[column_lst[i]])
            df[column_lst[i]]=MinMaxScaler().fit_transform(df[column_lst[i]].values.reshape(-1,1)).reshape(1,-1)[0]

        else:
            df=pd.get_dummies(df,columns=[column_lst[i]])
    if lower_d:
        return PCA(n_components=ld_n).fit_transform(df.values),label
    return df,label
d=dict([("low",0),("medium",1),("high",2)])
def map_salary(s):
    return d.get(s,0)
def hr_modeling_nn(features,label):
    from sklearn.model_selection import train_test_split
    f_v = features.values
    f_names = features.columns.values
    l_v = label.values
    X_tt, X_validation, Y_tt, Y_validation = train_test_split(f_v, l_v, test_size=0.2)
    X_train, X_test, Y_train, Y_test = train_test_split(X_tt, Y_tt, test_size=0.25)

    from keras.models import Sequential
    from keras.layers.core import Dense, Activation
    from keras.optimizers import SGD
    mdl = Sequential()
    mdl.add(Dense(50, input_dim=len(f_v[0])))
    mdl.add(Activation("sigmoid"))
    mdl.add(Dense(2))
    mdl.add(Activation("softmax"))
    sgd = SGD(lr=0.1)
    mdl.compile(loss="mean_squared_error", optimizer="adam")
    mdl.fit(X_train, np.array([[0, 1] if i == 1 else [1, 0] for i in Y_train]), nb_epoch=1000, batch_size=8999)
    xy_lst = [(X_train, Y_train), (X_validation, Y_validation), (X_test, Y_test)]
    import matplotlib.pyplot as plt
    from sklearn.metrics import roc_curve, auc, roc_auc_score
    f = plt.figure()
    for i in range(len(xy_lst)):
        X_part = xy_lst[i][0]
        Y_part = xy_lst[i][1]
        Y_pred = mdl.predict(X_part)
        print(Y_pred)
        Y_pred = np.array(Y_pred[:, 1]).reshape((1, -1))[0]
        print(i)
        print("NN", "-ACC:", accuracy_score(Y_part, Y_pred))
        print("NN", "-REC:", recall_score(Y_part, Y_pred))
        print("NN", "-F1:", f1_score(Y_part, Y_pred))
        f.add_subplot(1, 3, i + 1)
        fpr, tpr, threshold = roc_curve(Y_part, Y_pred)
        plt.plot(fpr, tpr)
        print("NN", "AUC", auc(fpr, tpr))
        print("NN", "AUC_Score", roc_auc_score(Y_part, Y_pred))
    plt.show()
    return
def hr_modeling(features,label):
    from sklearn.model_selection import train_test_split
    f_v=features.values
    f_names=features.columns.values
    l_v=label.values
    X_tt,X_validation,Y_tt,Y_validation=train_test_split(f_v,l_v,test_size=0.2)
    X_train,X_test,Y_train,Y_test=train_test_split(X_tt,Y_tt,test_size=0.25)

    from sklearn.metrics import accuracy_score, recall_score, f1_score
    from sklearn.neighbors import NearestNeighbors,KNeighborsClassifier
    from sklearn.naive_bayes import GaussianNB,BernoulliNB
    from sklearn.tree import DecisionTreeClassifier,export_graphviz
    from sklearn.externals.six import StringIO
    from sklearn.svm import SVC
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.ensemble import AdaBoostClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import GradientBoostingClassifier
    models=[]
    models.append(("KNN",KNeighborsClassifier(n_neighbors=3)))
    models.append(("GaussianNB",GaussianNB()))
    models.append(("BernoulliNB",BernoulliNB()))
    models.append(("DecisionTreeGini",DecisionTreeClassifier()))
    models.append(("DecisionTreeEntropy",DecisionTreeClassifier(criterion="entropy")))
    models.append(("SVM Classifier",SVC(C=1000)))
    models.append(("OriginalRandomForest",RandomForestClassifier()))
    models.append(("RandomForest",RandomForestClassifier(n_estimators=11,max_features=None)))
    models.append(("Adaboost",AdaBoostClassifier(n_estimators=100)))
    models.append(("LogisticRegression",LogisticRegression(C=1000,tol=1e-10,solver="sag",max_iter=10000)))
    models.append(("GBDT",GradientBoostingClassifier(max_depth=6,n_estimators=100)))
    for clf_name,clf in models:
        clf.fit(X_train,Y_train)
        xy_lst=[(X_train,Y_train),(X_validation,Y_validation),(X_test,Y_test)]
        for i in range(len(xy_lst)):
            X_part=xy_lst[i][0]
            Y_part=xy_lst[i][1]
            Y_pred=clf.predict(X_part)
            print(i)
            print(clf_name,"-ACC:",accuracy_score(Y_part,Y_pred))
            print(clf_name,"-REC:",recall_score(Y_part,Y_pred))
            print(clf_name,"-F1:",f1_score(Y_part,Y_pred))
            # dot_data=StringIO()
            # export_graphviz(clf,out_file=dot_data,
            #                          feature_names=f_names,
            #                          class_names=["NL","L"],
            #                          filled=True,
            #                          rounded=True,
            #                          special_characters=True)
            # graph=pydotplus.graph_from_dot_data(dot_data.getvalue())
            # graph.write_pdf("dt_tree_2.pdf")

def regr_test(features,label):
    print("X",features)
    print("Y",label)
    from sklearn.linear_model import LinearRegression,Ridge,Lasso
    #regr=LinearRegression()
    regr=Ridge(alpha=1)
    regr.fit(features.values,label.values)
    Y_pred=regr.predict(features.values)
    print("Coef:",regr.coef_)
    from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
    print("MSE:",mean_squared_error(label.values,Y_pred))
    print("MAE:",mean_absolute_error(label.values,Y_pred))
    print("R2:",r2_score(label.values,Y_pred))
def main():
    features,label=hr_preprocessing()
    regr_test(features[["number_project","average_monthly_hours"]],features["last_evaluation"])
    hr_modeling(features,label)
if __name__=="__main__":
    main()

