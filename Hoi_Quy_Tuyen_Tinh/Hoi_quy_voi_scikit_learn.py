import numpy as np
from sklearn.linear_model import LinearRegression


print('---------------- Dữ liệu nhiều biến ----------------')
x = np.array([
    [0, 1],
    [5, 1],
    [15, 2],
    [25, 5],
    [35, 11],
    [45, 15],
    [55, 34],
    [60, 35],
])
y = np.array([4, 5, 20, 14, 32, 22, 38, 43])

print('Kích thước X:', x.shape)
print('Kích thước y:', y.shape)

print('---------------- Huấn luyện mô hình ----------------')
model = LinearRegression()
model.fit(x, y)

print(f'Hệ số chặn: {model.intercept_:.4f}')
print('Hệ số của từng đặc trưng:')
print(model.coef_)

print('---------------- Đánh giá và dự đoán ----------------')
r_squared = model.score(x, y)
print(f'R² trên tập dữ liệu mẫu: {r_squared:.4f}')

x_new = np.arange(10).reshape(-1, 2)
y_new = model.predict(x_new)
print('Dữ liệu mới:')
print(x_new)
print('Giá trị dự đoán:')
print(y_new)
