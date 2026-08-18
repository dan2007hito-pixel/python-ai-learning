# ============================================================
# NUMPY - ÔN TẬP PHẦN 1: CƠ BẢN
# ============================================================

import numpy as np


# ============================================================
# 1. TẠO MẢNG
# ============================================================

print("\n==================== 1. TẠO MẢNG ====================")

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print("a =")
print(a)

arr = np.arange(10)
print("\nnp.arange(10):")
print(arr)

arr = np.arange(2, 10, 2)
print("\nnp.arange(2, 10, 2):")
print(arr)

arr = np.linspace(1, 10, 5)
print("\nnp.linspace(1, 10, 5):")
print(arr)

zeros = np.zeros(5)
print("\nnp.zeros(5):")
print(zeros)

ones = np.ones((2, 3))
print("\nnp.ones((2, 3)):")
print(ones)


# ============================================================
# 2. THUỘC TÍNH
# ============================================================

print("\n==================== 2. THUỘC TÍNH ====================")

print("a.size  =", a.size)       # Tổng số phần tử
print("a.shape =", a.shape)      # Kích thước (dòng, cột)
print("a.ndim  =", a.ndim)       # Số chiều
print("a.dtype =", a.dtype)      # Kiểu dữ liệu


# ============================================================
# 3. INDEXING / SLICING
# ============================================================

print("\n==================== 3. INDEXING / SLICING ====================")

print("a[:] - Tất cả:")
print(a[:])

print("\na[1] - Dòng index 1:")
print(a[1])

print("\na[[0, 2]] - Dòng 0 và dòng 2:")
print(a[[0, 2]])

print("\na[-1] - Dòng cuối:")
print(a[-1])

print("\na[:2] - Dòng 0, 1:")
print(a[:2])

print("\na[2, 1] - Dòng 2, cột 1:")
print(a[2, 1])

print("\na[1:, 1:] - Từ dòng 1, cột 1 đến cuối:")
print(a[1:, 1:])

# Công thức slicing:
# a[start:stop]
# stop KHÔNG lấy


# ============================================================
# 4. RESHAPE
# ============================================================

print("\n==================== 4. RESHAPE ====================")

arr = np.arange(15)

print("Mảng ban đầu:")
print(arr)

print("\narr.reshape(3, 5):")
print(arr.reshape(3, 5))

print("\narr.reshape(3, -1):")
print(arr.reshape(3, -1))

print("\narr.reshape(3, 5).copy():")
print(arr.reshape(3, 5).copy())

# -1: NumPy tự tính kích thước còn lại


# ============================================================
# 5. BOOLEAN / MASK
# ============================================================

print("\n==================== 5. BOOLEAN / MASK ====================")

arr = np.arange(100)

mask = (arr % 5 == 0)

print("Các số chia hết cho 5:")
print(arr[mask])

mask = ((arr % 5 == 0) & (arr > 0))

print("\nCác số chia hết cho 5 và > 0:")
print(arr[mask])

test_a = np.array([1, 4, 0, 2, 3, 8, 9, 7])

print("\ntest_a:")
print(test_a)

print("\ntest_a > 3:")
print(test_a > 3)

print("\nCác phần tử > 3:")
print(test_a[test_a > 3])

# & = AND
# | = OR


# ============================================================
# 6. PHÉP TOÁN MẢNG
# ============================================================

print("\n==================== 6. PHÉP TOÁN MẢNG ====================")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("a =", a)
print("b =", b)

print("\na + b =")
print(a + b)

print("\na - b =")
print(a - b)

print("\na * b =")
print(a * b)

print("\na / b =")
print(a / b)

print("\na ** 2 =")
print(a ** 2)


# ============================================================
# 7. HÀM THỐNG KÊ / TOÁN
# ============================================================

print("\n==================== 7. HÀM THỐNG KÊ / TOÁN ====================")

x = np.array([1, 2, 3, 4, 5])

print("x =", x)

print("\nTổng - x.sum():")
print(x.sum())

print("\nTrung bình - x.mean():")
print(x.mean())

print("\nTrung vị - np.median(x):")
print(np.median(x))

print("\nGiá trị lớn nhất - x.max():")
print(x.max())

print("\nGiá trị nhỏ nhất - x.min():")
print(x.min())

print("\nĐộ lệch chuẩn - x.std():")
print(x.std())

print("\nPhương sai - x.var():")
print(x.var())

print("\nGiá trị duy nhất - np.unique(x):")
print(np.unique(x))


# ---------- Hàm toán ----------

print("\n--- HÀM TOÁN ---")

print("Căn bậc hai - np.sqrt(x):")
print(np.sqrt(x))

print("\nHàm mũ - np.exp(x):")
print(np.exp(x))


# ============================================================
# 8. CUMSUM
# ============================================================

print("\n==================== 8. CUMSUM ====================")

print("x =", x)

print("\nTổng tích lũy - x.cumsum():")
print(x.cumsum())


# ============================================================
# 9. AXIS
# ============================================================

print("\n==================== 9. AXIS ====================")

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print("a =")
print(a)

print("\nTổng theo cột - axis=0:")
print(a.sum(axis=0))

print("\nTổng theo dòng - axis=1:")
print(a.sum(axis=1))

# axis=0 -> CỘT
# axis=1 -> DÒNG


# ============================================================
# 10. ARGMAX / ARGMIN
# ============================================================

print("\n==================== 10. ARGMAX / ARGMIN ====================")

print("a =")
print(a)

print("\nGiá trị lớn nhất - a.max():")
print(a.max())

print("\nVị trí của giá trị lớn nhất - a.argmax():")
print(a.argmax())

print("\nGiá trị nhỏ nhất - a.min():")
print(a.min())

print("\nVị trí của giá trị nhỏ nhất - a.argmin():")
print(a.argmin())


# ============================================================
# 11. APPEND / DELETE
# ============================================================

print("\n==================== 11. APPEND / DELETE ====================")

a = np.array([[1, 2],
              [3, 4]])

print("Mảng ban đầu:")
print(a)

print("\nThêm dòng [5, 6] - axis=0:")
print(np.append(a, [[5, 6]], axis=0))

print("\nThêm cột [5, 6] - axis=1:")
print(np.append(a, [[5], [6]], axis=1))

print("\nXóa dòng 0 - axis=0:")
print(np.delete(a, 0, axis=0))

print("\nXóa cột 1 - axis=1:")
print(np.delete(a, 1, axis=1))


# ============================================================
# 12. REPEAT
# ============================================================

print("\n==================== 12. REPEAT ====================")

print("np.repeat([1, 2, 3], 3):")
print(np.repeat([1, 2, 3], 3))
