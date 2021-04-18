from os.path import join, expanduser
import pandas as pd
df1 = pd.read_csv(join(expanduser("~"),"df1.csv"), index_col=0)

print(df1.describe())

df1.to_csv(join(expanduser("~"),"df1.csv"))