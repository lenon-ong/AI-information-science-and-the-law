from os.path import join, expanduser
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv(join(expanduser("~"),"df1.csv"), index_col=0)
print(df1)

plt.hist(df1["age"], bins=[15, 20, 25, 30, 35, 40]) # plotting histogram with bins of intervals of 5 from 15 to 40
plt.title('Distribution of the dataset by age of the donors') # setting the title of the graph
plt.xlabel('Age') # setting the x-axis label for the graph
plt.ylabel('Quantity') # setting the y-axis label for the graph
plt.show() # plot and show the graph


df1.to_csv(join(expanduser("~"),"df1.csv"))