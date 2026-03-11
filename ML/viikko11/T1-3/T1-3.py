import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import recall_score, precision_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('titanic-class-age-gender-survived.csv')
nans = df.isna().sum() #lasketaan puuttuvat arvot
survived = df['Survived'].value_counts()

#jataan X ja y
X = df.iloc[:, [0,1,2]]
y = df.iloc[:, [-1]] #viimeinen

#dummyt
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(drop='first'),
                                   ['PClass',
                                    'Gender'])],
                     remainder='passthrough')
X = ct.fit_transform(X)

#Jaa data opetus- ja testidataan (80 / 20 suhde)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
                                                    random_state=0)

#skaalaus
scaler_X = MinMaxScaler()
X_train = scaler_X.fit_transform(X_train)
X_test = scaler_X.transform(X_test)

#luodaan malli ja opetetaan se
model = LogisticRegression()
model.fit(X_train, y_train)

#ennusteet testidatalla
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)

#metriikat
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print('\nMetriikat')
print(f'cm: {cm}')
print(f'acc: {acc}')
print(f'precision: {precision}')
print(f'recall: {recall}')

sns.heatmap(cm, annot=True, fmt='g', cbar=False)
plt.show()

#ennustetaan kuvitteellisille matkustajille
Xnew = pd.read_csv('titanic-new.csv')
Xnew = ct.transform(Xnew)
Xnew = scaler_X.transform(Xnew)
y_new_pred = model.predict(Xnew)
y_new_proba = model.predict_proba(Xnew)