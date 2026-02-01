import scipy.stats as stats

mu = 178
sigma = 9

N = stats.norm(loc=mu, scale=sigma)

a = N.cdf(169)
b = 1 - N.cdf(169)
c = 1 - N.cdf(187)
d = N.cdf(187) - N.cdf(169)
e = N.cdf(196) - N.cdf(160)

print(f"Alle 169cm: {a:.3f}")
print(f"Yli 169cm: {b:.3f}")
print(f"yli 187cm: {c:.3f}")
print(f"Välillä 169cm-187cm: {d:.3f}")
print(f"Välillä 160cm-196cm: {e:.3f}")