from os.path import join, expanduser
import pandas as pd
import numpy as np
df1 = pd.read_csv(join(expanduser("~"),"df1.csv"), index_col=0)

# assigning variables to the respective percentiles required in the question
fifth_percentile_alcohol = np.percentile(df1["alcohol"], 5)
ninety_five_percentile_alcohol = np.percentile(df1["alcohol"], 95)

# variables used in the columns of a new dataframe
q10 = {'5%': [fifth_percentile_alcohol],
         '95%' : [ninety_five_percentile_alcohol]}

df_q10 = pd.DataFrame(q10, index = ['alcohol'], columns = ['5%', '95%'])

print(df_q10)

df1.to_csv(join(expanduser("~"),"df1.csv"))