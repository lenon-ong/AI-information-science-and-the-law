from os.path import join, expanduser
import pandas as pd
df1 = pd.read_csv(join(expanduser("~"),"df1.csv"), index_col=0)

bin_list = []
for i in range(20):
    input = i/19
    bin_list.append(input) # to append a list of 19 intervals between 0 and 1.

age_list = []
for j in range(100):
    if j > 17 and j < 37:
        age_list.append(j) # a list of numbers from 18 to 36.

df1["age"] = pd.cut(df1["age"], bins=bin_list, labels=age_list)

# labelling the bins from 18 to 36 and allocating the respective values between 0 and 1 into the bins

print(df1["age"].value_counts())

df1.to_csv(join(expanduser("~"),"df1.csv"))