from os.path import join, expanduser
import pandas as pd

# Attempted to improve the model by multiplying the parameters such that they are normalised to have a value
# close to 0 and 1. In addition, parameters with two outputs e.g. (Yes, No) and (Normal, Altered)
# have be re-calibrated as categorical variables. Given the low r-squared values after recalibration,
# and the fact that there are both categorical and quantitative variables, perhaps we could consider using
# other models.
# Instead of a linear regression model, a classification method may be more relevant
# because classifiers such as artificial neural networks can better account for the numerous variables which
# a linear regression model may not be able to effectively make meaningful analysis of.

df1.to_csv(join(expanduser("~"),"df1.csv"))