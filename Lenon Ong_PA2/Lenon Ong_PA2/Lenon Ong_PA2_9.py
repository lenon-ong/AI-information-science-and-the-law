from os.path import join, expanduser
import pandas as pd
import numpy as np
df1 = pd.read_csv(join(expanduser("~"),"df1.csv"), index_col=0)

# assigning variables to the respective percentiles required in the question
fifth_percentile_age = np.percentile(df1["age"], 5)
ninety_five_percentile_age = np.percentile(df1["age"], 95)
fifth_percentile_sitting = np.percentile(df1["sitting"], 5)
ninety_five_percentile_sitting = np.percentile(df1["sitting"], 95)

# variables used in the columns of a new dataframe
q9 = {'5%': [fifth_percentile_age, fifth_percentile_sitting],
         '95%' : [ninety_five_percentile_age, ninety_five_percentile_sitting]}

df_q9 = pd.DataFrame(q9, index = ['age', 'sitting'], columns = ['5%', '95%'])

print(df_q9)

df1.to_csv(join(expanduser("~"),"df1.csv"))