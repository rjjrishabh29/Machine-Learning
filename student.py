#importing modules
import matplotlib.pyplot as plt
import pandas as pd

#reading data 
df=pd.read_csv('student.csv')

#graphs 
plt.pie(df.age,labels=df.name,autopct='%1.1f%%')
plt.show()
plt.pie(df.marks,labels=df.name,autopct='%1.1f%%')
plt.show()
