import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
pd.set_option('display.max_columns', 25)
wadf = pd.read_csv("Team2_data_PDPCDecisions.csv")
wadf.industry = wadf.industry.replace({0:'Wholesale and Retail Trade',
                                   1:'Transportation and Storage',
                                   2:'Information and Communications',
                                   3:'Financial and Insurance Activities',
                                   4:'Real Estate Activities',
                                   5:'Professional, Scientific and Technical Activities',
                                   6:'Administrative and Support Service Activities',
                                   7:'Education',
                                   8:'Health and Social Services',
                                   9:'Arts, Entertainment and Recreation'})
print(wadf["industry"].value_counts())

linearmodel1 = smf.ols('fine ~ persons_affected', data = wadf).fit()
print(linearmodel1.summary())

MLlinmodel31 = smf.ols('fine ~ persons_affected + type_pd + '
                       'extent + fault + knowledge + C(appointment) + admission + C(voluntary) + '
                       'meaningful_engagement + C(cooperativeness) + aggravating + mitigation',
                       data = wadf).fit()
print(MLlinmodel31.summary())


#######################################################################################################################
#                                                                                                                     #
#                                                   Global Variables                                                  #
#                                                                                                                     #
#######################################################################################################################
NameML = "Ming Le's"
NameLO = "Lenon's"
NameYF = "Yi Fei's"
NameSL = "Stephenie's"
GraphWord = "Graph\n"
GraphMsg = "\nPlease see graphical output in the newly opened matplotlib windows.\n"
ModelWord = "Model\n"
LinModelPhrase = "\nLinear Regression Model"
LogitModelPhrase = "\nLogistic Regression Model"
failedModelMsg = "\nUnsuccessful Models\n"

#######################################################################################################################
#                                                                                                                     #
#                                                      Functions                                                      #
#                                                                                                                     #
#######################################################################################################################
#######################################################################################################################
#                              Functions for Statistical Measures in Logistic Regression                              #
#######################################################################################################################
# predictedOutput and actualOutput are lists
def StatisticalMeasures(predictedOutput, actualOutput):
    #Set all variables to 0 first.
    truePositives = 0
    trueNegatives = 0
    falsePositives = 0
    falseNegatives = 0
    for i in range(len((actualOutput))):
        if predictedOutput[i] >= 0.5:
            if actualOutput[i] == 1:
                truePositives += 1
            elif actualOutput[i] == 0:
                falsePositives += 1

        elif predictedOutput[i] < 0.5:
            if actualOutput[i] == 0:
                trueNegatives += 1
            elif actualOutput[i] == 1:
                falseNegatives += 1

        else:
            print("Your predicted output data is not in a numerical format. Please check your data.")

    return [truePositives, trueNegatives, falsePositives, falseNegatives]

def Accuracy(predictedOutput, actualOutput):
    StatMeasureVals = StatisticalMeasures(predictedOutput, actualOutput)
    accuracyValue = (StatMeasureVals[0] + StatMeasureVals[1])/sum(StatMeasureVals)
    return accuracyValue

def Precision(predictedOutput, actualOutput):
    StatMeasureVals = StatisticalMeasures(predictedOutput, actualOutput)
    precisionValue = StatMeasureVals[0]/(StatMeasureVals[0] + StatMeasureVals[2])
    return precisionValue

def Recall(predictedOutput, actualOutput):
    StatMeasureVals = StatisticalMeasures(predictedOutput, actualOutput)
    recallValue = StatMeasureVals[0]/(StatMeasureVals[0] + StatMeasureVals[3])
    return recallValue

#######################################################################################################################
#                                                Manual Data Recalibrators                                            #
#######################################################################################################################
#ogFine refers to df["fine"] column in the data set.
#This should have been exported to a list using the following command:
#TempListVar = df["fine"].tolist(), replace TempListVar with any variable name of your choice.
#TempListVar is to replace ogFine:

def fineBandRC(ogFineList):
    fineBandList = []
    for fineAmt in ogFineList:
        if fineAmt == 0:
            fineBandList.append(0)
        elif 1 <= fineAmt < 1000:
            fineBandList.append(1)
        elif 1000 <= fineAmt < 10000:
            fineBandList.append(2)
        elif 10000 <= fineAmt < 100000:
            fineBandList.append(3)
        elif 100000 <= fineAmt < 1000000:
            fineBandList.append(4)
        elif fineAmt == 1000000:
            fineBandList.append(5)
        else:
            print(
                "\nThe data must be in the form of a number. It cannot be blank. Please check your data and try "
                "again.\n")
            break

    # Verify that the lengths of the lists are the same.
    if len(ogFineList) == len(fineBandList):
        print("\nData looks OK! List lengths are the same."
              ""
              "Please wait, this function will exit to start joining this column into the dataframe...\n")
    else:
        print("Oh no! Looks like the list lengths aren't the same. This can happen if the original data was not in a"
              "numerical format. Please check your data and try again.")
        exit()

    return(fineBandList)

#######################################################################################################################
#                                                                                                                     #
#                                                       Models                                                        #
#                                                                                                                     #
#######################################################################################################################
#######################################################################################################################
#------------------------------------------------------Ming Le--------------------------------------------------------#
#######################################################################################################################
print(NameML, ModelWord)
ModelMLDF = pd.read_csv("Team2_data_PDPCDecisions.csv")

#######################################################################################################################
#                                           Independent Variable Calibration                                          #
#######################################################################################################################
ModelMLDF["fine_y_n"] = ModelMLDF["fine"].mask(ModelMLDF["fine"] > 0, 1)
ModelMLDF["persons_affected_lg"] = ModelMLDF["persons_affected"].apply(np.log10)
actualList = ModelMLDF["fine_y_n"]
#######################################################################################################################
#                                                        Models                                                       #
#######################################################################################################################
print('\n The models in this section are listed here as they produced the best results for each stage.')

print(LinModelPhrase, '9\n'
                      'For Slide 22: This linearmodel aims to determine the strength of the model and the colinearity\n'
                      'between fine and independent variables that only pertain to the company identity and ownership.'
                      '\n')
MLlinmodel9 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + industry + type + ownership',
                      data = ModelMLDF).fit()
print(MLlinmodel9.summary())

print(LinModelPhrase, '17\n'
                       'For Slide 23: This linearmodel aims to determine the strength of the model and the colinearity\n'
                      'between fine and independent variables that pertain to aggravating factors only.\n')
MLlinmodel17 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + C(industry) + type + C(ownership) + '
                                 'fault + C(appointment) + aggravating', data = ModelMLDF).fit()
print(MLlinmodel17.summary())

print(LinModelPhrase, '24\n'
                       'For Slide 24: This linearmodel aims to determine the strength of the model and the colinearity\n'
                      'between fine and independent variables that pertain to the mitigating factors only.\n')
MLlinmodel24 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + C(industry) + type + C(ownership) + '
                                 'C(appointment) + admission + C(voluntary) + C(cooperativeness) + mitigation',
                       data = ModelMLDF).fit()
print(MLlinmodel24.summary())

print(LinModelPhrase, '27\n'
                      'For Slide 27: This linearmodel aims to determine the strength of the model and the colinearity\n'
                      'between fine and independent variables that pertain to both the aggravating and mitigating\n'
                      'factors.\n')
MLlinmodel27 = smf.ols(formula = 'fine ~ C(year_enforcement) + type_pd + persons_affected + C(industry) + type + '
                                 'C(ownership) + fault + aggravating + C(appointment) + admission + C(voluntary) + '
                                 'cooperativeness + mitigation', data = ModelMLDF).fit()
print(MLlinmodel27.summary())

#################
#Models not used#
#################

print(failedModelMsg, '\n'
                      'These models were not listed in the slide. Rather, they were part of the trial and error\n'
                      'process to arrive at the best R-squared or adjusted R-squared, or to get the lowest possible\n'
                      'p-value on as many independent variables as possible.\n\n'
                      '#These set of models concern only the identity of the organisation only.\n')
#######################################################################################################################
#Identity of the organisation only.
#######################################################################################################################
print(LinModelPhrase, '1\n')
MLlinmodel1 = smf.ols(formula = 'fine ~ type_pd', data = ModelMLDF).fit()
print(MLlinmodel1.summary())

print(LinModelPhrase, '2\n')
MLlinmodel2 = smf.ols(formula = 'fine ~ C(year_incident) + C(year_enforcement)', data = ModelMLDF).fit()
print(MLlinmodel2.summary())

print(LinModelPhrase, '3\n')
MLlinmodel3 = smf.ols(formula = 'fine ~ C(year_incident) + C(year_enforcement) + persons_affected',
                      data = ModelMLDF).fit()
print(MLlinmodel3.summary())

print(LinModelPhrase, '4\n')
MLlinmodel4 = smf.ols(formula = 'fine ~ C(year_incident) + C(year_enforcement) + persons_affected + industry',
                      data = ModelMLDF).fit()
print(MLlinmodel4.summary())

print(LinModelPhrase, '5\n')
MLlinmodel5 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + industry', data = ModelMLDF).fit()
print(MLlinmodel5.summary())

print(LinModelPhrase, '6\n')
MLlinmodel6 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + type_pd + industry',
                      data = ModelMLDF).fit()
print(MLlinmodel6.summary())

print(LinModelPhrase, '7\n')
MLlinmodel7 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + industry + type',
                      data = ModelMLDF).fit()
print(MLlinmodel7.summary())

print(LinModelPhrase, '8\n')
MLlinmodel8 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + type_pd + industry + type',
                      data = ModelMLDF).fit()
print(MLlinmodel8.summary())

#######################################################################################################################
#Models from this point consider aggravating factors only
#######################################################################################################################
print('\n#These set of models concern tested the colinearity between fine and aggravating factors only.\n')
print(LinModelPhrase, '10\n')
MLlinmodel10 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + industry + type + ownership + extent'
                                 '', data = ModelMLDF).fit()
print(MLlinmodel10.summary())

print(LinModelPhrase, '11\n')
MLlinmodel11 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + industry + type + ownership + fault'
                                 '', data = ModelMLDF).fit()
print(MLlinmodel11.summary())

print(LinModelPhrase, '12\n')
MLlinmodel12 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + industry + type + ownership + fault +'
                                 'knowledge', data = ModelMLDF).fit()
print(MLlinmodel12.summary())

print(LinModelPhrase, '13\n')
MLlinmodel13 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + industry + type + ownership + fault +'
                                 'appointment', data = ModelMLDF).fit()
print(MLlinmodel13.summary())

print(LinModelPhrase, '14\n')
MLlinmodel14 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + C(industry) + type + ownership + '
                                 'fault + appointment', data = ModelMLDF).fit()
print(MLlinmodel14.summary())

print(LinModelPhrase, '15\n')
MLlinmodel15 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + C(industry) + type + C(ownership) + '
                                 'fault + appointment', data = ModelMLDF).fit()
print(MLlinmodel15.summary())

print(LinModelPhrase, '16\n')
MLlinmodel16 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + C(industry) + type + C(ownership) + '
                                 'fault + C(appointment)', data = ModelMLDF).fit()
print(MLlinmodel16.summary())

print(LinModelPhrase, '17\n')
MLlinmodel18 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + C(industry) + type + C(ownership) + '
                                 'fault + C(appointment) + aggravating + C(enforcement_action)', data = ModelMLDF).fit()
print(MLlinmodel18.summary())

#######################################################################################################################
#Models from this point on are focused on mitigating factors.
#######################################################################################################################
print('\n#These set of models concern tested the colinearity between fine and mitigating factors only.\n')
print(LinModelPhrase, '19\n')
MLlinmodel19 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + C(industry) + type + C(ownership) + '
                                 'C(appointment) + admission', data = ModelMLDF).fit()
print(MLlinmodel19.summary())

print(LinModelPhrase, '20\n')
MLlinmodel20 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + C(industry) + type + C(ownership) + '
                                 'C(appointment) + admission + C(voluntary)', data = ModelMLDF).fit()
print(MLlinmodel20.summary())

print(LinModelPhrase, '21\n')
MLlinmodel21 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + C(industry) + type + C(ownership) + '
                                 'C(appointment) + admission + C(voluntary) + remedial', data = ModelMLDF).fit()
print(MLlinmodel21.summary())

print(LinModelPhrase, '22\n')
MLlinmodel22 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + C(industry) + type + C(ownership) + '
                                 'C(appointment) + admission + C(voluntary) + meaningful_engagement',
                       data = ModelMLDF).fit()
print(MLlinmodel22.summary())

print(LinModelPhrase, '23\n')
MLlinmodel23 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + C(industry) + type + C(ownership) + '
                                 'C(appointment) + admission + C(voluntary) + cooperativeness', data = ModelMLDF).fit()
print(MLlinmodel23.summary())

print(LinModelPhrase, '25\n')
MLlinmodel25 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + C(industry) + type + C(ownership) + '
                                 'C(appointment) + admission + C(voluntary) + cooperativeness + mitigation + '
                                 'enforcement_action', data = ModelMLDF).fit()
print(MLlinmodel25.summary())

#######################################################################################################################
#Models from this point merge both the aggravating and mitigating factors less unhelpful categories.
#######################################################################################################################
print('\n#These set of models concern tested the colinearity between fine and the aggravating with theitigating factors\n'
      'combined.\n')

print(LinModelPhrase, '26\n')
MLlinmodel26 = smf.ols(formula = 'fine ~ C(year_enforcement) + persons_affected + C(industry) + type + C(ownership) + '
                                 'fault + aggravating + C(appointment) + admission + C(voluntary) + cooperativeness + '
                                 'mitigation', data = ModelMLDF).fit()
print(MLlinmodel26.summary())

print(LinModelPhrase, '27\n')
MLlinmodel28 = smf.ols(formula = 'fine ~ C(year_enforcement) + type_pd + persons_affected + C(industry) + type + fault '
                                 '+ aggravating + C(appointment) + admission + C(voluntary) + cooperativeness + '
                                 'mitigation', data = ModelMLDF).fit()

print(MLlinmodel28.summary())

#######################################################################################################################
#Subsequent model tests based on models generated by others
#######################################################################################################################
print('\n#These set of models were tested post the sharing of models by other team members and further results were\n'
      'run, but no useful information could be yielded from it.\n'
      'This section includes both linear and logistic regression models.')

print(LinModelPhrase, '29\n')
MLlinmodel29 = smf.ols(formula='fine ~ fault + extent + persons_affected + C(appointment) + type_pd + knowledge',
                       data=ModelMLDF).fit()
print(MLlinmodel29.summary())

print(LinModelPhrase, '30\n')
MLlinmodel30 = smf.ols(formula='fine ~ fault + extent + persons_affected_lg + C(appointment) + type_pd + knowledge',
                       data=ModelMLDF).fit()
print(MLlinmodel30.summary())

print(LinModelPhrase, '31\n')
MLlinmodel31 = smf.ols('fine ~ C(year_enforcement) + persons_affected + type_pd + C(industry) + type +'
                       'C(ownership) + extent + fault + knowledge + C(appointment) + admission + C(voluntary) + '
                       'remedial + meaningful_engagement + C(cooperativeness) + aggravating + mitigation',
                       data = ModelMLDF).fit()
print(MLlinmodel31.summary())

#Logistic Regression Models
print(LogitModelPhrase + 's', '\n')
print(LogitModelPhrase, '1\n')
MLlogitmodel1 =  smf.logit('fine_y_n ~ C(year_enforcement) + persons_affected + type_pd + C(industry) + type +'
                        'C(ownership) + extent + fault + knowledge + C(appointment) + admission + C(voluntary) + '
                        'remedial + meaningful_engagement + C(cooperativeness) + aggravating + mitigation',
                         data = ModelMLDF).fit()
print(MLlogitmodel1.summary())
predictedList = MLlogitmodel1.predict()
print(StatisticalMeasures(predictedList, actualList))
logitAccuracy = Accuracy(predictedList, actualList)
logitPrecision = Precision(predictedList, actualList)
logitRecall = Recall(predictedList, actualList)

print("\naccuracy:", logitAccuracy)
print("precision:", logitPrecision)
print("recall:", logitRecall)

print(LogitModelPhrase, '2\n')
mllogitmodel2 = smf.logit('fine_y_n ~ C(year_enforcement) + persons_affected_lg + type_pd + C(industry) + type +'
                       'C(ownership) + extent + fault + knowledge + C(appointment) + admission + C(voluntary) + remedial'
                       '+ meaningful_engagement + C(cooperativeness) + aggravating + mitigation',
                          data = ModelMLDF).fit()
print(mllogitmodel2.summary())
predictedList = mllogitmodel2.predict()
print(StatisticalMeasures(predictedList, actualList))
logitAccuracy = Accuracy(predictedList, actualList)
logitPrecision = Precision(predictedList, actualList)
logitRecall = Recall(predictedList, actualList)

print("\naccuracy:", logitAccuracy)
print("precision:", logitPrecision)
print("recall:", logitRecall, 'n')
#######################################################################################################################
#--------------------------------------------------------Lenon--------------------------------------------------------#
#######################################################################################################################
print(NameLO, ModelWord)
ModelLODF = pd.read_csv("Team2_data_PDPCDecisions.csv")
# ---------------------------------------------------------------------------------------------------------------
#######################################################################################################################
#                                                                                                                     #
#                                           Independent Variable Calibration                                          #
#                                                                                                                     #
#######################################################################################################################
for i in ["cooperativeness", "voluntary", "year_incident",
          "appointment", "year_enforcement", "industry",
          "section", "ownership", "enforcement_action"]:
    ModelLODF[i] = ModelLODF[i].astype('category')
ModelLODF["fine_y_n"] = ModelLODF["fine"].mask(ModelLODF["fine"] > 0, 1)
fineList = ModelLODF["fine"].tolist()
fineBandList = fineBandRC(fineList)
ModelLODF.insert(2, 'fine_calibrated', fineBandList)
# ---------------------------------------------------------------------------------------------------------------
# For the graphs between slides 12 to 17 and 72 to 80 , refer to Graphs - Lenon, Yi Fei, Ming Le
# ---------------------------------------------------------------------------------------------------------------

#######################################################################################################################
#                                                                                                                     #
#                                                        Models                                                       #
#                                                                                                                     #
#######################################################################################################################
# Slide 27 - 28: Lenon's Approach #1 (OLS)
print(LinModelPhrase, '1\n'
                      "Slide 27 - 28: Lenon's Approach #1 (OLS)"
                      'Initial Approach: perform an smf.ols model with all relevant independent variables from the \n'
                      'PDPC’s Guide to Active Enforcement, and other variables which the group thought would be\n '
                      'relevant, but not in the PDPC’s enforcement guidelines.\n')

model1 = smf.ols(formula="fine ~ enforcement_action + ownership + industry + aggravating + mitigation + cooperativeness"
                         "+ remedial + voluntary + meaningful_engagement + admission + persons_affected + fault + "
                         "extent + appointment + type_pd", data=ModelLODF).fit()
print(model1.summary(), '\n')

print('fine = the actual amount of fine meted out by the PDPC in SGD\n'
      'R-squared = 0.450, Adj. R-squared = 0.284\n'
      'Note that the p-value for persons_affected = 0.000, and that the p-values for industry are very high.\n')

# -----
print(LinModelPhrase, '1_1`\n'
                      'Removed “ownership” and “industry” independent variables, which are not based on PDPC’s Guide \n'
                      'to Active Enforcement.\n')

model1_1 = smf.ols(formula="fine ~ enforcement_action + aggravating + mitigation + cooperativeness + remedial + "
                           "voluntary + meaningful_engagement + admission + persons_affected + fault + extent + "
                           "appointment + type_pd", data=ModelLODF).fit()
print(model1_1.summary(), '\n')

print('fine = the actual amount of fine meted out by the PDPC in SGD\n'
      'R-squared dropped to 0.438 from 0.450,\n'
      'Adj. R-squared increased to 0.344 from 0.284\n'
      'Note that the p-value for persons_affected = 0.000\n\n'
      'Evaluation: Although the fine was actually quite statistically significant (with a low-p value) with a strong\n'
      'positive correlation, the model itself was not the best model that could be achieved with an adjusted r-\n'
      'squared value of 0.344. We then looked to see if we could find a better model that could explain the\n'
      'correlation between the independent variables and the fine amount.\n')

# ---------------------------------------------------------------------------------------------------------------
#Slide 30 - 32: Lenon's Approach #2 (OLS)
print(LinModelPhrase, '2\n'
                      "Slide 30 - 32: Lenon's Approach #2 (OLS)\n")
model2 = smf.ols(formula="fine_y_n ~ enforcement_action + ownership + industry + aggravating + mitigation + "
                         "cooperativeness + remedial + voluntary + meaningful_engagement + admission + persons_affected"
                         "+ fault + extent + appointment + type_pd", data=ModelLODF).fit()
print(model2.summary(), '\n')

print('fine_y_n = the amount of fine meted out by the PDPC in SGD recalibrated as:\n'
      '0 when the actual amount of fine = $0\n'
      '1 when the actual amount of fine > $0\n\n'
      'R-squared = 1.000, Adj. R-squared = 1.000')

# -----
print(LinModelPhrase, '2_1\n'
                      "Removed “enforcement_action” due to red herring.\n")
model2_1 = smf.ols(formula="fine_y_n ~ ownership + industry + aggravating + mitigation + cooperativeness + remedial + "
                           "voluntary + meaningful_engagement + admission + persons_affected + fault + extent + "
                           "appointment + type_pd", data=ModelLODF).fit()
print(model2_1.summary(), '\n')
print('R-squared = 0.341, Adj. R-squared = 0.168\n'
      'Note that the p-value for persons_affected increased from 0.000 to 0.398, and that the p-values for industry\n'
      'are high.\n')

# -----
print(LinModelPhrase, '2_2\n'
                      'Removed “ownership” and “industry” independent variables, which are not based on PDPC’s Guide\n'
                      'to Active Enforcement.\n')
model2_2 = smf.ols(formula="fine_y_n ~ aggravating + mitigation + cooperativeness + remedial + voluntary + "
                           "meaningful_engagement + admission + persons_affected + fault + extent + "
                           "appointment + type_pd", data=ModelLODF).fit()
print(model2_2.summary(), '\n')
print('R-squared dropped to 0.315 from 0.341,\n'
      'Adj. R-squared increased to 0.222 from 0.168\n'
      'Note that the p-value for persons_affected increased from 0.398 to 0.367.\n\n'
      'Evaluation: With a relatively lower r-squared and adjusted r-squared, this is not a good model because:\n'
      'it is only good at tell us that there was a correlation between the independent variables and whether there\n'
      'was a fine or not, NOT on the quantum of the fine.\n\n'
      'In addition, the persons_affected variable also became statistically insignificant, as the p-value jumped to\n'
      'above 0.3. Hence, this model would not be able to make out a good correlation between the independent \n'
      'variables and the imposition of a fine.\n\n'
      'Approach #3 was thus conceived, to band the fines into certain categories.\n')

# ---------------------------------------------------------------------------------------------------------------
#Slide 34 - 37: Lenon's Approach #3 (OLS)
print(LinModelPhrase, '3\n'
                      "Slide 34 - 37: Lenon's Approach #3 (OLS)\n")
model3 = smf.ols(formula="fine_calibrated ~ enforcement_action + ownership + industry + aggravating + mitigation + "
                         "cooperativeness + remedial + voluntary + meaningful_engagement + admission + "
                         "persons_affected + fault + extent + appointment + type_pd", data=ModelLODF).fit()
print(model3.summary(), '\n')
print('fine_calibrated = the amount of fine meted out by the PDPC in SGD recalibrated as:\n'
      '0 when the actual amount of fine = $0\n'
      '1 when the $0 < actual amount of fine < $999\n'
      '2 when the $1,000 < actual amount of fine < $9,999\n'
      '3 when the $10,000 < actual amount of fine < $99,999\n'
      '4 when the $100,000 < actual amount of fine < $999,999\n'
      '5 when the actual amount of fine = $1,000,000\n\n'
      'R-squared = 0.919, Adj. R-squared = 0.895\n\n'
      'Note that the p-value for persons_affected is 0.001.\n')
# -----
print(LinModelPhrase, '3_1\n'
                      'Removed “enforcement_action”.\n')
model3_1 = smf.ols(formula="fine_calibrated ~ ownership + industry + aggravating + mitigation + cooperativeness + knowledge +  "
                           "remedial + voluntary + meaningful_engagement + admission + persons_affected + fault + "
                           "extent + appointment + type_pd", data=ModelLODF).fit()
print(model3_1.summary(), '\n')
print('R-squared dropped to 0.408 from 0.919,\n'
      'Adj. R-squared dropped to 0.253 from 0.895\n\n'
      'Note that the p-value for persons_affected is 0.038, and that the p-values for industry are very high.\n')

# -----
print(LinModelPhrase, '3_2\n'
                      'Removed “ownership” and “industry” independent variables, which are not based on PDPC’s Guide\n'
                      'to Active Enforcement.\n')
model3_2 = smf.ols(formula="fine_calibrated ~ aggravating + mitigation + cooperativeness + remedial + voluntary + "
                           "meaningful_engagement + admission + persons_affected + fault + extent + appointment + "
                           "type_pd", data=ModelLODF).fit()
print(model3_2.summary(), '\n')
print('R-squared dropped to 0.382 from 0.408,\n'
      'Adj. R-squared rose to 0.297 from 0.253\n\n'
      'Note that the p-value for persons_affected is lower at 0.031.\n')
# ---------------------------------------------------------------------------------------------------------------
# Slide 38: Lenon's Approach (Logit)
print(LogitModelPhrase, '1\n'
                      "Slide 38: Lenon's Approach (Logit)\n")
model4 = smf.logit(formula="fine_y_n ~ ownership + industry + aggravating + mitigation + cooperativeness + remedial + "
                            "voluntary + meaningful_engagement + admission + persons_affected + fault + extent + "
                            "appointment + type_pd", data=ModelLODF).fit()

# Creating dataframe for prediction model
Lenon_Logmodel_DF = ModelLODF[["ownership", "industry", "aggravating", "mitigation", "cooperativeness", "remedial",
                              "voluntary", "meaningful_engagement", "admission", "persons_affected",
                              "fault", "extent", "appointment", "type_pd", "fine_y_n"]].copy()
Lenon_Logmodel_DF["fine_y_n_logmodel"] = model4.predict(Lenon_Logmodel_DF) # or Lenon_Logmodel_DF[:-1]?

# Using the functions for prediction
LOactualOutput = list(Lenon_Logmodel_DF["fine_y_n"])
LOpredictedOutput = list(Lenon_Logmodel_DF["fine_y_n_logmodel"])

# Printing logit model
print(model4.summary(), '\n')
print(list(StatisticalMeasures(LOpredictedOutput, LOactualOutput)), '\n\n')

# Printing the required Accuracy, Precision, and Recall values
print("Accuracy = " + str(Accuracy(LOpredictedOutput, LOactualOutput)))
print("Precision = " + str(Precision(LOpredictedOutput, LOactualOutput)))
print("Recall = " + str(Recall(LOpredictedOutput, LOactualOutput)))
# ---------------------------------------------------------------------------------------------------------------
# Unused Models - For initial illustration only.
# ---------------------------------------------------------------------------------------------------------------
print(failedModelMsg, '\n'
                      'These models are unused as they are only used for the initial illustration of the possible\n'
                      'relationships in the data set. However, they did not yield useful results. Nonetheless,\n'
                      'they formed the basis of the later models as shown above. The models here are displayed\n'
                      'for archiving purposes only.')
print(LinModelPhrase, '0_0\n'
                      'This model relates to the first set of variables in the enforcement guide.\n')
model0_0 = smf.ols(formula="fine ~ persons_affected + fault + extent + appointment + type_pd + knowledge",
                   data=ModelLODF).fit()
print(model0_0.summary(), '\n')

print(LinModelPhrase, '0_1\n'
                      "This model relates to the second set of variables in the enforcement guide.\n")
model0_1 = smf.ols(formula="fine ~ aggravating + mitigation + cooperativeness + remedial + voluntary + "
                           "meaningful_engagement + admission", data=ModelLODF).fit()
print(model0_1.summary(), '\n')

# ---------------------------------------------------------------------------------------------------------------
#######################################################################################################################
# ------------------------------------------------------Yi Fei--------------------------------------------------------#
#######################################################################################################################
print('\n', NameYF, ModelWord)
ModelYFDF = pd.read_csv("Team2_data_PDPCDecisions.csv", header=0)
#######################################################################################################################
#                                           Independent Variable Calibration                                          #
#######################################################################################################################
# applying logarithmic transformation to fine and persons_affected
ModelYFDF = ModelYFDF[ModelYFDF.fine!=0]
ModelYFDF["fine_lg"] = ModelYFDF["fine"].apply(np.log10)
ModelYFDF["persons_affected_lg"] = ModelYFDF["persons_affected"].apply(np.log10)

'''
Rationale: to better observe the relationship with other variables, since both of them vary extremely widely in value.

Both values were given logarithmic transformation, because if only one was applied, it will further distort the
comparison due to the large value of some of the data. The lowest value for fine is 1000, and the highest is 1m.

Similarly the lowest number of persons affected are in single digits, while the highest is in excess of millions.
'''
#######################################################################################################################
#                                                        Models                                                       #
#######################################################################################################################
# categorising pdpa factors for determining fine amount
for i in ["aggravating", "mitigation", "cooperativeness",
          "remedial", "voluntary", "meaningful_engagement",
          "admission"]:
    ModelYFDF[i] = ModelYFDF[i].astype('category')

# categorising the remaining collected data
for i in ["year_incident", "year_enforcement", "industry",
          "type", "ownership", "fault",
          "knowledge", "appointment", "enforcement_action" ]:
    ModelYFDF[i] = ModelYFDF[i].astype('category')

# slide 53: compare fine(log10) against pdpc factors for fine amount only
print(LinModelPhrase, '1\n',
      "Compare fine(log10) against pdpc factors for fine amount only")
YFlinmodel1 = smf.ols('fine_lg ~ persons_affected_lg + aggravating + mitigation + cooperativeness + remedial + '
             'voluntary + meaningful_engagement + admission', data=ModelYFDF).fit()
print(YFlinmodel1.summary())

print(LinModelPhrase, '2\n',
      "Attempt to achieve highest r^2, end up all collected variables were put in. r^2 = 0.830")
# slide 54: attempt to achieve highest r^2, end up all collected variables were put in. r^2 = 0.830
YFlinmodel2 = smf.ols('fine_lg ~ year_incident + year_enforcement + persons_affected_lg + type_pd + industry + type + '
             'ownership + extent + fault + knowledge + appointment + admission + voluntary + remedial +'
             'meaningful_engagement + cooperativeness + aggravating + mitigation + enforcement_action',
              data=ModelYFDF).fit()
print(YFlinmodel2.summary())

print(LinModelPhrase, '3\n',
      "Remove variables with high p values. r^2 = 0.813")
# slide 55: remove variables with high p values. r^2 = 0.813
YFlinmodel3 = smf.ols('fine_lg ~ year_enforcement + persons_affected_lg + type_pd + industry + '
             'ownership + knowledge + appointment + admission + voluntary +'
             'cooperativeness + aggravating + enforcement_action', data=ModelYFDF).fit()
# not sure whether to remove 'industries' variable, considering that the p value varies widely for different industries
print(YFlinmodel3.summary())

print(failedModelMsg)
print(NameYF, LinModelPhrase, '4\n',
      "Plotting with variables fine and persons_affected without log transformation\n"
      "he r^2 was very low compared to the models with log-transformed variables in it. Hence it was not used. ")
#Failed Model 1: Plotting with variables fine and persons_affected without log transformation
YFlinmodel4 = smf.ols('fine ~ year_incident + year_enforcement + persons_affected + type_pd + industry + type + '
             'ownership + extent + fault + knowledge + appointment + admission + voluntary + remedial +'
             'meaningful_engagement + cooperativeness + aggravating + mitigation + enforcement_action',
              data=ModelYFDF).fit()
print(YFlinmodel4.summary(), '\n')

#######################################################################################################################
#------------------------------------------------------Stephenie------------------------------------------------------#
#######################################################################################################################
ModelSLDF = pd.read_csv("Team2_data_PDPCDecisions.csv")

#######################################################################################################################
#                                           Independent Variable Calibration                                          #
#######################################################################################################################
# Recalibrating to categorical variables
for i in ["year_incident", "year_enforcement", "industry",
          "ownership", "section", "appointment",
          "voluntary", "cooperativeness", "enforcement_action"]:
    ModelSLDF[i] = ModelSLDF[i].astype('category')

# Recalibrating enforcement_action into with or without financial penalty
ModelSLDF.enforcement_action = ModelSLDF.enforcement_action.replace({1:0, 2:1, 3:1})

#######################################################################################################################
#                                                        Models                                                       #
#######################################################################################################################
print('\n', NameSL, ModelWord)
print("\nLinear Model and Logistic Regression Model 1\n"
      "Assessing seriousness of breach to determine whether financial penalty warranted\n"
      "enforcement_action as dependent variable,\n"
      "fault, extent, knowledge, persons_affected, appointment, type_pd as independent variable\n")

# Linear Regression Model
print(LinModelPhrase + ' 1')
SLlinmodel1 = smf.ols(formula = 'enforcement_action ~ fault + knowledge + extent + persons_affected + appointment + '
                              'type_pd', data = ModelSLDF).fit()
print(SLlinmodel1.summary())

# Logistic regression model
print(LogitModelPhrase, '1')
SLlogitmodel1 = smf.logit(formula='enforcement_action ~ fault + extent + persons_affected + appointment + type_pd',
                        data=ModelSLDF).fit()
print(SLlogitmodel1.summary())

predictions = SLlogitmodel1.predict()
print('accuracy: ' + str(Accuracy(predictions, ModelSLDF.enforcement_action)))
print('precision: ' + str(Precision(predictions, ModelSLDF.enforcement_action)))
print('recall: ' + str(Recall(predictions, ModelSLDF.enforcement_action)))


print("\nLinear Model 2\n"
      "Fine quantum determination\n"
      "Using all cases including those where there is no financial penalty\n"
      "Fine as dependent variable,\n"
      "fault, knowledge, extent, persons_affected, appointment, type_pd, cooperativeness, voluntary, admission,\n"
      "remedial, meaningful_engagement, aggravating, mitigation as independent variable.\n")

# Linear regression model 2
print(LinModelPhrase, '2')
SLlinmodel2 = smf.ols(formula='fine ~ fault + knowledge + extent + persons_affected + appointment + type_pd + '
                            'cooperativeness + voluntary + admission + remedial + meaningful_engagement + aggravating +'
                            'mitigation', data=ModelSLDF).fit()
print(SLlinmodel2.summary())

print("\nLinear Model 3\n"
      "Using only cases which involved a financial penalty\n")

ModelSLDF2 = ModelSLDF.loc[ModelSLDF.enforcement_action == 1]

print(LinModelPhrase, '3')
SLlinmodel3 = smf.ols(formula='fine ~ fault + knowledge + extent + persons_affected + appointment + type_pd + '
                            'cooperativeness + voluntary + admission + remedial + meaningful_engagement + aggravating +'
                            'mitigation', data=ModelSLDF2).fit()
print(SLlinmodel3.summary())

print("\n Newly Generated Models")
newmodel1 = smf.ols(formula="fine_calibrated ~ persons_affected + "
                       'fault + knowledge + C(appointment) + C(voluntary) + '
                       'C(cooperativeness) + aggravating + mitigation',
                       data = ModelLODF).fit()
print(newmodel1.summary())

NMDF = pd.read_csv("Team2_data_PDPCDecisions.csv", header=0)
#######################################################################################################################
#                                           Independent Variable Calibration                                          #
#######################################################################################################################
# applying logarithmic transformation to fine and persons_affected
NMDF = NMDF[NMDF.fine!=0]
NMDF["fine_lg"] = NMDF["fine"].apply(np.log10)
NMDF["persons_affected_lg"] = NMDF["persons_affected"].apply(np.log10)

newmodel2 = smf.ols('fine_lg ~ C(year_incident) + C(year_enforcement) + persons_affected_lg + type_pd + C(industry) + type + '
             'C(ownership) + extent + fault + knowledge + C(appointment) + admission + voluntary + remedial +'
             'meaningful_engagement + C(cooperativeness) + aggravating + mitigation',
              data=NMDF).fit()
print(newmodel2.summary())

newmodel3 = smf.ols('fine_lg ~ C(year_enforcement) + persons_affected_lg + type_pd + C(industry) +  '
             'C(ownership)  + fault + knowledge + C(appointment) + admission + voluntary + '
             'meaningful_engagement + C(cooperativeness) + aggravating + mitigation',
              data=NMDF).fit()
print(newmodel3.summary())

newmodel4 = smf.ols('fine_lg ~ C(year_enforcement) + persons_affected_lg + type_pd +  '
             'C(ownership)  + fault + knowledge + C(appointment) + admission + voluntary + '
             'meaningful_engagement + C(cooperativeness) + aggravating + mitigation',
              data=NMDF).fit()
print(newmodel4.summary())

newmodel5 = smf.ols('fine_lg ~ C(year_enforcement) + persons_affected_lg + type_pd +  '
             'C(ownership)  + fault + knowledge + C(appointment) + admission + voluntary + '
             'meaningful_engagement + C(cooperativeness) + aggravating',
              data=NMDF).fit()
print(newmodel5.summary())

newmodel6 = smf.ols(formula="fine_y_n ~ persons_affected + type_pd + "
                       'extent + fault + knowledge + C(appointment) + admission + C(voluntary) + '
                       'meaningful_engagement + C(cooperativeness) + aggravating + mitigation', data=ModelLODF).fit()
print(newmodel6.summary(), '\n')

newmodel7 = smf.ols(formula="fine_y_n ~ persons_affected + "
                       'fault + knowledge + C(appointment) + C(voluntary) + '
                       'C(cooperativeness) + aggravating + mitigation', data=ModelLODF).fit()
print(newmodel7.summary(), '\n')