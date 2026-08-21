import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


print('---------------- Bài tập: California Housing ----------------')

print('---------------- Tải và xem dữ liệu ----------------')
housing = fetch_california_housing(as_frame=True)
data = housing.frame
print(data.head())

print('---------------- Chọn đặc trưng và biến mục tiêu ----------------')
features = data[['MedInc', 'HouseAge', 'AveRooms']]
target = data['MedHouseVal']

print('Các đặc trưng:')
print(features.head())
print('Biến mục tiêu:')
print(target.head())

print('---------------- Chia dữ liệu và huấn luyện ----------------')
x_train, x_test, y_train, y_test = train_test_split(
    features,
    target,
    test_size=0.3,
    random_state=77,
)

model = LinearRegression()
model.fit(x_train, y_train)

print('Hệ số của từng đặc trưng:')
print(pd.Series(model.coef_, index=features.columns))
print(f'Hệ số chặn: {model.intercept_:.4f}')

print('---------------- Đánh giá mô hình ----------------')
y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
r_squared = model.score(x_test, y_test)

print(f'Mean Squared Error (MSE) trên tập kiểm tra: {mse:.4f}')
print(f'R² trên tập kiểm tra: {r_squared:.4f}')
