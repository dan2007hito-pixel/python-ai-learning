# ============================================================
# PANDAS - PHẦN 1: SERIES
# ============================================================

import pandas as pd
import numpy as np


# ============================================================
# 1. TẠO SERIES
# ============================================================

print("\n==================== 1. TẠO SERIES ====================")

values = [222, 333, 444]
index = ['a', 'b', 'c']
data_dict = {'a': 222, 'b': 333, 'c': 444}

print("Series từ List:")
print(pd.Series(values))

print("\nSeries từ List + Index:")
print(pd.Series(values, index=index))

print("\nSeries từ NumPy Array + Index:")
print(pd.Series(np.array(values), index=index))

print("\nSeries từ Dictionary:")
print(pd.Series(data_dict))


# ============================================================
# 2. THUỘC TÍNH
# ============================================================

print("\n==================== 2. THUỘC TÍNH ====================")

s = pd.Series([111, 222, 333, 444],
              index=['a', 'b', 'c', 'd'],
              name='MySeries')

print("Series s:")
print(s)

print("\nIndex - s.index:")
print(s.index)

print("\nTên Series - s.name:")
print(s.name)

print("\nKiểu dữ liệu - s.dtype:")
print(s.dtype)

print("\nDữ liệu dạng NumPy Array - s.values:")
print(s.values)


# ============================================================
# 3. INDEXING / SLICING
# ============================================================

print("\n==================== 3. INDEXING / SLICING ====================")

print("Series s:")
print(s)

print("\ns.iloc[1] - Lấy theo vị trí:")
print(s.iloc[1])

print("\ns.loc['a'] - Lấy theo nhãn:")
print(s.loc['a'])

print("\ns.iloc[2:4] - Lấy vị trí 2 -> 3:")
print(s.iloc[2:4])

print("\ns.loc[['a', 'd']] - Lấy theo nhiều nhãn:")
print(s.loc[['a', 'd']])


# ============================================================
# 4. TÍNH TOÁN GIỮA SERIES
# ============================================================

print("\n==================== 4. TÍNH TOÁN GIỮA SERIES ====================")

s1 = pd.Series([1, 2, 3, 4],
               index=['d', 'b', 'c', 'a'])

s2 = pd.Series([1, 2, 3, 4],
               index=['a', 'b', 'd', 'e'])

print("s1:")
print(s1)

print("\ns2:")
print(s2)

print("\ns1 + s2:")
print(s1 + s2)

# Pandas ghép dữ liệu theo INDEX.
# Index không khớp -> NaN.


# ============================================================
# 5. HÀM THỐNG KÊ
# ============================================================

print("\n==================== 5. HÀM THỐNG KÊ ====================")

print("s1:")
print(s1)

print("\nTổng - s1.sum():")
print(s1.sum())

print("\nTrung bình - s1.mean():")
print(s1.mean())

print("\nTrung vị - s1.median():")
print(s1.median())

print("\nGiá trị lớn nhất - s1.max():")
print(s1.max())

print("\nĐộ lệch chuẩn - s1.std():")
print(s1.std())


# ============================================================
# 6. SẮP XẾP
# ============================================================

print("\n==================== 6. SẮP XẾP ====================")

print("s1 ban đầu:")
print(s1)

print("\ns1.sort_values() - Sắp xếp theo GIÁ TRỊ:")
print(s1.sort_values())

print("\ns1.sort_index() - Sắp xếp theo INDEX:")
print(s1.sort_index())


# ============================================================
# 7. APPLY
# ============================================================

print("\n==================== 7. APPLY ====================")

ser_height = pd.Series(
    [165.3, 170.1, 175.0, 182.1, 168.0],
    name='height'
)

print("Chiều cao ban đầu (cm):")
print(ser_height)

print("\nChiều cao sau khi chia 100 (m):")
print(ser_height.apply(lambda x: x / 100))

# apply() áp dụng một hàm cho từng phần tử


# ============================================================
# 8. GIÁ TRỊ THIẾU NaN
# ============================================================

print("\n==================== 8. GIÁ TRỊ THIẾU NaN ====================")

obj = pd.Series({
    'Ohio': 35000,
    'Texas': 71000,
    'Oregon': 16000
})

obj2 = pd.Series(
    obj,
    index=['California', 'Ohio', 'Oregon', 'Texas']
)

print("obj:")
print(obj)

print("\nobj2:")
print(obj2)

print("\npd.isnull(obj2) - Kiểm tra giá trị thiếu:")
print(pd.isnull(obj2))

print("\npd.notnull(obj2) - Kiểm tra giá trị KHÔNG thiếu:")
print(pd.notnull(obj2))

print("\nobj2.isnull() - Kiểm tra giá trị thiếu:")
print(obj2.isnull())


# ============================================================
# 9. ĐỔI TÊN SERIES VÀ INDEX
# ============================================================

print("\n==================== 9. ĐỔI TÊN SERIES VÀ INDEX ====================")

obj2.name = 'population'
obj2.index.name = 'state'

print("Sau khi đổi tên:")
print(obj2)

print("\nTên Series - obj2.name:")
print(obj2.name)

print("\nTên Index - obj2.index.name:")
print(obj2.index.name)


# ============================================================
# 10. ĐỔI INDEX
# ============================================================

print("\n==================== 10. ĐỔI INDEX ====================")

print("obj trước khi đổi index:")
print(obj)

obj.index = ['A', 'B', 'C']

print("\nobj sau khi đổi index:")
print(obj)


# ============================================================
# NHỚ NHANH
# ============================================================

print("\n============================================================")
print("                       NHỚ NHANH")
print("============================================================")

print("pd.Series(...)")
print("  -> Tạo Series")

print("\ns.iloc[...]")
print("  -> Truy cập theo VỊ TRÍ")

print("\ns.loc[...]")
print("  -> Truy cập theo NHÃN INDEX")

print("\ns.sum() / s.mean() / s.median()")
print("  -> Tổng / Trung bình / Trung vị")

print("\ns.sort_values()")
print("  -> Sắp xếp theo GIÁ TRỊ")

print("\ns.sort_index()")
print("  -> Sắp xếp theo INDEX")

print("\ns.apply(func)")
print("  -> Áp dụng hàm cho từng phần tử")

print("\npd.isnull(s)")
print("  -> Kiểm tra giá trị thiếu NaN")

print("\npd.notnull(s)")
print("  -> Kiểm tra giá trị không thiếu")
