import pandas as pd
import numpy as np
df = pd.read_csv("../HR.csv")
df_new = df["salary"]
print(df_new.value_counts(normalize=True))
print(df_new.where(df_new!='nme').dropna())