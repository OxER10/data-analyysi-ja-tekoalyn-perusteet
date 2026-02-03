import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../emp-dep.csv')

age_counts = df['age_group'].value_counts().sort_index()

plt.figure(figsize=(6,4))
age_counts.plot(kind='bar')
plt.xlabel('Ikäryhmä')
plt.ylabel('Lukumäärä')
plt.title('Työntekijöiden määrä ikäryhmittäin')
plt.tight_layout()
plt.savefig('age_groups.png')
plt.close()