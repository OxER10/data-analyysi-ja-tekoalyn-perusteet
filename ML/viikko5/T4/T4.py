import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

xl = pd.read_excel('../unemployment.xlsx', sheet_name='Sheet1', engine='openpyxl')
df = xl.copy()
df['Period'] = pd.to_datetime(df['Period'])

total = df.groupby('Period')['Unemployed'].sum().reset_index()
plt.figure(figsize=(8,4))
sns.lineplot(data=total, x='Period', y='Unemployed')
plt.title('Total Unemployment')
plt.tight_layout()
plt.savefig('total_unemp.png')
plt.close()

gen = df.groupby(['Period', 'Gender'])['Unemployed'].sum().reset_index()
plt.figure(figsize=(8,4))
sns.lineplot(data=gen, x='Period', y='Unemployed', hue='Gender')
plt.title('Unemployment by Gender')
plt.tight_layout()
plt.savefig('unemp_gender.png')
plt.close()

age = df.groupby(['Period', 'Age'])['Unemployed'].sum().reset_index()
plt.figure(figsize=(10,6))
sns.lineplot(data=age, x='Period', y='Unemployed', hue='Age')
plt.title('Unemployment by Age')
plt.tight_layout()
plt.savefig('unemp_age.png')
plt.close()