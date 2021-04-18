from os.path import join, expanduser
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
df1 = pd.read_csv(join(expanduser("~"),"df1.csv"), index_col=0)

df1 = df1.dropna() # remove any na values in the dataframe

model = smf.ols(formula="diagnosis ~ age + season + disease + accident + surgery + fever + alcohol + smoking + sitting",
               data=df1) # "diagnosis" is the dependent variable according to the question

result = model.fit()

print(result.summary())

df1.to_csv(join(expanduser("~"),"df1.csv"))