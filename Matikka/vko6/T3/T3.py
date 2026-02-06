import numpy as np
from scipy import stats

alpha = 0.005
mu = 6.72

malli1 = np.array([7.0642, 7.0431, 7.1501, 7.2159, 7.2381, 7.1285], dtype=float)
malli2 = np.array([6.8185, 6.7597, 6.9597, 7.0431, 6.9804, 6.9392], dtype=float)
malli3 = np.array([6.2898, 6.3924, 6.2564, 6.4273, 6.3578, 6.4098], dtype=float)

mallit = [malli1, malli2, malli3]


print("a) Otoskeskiarvot ja otoskeskihajonnat")
for i, malli in enumerate(mallit, start=1):
    mean = malli.mean()
    sd = malli.std(ddof=1)
    print(f"Malli{i}, Keskiarvo: {mean:.3f}, Otoskeskihajonta: {sd:.3f}")

print("b)Yksiotos t‑testi arvoa 6.72 vastaan")
print("merkitsevyystaso: {alpha}")
for i, malli in enumerate(mallit, start=1):
    t_stat, p_two_sided = stats.ttest_1samp(malli, mu)
    print(f"Malli{i}, p: {p_two_sided:.6f}")
    if p_two_sided < alpha:
        print("Tilastollisesti merkitsevä ero")
    else:
        print("Ei tilastollisesti merkitsevää eroa")


