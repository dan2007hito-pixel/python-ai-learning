# ============================================================
# NUMPY - ÔN TẬP PHẦN 2: MA TRẬN, TRỤC, BIẾN ĐỔI MẢNG
# ============================================================

import numpy as np


# ============================================================
# 1. TRANSPOSE (.T)
# ============================================================

print("\n==================== 1. TRANSPOSE (.T) ====================")

arr = np.arange(15).reshape((3, 5))

print("Mảng ban đầu - shape (3, 5):")
print(arr)

print("\nMảng sau khi dùng .T - shape (5, 3):")
print(arr.T)

# .T: đổi hàng thành cột, cột thành hàng
# (3,5) -> (5,3)


# ============================================================
# 2. RANDOM
# ============================================================

print("\n==================== 2. RANDOM ====================")

arr = np.random.randn(6, 3)

print("Mảng ngẫu nhiên - shape (6, 3):")
print(arr)

print("\nShape của mảng:")
print(arr.shape)

# randn: tạo số ngẫu nhiên theo phân phối chuẩn
# Kích thước (6,3) = 6 dòng, 3 cột


# ============================================================
# 3. NHÂN MA TRẬN
# ============================================================

print("\n==================== 3. NHÂN MA TRẬN ====================")

print("arr.T:")
print(arr.T)

print("\narr:")
print(arr)

print("\nnp.dot(arr.T, arr) - Kết quả nhân ma trận:")
print(np.dot(arr.T, arr))

print("\nShape của kết quả:")
print(np.dot(arr.T, arr).shape)

# np.dot(): nhân ma trận
# arr.T có kích thước (3,6)
# arr có kích thước (6,3)
# Kết quả: (3,3)


# ============================================================
# 4. MẢNG NHIỀU CHIỀU
# ============================================================

print("\n==================== 4. MẢNG NHIỀU CHIỀU ====================")

arr = np.arange(16).reshape(2, 2, 4)

print("Mảng 3 chiều:")
print(arr)

print("\nShape:")
print(arr.shape)

print("\nSố chiều - ndim:")
print(arr.ndim)


# ============================================================
# 5. TRANSPOSE VỚI NHIỀU TRỤC
# ============================================================

print("\n==================== 5. TRANSPOSE VỚI NHIỀU TRỤC ====================")

print("Mảng ban đầu:")
print(arr)

print("\nShape ban đầu:")
print(arr.shape)

print("\narr.transpose((1, 0, 2)):")
print(arr.transpose((1, 0, 2)))

print("\nShape sau transpose((1, 0, 2)):")
print(arr.transpose((1, 0, 2)).shape)

# (1,0,2):
# - đổi trục 0 và trục 1
# - trục 2 giữ nguyên
#
# (2,1,0):
# - đưa trục 2 lên đầu
# - sau đó trục 1
# - cuối cùng trục 0


# ============================================================
# 6. SWAPAXES
# ============================================================

print("\n==================== 6. SWAPAXES ====================")

print("Mảng ban đầu:")
print(arr)

print("\nShape ban đầu:")
print(arr.shape)

print("\narr.swapaxes(1, 2):")
print(arr.swapaxes(1, 2))

print("\nShape sau swapaxes(1, 2):")
print(arr.swapaxes(1, 2).shape)

# Đổi trục 1 và trục 2
# Với mảng 3 chiều: trục 1 <-> trục 2


# ============================================================
# NHỚ NHANH
# ============================================================

print("\n============================================================")
print("                       NHỚ NHANH")
print("============================================================")

print(".T")
print("  -> transpose mảng 2D")
print("  -> đổi hàng thành cột, cột thành hàng")

print("\nnp.dot(A, B)")
print("  -> nhân ma trận")

print("\ntranspose((...))")
print("  -> sắp xếp lại thứ tự các trục")

print("\nswapaxes(i, j)")
print("  -> đổi 2 trục i và j")

print("\nnp.random.randn()")
print("  -> tạo số ngẫu nhiên theo phân phối chuẩn")
