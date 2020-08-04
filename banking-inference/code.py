# --------------
#Importing header files
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import ztest
from scipy.stats import chi2_contingency

import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

# Critical Value
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1


#Reading file
data=pd.read_csv(path)

#Code starts here
data_sample=data.sample(n=sample_size,random_state=0)
meann=data_sample['installment'].mean()
stddev=data_sample['installment'].std()
confidence_interval=(meann-z_critical*stddev/(np.sqrt(sample_size))),(meann+z_critical*stddev/(np.sqrt(sample_size)))
print(confidence_interval)
true_mean=data['installment'].mean()
print(true_mean)


size=np.array([20,50,100])
a=data.sample(n=20,random_state=1)
b=data.sample(n=50,random_state=2)
c=data.sample(n=100,random_state=3)
d=a['installment'].mean()
e=b['installment'].mean()
f=c['installment'].mean()
print(d,e,f)

data['int.rate'] = data['int.rate'].map(lambda x: x.rstrip('%'))
data['int.rate'] = data['int.rate'].apply(pd.to_numeric)
data['int.rate'] = data['int.rate'] / 100
z_statistic_1,p_value_1=ztest(x1=data[data['purpose']=='small_business']['int.rate'],value=data['int.rate'].mean(),alternative='larger')
print(z_statistic_1,p_value_1)
z_statistic_2,p_value_2=ztest(x1=data[data['paid.back.loan']=='No']['installment'],x2=data[data['paid.back.loan']=='Yes']['installment'],alternative='two-sided')
print(z_statistic_2,p_value_2)
yes=data[data['paid.back.loan']=='Yes']['purpose'].value_counts()
no=data[data['paid.back.loan']=='No']['purpose'].value_counts()
observed = pd.concat([yes.transpose(), no.transpose()], axis = 1, keys = ['Yes', 'No'])
chi2, p, dof, ex = chi2_contingency(observed)
if chi2 > critical_value:
    print("Reject the Null Hypothesis.")
else:
    print("Do not reject the Null Hypothesis.")


