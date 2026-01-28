import numpy as np

# selitettävä muuttuja
y = np.array([10.2, 11.5, 13.9, 15.0])

# selittävät muutujat
x1 = np.array([3.1, 3.9, 5.2, 6.9])
x2 = np.array([9.0, 7.5, 6.0, 5.0])

n = len(x2)

# Sovita 2. asteen polynomi x1, y-dataan
p = np.polyfit(x1, y, 2, full=True)
mults = p[0]

# Laske mallin residuaalien neliöiden summa
SSres = p[1]

# Laske mallin residuaalien neliöiden summa
ennuste = np.polyval(mults, x1)
res = y - ennuste
SSres_2 = sum(res**2)
print("SSres:", SSres_2)

# Laske kokonaisvaihtelun neliösumma
y_mean = np.mean(y)
y_res = y - y_mean
y_res_pow2 = y_res**2
SStot = sum(y_res_pow2)
print("SStot:", SStot)

# Laske selitysaste
R2 = 1 - (SSres / SStot)
print("Selitysaste:", R2)




