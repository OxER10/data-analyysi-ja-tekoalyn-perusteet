import numpy as np

# selitettävä muuttuja
y = np.array([10.2, 11.5, 13.9, 15.0])

# selittävät muutujat
x1 = np.array([3.1, 3.9, 5.2, 6.9])
x2 = np.array([9.0, 7.5, 6.0, 5.0])

n = len(x2)

# Sovita 2. asteen polynomi x1, y-dataan
mults = np.polyfit(x2, y, 3)
p = np.poly1d(mults)

# Laske mallin residuaalien neliöiden summa
ennuste = p(x2)
res = y - ennuste
SSres = sum(res**2)
print("SSres:", SSres)

# Laske kokonaisvaihtelun neliösumma
y_mean = np.mean(y)
y_res = y - y_mean
y_res_pow2 = y_res**2
SStot = sum(y_res_pow2)
print("SStot:", SStot)

# Laske selitysaste
R2 = 1 - (SSres / SStot)
print("Selitysaste:", R2)

# Laske korrelaatiokerroin y ja ennuste välillä
r = np.corrcoef(y, ennuste)[0,1]
print("Korrelaatiokerroin:", r)




