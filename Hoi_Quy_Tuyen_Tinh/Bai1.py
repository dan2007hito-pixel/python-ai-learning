# Bài toán hồi quy phân loại các biến và dữ liệu thành các nhóm:
# Đặc trưng(Features): Là thuộc tính của hiện tượng đc quan sắt
# Quán sát(Observation): Là một tập hợp dữ liệu liên quan đến một đối tượng cụ thể(VD: Dữ liệu liên quan đến 1 nv duy nhất)
# Biến độc lập(Independent variables): Đầu vào(inputs), thường ký hiệu x, nếu nhiều biến thì biểu diễn dạng vectơ 
# Biến phụ thuộc(Dependent variables): Đầu ra (outputs), thường là 1 biến liên tục, ko bị giới hạn


# Khi nào cần đến hồi quy tuyến tính
# Xác định sự ảnh hưởng: Liệu 1 hiện tượng có ảnh hưởng đến hiện tượng khác hay ko và các biến có mối quan hệ với nhau như nào
# Đo lường mức độ tắc động: Định lượng mức độ tác động của các yếu tố khác nhau(VD: Kinh nghiệm hoặc giới tính ảnh hưởng bao nhiêu đến mức lương) 


# Các thành phần chính trong mô hình 

import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1,1))
y = np.array([5, 20, 14, 32, 22, 38])

# fit_intercept: Kiểu Boolean (mặc định là True), quyết định xem có tính toán hệ số cắt b₀ hay không (True) hoặc coi nó bằng 0 (False).
# normalize: Kiểu Boolean (mặc định là False), quyết định xem có chuẩn hóa các biến đầu vào hay không.
# copy_X: Kiểu Boolean (mặc định là True), quyết định xem có sao chép (True) hay ghi đè lên các biến đầu vào (False).
# n_jobs: Số nguyên hoặc None (mặc định), đại diện cho số lượng tác vụ sử dụng trong tính toán song song. None thường có nghĩa là 1 tác vụ và -1 có nghĩa là sử dụng tất cả các bộ xử lý.

model = LinearRegression()
model.fit(x, y)

print('Hệ số góc: ', model.coef_)
print('Hệ số cắt: ', model.intercept_)

r_sq = model.score(x, y)
print('Score: ', r_sq)

y_pred = model.predict(x)
print(y_pred)
