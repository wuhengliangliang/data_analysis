import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

titanic=pd.read_csv('train.csv')
#绘制一个展示男女乘客比例的扇形图
#sum the instances of males and females
males=(titanic['Sex']=='male').sum()
females=(titanic['Sex']=='female').sum()
#put them into a list called proportions
proportions=[males,females]
#Create a pie chart
plt.pie(
#        using proportions
        proportions,
#        with the labels being officer names
        labels=['Males','Females'],
#        with no shadows
        shadow=False,
#        with colors
        colors=['blue','red'],
        explode=(0.15,0

                 ),
        startangle=90
        )
plt.axis('equal')
plt.title("Sex Proportion")
plt.tight_layout()
plt.show()