import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series,DataFrame
# %matplotlib inline
import seaborn as sns

s1=Series(np.random.randn(1000))
plt.hist(s1)
# plt.savefig("jp.jpg")

s1.plot(kind='kde')
# plt.savefig("j.jpg")
tm=sns.distplot(s1)
sns.violinplot(s1)


plt.show()

# plt.savefig('m.jpg')