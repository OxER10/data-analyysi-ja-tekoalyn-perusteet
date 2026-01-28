import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# T1
employees = pd.read_csv("employees.csv", sep=",")
departments = pd.read_csv("departments.csv", sep=",")

print(employees.describe())
print(employees.info())
print(employees.isnull().sum())
print(employees.nunique())
print(employees.nlargest(5, "salary"))
print(employees.nsmallest(5, "salary"))

print(departments.describe())
print(departments.info())
print(departments.isnull())
print(departments.nunique())
print(departments.nlargest(3, "dep"))
print(departments.nsmallest(3, "dep"))

df = pd.merge(employees, departments, how="inner", on="dep")

df = df.drop(columns=["image"])

# T2
print("\nTyöntekijöiden määrä:")
print(len(employees))

print("\nMiesten määrä:")
print(len(employees[employees["gender"] == 0]))

print("\nNaisten määrä:")
print(len(employees[employees["gender"] == 1]))

male_pct = employees["gender"].value_counts(normalize=True).get(0, 0) * 100
female_pct = employees["gender"].value_counts(normalize=True).get(1, 0) * 100

print("\nMiesten osuus (%):")
print(f"{male_pct:.1f}")

print("\nNaisten osuus (%):")
print(f"{female_pct:.1f}")

print("\nPalkan minimi, maksimi ja keskiarvo:")
print(employees["salary"].min())
print(employees["salary"].max())
print(employees["salary"].mean())

print("\nTuotekehityksen osaston keskipalkka:")
print(employees[employees["dep"] == 4]["salary"].mean())

print("\nMonelta puuttuu kakkospuhelin:")
print(employees["phone2"].isnull().sum())

employees["age"] = 2026 - pd.to_datetime(employees["bdate"]).dt.year

print("\nIkä-sarakkeen alku:")
print(employees[["bdate", "age"]].head())

employees["age_group"] = ( (employees["age"] // 5) * 5 ) + 5

print("\nIkäryhmät ensimmäisiltä riveiltä:")
print(employees[["age", "age_group"]].head())

corr_df = employees[["salary", "age", "gender"]]

plt.figure(figsize=(6,4))
sns.heatmap(corr_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Korrelaatiomatriisi:")
plt.show()
