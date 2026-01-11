import pandas as pd

data = pd.read_csv("../diabetes.csv")

agesCount = data["Age"].value_counts()
print(agesCount)

outcomesCount = data["Outcome"].value_counts()
print(outcomesCount)