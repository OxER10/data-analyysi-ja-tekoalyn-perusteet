import numpy as np
from scipy import stats

lsat = np.array([576, 635, 558, 578, 666, 580, 555, 661, 651, 605, 653, 575, 545, 572, 594])
lsat_vertailu = np.array([663, 614, 649, 643, 676])
alpha = 0.05

n1, n2 = len(lsat), len(lsat_vertailu)
mean1, mean2 = lsat.mean(), lsat_vertailu.mean()
sd1, sd2 = lsat.std(ddof=1), lsat_vertailu.std(ddof=1)

se = np.sqrt(sd1**2 / n1 + sd2**2 / n2)
t_stat = (mean1 - mean2) / se

df = (sd1**2 / n1 + sd2**2 / n2)**2 / ((sd1**2 / n1)**2 / (n1 - 1) + (sd2**2 / n2)**2 / (n2 - 1))

p_value = 2 * stats.t.cdf(-abs(t_stat), df=df)

print(f"Keskiarvo (lsat): {mean1:.2f}, sd: {sd1:.2f}, n: {n1}")
print(f"Keskiarvo (vertailu): {mean2:.2f}, sd: {sd2:.2f}, n: {n2}")
print(f"Erotus (keskiarvo1-keskiarvo2): {(mean1-mean2):.2f}")

print(f"t-arvo: {t_stat:.3f}")
print(f"df: {df:.2f}")
print(f"p-arvo: {p_value:.3f}")
print(f"merkitsevyystaso: {alpha}")

print("a)")
if p_value < alpha:
    print("Tilastollisesti merkitsevä ero")
else:
    print("Ei tilastollisesti merkitsevää eroa")