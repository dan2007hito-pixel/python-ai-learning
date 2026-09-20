import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

x = np.arange(10).reshape(-1,1)
y = np.array([0,0,0,0,1,1,1,1,1,1])

model = LogisticRegression(solver='liblinear', random_state=0)
model.fit(x, y)

print('Các lớp: ', model.classes_)
print('Hệ số cắt: ', model.intercept_)
print('Hệ số góc: ', model.coef_)

# y = ax + b
# y = Hệ số góc * x + Hệ số cắt
print(f"Phương trình đường thẳng y = {model.coef_[0][0]}x + {model.intercept_[0]}")

# Dự đoán nhãn
y_pred = model.predict(x)
print(y_pred)

# Dự đoán xác suất
p_pred = model.predict_proba(x)
print(p_pred)

# Độ chính xác
score_ = model.score(x, y)
print(score_*100 ,'%')

# Ma trận nhầm lẫn
conf_m = confusion_matrix(y, y_pred)
print(conf_m)

# Ma trận nhầm lẫn (Confusion Matrix)
# Hiệu suất của bộ phân loại được đánh giá bằng cách so sánh giá trị thực tế với giá trị dự đoán, tạo thành 
# 4 nhóm kết quả:
#  True Negatives (TN): Âm tính thật - Dự đoán đúng các trường hợp âm tính (0).
#  True Positives (TP): Dương tính thật - Dự đoán đúng các trường hợp dương tính (1).
#  False Negatives (FN): Âm tính giả - Dự đoán sai thành âm tính (0), đây là các trường hợp bỏ sót.
#  False Positives (FP): Dương tính giả - Dự đoán sai thành dương tính (1), đây là các trường hợp báo 
# động giả

# Các chỉ số đánh giá
#  Độ chính xác chung (Classification Accuracy): Chỉ số đơn giản nhất, là tỷ lệ giữa số dự đoán đúng (TP 
# + TN) trên tổng số dự đoán.
#  Độ chính xác dương tính (Precision / Positive Predictive Value): Tỷ lệ giữa dương tính thật trên 
# tổng số dự đoán dương tính (TP / (TP + FP)).
#  Độ nhạy (Recall / Sensitivity / True Positive Rate): Tỷ lệ giữa dương tính thật trên tổng số thực tế 
# dương tính (TP / (TP + FN)).
#  Độ đặc hiệu (Specificity / True Negative Rate): Tỷ lệ giữa âm tính thật trên tổng số thực tế âm tính 
# (TN / (TN + FP)).

report = classification_report(y, y_pred)
print(report)

print('------------------------------------------------------------------------------------------------')
# Step 1: Import thư viện
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# Step 2a: Tai dữ liệu
x_b, y_b = load_digits(return_X_y=True)
# print(np.array(x_b[1]).reshape(8,8))
# Step 2b: Chia tập dữ liệu (80% train, 20% test)
x_train, x_test, y_train, y_test = train_test_split(x_b, y_b, test_size=0.2, 
random_state=0)
# Step 2c: Chuấn hóa dữ liệu (Standardization: z = (x - µ) / σ)
scaler_b = StandardScaler()
x_train = scaler_b.fit_transform(x_train)
x_test = scaler_b.transform(x_test) # Chỉ transform trến tập test
# Step 3: Tạo và Huấn luyện mố hình (Phấn loại đa lớp OvR)
model_b = LogisticRegression(solver='lbfgs', C=0.05, 
random_state=0)
model_b.fit(x_train, y_train)
# Step 4: Đánh giá mố hình
y_pred = model_b.predict(x_test)
print('Train Accuracy:', model_b.score(x_train, y_train))
print('Test Accuracy:', model_b.score(x_test, y_test))
print('\nBáo cáo phấn loại:\n', classification_report(y_test, y_pred))