import numpy as np
from scipy import stats

O = np.array([
    [936, 240, 195, 101],
    [909, 297, 150, 115]
], dtype=float)
alpha = 0.05

row_sum = O.sum(axis=1, keepdims=True)
col_sum = O.sum(axis=0, keepdims=True)
N = O.sum()

E = row_sum @ col_sum / N
terms = (O - E)**2 / E
chi2_stat = terms.sum()

r, c = O.shape
df = (r - 1) * (c - 1)
p_value = 1 - stats.chi2.cdf(chi2_stat, df=df)

print("Havaitut O:", O.astype(int))
print("Rivisummat:", row_sum.flatten().astype(int))
print("Sarakesummat:", col_sum.flatten().astype(int))
print("N =", int(N))

print("Odotetut E (pyöristetty):", np.round(E, 2))
print("X²-osatermit (O-E)²/E (pyöristetty):", np.round(terms, 4))

print(f"\nchi2 = {chi2_stat:.4f}")
print(f"df = {df}")
print(f"p-arvo = {p_value:.6g}")
print(f"alpha = {alpha}")

if p_value < alpha:
    print("Vuosi ja etnisyys ovat riippuvaisia.")
else:
    print("Vuosi ja etnisyys eivät ole riippuvaisia")