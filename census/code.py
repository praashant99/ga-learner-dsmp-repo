# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')
data=np.genfromtxt(path,delimiter=',',skip_header=1)
print(data)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census=np.concatenate((data,new_record))

age=census[0]
max_age=age.max()
min_age=age.min()
age_mean=sum(age)/len(age)
age_std=np.std(age)

race_0=census[0]==0
race_1=census[0]==1
race_2=census[0]==2
race_3=census[0]==3
race_4=census[0]==4

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

min_race=min(len_0,len_1,len_2,len_3,len_4)
if min_race== len(race_0):
    minority_race=0
elif min_race== len(race_1):
    minority_race=1
elif min_race== len(race_2):
    minority_race=2
elif min_race== len(race_3):
    minority_race=3
elif min_race== len(race_4):
    minority_race=4


senior_citizen=np.asarray([i for i in census if i[0]>60])
working_hours_sum=senior_citizen[:,6].sum()
senior_citizen_len=len(senior_citizen)
avg_working_hours=working_hours_sum/senior_citizen_len
print(avg_working_hours)

high=np.asarray([i for i in census if i[1]>10])
low=np.asarray([i for i in census if i[1]<=10])

avg_pay_high=high[:,7].mean()
avg_pay_low=low[:,7].mean()
print(avg_pay_high)
print(avg_pay_low)

#Reading file

#Code starts here




