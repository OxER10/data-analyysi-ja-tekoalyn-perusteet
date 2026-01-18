import pandas as pd

data = pd.read_csv("../diabetes.csv")

print("Count:")
print(data.count())
print("Mean:")
print(data.mean())
print("Min:")
print(data.min())
print("Max:")
print(data.max())
print("Std:")
print(data.std())

histogram = data.hist()