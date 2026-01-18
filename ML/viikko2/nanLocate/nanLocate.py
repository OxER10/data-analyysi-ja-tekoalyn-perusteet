import pandas as pd

data = pd.read_csv("../diabetes.csv")

nans = data.isnull().sum()
print("NaN-arvot sarakkeittain: ")
print(nans)

nanSum = data.isnull().sum().sum()
print(f"NaN-arvot yhteensä: {nanSum}")


