# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)
data.replace(to_replace='-',value='Agender',inplace=True)
print(data.head())
data['Gender'].value_counts().plot(kind='bar')
plt.show()
data['Alignment'].value_counts().plot(kind='bar')
plt.show()
highheroes=data['Total'].quantile(q=0.99)
newdata=data[data['Total']>554]
super_best_names=newdata['Name'].tolist()
print(super_best_names)
# Code starts here



