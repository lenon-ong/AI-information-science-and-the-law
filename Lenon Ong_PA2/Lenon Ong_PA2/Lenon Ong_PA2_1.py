from os.path import join, expanduser

import pandas as pd

df1 = pd.read_csv("fertility_Diagnosis.txt",
                 sep=",", header=None, names=["season", "age", "disease", "accident",
                                              "surgery", "fever", "alcohol", "smoking",
                                              "sitting", "diagnosis"])
# Data in fertility_Diagnosis.txt is separated by commas.

print(df1)

df1.to_csv(join(expanduser("~"),"df1.csv"))