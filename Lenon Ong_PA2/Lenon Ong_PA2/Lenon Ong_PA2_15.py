from os.path import join, expanduser
import pandas as pd

# A low p-value indicates that the parameter is a meaningful one as changes in the parameter's value is related to
# changes in the dependent variable. In this particular dataset, the p-values are constantly high. (A low p-value
# is considered to be < 0.05). This suggests that a linear regression model may not be the best model for this analysis.
# Regardless, the correlation between sperm damage and accident, age, season, alcohol, fever, and sitting appear
# to be more significant than the correlation between sperm damage and disease, surgery, and smoking (these 3 parameters
# have p-values that are much higher relative to the rest (and they are higher than 0.5).
# In addition, the only meaningful analysis one could make in this model is that the history of accident
# or serious trauma is the most relevant factor in trying to predict the possibility of sperm damage.

df1.to_csv(join(expanduser("~"),"df1.csv"))