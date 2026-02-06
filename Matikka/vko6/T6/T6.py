import numpy as np
from scipy import stats

a = np.array([178, 190, 166, 175, 181])
b = np.array([166, 179, 155, 164, 170])

t_ab, p_two = stats.ttest_ind(a, b, equal_var=False)

print("a) Keskiarvojen yhtäsuuruustesti (kaksisuuntainen Welch)")
print("Merkitsevyystaso: 0.05")
print(f"p: {p_two:.6f}")
if p_two < 0.05:
    print("Keskiarvot ovat tilastollisesti merkitsevästi erisuuret")
else:
    print("Keskiarvot eivät ole tilastollisesti merkitsevästi erisuuret")

if t_ab > 0:
    p_one = p_two / 2
else:
    p_one = 1 - p_two / 2

print("b) Onko b-datan keskiarvo tilastollisesti merkitsevästi pienempi kuin a-datan?")
print("Merkitsevyystaso: 0.05")
print(f"p: {p_one:.6f}")
if p_one < 0.05:
    print("Keskiarvo on tilastollisesti merkitsevästi pienempi")
else:
    print("Keskiarvo ei ole tilastollisesti merkitsevästi pienempi")

print("c) Merkitsevyystaso: 0.05")
if p_one < 0.01:
    print("Keskiarvo on tilastollisesti merkitsevästi pienempi")
else:
    print("Keskiarvo ei ole tilastollisesti merkitsevästi pienempi")