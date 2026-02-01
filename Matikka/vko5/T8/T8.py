import numpy as np
from scipy import stats

alpha = 0.05

a = np.array([171, 183, 159, 168, 174])
mu0 = 180

n = len(a)
mean = a.mean()
s = a.std(ddof=1)
se = s / np.sqrt(n)
t_stat = (mean - mu0) / se
df = n - 1

p_value = 2 * stats.t.cdf(-abs(t_stat), df=df)

print(f"a) Keskiarvo: {mean}")
print("b)")
print(f"p-arvo: {p_value:.3f}")
print(f"merkitsevyystaso: {alpha}")

if p_value < alpha:
    print("Tilastollisesti merkitsevä ero")
else:
    print("Ei tilastollisesti merkitsevää eroa")