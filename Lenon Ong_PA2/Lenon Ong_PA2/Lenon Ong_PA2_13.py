from os.path import join, expanduser
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
df1 = pd.read_csv(join(expanduser("~"),"df1.csv"), index_col=0)

df2 = df1

df2["season"] = df2["season"]/4
df2["sitting"] = df2["sitting"]/16
df2["age"] = df2["age"]/36
df2.fever.replace([2, 1, 0], [-1, 0, 1], inplace=True)


df2["disease"] = df2.disease.astype('category')
df2["accident"] = df2.accident.astype('category')
df2["surgery"] = df2.surgery.astype('category')

model = smf.ols(formula="diagnosis ~ age + season + disease + accident + surgery + fever + alcohol + smoking + sitting",
               data=df2) # "diagnosis" is the dependent variable according to the question

result = model.fit()

print(result.summary())

df1.to_csv(join(expanduser("~"),"df1.csv"))