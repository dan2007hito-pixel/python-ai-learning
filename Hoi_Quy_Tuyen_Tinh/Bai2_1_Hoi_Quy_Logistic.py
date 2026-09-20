# HỒI QUY LOGISTIC TRONG PYTHON

# 1. IMPORT THƯ VIỆN
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_digits


# ============================================================
# PHẦN 1 - PHÂN LOẠI (CLASSIFICATION)
# ============================================================
#
# Hồi quy (Regression):
#   - Dự đoán một giá trị số liên tục.
#   - Ví dụ: dự đoán mức lương = 15 triệu.
#
# Phân loại (Classification):
#   - Dự đoán một lớp/nhóm.
#   - Ví dụ:
#       0 = Không mua
#       1 = Có mua
#
# Phân loại nhị phân:
#   Chỉ có 2 lớp: 0/1, Đúng/Sai, Có/Không
#
# Phân loại đa lớp:
#   Có từ 3 lớp trở lên: 0,1,2,...9


# ============================================================
# PHẦN 2 - HÀM SIGMOID
# ============================================================
#
# Sigmoid biến một giá trị bất kỳ thành số nằm trong khoảng 0 -> 1.
#
# Công thức:
#       sigmoid(x) = 1 / (1 + e^(-x))
#
# Trong Logistic Regression:
#       p = sigmoid(f(x))
#
# p được hiểu là xác suất dự đoán y = 1.

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x_sigmoid = np.linspace(-10, 10, 100)
y_sigmoid = sigmoid(x_sigmoid)

plt.plot(x_sigmoid, y_sigmoid)
plt.xlabel("x")
plt.ylabel("sigmoid(x)")
plt.title("Hàm Sigmoid")
plt.grid()
plt.show()


# ============================================================
# PHẦN 3 - CẤU TRÚC TOÁN HỌC CỦA LOGISTIC REGRESSION
# ============================================================
#
# Bước 1: Tính hàm tuyến tính (Logit)
#
# Với 1 biến:
#       f(x) = b0 + b1*x
#
# Với nhiều biến:
#       f(x) = b0 + b1*x1 + b2*x2 + ... + br*xr
#
# Bước 2: Đưa f(x) qua Sigmoid
#
#       p(x) = 1 / (1 + exp(-f(x)))
#
# p(x) nằm trong khoảng 0 -> 1.
#
# Mặc định:
#       p > 0.5  -> dự đoán 1
#       p <= 0.5 -> dự đoán 0
#
# Ví dụ:
#       f(x) = -3 + 2*x
#       x = 5
#
#       f(x) = -3 + 2*5 = 7
#       p(x) = sigmoid(7) ≈ 0.999
#
#       0.999 > 0.5
#       => dự đoán 1


f = -3 + 2 * 5
p = sigmoid(f)

print("Ví dụ Sigmoid:")
print("f(x) =", f)
print("p(x) =", p)
print("Dự đoán =", 1 if p > 0.5 else 0)


# ============================================================
# PHẦN 4 - LOG-LIKELIHOOD
# ============================================================
#
# Logistic Regression tìm các hệ số b0, b1,... sao cho
# xác suất dự đoán gần với kết quả thực tế.
#
# Công thức Log-Likelihood:
#
# LLF = sum(
#       y * log(p)
#       + (1-y) * log(1-p)
# )
#
# Nếu y = 1:
#       muốn p gần 1.
#
# Nếu y = 0:
#       muốn p gần 0.
#
# Trong sklearn, ta không cần tự tính LLF để huấn luyện.
# model.fit() sẽ thực hiện quá trình tối ưu.


# ============================================================
# PHẦN 5 - CONFUSION MATRIX
# ============================================================
#
# Sau khi dự đoán, có 4 trường hợp:
#
# TP (True Positive):
#   Thực tế 1, dự đoán 1 -> đúng
#
# TN (True Negative):
#   Thực tế 0, dự đoán 0 -> đúng
#
# FP (False Positive):
#   Thực tế 0, dự đoán 1 -> báo động giả
#
# FN (False Negative):
#   Thực tế 1, dự đoán 0 -> bỏ sót
#
# Accuracy  = (TP + TN) / Tổng
#
# Precision = TP / (TP + FP)
#
# Recall    = TP / (TP + FN)
#
# Specificity = TN / (TN + FP)


# Ví dụ theo tài liệu:
TP = 8
TN = 85
FN = 2
FP = 5

accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP)
recall = TP / (TP + FN)
specificity = TN / (TN + FP)

print("\nCác chỉ số đánh giá:")
print("Accuracy  =", accuracy)
print("Precision =", precision)
print("Recall    =", recall)
print("Specificity =", specificity)


# ============================================================
# PHẦN 6 - LOGISTIC REGRESSION ĐƠN BIẾN
# ============================================================
#
# Chỉ có 1 biến đầu vào.
#
# Ví dụ:
# x = số lần xuất hiện từ "Khuyến mãi"
# y = 0 (không spam), 1 (spam)

x = np.arange(10).reshape(-1, 1)

y = np.array([
    0, 0, 0, 0,
    1, 1, 1, 1, 1, 1
])

model = LogisticRegression(
    solver="liblinear",
    random_state=0
)

model.fit(x, y)

print("\n--- Logistic Regression đơn biến ---")
print("Các lớp:", model.classes_)
print("Hệ số cắt b0:", model.intercept_)
print("Hệ số b1:", model.coef_)

# Xác suất dự đoán
p_pred = model.predict_proba(x)

# Nhãn dự đoán
y_pred = model.predict(x)

# Accuracy
score = model.score(x, y)

# Confusion Matrix
conf_m = confusion_matrix(y, y_pred)

# Classification Report
report = classification_report(y, y_pred)

print("\nXác suất dự đoán:")
print(p_pred)

print("\nNhãn dự đoán:")
print(y_pred)

print("\nAccuracy:")
print(score)

print("\nConfusion Matrix:")
print(conf_m)

print("\nClassification Report:")
print(report)


# ============================================================
# PHẦN 7 - THAM SỐ C
# ============================================================
#
# C là cường độ nghịch đảo của chuẩn hóa.
#
# C nhỏ:
#   -> chuẩn hóa mạnh hơn
#   -> hạn chế mô hình quá phức tạp
#
# C lớn:
#   -> chuẩn hóa yếu hơn
#   -> mô hình được phép khớp dữ liệu mạnh hơn
#
# Thử C = 10

model_c10 = LogisticRegression(
    solver="liblinear",
    C=10.0,
    random_state=0
)

model_c10.fit(x, y)

print("\n--- Mô hình C = 10 ---")
print("Accuracy:", model_c10.score(x, y))
print("Confusion Matrix:")
print(confusion_matrix(y, model_c10.predict(x)))

print("Classification Report:")
print(classification_report(y, model_c10.predict(x)))


# ============================================================
# PHẦN 8 - DỮ LIỆU CÓ NHIỄU
# ============================================================
#
# Dữ liệu:
# tại x = 1 có y = 1, trong khi xu hướng chung chưa hoàn toàn
# theo một đường phân chia rõ ràng.
#
# Logistic Regression vẫn tìm một ranh giới phù hợp.

x_noise = np.arange(10).reshape(-1, 1)

y_noise = np.array([
    0, 1, 0, 0,
    1, 1, 1, 1, 1, 1
])

model_noise = LogisticRegression(
    solver="liblinear",
    C=10.0,
    random_state=0
)

model_noise.fit(x_noise, y_noise)

y_pred_noise = model_noise.predict(x_noise)

print("\n--- Dữ liệu có nhiễu ---")
print("Accuracy:", model_noise.score(x_noise, y_noise))
print("Confusion Matrix:")
print(confusion_matrix(y_noise, y_pred_noise))
print("Classification Report:")
print(classification_report(y_noise, y_pred_noise))


# ============================================================
# PHẦN 9 - LOGISTIC REGRESSION ĐA BIẾN
# ============================================================
#
# Khi có nhiều biến đầu vào:
#
#       f(x) = b0 + b1*x1 + b2*x2 + ... + br*xr
#
# Ví dụ:
# x1 = tuổi
# x2 = mức lương
#
# y = mua hàng hay không
#
# Trong Python:
#
# X = data[["Age", "EstimatedSalary"]]
# y = data["Purchased"]
#
# model.fit(X, y)


# ============================================================
# PHẦN 10 - CHUẨN HÓA DỮ LIỆU
# ============================================================
#
# Khi các đặc trưng có thang đo rất khác nhau, nên chuẩn hóa.
#
# Công thức:
#
#       z = (x - mean) / standard_deviation
#
# StandardScaler thực hiện việc này.
#
# QUAN TRỌNG:
#   scaler.fit_transform(X_train)
#   scaler.transform(X_test)
#
# Không fit lại trên X_test.


# ============================================================
# PHẦN 11 - PHÂN LOẠI ĐA LỚP: NHẬN DẠNG CHỮ SỐ
# ============================================================
#
# Dataset load_digits:
#   - 1,797 ảnh
#   - ảnh 8 x 8 pixel
#   - 64 đặc trưng
#   - 10 lớp: 0 -> 9
#
# Đây là bài toán phân loại đa lớp.

x_digits, y_digits = load_digits(return_X_y=True)

# Chia 80% train, 20% test
x_train, x_test, y_train, y_test = train_test_split(
    x_digits,
    y_digits,
    test_size=0.2,
    random_state=0
)

# Chuẩn hóa
scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Logistic Regression đa lớp
model_digits = LogisticRegression(
    solver="liblinear",
    C=0.05,
    multi_class="ovr",
    random_state=0
)

model_digits.fit(x_train, y_train)

# Dự đoán
y_pred_digits = model_digits.predict(x_test)

print("\n--- Nhận dạng chữ số ---")
print("Train Accuracy:", model_digits.score(x_train, y_train))
print("Test Accuracy:", model_digits.score(x_test, y_test))

print("\nClassification Report:")
print(classification_report(y_test, y_pred_digits))


# ============================================================
# PHẦN 12 - TÓM TẮT QUY TRÌNH LOGISTIC REGRESSION
# ============================================================
#
# Bước 1:
#   Chuẩn bị X và y
#
# Bước 2:
#   Chia train/test nếu có dữ liệu thực tế
#
# Bước 3:
#   Chuẩn hóa X nếu cần
#
# Bước 4:
#   Tạo LogisticRegression()
#
# Bước 5:
#   model.fit(X_train, y_train)
#
# Bước 6:
#   model.predict(X_test)
#
# Bước 7:
#   model.predict_proba(X_test)
#
# Bước 8:
#   Đánh giá bằng:
#       Accuracy
#       Precision
#       Recall
#       Confusion Matrix
#       Classification Report