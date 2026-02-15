import numpy as np
from scipy import stats

a = np.array([178, 190, 166, 175, 181])
aM = np.array([166, 179, 155, 164, 170])

n1, n2 = len(a), len(aM)
mean1, mean2 = a.mean(), aM.mean()
sd1, sd2 = a.std(ddof=1), aM.std(ddof=1)

print(f"mean(a)  = {mean1:.2f}, sd(a)  = {sd1:.2f}, n = {n1}")
print(f"mean(aM) = {mean2:.2f}, sd(aM) = {sd2:.2f}, n = {n2}")
print()

se = np.sqrt(sd1**2 / n1 + sd2**2 / n2)
t_stat = (mean1 - mean2) / se
df = (sd1**2 / n1 + sd2**2 / n2)**2 / ((sd1**2 / n1)**2 / (n1 - 1) + (sd2**2 / n2)**2 / (n2 - 1))

p_two = 2 * stats.t.cdf(-abs(t_stat), df=df)
print("a) Kaksisuuntainen t-testi (mean(a) != mean(aM))")
print(f"t = {t_stat:.3f}, df = {df:.2f}, p = {p_two:.4f}")
alpha = 0.05
print("Tilastollisesti merkitsevä ero" if p_two < alpha else "Ei tilastollisesti merkitsevää eroa")
print()

p_one = 1 - stats.t.cdf(t_stat, df=df)
print("b) Yksisuuntainen t-testi (mean(aM) < mean(a))")
print(f"t = {t_stat:.3f}, df = {df:.2f}, p = {p_one:.4f}")
alpha = 0.05
print("Tilastollisesti merkitsevä ero" if p_one < alpha else "Ei tilastollisesti merkitsevää eroa")
print()

alpha = 0.01
print("c) testi 1% merkitsevyystasolla")
if p_one < alpha:
    print("Tilastollisesti merkitsevä ero")
else:
    print("Ei tilastollisesti merkitsevää eroa")