from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd

print('-----------------------------------------------B1-----------------------------------------------')
print('-------------C1-------------')
hourt = fetch_california_housing(as_frame=True)
df = hourt.frame
print(hourt)

print('-------------C2-------------')
x = df[['MedInc', 'HouseAge', 'AveRooms']]
y = df['MedHouseVal']
print(x)
print(y)

print('-------------C3-------------')
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=77)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)

print(f"Hệ số góc (Coeff): {model.coef_[0]:.4f}")
print(f"Hệ số tự do (Intercept): {model.intercept_:.4f}")
print(f"Mean Squared Error (MSE) trên tập Test: {mse:.4f}")

# print('-----------------------------------------------B2-----------------------------------------------')

