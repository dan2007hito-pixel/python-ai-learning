from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

housing = fetch_california_housing()

x = housing.data
y = housing.target

print("Shape: ")
print(x.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
x_train_scaler = scaler.fit_transform(x_train)
x_test_scaler = scaler.transform(x_test)

model = LinearRegression()

model.fit(x_train_scaler, y_train)
print("B0: ", model.intercept_)
print("B1->B8: ", model.coef_)

y_pred = model.predict(x_test)

rmse = np.sqrt(np.mean((y_test - y_pred)**2))

my_input = [[7.0, 54.0, 8.1, 1.0, 450.0, 3.0, 37.0, -122.0]]
my_new_input = scaler.transform(my_input)
my_new_output = model.predict(my_new_input)
print("Output: ",my_new_output)