import pandas as pd
import matplotlib.pyplot as plt

# T3
df_titanic_data = pd.read_csv("Titanic_data.csv")
df_titanic_names = pd.read_csv("Titanic_names.csv")

print(df_titanic_data.info())
print(df_titanic_data.describe())
print(df_titanic_names.info())
print(df_titanic_names.head())

df_titanic_data.hist(bins=4, figsize=(10, 6))
plt.suptitle("Titanic (bins=4)")
plt.tight_layout()
plt.show()

df = pd.merge(df_titanic_data, df_titanic_names, how="inner", on="id")
print(df.head())

print("\nHenkilöitä yhteensä:")
print(len(df))

print("\nMiehiä (Gender=='male'):")
print((df["Gender"] == "male").sum())

print("\nNaisia (Gender=='female'):")
print((df["Gender"] == "female").sum())

print("\nMatkustajien keski-ikä (sis. nollaikäiset):")
print(df["Age"].mean())

print("\nNollan ikäisiä matkustajia (Age==0):")
print((df["Age"] == 0).sum())

# T4
nonzero_mean_age = df.loc[df["Age"] > 0, "Age"].mean()
print("\nEi-nollaikäisten keski-ikä:")
print(nonzero_mean_age)

df.loc[df["Age"] == 0, "Age"] = nonzero_mean_age

print("\nTarkistus: montako Age==0 päivityksen jälkeen?")
print((df["Age"] == 0).sum())

print("\nPClass – uniikit arvot:")
print(df["PClass"].unique())

print("\nRivit, joilla PClass == '*':")
rows_star = df[df["PClass"] == "*"]
print(rows_star[["id", "Name", "PClass"]])

print("\nSelviytyneet (1) ja ei-selviytyneet (0) – lukumäärät:")
surv_counts = df["Survived"].value_counts().sort_index()
print(surv_counts)

print("\nSelviytyneet (1) ja ei-selviytyneet (0) – prosentit (%):")
surv_pct = df["Survived"].value_counts(normalize=True).sort_index() * 100
print(surv_pct.round(1))

print("\nSelviytyminen sukupuolen mukaan – ristikointi (lukumäärät):")
print(pd.crosstab(df["Gender"], df["Survived"]))

print("\nSelviytyminen sukupuolen mukaan – prosentit (% rivi):")
print(pd.crosstab(df["Gender"], df["Survived"], normalize="index").round(3) * 100)