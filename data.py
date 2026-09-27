import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
data = {
    'Month':['jan','Fed','Mar','Apr','May','Jun'],
    'Sales': [12000,15000,17000,13000,22000,24000],
    'Expenses':[8000,9500,11000,8500,13000,14000]
}
df = pd.DataFrame(data)
print("---Raw Data---")
print(df)
df['profit'] = df['Sales'] - df['Expenses']
mean_sales = np.mean(df['Sales'])
max_profit = np.max(df['profit'])
print("\n --- processed Data----")
print(df)
print(f"\n Average sales: ${mean_sales:,.2f}")
print(f"Highest Monthly profit : ${max_profit:,.2f}")
plt.figure(figsize=(8,5))
plt.plot(df['Month'],df['Sales'],marker='o',color='blue',label='Sales')
plt.plot(df['Month'],df['Expenses'],marker='s',color= 'red',linestyle='--',label='Expenses')
plt.title("Monthly sales vs Expenses",fontsize=14,fontweight='bold')
plt.xlabel('Month',fontsize=12)
plt.ylabel('Amount in USD($)',fontsize=12)
plt.legend()
plt.grid(True,linestyle=':',alpha=0.6)
plt.show()
# python:select inpterpeter python 3.13