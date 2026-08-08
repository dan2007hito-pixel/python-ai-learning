# Học máy: Mô hình thống kê có thể "Học" từ dữ liệu
# 1 mô hình đơn giản có thể đưa ra những dự đoán phức tạp
#-----------------------------------------------------------------------------
#VD
#  Định nghĩa toán học

# • Giả sử trục x thể hiện chi phí đầu tư cho quảng cáo trong khi y là doanh số bán hàng.

# • Câu hỏi về dự đoán - Doanh số bán hàng là bao nhiêu khi chi phí quảng cáo như thế nào được đưa ra?

# • Hồi quy tuyến tính
#   • w và b làm tham số
#         y = wx + b
#   • 'w' thường được sử dụng như một từ viết tắt của "trọng số - weigh".

# • Vì giá trị tối ưu chưa được biết ngay từ đầu, hãy bắt đầu với một giá trị tùy ý và sau đó đạt được giá trị tối ưu bằng cách đánh dấu dần dần cao hiệu suất sau.

#   - Từ biểu đồ, bắt đầu từ f1 để tiếp tục là f1 → f2 → f3.
#   - Giá trị tối ưu là f3 trong đó w = 0.5 và b = 2.
#-----------------------------------------------------------------------------

# Các loại học máy
# - Có giám sát: Thông tin đối tượng đc cho trước(Gắn nhãn)
# - Không giám sát: Chưa đc gán nhãn, cần được xác định
# - Tăng cường: Học theo phương pháp thưởng phạt

#-----------------------------------------------------------------------------

# Quy trình tiến hành học máy
# • Hiểu và định nghĩa được vấn đề
#   → Định nghĩa vấn đề

# • Tiền xử lý và tìm kiếm dữ liệu
#   → Chuẩn bị dữ liệu
#   → Thu thập dữ liệu
#   → Dữ liệu thô

# • Học máy
#   → Huấn luyện
#   → Xác nhận
#   → Kiểm tra

# • Trích chọn đặc trưng
#   ↕
#   Tạo mẫu và tối ưu
#   ↓
#   Chỉ số hiệu năng
#   → Dữ liệu huấn luyện mô hình
#   → Đánh giá hiệu năng của mô hình

# • Nâng cao hiệu suất mô hình
#   và
#   Ứng dụng vào thực tế

#-----------------------------------------------------------------------------

# Học máy không giám sát: Cụm, MDS, t-SNE, PCA, NMF, Phân tích cụm.
# Học máy có giám sát: Hồi quy tuyến tính, Hồi quy Logistic, Cây, Rừng ngẫu nhiên, AdaBoost, XGBoost, Naive Bayes, KNN, Support Vector Machine (SVM), Mạng Nơ-ron.

#-----------------------------------------------------------------------------

# Cơ chế của scikit-learn
#Instance -> Fit -> Predict / transform

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

data = load_breast_cancer()

df = pd.DataFrame(data['data'])
label = pd.DataFrame(data['target'])
# print(label)
# print(df)

# help(train_test_split)
x_train, x_test, y_train, y_test = train_test_split(data['data'], data['target'], random_state=42) 
# print(x_test)

model = DecisionTreeClassifier(criterion='entropy')
model.fit(x_train, y_train)
# print(
# model.score(x_test, y_test))

y_pred = model.predict(x_test)
# print(y_pred)
# print(y_test)
y_pred_2d = y_pred.reshape(len(y_pred),1)
y_test_2d = y_test.reshape(len(y_test),1)

df1 = pd.DataFrame(y_pred_2d, columns=['pred'])
df2 = pd.DataFrame(y_pred_2d, columns=['real'])

df_concat = pd.concat([df1, df2], axis=1)
# df_concat[df_concat['pred'] == df_concat['real']]

# print(y_pred_2d)
print(df1)
print(df2)

print(df_concat[df_concat['pred'] == df_concat['real']].shape[0] / df_concat.shape[0])

