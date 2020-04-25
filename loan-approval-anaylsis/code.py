# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
bank = pd.read_csv(path)

categorical_var =bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)

bank.drop(["Loan_ID"],inplace=True,axis=1)
banks=bank
print(banks.isnull().sum())

bank_mode=banks.mode()

bank.fillna(banks.mode().iloc[0], inplace=True)
print(bank)

avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values="LoanAmount")

print(avg_loan_amount)

loan_approved_se=banks[(banks['Self_Employed'] == 'Yes') &(banks['Loan_Status'] == 'Y')].count()
loan_approved_nse=banks[(banks['Self_Employed'] == 'No') &(banks['Loan_Status'] == 'Y')].count()

percentage_se=(loan_approved_se['Self_Employed']*100/614)
percentage_nse=(loan_approved_nse['Self_Employed']*100/614)

loan_term=banks['Loan_Amount_Term'].apply(lambda x:x/12)
big_loan_term=loan_term[loan_term>=25].count()
print(big_loan_term)

column_imp=['ApplicantIncome', 'Credit_History']

loan_groupby=banks.groupby(['Loan_Status'])[column_imp]


mean_values=loan_groupby.agg([np.mean])

print(mean_values)

#Code starts here




