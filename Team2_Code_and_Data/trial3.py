'''
Initial Graph Plots

Created on 09 April 2020

@authors: Lenon Ong, Lee Ming Le
'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from os.path import join, expanduser

FineDF = pd.read_csv("PDPCFD.csv", header=0)

# Preparing the data to plot a graph of the fine against the log of the number of persons affected
print(list(FineDF.columns))
FineDF["fine"] = FineDF["fine"].astype(float)
fineList = FineDF["fine"].tolist()
#print(fineList) #Remove the hashtag for debugging purposes.
fineBandList = []
for fineAmt in fineList:
    if fineAmt == 0:
        fineBandList.append(0)
    elif 1 <= fineAmt < 1000:
        fineBandList.append(1)
    elif 1000 <= fineAmt < 10000:
        fineBandList.append(2)
    elif 10000 <= fineAmt < 100000:
        fineBandList.append(3)
    elif 100000 <= fineAmt < 1000000:
        fineBandList.append('4')
    elif fineAmt == 1000000:
        fineBandList.append('5')
    else:
        print("\nThe data must be in the form of a number. It cannot be blank. Please check your data and try again.\n")
        break

#Verify that the lengths of the lists are the same.
if len(fineList) == len(fineBandList):
    print("\nData looks OK! List lengths are the same. Please wait, joining this column into the dataframe...\n")
else:
    print("Oh no! Looks like the list lengths aren't the same. This can happen if the original data was not in a"
          "numerical format. Please check your data and try again.")
    exit()

#Add the new column
FineDF.insert(2, 'fine_calibrated', fineBandList)
FineDF["fine_calibrated"] = FineDF["fine_calibrated"].astype(float)

FineDF["persons_affected_log"] = np.log10(FineDF["persons_affected"])
FineDF["fine_log"] = np.log10(FineDF["fine"])
FineDF["fine_calibrated_log"] = np.log10(FineDF["fine_calibrated"])
FineDF.year_enforcement = FineDF.year_enforcement.replace({0:'2016',
                                                   1:'2017',
                                                   2:'2018',
                                                   3:'2019',
                                                   4:'2020'})
FineDF.cooperativeness = FineDF.cooperativeness.replace({0:'0',
                                                   1:'1',
                                                   2:'2'})
FineDF.remedial = FineDF.remedial.replace({0:'0',
                                     1:'1'})
t_series_df = FineDF.copy()
t_series_df = t_series_df[t_series_df.fine!=0]

# Each data point will be color-coded according to the calibrated industry (from values 0 to 9)
color = list(FineDF["industry"])

# --------------------------------------------------------------------------------------------------------------

def SMA3(inputList):
    '''
    Code by Ming Le
    We are going to plot a time series graph on a single moving average basis.
    There are 81 rows. We will be proceeding on a SMA set of 3 to determine the moving average
    This function will compute the single moving average(SMA) with a set size of 3. The function was derived from the
    mathematical explanation on https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc421.htm.
    '''
    Offset = 0
    SMAList = []
    SMAList.append(Offset)
    SMAList.append(Offset)
    for i in range(len(inputList)):
        #Begin computing the first entry on SMA
        if i + 2 < len(inputList):
            SMAIter = (inputList[i] + inputList[i + 1] + inputList[i + 2]) / 3
            SMAList.append(SMAIter)
        elif i + 2 > len(inputList):
            print("Reached the end of the list, terminating function...")
    return(SMAList)

FineLogList = t_series_df["fine_log"].tolist()
ComputedSMA = SMA3(FineLogList)
t_series_df.insert(3, 'fine_SMA', ComputedSMA)
print(t_series_df.to_string())

# 0 time series analysis (fine against Index)
x0 = t_series_df["Index"]
y0 = t_series_df["fine_log"]
y1 = t_series_df["fine_SMA"]

# Plotting line plot of the amount of fine against relative time
plt.plot(x0, y0, y1)

# Setting the title and labels of the graph
plt.title('Line plot of the amount of fine against relative time')
plt.xlabel('Relative Time')
plt.ylabel('Log of Fine (SGD)')
plt.show()