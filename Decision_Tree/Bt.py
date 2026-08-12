import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.metrics import mean_squared_error

diabetes = load_diabetes()

df= pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df['target'] = diabetes.target
x = df.drop('target', axis=1)
y = df['target']

print('---------1: ', df)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = DecisionTreeRegressor(criterion='squared_error', max_depth=5, random_state=42)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

score = model.score(x_test, y_test)
mse = mean_squared_error(y_test, y_pred)

print('Score: ', score)
print('MSE: ', mse)
