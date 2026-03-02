import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np

# 1. Lataa aineisto pandas dataframeen
df = pd.read_csv('housing.csv')
print(df.head)

# 2. Tutustu dataan ja visualisoi pistepilvellä data, ja selvitä korrelaatio (työkokemus, palkka) ja p-arvo sekä visualisoi vielä heatmap korrelaatioista (työkokemus, palkka)
plt.figure()
plt.scatter(df['median_house_value'], df['median_income'], alpha=0.4)
plt.xlabel("Kotitalouden vuositulot (Kymmeniä tuhansia dollareita")
plt.ylabel("Talon mediaaniarvo")
plt.show()

# 3. Jaa aineisto opetusdataan ja testidataan 70/30 suhteessa
X = df[['median_income']]
y = df['median_house_value']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# 4. Opeta lineaarinen regressio -malli
model = LinearRegression()
model.fit(X_train, y_train)

coef = model.coef_[0]
intercept = model.intercept_

# 5. Tulosta suoran yhtälö
print(f"Suoran kerroin: {coef}")
print(f"Suoran vakio: {intercept}")
print(f"Suoran yhtälö: Median income = {coef} * Median house value + {intercept}")

# 6. Tee ennuste testidatalla
y_pred = model.predict(X_test)

# 7. Visualisoi testiaineiston tulokset pistepilven ja suoran sovituksen avulla
errors = y_test - y_pred

plt.figure()
plt.hist(errors, bins=40)
plt.title("Ennustevirheet (todellinen - ennustettu)")
plt.xlabel("Virhe (dollaria)")
plt.ylabel("Frekvenssi")
plt.show()

# 8. Arvioi mallia käyttäen metriikoita: R2, MAE ja RMSE. Mitä mallista voidaan sanoa näiden metriikoiden perusteella?
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"MAE:  {mae:.6f}")
print(f"MSE:  {mse:.6f}")
print(f"RMSE: {rmse:.6f}")
print(f"R2:   {r2:.12f}")

print("Tulkinta:")
if r2 > 0.7:
    print("Malli selittää suuren osan vaihtelusta, lineaarinen malli toimii kohtuullisen hyvin.")
elif r2 > 0.4:
    print("Mallilla on kohtalainen selitysvoima, mutta parempia malleja olisi saatavilla.")
else:
    print("Lineaarinen malli ei kuvaa ilmiötä kovin hyvin.")

# 10. Ennusta vielä kuvitteellisen työntekijän palkka 7v kokemuksella
income_30 = model.predict(pd.DataFrame({"median_income": [3.0]}))[0]
print(f"Kotitalouden ennustettu talon arvo 30 000 dollarin tuloilla: {income_30:.2f} €")