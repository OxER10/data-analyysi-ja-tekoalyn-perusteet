import numpy as np

# selitettävä muuttuja
y = np.array([10.2, 11.5, 13.9, 15.0])

# selittävät muutujat
x1 = np.array([3.1, 3.9, 5.2, 6.9])
x2 = np.array([9.0, 7.5, 6.0, 5.0])

# Vakio mukana
X = np.column_stack([np.ones(len(y)),x1, x2])

p = np.linalg.lstsq(X,y,rcond=None)
b, SSres, rank, s = p
ennuste = X @ b
res = y - ennuste
y_mean = np.mean(y)
y_res = y - y_mean
y_mean_res = y_res - res
y_mean_res_pow2 = y_mean_res**2
SSreg = sum(y_mean_res_pow2)
print("SSreg: ", SSreg)

y_res_pow2 = y_res**2
SStot = sum(y_res_pow2)
R2 = (SSreg / SStot)
print("Selitysaste:", R2)