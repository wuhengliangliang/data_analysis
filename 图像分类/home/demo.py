from PIL import Image
import numpy as np
i = Image.open("C:\\Users\\User\\PycharmProjects\\data_analysis\\图像分类\\home\\aistudio\\data\\data9657\\Images\\ak47\\001_0001.jpg")
I_array = np.array(i)
Xtr = np.concatenate(I_array)
print(Xtr)
