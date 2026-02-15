import numpy as np
from scipy import stats

a = np.array([51, 59, 40, 47, 53])
alpha = 0.05

n = a.sum()
k = len(a)
expected = np.ones(k) * (n / k)

chi2_stat = ((a - expected) ** 2 / expected).sum()
df = k - 1
p_value = 1 - stats.chi2.cdf(chi2_stat, df=df)

print(f"Havaitut: {a.tolist()}")
print(f"Yhteensä n = {n}")
print(f"Odotetut (tasajakauma): {expected.tolist()}")

print(f"\nchi2 = {chi2_stat:.3f}")
print(f"df = {df}")
print(f"p-arvo = {p_value:.4f}")
print(f"alpha = {alpha}")

if p_value < alpha:
    print("Myynti ei ole tasajakautunutta (tilastollisesti merkitsevä ero)")
else:
    print("Myynti on tasajakautunutta (Ei tilastollisesti merkitsevää eroa)")