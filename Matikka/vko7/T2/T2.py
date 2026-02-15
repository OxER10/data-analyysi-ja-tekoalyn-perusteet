import numpy as np
from scipy import stats

a = np.array([178, 190, 166, 175, 181])
aM = np.array([166, 179, 155, 164, 170])
alpha = 0.05

d = a - aM

n = len(d)
mean_d = d.mean()
sd_d = d.std(ddof=1)
se_d = sd_d / np.sqrt(n)

t_stat = mean_d / se_d
df = n - 1
p_value = 2 * stats.t.cdf(-abs(t_stat), df=df)

print("Erot d = a - aM:", d)
print(f"Keskiarvo eroille: {mean_d:.2f}")
print(f"t-arvo: {t_stat:.3f}")
print(f"df: {df}")
print(f"p-arvo: {p_value:.3f}")
print(f"merkitsevyystaso: {alpha}")

print("a)")
if p_value < alpha:
    print("Tilastollisesti merkitsevä ero")
else:
    print("Ei tilastollisesti merkitsevää eroa")