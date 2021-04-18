from os.path import join, expanduser
import pandas as pd
df1 = pd.read_csv(join(expanduser("~"),"df1.csv"), index_col=0)

df1["sitting"] = df1["sitting"]*16 # multiplication by 16 to get the actual number of hours

print(df1["sitting"].value_counts())

df1.to_csv(join(expanduser("~"),"df1.csv"))