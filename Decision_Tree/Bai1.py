# Định nghĩa:
# Cây quyết định (Decision Tree) là một trong những thuật toán học máy có giám sát (Supervised 
# Learning) phổ biến và dễ hiểu nhất. Mục tiêu chính của nó là tạo ra một mô hình dự đoán giá trị 
# của biến mục tiêu bằng cách học các quy tắc quyết định đơn giản được rút ra từ các đặc trưng 
# dữ liệu.

# Cấu trúc của cây quyết định bao gồm:
# ● Gốc (Root Node): Nút trên cùng đại diện cho toàn bộ tập dữ liệu.
# ● Nút nhánh (Decision/Internal Node): Đại diện cho một câu hỏi/điều kiện phân tách dựa 
# trên một đặc trưng.
# ● Nhánh (Branch): Đại diện cho kết quả của điều kiện kiểm tra.
# ● Nút lá (Leaf/Terminal Node): Nút cuối cùng biểu diễn kết quả dự đoán (nhãn phân loại 
# hoặc giá trị số).

import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Features: [Tuổi, Thu nhập (triệu/tháng)]
X = np.array([
    [22, 10], [25, 12], [47, 35], [52, 40],
    [46, 15], [56, 50], [23, 20], [38, 25]
])
# Labels: 0 = Không mua, 1 = Mua
y = np.array([0, 0, 1, 1, 0, 1, 0, 1])

# Khởi tạo mô hình Decision Tree với chỉ số Gini và độ sâu tối đa = 3
model = DecisionTreeClassifier(criterion='gini', max_depth=3, 
random_state=42)

# Fit mô hình với dữ liệu
model.fit(X, y)
 
accuracy = model.score(X, y)
print('Accuracy:', accuracy)

X_new = np.array([[30, 18], [50, 30]])
y_pred = model.predict(X_new)
print('Predicted classes for new data:', y_pred)

print('-----------Phân loại rượu-------------')

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd

wine = load_wine()
# print(wine)

x = wine.data
y = wine.target
feature_names= wine.feature_names
target_names = wine.target_names

print(target_names)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print('y_pred: ', y_pred)
print('y_test: ', y_test)
print('Accurary: ', accuracy_score(y_test, y_pred))
print('Confusion Matrix: ', confusion_matrix(y_test, y_pred))
print('Classifision Repost: ', classification_report(y_test, y_pred))