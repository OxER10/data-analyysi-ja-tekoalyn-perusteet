import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../emp-dep.csv')

plt.figure(figsize=(6,4))
plt.scatter(df['age'], df['salary'])
plt.xlabel('Ikä')
plt.ylabel('Palkka')
plt.title('Ikä vs. palkka')
plt.tight_layout()
plt.savefig('scatter.png')
plt.close()

dep_counts = df['dname'].value_counts()
plt.figure(figsize=(6,4))
dep_counts.plot(kind='bar')
plt.ylabel('Lukumäärä')
plt.xlabel('Osasto')
plt.title('Osastojen työntekijämäärät')
plt.tight_layout()
plt.savefig('bar.png')
plt.close()

plt.figure(figsize=(6,4))
dep_counts.plot(kind='barh')
plt.xlabel('Lukumäärä')
plt.ylabel('Osasto')
plt.title('Osastojen työntekijämäärät (horisontaalinen)')
plt.tight_layout()
plt.savefig('barh.png')
plt.close()