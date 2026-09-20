# ============================================================
# PANDAS - PHẦN 2: DATAFRAME CƠ BẢN
# ============================================================

import pandas as pd
import numpy as np


# ============================================================
# 1. TẠO DATAFRAME
# ============================================================

print("\n==================== 1. TẠO DATAFRAME ====================")

data = {
    'NAME': ['Jake', 'Jennifer', 'Paul', 'Andrew'],
    'AGE': [24, 21, 25, 19],
    'GENDER': ['M', 'F', 'M', 'M']
}

df = pd.DataFrame(data)

print("DataFrame từ Dictionary:")
print(df)


# ---------- Từ NumPy Array ----------

df2 = pd.DataFrame(
    np.random.rand(5, 3),
    columns=['A', 'B', 'C']
)

print("\nDataFrame từ NumPy Array:")
print(df2)


# ============================================================
# 2. THUỘC TÍNH
# ============================================================

print("\n==================== 2. THUỘC TÍNH ====================")

print("df.shape - (số dòng, số cột):")
print(df.shape)

print("\ndf.size - Tổng số phần tử:")
print(df.size)

print("\ndf.ndim - Số chiều:")
print(df.ndim)

print("\ndf.columns - Tên các cột:")
print(df.columns)

print("\ndf.index - Index:")
print(df.index)

print("\ntype(df) - Kiểu dữ liệu:")
print(type(df))


# ============================================================
# 3. XEM DỮ LIỆU
# ============================================================

print("\n==================== 3. XEM DỮ LIỆU ====================")

print("df.head() - 5 dòng đầu:")
print(df.head())

print("\ndf.tail() - 5 dòng cuối:")
print(df.tail())

print("\ndf.info() - Thông tin DataFrame:")
print(df.info())

print("\ndf.describe() - Thống kê:")
print(df.describe())


# ============================================================
# 4. ĐỔI TÊN CỘT
# ============================================================

print("\n==================== 4. ĐỔI TÊN CỘT ====================")

print("Tên cột ban đầu:")
print(df.columns)

df.columns = ['NAME', 'AGE', 'GENDER']

print("\nTên cột sau khi đổi:")
print(df.columns)

print("\nDataFrame:")
print(df)


# ============================================================
# 5. LẤY CỘT
# ============================================================

print("\n==================== 5. LẤY CỘT ====================")

print("df['NAME'] - Lấy 1 cột -> Series:")
print(df['NAME'])

print("\ndf[['NAME']] - Lấy 1 cột -> DataFrame:")
print(df[['NAME']])

print("\ndf.loc[:, 'NAME'] - Lấy cột NAME:")
print(df.loc[:, 'NAME'])

print("\ndf.loc[:, ['NAME', 'GENDER']] - Lấy nhiều cột:")
print(df.loc[:, ['NAME', 'GENDER']])

print("\ndf.iloc[:, [0, 1]] - Lấy cột theo vị trí:")
print(df.iloc[:, [0, 1]])


# ============================================================
# 6. LẤY DÒNG
# ============================================================

print("\n==================== 6. LẤY DÒNG ====================")

print("df.loc[0] - Lấy dòng có index 0:")
print(df.loc[0])

print("\ndf.loc[0:2] - Lấy dòng index 0 -> 2:")
print(df.loc[0:2])

print("\ndf.iloc[0:2] - Lấy dòng theo vị trí 0 -> 1:")
print(df.iloc[0:2])


# ============================================================
# 7. LỌC THEO ĐIỀU KIỆN
# ============================================================

print("\n==================== 7. LỌC THEO ĐIỀU KIỆN ====================")

print("Người có GENDER = 'M':")
print(df[df['GENDER'] == 'M'])

print("\nNgười có AGE > 20:")
print(df[df['AGE'] > 20])

print("\nNgười có AGE > 20 VÀ GENDER = 'M':")
print(df[
    (df['AGE'] > 20) &
    (df['GENDER'] == 'M')
])

# & = AND
# | = OR


# ============================================================
# 8. XÓA
# ============================================================

print("\n==================== 8. XÓA ====================")

print("DataFrame ban đầu:")
print(df)

print("\nXóa cột NAME:")
print(df.drop(columns=['NAME']))

# inplace=True
# -> thay đổi trực tiếp DataFrame


# ============================================================
# 9. ĐỔI TÊN CỘT / INDEX
# ============================================================

print("\n==================== 9. ĐỔI TÊN CỘT / INDEX ====================")

df.rename(
    columns={'NAME': 'name'},
    inplace=True
)

print("Sau khi đổi NAME -> name:")
print(df)


# ============================================================
# 10. SET INDEX
# ============================================================

print("\n==================== 10. SET INDEX ====================")

print("DataFrame trước set_index:")
print(df)

df.set_index('name', inplace=True)

print("\nDataFrame sau set_index('name'):")
print(df)

# Cột name trở thành INDEX


# ============================================================
# 11. THÊM CỘT
# ============================================================

print("\n==================== 11. THÊM CỘT ====================")

df['score'] = 80

print("Sau khi thêm cột score:")
print(df)


# ============================================================
# 12. SỬA GIÁ TRỊ
# ============================================================

print("\n==================== 12. SỬA GIÁ TRỊ ====================")

print("DataFrame trước khi sửa:")
print(df)

df.loc['Jake', 'score'] = 90

print("\nSau khi sửa score của Jake thành 90:")
print(df)


# ============================================================
# 13. XÓA DÒNG / CỘT
# ============================================================

print("\n==================== 13. XÓA DÒNG / CỘT ====================")

print("DataFrame ban đầu:")
print(df)

df.drop('Jake', inplace=True)

print("\nSau khi xóa dòng Jake:")
print(df)

df.drop('score', axis=1, inplace=True)

print("\nSau khi xóa cột score:")
print(df)


# ============================================================
# 14. REINDEX / RESET INDEX
# ============================================================

print("\n==================== 14. REINDEX / RESET INDEX ====================")

data = {
    'c0': [1, 2, 3],
    'c1': [4, 5, 6]
}

df = pd.DataFrame(
    data,
    index=['r0', 'r1', 'r2']
)

print("DataFrame ban đầu:")
print(df)

print("\ndf.reindex(['r0','r1','r2','r3']):")
print(df.reindex(['r0', 'r1', 'r2', 'r3']))

print("\nreindex + fill_value=0:")
print(
    df.reindex(
        ['r0', 'r1', 'r2', 'r3'],
        fill_value=0
    )
)

print("\ndf.reset_index():")
print(df.reset_index())


# ============================================================
# 15. SẮP XẾP
# ============================================================

print("\n==================== 15. SẮP XẾP ====================")

print("DataFrame ban đầu:")
print(df)

print("\ndf.sort_index(ascending=False):")
print(df.sort_index(ascending=False))

print("\ndf.sort_values(by='c1', ascending=False):")
print(df.sort_values(
    by='c1',
    ascending=False
))


# ============================================================
# NHỚ NHANH
# ============================================================

print("\n============================================================")
print("                       NHỚ NHANH")
print("============================================================")

print("pd.DataFrame(data)")
print("  -> Tạo DataFrame")

print("\ndf.shape")
print("  -> (số dòng, số cột)")

print("\ndf.head() / df.tail()")
print("  -> Xem đầu / cuối DataFrame")

print("\ndf['NAME']")
print("  -> Lấy 1 cột -> Series")

print("\ndf[['NAME']]")
print("  -> Lấy 1 cột -> DataFrame")

print("\ndf.loc[...]")
print("  -> Truy cập theo LABEL")

print("\ndf.iloc[...]")
print("  -> Truy cập theo VỊ TRÍ")

print("\ndf[df['AGE'] > 20]")
print("  -> Lọc theo điều kiện")

print("\ndf.drop(...)")
print("  -> Xóa dòng / cột")

print("\ndf.rename(...)")
print("  -> Đổi tên cột / index")

print("\ndf.set_index(...)")
print("  -> Đưa một cột thành INDEX")

print("\ndf.reindex(...)")
print("  -> Thay đổi / sắp xếp lại INDEX")

print("\ndf.reset_index()")
print("  -> Đưa INDEX trở lại thành cột")

print("\ndf.sort_index()")
print("  -> Sắp xếp theo INDEX")

print("\ndf.sort_values()")
print("  -> Sắp xếp theo GIÁ TRỊ")
