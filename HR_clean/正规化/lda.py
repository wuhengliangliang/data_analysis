import  numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
X = np.array([[-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])
Y = np.array([1,1,1,2,2,2])
m_lda = LinearDiscriminantAnalysis(n_components=1).fit_transform(X,Y)
print(m_lda)