'''
Author ~ Raunak Joshi
'''
import pandas as pd

data = pd.read_csv('./titanic.csv')

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse_output=False, dtype=int)
data[['female', 'male']] = ohe.fit_transform(data[['Sex']])

data = data.dropna()
# print(data.head())
# data.isnull().values.any()

X = data[['Pclass', 'Age', 'female', 'male']]
y = data['Survived']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

from joblib import dump

dump(model, 'model.joblib')