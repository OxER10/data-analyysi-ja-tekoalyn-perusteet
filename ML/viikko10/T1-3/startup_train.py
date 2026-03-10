import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler

#T1
#1. lataa aineisto pandas dataframeen
df = pd.read_csv('startup.csv')

#2. luo X ja y datasetit
X = df.iloc[:,:-1]
y = df.iloc[:,[-1]]

X_org = X.copy()

#3. rakenna dummy-muuttujat State sarakkeesta
#tee kaksi ratkaisua: get_dummies ja ColumnTransformer&OneHotEncoder
#Ratkaisu 1.
dummies = pd.get_dummies(X, columns=['State'], drop_first=True)

#Ratkaisu 2.
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(drop='first'), ['State'])], remainder='passthrough')

X = ct.fit_transform(X)

#4. jaa data opetusdataan (80 %) ja testidataan (20 %)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

#Skaalataan data
X_scaler = MinMaxScaler()
X_train = X_scaler.fit_transform(X_train)
X_test = X_scaler.transform(X_test)

y_scaler = MinMaxScaler()
y_train = y_scaler.fit_transform(y_train)

#5. opeta malli opetusdatalla
model = LinearRegression()
model.fit(X_train, y_train)

#6. mikä on suoran yhtälö?
coef = model.coef_
inter = model.intercept_

clean_names = ct.get_feature_names_out()

print('\nVakiotermi:')
print(model.intercept_)

print('\nYhtälö:')
print(f'Profit = {model.intercept_} '
      f'+ ({model.coef_[0][0]:.4f} * {clean_names[0]}) '
      f'+ ({model.coef_[0][1]:.4f} * {clean_names[1]}) '
      f'+ ({model.coef_[0][2]:.4f} * {clean_names[2]}) '
      f'+ ({model.coef_[0][3]:.4f} * {clean_names[3]}) '
      f'+ ({model.coef_[0][4]:.4f} * {clean_names[4]})')

#7. tee ennusteet testidatalla
y_pred = y_scaler.inverse_transform(model.predict(X_test))

comparison = pd.DataFrame({
    'Todellinen': y_test.values.flatten(),
    'Ennustettu': y_pred.flatten()
})

print('\nTodelliset ja ennustetut arvot:')
print(comparison.head(10))

#8. laske metriikat (R2, MAE ja RMSE)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print('\nMetriikka:')
print(f'mae: {mae}')
print(f'mse: {mse}')
print(f'rmse: {rmse}')
print(f'R2: {r2}')

#9. miten malli suoriutuu?
print('\nTulkinta:')
if r2 > 0.7:
    print('Malli selittää suuren osan vaihtelusta, lineaarinen malli toimii kohtuullisen hyvin.')
elif r2 > 0.4:
    print('Mallilla on kohtalainen selitysvoima, mutta parempia malleja olisi saatavilla.')
else:
    print('Lineaarinen malli ei kuvaa ilmiötä kovin hyvin.')
    
#T2 dummies osio ennustus
dummy_columns = dummies.columns

new_company = pd.read_csv('new_company.csv')
X_new_d = new_company.copy()

X_new_d.reindex(columns=dummy_columns, fill_value=0)

new_pred_d = y_scaler.inverse_transform(model.predict(X_new_d.values))

print("\nEnnustettu Profit (get_dummies):")
print(new_pred_d)

actual_profit_d = df["Profit"].values
print("\nTodellinen Profit:")
print(actual_profit_d[0])

print("\nErotus (todellinen - ennuste):")
print(actual_profit_d[0] - new_pred_d[0])

print('\nEnnustus ei toimi luotettavasti, kun sekoitetaan ct ja dummy keskenään.')

#T3
#Tallennetaan malli ja enkooderi picklellä
with open('startup-model.pickle', 'wb') as f:
    pickle.dump(model, f)
    
with open('startup-ct.pickle', 'wb') as f:
    pickle.dump(ct, f)
    
with open('startup-X_scaler.pickle', 'wb') as f:
    pickle.dump(X_scaler, f)
    
with open('startup-y_scaler.pickle', 'wb') as f:
    pickle.dump(y_scaler, f)