import numpy as np
from sklearn.linear_model import LinearRegression


# Hồi quy tuyến tính dùng để dự đoán một biến liên tục dựa trên một hoặc nhiều
# biến đầu vào.
#
# - Đặc trưng (features): các thuộc tính đầu vào, thường ký hiệu là X.
# - Quan sát (observations): các bản ghi dữ liệu.
# - Biến độc lập: các biến đầu vào.
# - Biến phụ thuộc: giá trị cần dự đoán, thường ký hiệu là y.


print('---------------- Dữ liệu mẫu ----------------')
x = np.array([5, 15, 25, 35, 45, 55]).reshape(-1, 1)
y = np.array([5, 20, 14, 32, 22, 38])

print('X:')
print(x)
print('y:')
print(y)

print('---------------- Huấn luyện mô hình ----------------')
# fit_intercept=True (mặc định) để mô hình tự tính hệ số chặn.
model = LinearRegression()
model.fit(x, y)

print(f'Hệ số góc: {model.coef_[0]:.4f}')
print(f'Hệ số chặn: {model.intercept_:.4f}')

print('---------------- Đánh giá và dự đoán ----------------')
r_squared = model.score(x, y)
y_pred = model.predict(x)

print(f'R² trên tập dữ liệu mẫu: {r_squared:.4f}')
print('Giá trị dự đoán:')
print(y_pred)
