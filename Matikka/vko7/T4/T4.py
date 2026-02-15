import numpy as np
from scipy import stats

a = np.array([7.0642, 7.0431, 7.1501, 7.2159, 7.2381, 7.1285])
b = np.array([6.8185, 6.7597, 6.9597, 7.0431, 6.9804, 6.9392])
c = np.array([6.2898, 6.3924, 6.2564, 6.4273, 6.3578, 6.4098])
alpha = 0.001

n1, n2 = len(a), len(b)
mean1, mean2 = a.mean(), b.mean()
sd1, sd2 = a.std(ddof=1), b.std(ddof=1)
se = np.sqrt(sd1**2 / n1 + sd2**2 / n2)
t_stat = (mean1 - mean2) / se
df = (sd1**2 / n1 + sd2**2 / n2)**2 / ((sd1**2 / n1)**2 / (n1 - 1) + (sd2**2 / n2)**2 / (n2 - 1))
p_value = 2 * stats.t.cdf(-abs(t_stat), df=df)

print("a ja b")
print(f"mean(a)={mean1:.4f}, mean(b)={mean2:.4f}, erotus={mean1-mean2:.4f}")
print(f"t={t_stat:.3f}, df={df:.2f}, p={p_value:.6g}, alpha={alpha}")
print("Merkitsevä ero" if p_value < alpha else "Ei merkitsevää eroa")

n1, n2 = len(a), len(c)
mean1, mean2 = a.mean(), c.mean()
sd1, sd2 = a.std(ddof=1), c.std(ddof=1)
se = np.sqrt(sd1**2 / n1 + sd2**2 / n2)
t_stat = (mean1 - mean2) / se
df = (sd1**2 / n1 + sd2**2 / n2)**2 / ((sd1**2 / n1)**2 / (n1 - 1) + (sd2**2 / n2)**2 / (n2 - 1))
p_value = 2 * stats.t.cdf(-abs(t_stat), df=df)

print("a ja c")
print(f"mean(a)={mean1:.4f}, mean(c)={mean2:.4f}, erotus={mean1-mean2:.4f}")
print(f"t={t_stat:.3f}, df={df:.2f}, p={p_value:.6g}, alpha={alpha}")
print("Merkitsevä ero" if p_value < alpha else "Ei merkitsevää eroa")

n1, n2 = len(b), len(c)
mean1, mean2 = b.mean(), c.mean()
sd1, sd2 = b.std(ddof=1), c.std(ddof=1)
se = np.sqrt(sd1**2 / n1 + sd2**2 / n2)
t_stat = (mean1 - mean2) / se
df = (sd1**2 / n1 + sd2**2 / n2)**2 / ((sd1**2 / n1)**2 / (n2 - 1) + (sd2**2 / n2)**2 / (n2 - 1))
p_value = 2 * stats.t.cdf(-abs(t_stat), df=df)

print("b ja c")
print(f"mean(b)={mean1:.4f}, mean(c)={mean2:.4f}, erotus={mean1-mean2:.4f}")
print(f"t={t_stat:.3f}, df={df:.2f}, p={p_value:.6g}, alpha={alpha}")
print("Merkitsevä ero" if p_value < alpha else "Ei merkitsevää eroa")