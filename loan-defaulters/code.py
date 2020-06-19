# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)
p_a=len(df[df['fico']>700])/len(df)
p_b=len(df[df['purpose']=='debt_consolidation'])/len(df)
df1=df.loc[df['purpose']=='debt_consolidation']
p_a_b=len(df1[df1['fico']>700])/len(df1)
result=(p_a_b==p_b)
print(result)


#Code starts here
prob_lp=len(df[df['paid.back.loan']=='Yes'])/len(df)
prob_cs=len(df[df['credit.policy']=='Yes'])/len(df)
new_df=df.loc[df['paid.back.loan']=='Yes']
prob_pd_cs=len(new_df[new_df['credit.policy']=='Yes'])/len(new_df)
bayes=prob_pd_cs*prob_lp/prob_cs
print(bayes)


df['purpose'].value_counts().plot(kind='bar')
plt.show()
df1=df[df['paid.back.loan']=='No']
df1['purpose'].value_counts().plot(kind='bar')
plt.show()

inst_meadian=df['installment'].median()
inst_mean=df['installment'].mean()
df['installment'].plot(kind='hist')
plt.show()
df['log.annual.inc'].plot(kind='hist')
plt.show()













