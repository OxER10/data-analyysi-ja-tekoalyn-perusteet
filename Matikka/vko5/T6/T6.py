import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

x = np.linspace(-5, 5, 800)

norm_pdf = stats.norm.pdf(x, loc=0, scale=1)

t1_pdf = stats.t.pdf(x, df=1)

t3_pdf = stats.t.pdf(x, df=3)
t5_pdf = stats.t.pdf(x, df=5)

t30_pdf = stats.t.pdf(x, df=30)
t100_pdf = stats.t.pdf(x, df=100)

plt.figure(figsize=(9, 6))

# Piirrot samaan kuvaajaan
plt.plot(x, norm_pdf, 'b--', linewidth=2, label='N(0,1) (standardinormaali)')
plt.plot(x, t1_pdf,  color='#d62728', label='t(df=1)')
plt.plot(x, t3_pdf,  color='#ff7f0e', label='t(df=3)')
plt.plot(x, t5_pdf,  color='#2ca02c', label='t(df=5)')
plt.plot(x, t30_pdf, color='#9467bd', alpha=0.9, label='t(df=30)')
plt.plot(x, t100_pdf, color='#8c564b', alpha=0.9, label='t(df=100)')

plt.title('Standardinormaali ja t-jakaumat samalla kuvaajalla')
plt.xlabel('x')
plt.ylabel('Tiheys (pdf)')
plt.grid(True, alpha=0.25)
plt.legend()
plt.tight_layout()
plt.show()