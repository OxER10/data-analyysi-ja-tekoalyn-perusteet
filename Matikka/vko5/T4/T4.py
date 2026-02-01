import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# A)
mu = 178
sigma = 9
x = np.linspace(130, 230, 400)
N = stats.norm(mu, sigma)
y = N.pdf(x)

plt.figure()
plt.plot(x, y, label="N(178, 9)")
plt.title("Suomalaisten miesten pituusjakauma")
plt.xlabel("Pituus (cm)")
plt.ylabel("Tiheys")
plt.grid(True)
plt.legend()
plt.show()

# B)
x2 = np.linspace(-4, 4, 400)
N2 = stats.norm(0, 1)
y2 = N2.pdf(x2)

plt.figure()
plt.plot(x2, y2, label="N(0, 1)")
plt.title("Standardinormaalijakauma")
plt.xlabel("z")
plt.ylabel("Tiheys")
plt.grid(True)
plt.legend()
plt.show()