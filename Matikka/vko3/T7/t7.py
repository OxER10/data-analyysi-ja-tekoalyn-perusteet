import numpy as np
import matplotlib.pyplot as plt

# T1
# Tehtävän 4 data
x1 = np.array([3.1, 3.9, 5.2, 6.9])
y = np.array([10.2, 11.5, 13.9, 15.0])

# Sovita 2. asteen polynomi x1, y-dataan
mults = np.polyfit(x1, y, 2)
a, b, c = mults
print(f"Polyfitin antamat kertoimet: a = {a:.3f}, b = {b:.3f}, c = {c:.3f}")

# T2
# Laske sovitetut arvot
y_hat = np.polyval(mults, x1)
residuals = y - y_hat

# Piirrä datapisteet ja polynomisovite
x_plot = np.linspace(min(x1), max(x1), 200)
y_plot = np.polyval(mults, x_plot)

plt.figure(figsize=(8,5))

# Polynomikäyrä
plt.plot(x_plot, y_plot, color='crimson', label='2. asteen polynomi')

# Datapisteet
plt.scatter(x1, y, label='Data')

# Residuaalit pystypuikkoina
for xi, yi, yhi in zip(x1, y, y_hat):
    plt.plot([xi, xi], [yhi, yi], color='purple', lw=2, alpha=0.9)
plt.xlabel('x1'); plt.ylabel('y')
plt.title('Data + polynomikäyrä + residuaalit')
plt.grid(alpha=0.3)
plt.legend()