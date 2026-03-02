import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np

# 1. Lataa aineisto pandas dataframeen
df = pd.read_csv('salary.csv')
print(df.head)

# 2. Tutustu dataan ja visualisoi pistepilvellä data, ja selvitä korrelaatio (työkokemus, palkka) ja p-arvo sekä visualisoi vielä heatmap korrelaatioista (työkokemus, palkka)
plt.figure()
plt.scatter(df['YearsExperience'], df['Salary'])
plt.xlabel('YearsExperience')
plt.ylabel('Salary')
plt.show()

corr, pval = stats.pearsonr(df["YearsExperience"], df["Salary"])
print(f"Korrelaatio: {corr}")
print(f"P-arvo: {pval}")

plt.figure()
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()

# 3. Jaa aineisto opetusdataan ja testidataan 70/30 suhteessa
X = df[["YearsExperience"]]
y = df["Salary"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

# 4. Opeta lineaarinen regressio -malli
model = LinearRegression()
model.fit(X_train, y_train)

coef = model.coef_[0]
intercept = model.intercept_

# 5. Tulosta suoran yhtälö
print(f"Suoran kerroin: {coef}")
print(f"Suoran vakio: {intercept}")
print(f"Suoran yhtälö: Salary = {coef} * YearsExperience + {intercept}")

# 6. Tee ennuste testidatalla
y_pred = model.predict(X_test)

# 7. Visualisoi testiaineiston tulokset pistepilven ja suoran sovituksen avulla
plt.figure()
plt.scatter(X_test, y_test, color="red")
plt.plot(X_test, y_pred)
plt.xlabel("Kokemus")
plt.ylabel("Palkka")
plt.title("Palkka vs kokemus (testidata)")
plt.show()

# 8. Luo seabornin regplot-visualisointi ja vertaa tulosta edelliseen visualisointiin
plt.figure()
sns.regplot(x=X_test["YearsExperience"], y=y_test)

# 9. Arvioi mallia käyttäen metriikoita: R2, MAE ja RMSE. Mitä mallista voidaan sanoa näiden metriikoiden perusteella?
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"MAE:  {mae:.6f}")
print(f"MSE:  {mse:.6f}")
print(f"RMSE: {rmse:.6f}")
print(f"R2:   {r2:.12f}")

# 10. Ennusta vielä kuvitteellisen työntekijän palkka 7v kokemuksella
salary_7 = model.predict(pd.DataFrame({"YearsExperience": [7]}))[0]
print(f"7 vuoden ennuste: {salary_7:.2f} €")