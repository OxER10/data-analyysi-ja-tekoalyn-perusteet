import numpy as np

X = np.array([[1.0, 1.0], [1.5, 2.0]])
y = np.array([[2.0], [-3.0]])

XtX_inv = np.array([[20.0, -16.0], [-16.0, 13.0]])

Xty = X.T @ y

b = XtX_inv @ Xty

print(b)