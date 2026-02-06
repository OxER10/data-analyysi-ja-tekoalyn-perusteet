import numpy as np
from scipy import stats

alpha = 0.05

lsat = np.array([576, 635, 558, 578, 666, 580, 555, 661, 651, 605, 653, 575, 545, 572, 594])

n = len(lsat)
mean = lsat.mean()
s = lsat.std(ddof=1)
se = s / np.sqrt(n)
df = n - 1

print("a) Testin keskimääräinen pistemäärä")
print(f"Keskiarvo = {mean:.3f}, otoskeskihajonta = {s:.3f}")

# Yksisuuntainen t-testi '>' mu vastaan
def ttest_greater(data, mu0):
    t_stat, p_two = stats.ttest_1samp(data, mu0)
    if mean > mu0:
        p_one = p_two / 2 
    else:
        p_one = 1 - p_two/2
    return t_stat, p_one

mu_b = 600
t_b, p_b = ttest_greater(lsat, mu_b)
print("b) Onko keskiarvo tilastollisesti merkitsevästi suurempi kuin 600?")
print(f"t: {t_b:.4f}, p: {p_b:.6f}")
if p_b < alpha:
    print("Tilastollisesti merkitsevästi suurempi")
else:
    print("Ei tilastollisesti merkitsevästi suurempi")

mu0_c = 570
t_c, p_c = ttest_greater(lsat, mu0_c)
print("c) Onko keskiarvo tilastollisesti merkitsevästi suurempi kuin 570?")
print(f"t: {t_c:.4f}, p: {p_c:.6f}")
if p_c < alpha:
    print("Tilastollisesti merkitsevästi suurempi")
else:
    print("Ei tilastollisesti merkitsevästi suurempi")

t = stats.t.ppf(1 - alpha, df=df)
mu_max = mean - t * se
print("d) Suurin luku, jota suurempi a-kohdan keskiarvo on tilastollisesti merkitsevästi:")
print(f"Suurin luku:{mu_max:.3f}")