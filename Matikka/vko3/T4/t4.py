import numpy as np
import matplotlib.pyplot as plt

# Data
x1 = np.array([3.1, 3.9, 5.2, 6.9], dtype=float)
x2 = np.array([9.0, 7.5, 6.0, 5.0], dtype=float)
y = np.array([10.2, 11.5, 13.9, 15.0], dtype=float)

# A) 2D-visualisoinnit
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.scatter(x1, y)
plt.xlabel("x1")
plt.ylabel("y")
plt.title("y suhteessa x1:een")
plt.grid(alpha=0.3)

plt.subplot(1, 2, 2)
plt.scatter(x2, y)
plt.xlabel("x2")
plt.ylabel("y")
plt.title("y suhteessa x2:een")
plt.grid(alpha=0.3)

# B) 3D-pistepilvi
fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(x1, x2, y)
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_zlabel("y")
ax.set_title("3D datapisteet")
plt.show()

# C) Kahden muuttujan lineaarinen regressio
X = np.column_stack([np.ones_like(x1), x1, x2])
XtX = X.T @ X
Xty = X.T @ y
b_normal = np.linalg.inv(XtX) @ Xty
b0, b1, b2 = b_normal

# D) Tuloste
print(f"Vakio: b0 = {b0:.3f}")
print(f"Kerroin x1:lle: b1 = {b1:.3f}")
print(f"kerroin x2:lle: b2 = {b2:.3f}")
print(f"Regressiomalli: y = {b0:.3f} + {b1:.3f}*x1 - {b2:.3f}*x2")