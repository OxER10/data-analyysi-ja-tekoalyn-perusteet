import numpy as np
import matplotlib.pyplot as plt

# Data
y  = np.array([10.2, 11.5, 13.9, 15.0])  # selitettävä muuttuja
x1 = np.array([3.1, 3.9, 5.2, 6.9])      # 1. selittävä muuttuja
x2 = np.array([9.0, 7.5, 6.0, 5.0])      # 2. selittävä muuttuja

# --- Sovite 1: 2. asteen polynomi x1 -> y ---
coef2 = np.polyfit(x1, y, deg=2)  # [a, b, c]
p2 = np.poly1d(coef2)

# Sovitekäyrä
x1_grid = np.linspace(x1.min(), x1.max(), 300)
y1_fit_grid = p2(x1_grid)

# Ennusteet havaintopisteissä ja residuaalit
y1_hat = p2(x1)
res1 = y - y1_hat

# R^2
SSE1 = np.sum(res1**2)
SST = np.sum((y - y.mean())**2)
R2_1 = 1 - SSE1/SST if SST != 0 else np.nan

# --- Sovite 2: 3. asteen polynomi x2 -> y ---
coef3 = np.polyfit(x2, y, deg=3)  # [a, b, c, d]
p3 = np.poly1d(coef3)

x2_grid = np.linspace(x2.min(), x2.max(), 300)
y2_fit_grid = p3(x2_grid)

y2_hat = p3(x2)
res2 = y - y2_hat

SSE2 = np.sum(res2**2)
R2_2 = 1 - SSE2/SST if SST != 0 else np.nan

# Tulosta mallien yhtälöt ja suorituskykymitat
def poly_to_str(coefs):
    # Muodosta luettava polynomi (korkein aste ensin)
    terms = []
    deg = len(coefs) - 1
    for i, a in enumerate(coefs):
        power = deg - i
        if abs(a) < 1e-12:
            continue
        coeff = f"{a:.6g}"
        if power > 1:
            terms.append(f"{coeff}·x^{power}")
        elif power == 1:
            terms.append(f"{coeff}·x")
        else:
            terms.append(f"{coeff}")
    return " + ".join(terms).replace("+-", "-")

print("2. asteen polynomi (x1 → y): y =", poly_to_str(coef2))
print(f"R^2 (x1): {R2_1:.6f}")
print("3. asteen polynomi (x2 → y): y =", poly_to_str(coef3))
print(f"R^2 (x2): {R2_2:.6f}")

# --- Piirretään samaan kuvaan kaksi alikuvaa: (1) data + sovitteet, (2) residuaalit ---
plt.figure(figsize=(10, 8))

# Yläkuva: data ja sovitteet
ax1 = plt.subplot(2, 1, 1)
ax1.scatter(x1, y, color="#1f77b4", marker="o", s=70, label="Havainnot (x1, y)")
ax1.plot(x1_grid, y1_fit_grid, color="#1f77b4", linestyle="-", label="2. asteen sovite (x1 → y)")

ax1.scatter(x2, y, color="#d62728", marker="s", s=70, label="Havainnot (x2, y)")
ax1.plot(x2_grid, y2_fit_grid, color="#d62728", linestyle="--", label="3. asteen sovite (x2 → y)")

ax1.set_title("Polynomisovitteet alkuperäisen datan kanssa", fontsize=12)
ax1.set_xlabel("Selittävä muuttuja (x1 ja x2)")
ax1.set_ylabel("Selitettävä muuttuja (y)")
ax1.grid(True, alpha=0.3)
ax1.legend()

# Alakuva: residuaalit
ax2p = plt.subplot(2, 1, 2)
ax2p.axhline(0, color="black", linewidth=1)
ax2p.scatter(x1, res1, color="#1f77b4", marker="o", s=70, label="Residuaalit (x1)")
ax2p.scatter(x2, res2, color="#d62728", marker="s", s=70, label="Residuaalit (x2)")
ax2p.set_title("Residuaalit")
ax2p.set_xlabel("Selittävä muuttuja (x1 ja x2)")
ax2p.set_ylabel("Residuaali (y − ŷ)")
ax2p.grid(True, alpha=0.3)
ax2p.legend()

plt.tight_layout()
plt.savefig("polynomi_sovitteet_ja_residuaalit.png", dpi=200, bbox_inches="tight")
plt.show()
