import numpy as np
arr=np.arange(15).reshape((3, 5))
print(arr)
print(arr.T) # Chuyen hanh thanh cot, cot thanh hang

arr=np.random.randn(6, 3)
print(arr)

print('--------------------------')
np.dot(arr.T, arr) #Nhân ma trận
arr=np.arange(16).reshape(2, 2, 4) 
print(arr)
# print(arr.transpose((1, 0, 2))) 
# Hoán đổi trục:
# (1,0) → đổi hàng ↔ cột (đối với mảng 2 chiều).
# (1,0,2) → đổi trục 0 và trục 1, trục 2 giữ nguyên.
# (2,1,0) → đưa trục 2 lên đầu, rồi đến trục 1, cuối cùng là trục 0.
print('--------------------------')
print(arr.swapaxes(1, 2)) #Đổi ngang thành dọc, dọc thành ngang
