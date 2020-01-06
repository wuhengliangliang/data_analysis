from sklearn.preprocessing import Normalizer
import numpy  as np
#正规化实际上是对行进行正规化的

x = Normalizer(norm="l1").fit_transform(np.array([1,1,3,-1,2]).reshape(-1,1))
print(x)
b = Normalizer(norm="l1").fit_transform(np.array([[1,1,3,-1,2]]))
print(b)