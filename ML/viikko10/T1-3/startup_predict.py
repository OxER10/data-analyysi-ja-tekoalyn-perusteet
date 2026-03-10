import pandas as pd
import pickle
 
# T3
# ladataan malli levyltä
with open ('startup-model.pickle', 'rb') as f:
    model = pickle.load(f)

with open ('startup-ct.pickle', 'rb') as f:
    ct = pickle.load(f)

with open ('startup-X_scaler.pickle', 'rb') as f:
    X_scaler = pickle.load(f)

with open ('startup-y_scaler.pickle', 'rb') as f:
    y_scaler = pickle.load(f)
 
Xnew = pd.read_csv('new_company_ct.csv')
Xnew_org = Xnew.copy()
 
#muunnokset
Xnew = ct.transform(Xnew)
Xnew = X_scaler.transform(Xnew)
 
# ennusta ja aja inverse scaler
ynew = y_scaler.inverse_transform(model.predict(Xnew))

#T2 (B)
for i in range (len(ynew)):
    print (f'\n{Xnew_org.iloc[i]}\nVoitto: {ynew[i][0]}\n')

df = pd.read_csv('startup.csv')

print("\nEnnustettu Profit (get_dummies):")
print(ynew[0][0])

actual_profit_d = df["Profit"].values
print("\nTodellinen Profit:")
print(actual_profit_d[0])

print("\nErotus (todellinen - ennuste):")
print(actual_profit_d[0] - ynew[0][0])

print('\nEnnustus toimii luotettavasti.')