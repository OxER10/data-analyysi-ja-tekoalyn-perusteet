import numpy as np
from scipy import stats

n = 30
mean = 61.0
sd = 2.0
mu = 60.0
alpha = 0.03

se = sd / np.sqrt(n)
df = n - 1

t_stat = (mean - mu) / se
p_value = 1 - stats.t.cdf(t_stat, df=df)

print(f"p: {p_value:.6f}")
print(f"Merkitsevyystaso: {alpha}")
if p_value < alpha:
    print("Keskiarvo 61MB/s on tilastollisesti merkitsevästi suurempi kuin 60 MB/s, joten lupaus on pidetty")
else:
    print("Keskiarvo 61MB/s ei ole tilastollisesti merkitsevästi suurempi kuin 60 MB/s, joten lupaus ei ole pidetty")