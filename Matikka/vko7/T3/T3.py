import numpy as np
from scipy import stats

alpha = 0.05

x = np.array([
    7.0642, 7.0431, 7.1501, 7.2159, 7.2381, 7.1285,
    6.8185, 6.7597, 6.9597, 7.0431, 6.9804, 6.9392,
    6.2898, 6.3924, 6.2564, 6.4273, 6.3578, 6.4098
])

sigma0 = 0.09
sigma0_2 = sigma0**2

n = len(x)
s2 = x.var(ddof=1)
df = n - 1

chi2_stat = df * s2 / sigma0_2

p_value = 2 * min(stats.chi2.cdf(chi2_stat, df=df), 1 - stats.chi2.cdf(chi2_stat, df=df))

print(f"n = {n}")
print(f"otoskeskihajonta s = {np.sqrt(s2):.4f}")
print(f"H0: sigma = {sigma0}  (sigma^2 = {sigma0_2})")
print(f"chi2 = {chi2_stat:.3f}")
print(f"df = {df}")
print(f"p-arvo = {p_value:.6f}")
print(f"merkitsevyystaso = {alpha}")

if p_value < alpha:
    print("Tilastollisesti merkitsevä ero")
else:
    print("Ei tilastollisesti merkitsevää eroa")