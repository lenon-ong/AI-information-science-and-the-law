from os.path import join, expanduser
import pandas as pd
df1 = pd.read_csv(join(expanduser("~"),"df1.csv"), index_col=0)

# An assumption made was that the data was assorted from the lowest to the highest, and that is is a standard
# normal distribution. Another assumption made is that the regression model is linear such that the variable
# is either a constant or a parameter multiplied by an independent variable (e.g. y = B0 + B1X1 +...+ E).



df1.to_csv(join(expanduser("~"),"df1.csv"))