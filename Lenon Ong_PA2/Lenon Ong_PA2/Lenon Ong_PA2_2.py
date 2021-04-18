from os.path import join, expanduser
import pandas as pd
df1 = pd.read_csv(join(expanduser("~"),"df1.csv"), index_col=0)

df1.season.replace([-1.00, -0.33, 0.33, 1.00], [1, 2, 3, 4], inplace=True)

df1["season"] = df1.season.astype('category') # question specified a recalibration as a categorical variable

print(df1["season"].value_counts())

df1.to_csv(join(expanduser("~"), "df1.csv"))

