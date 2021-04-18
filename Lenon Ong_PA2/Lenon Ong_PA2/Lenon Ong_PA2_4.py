from os.path import join, expanduser
import pandas as pd
df1 = pd.read_csv(join(expanduser("~"),"df1.csv"), index_col=0)

df1.fever.replace([-1, 0, 1], [2, 1, 0], inplace=True)

df1["fever"] = df1.fever.astype('category') # question specified a recalibration as a categorical variable

print(df1["fever"].value_counts())

df1.to_csv(join(expanduser("~"),"df1.csv"))