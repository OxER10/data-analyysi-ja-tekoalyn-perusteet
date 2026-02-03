import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../emp-dep.csv')

g_counts = df['gender'].value_counts()  # 0=male, 1=female
labels = ['Miehet', 'Naiset']
plt.figure(figsize=(6,6))
plt.pie(g_counts, labels=labels, autopct='%1.1f%%')
plt.title('Miesten ja naisten prosenttiosuudet')
plt.savefig('pie_gender.png')
plt.close()

age_gender = df.groupby(['age_group', 'gender']).size().unstack(fill_value=0)
plt.figure(figsize=(8,5))
age_gender.plot(kind='bar', width=0.8)
plt.xlabel('Ikäryhmä')
plt.ylabel('Lukumäärä')
plt.title('Työntekijät ikäryhmittäin (miehet vs naiset)')
plt.tight_layout()
plt.savefig('age_gender.png')
plt.close()