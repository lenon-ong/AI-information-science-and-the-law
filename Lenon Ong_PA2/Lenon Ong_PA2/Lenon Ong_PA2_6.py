from os.path import join, expanduser
import pandas as pd
df1 = pd.read_csv(join(expanduser("~"),"df1.csv"), index_col=0)

df1.diagnosis.replace(["N", "O"], [0, 1], inplace=True)

df1["diagnosis"] = df1.diagnosis.astype('category') # question specified a recalibration as a categorical variable

print(df1["diagnosis"].value_counts())

df1.to_csv(join(expanduser("~"),"df1.csv"))