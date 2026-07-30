import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(a)
# print(a[:]) # Lấy hết

# print(a[1]) # Theo vị trí
# print(a[[0, 2]]) 

# print(a[-1]) # Cuối cùng
# print(a[:2]) # Lấy số luợng phần tử 

# print(a[2][1]) # Lấy trong mảng 2, vị trí 1
# print(a[2, 1]) # Giống cái trên

# print(a[1:, 1:]) # Lấy các phần tử của các mảng từ 1 và lấy phần tử có vị trí từ 1

arr = np.arange(100) # Tao 1 mang co 100 phan tu bat dau tu 0
# arrMask = ((arr % 5) == 0) # Chia het cho 5 thi true
# arrMask = (((arr % 5) == 0) & (arr > 0)) # Thêm điều kiện
# print(arr[arrMask]) #Lấy các phần tử vị trí true

test_a = np.array([1, 4, 0, 2, 3, 8, 9, 7])
# print(test_a > 3) # Thêm đk, trả về true, false
