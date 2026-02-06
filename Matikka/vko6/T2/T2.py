import numpy as np
from scipy import stats

alpha = 0.05

am = np.array([171, 183, 159, 168, 174])
mu = 180

n = len(am)
mean = am.mean()
sd = am.std(ddof=1)
se = sd / np.sqrt(n)
t_stat = (mean - mu) / se
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
