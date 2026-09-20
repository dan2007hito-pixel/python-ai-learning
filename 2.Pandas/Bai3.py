# ============================================================
# PANDAS - PHẦN 3: DATAFRAME NÂNG CAO
# ============================================================

import pandas as pd
import numpy as np


# ============================================================
# 1. MERGE - GỘP THEO CỘT KHÓA
# ============================================================

print("\n==================== 1. MERGE ====================")

left = pd.DataFrame({
    'NAME': ['A', 'B', 'C'],
    'AGE': [20, 21, 22]
})

right = pd.DataFrame({
    'NAME': ['B', 'C', 'D'],
    'HEIGHT': [170, 175, 180]
})

print("DataFrame left:")
print(left)

print("\nDataFrame right:")
print(right)

print("\nMERGE - INNER:")
print(pd.merge(left, right, on='NAME', how='inner'))

print("\nMERGE - LEFT:")
print(pd.merge(left, right, on='NAME', how='left'))

print("\nMERGE - RIGHT:")
print(pd.merge(left, right, on='NAME', how='right'))

print("\nMERGE - OUTER:")
print(pd.merge(left, right, on='NAME', how='outer'))

# inner -> chỉ lấy NAME xuất hiện ở cả 2
# left  -> giữ toàn bộ left
# right -> giữ toàn bộ right
# outer -> lấy tất cả NAME


# ============================================================
# 2. CONCAT - NỐI DATAFRAME
# ============================================================

print("\n==================== 2. CONCAT ====================")

print("DataFrame left:")
print(left)

print("\nDataFrame right:")
print(right)

print("\nCONCAT theo dòng - axis=0:")
print(pd.concat([left, right], sort=True))

print("\nCONCAT theo cột - axis=1:")
print(pd.concat([left, right], axis=1, sort=True))

# axis=0 -> nối theo dòng
# axis=1 -> nối theo cột


# ============================================================
# 3. GROUPBY
# ============================================================

print("\n==================== 3. GROUPBY ====================")

df = pd.DataFrame({
    'gender': ['M', 'F', 'M', 'F'],
    'height': [170, 160, 180, 165],
    'weight': [65, 50, 75, 55],
    'grade': [8, 9, 7, 10]
})

print("DataFrame:")
print(df)

print("\nChiều cao trung bình theo gender:")
print(
    df.groupby('gender')['height'].mean()
)

print("\nChiều cao + cân nặng trung bình theo gender:")
print(
    df.groupby('gender')[['height', 'weight']].mean()
)

print("\nĐộ lệch chuẩn của grade + height theo gender:")
print(
    df.groupby('gender')[['grade', 'height']].std()
)


# ============================================================
# 4. APPLY
# ============================================================

print("\n==================== 4. APPLY ====================")

print("Chiều cao ban đầu:")
print(df['height'])

print("\nChiều cao sau khi đổi từ cm -> m:")
print(
    df['height'].apply(lambda x: x / 100)
)

# apply() áp dụng hàm cho từng phần tử


# ============================================================
# 5. UNIQUE / NUNIQUE / VALUE_COUNTS
# ============================================================

print("\n==================== 5. UNIQUE / NUNIQUE / VALUE_COUNTS ====================")

print("Cột gender:")
print(df['gender'])

print("\nunique() - Các giá trị khác nhau:")
print(df['gender'].unique())

print("\nnunique() - Số lượng giá trị khác nhau:")
print(df['gender'].nunique())

print("\nvalue_counts() - Đếm số lần xuất hiện:")
print(df['gender'].value_counts())


# ============================================================
# 6. MULTIINDEX
# ============================================================

print("\n==================== 6. MULTIINDEX ====================")

header = ['A', 'B', 'C']

outer = ['G1'] * 2 + ['G2'] * 2 + ['G3'] * 2
inner = ['a', 'b'] * 3

multi_index = pd.MultiIndex.from_tuples(
    list(zip(outer, inner))
)

df = pd.DataFrame(
    np.random.randn(6, 3),
    index=multi_index,
    columns=header
)

print("DataFrame có MultiIndex:")
print(df)

print("\nLấy nhóm G1:")
print(df.loc['G1'])

print("\nLấy G1 -> a:")
print(df.loc['G1'].loc['a'])

print("\nLấy G1 -> a -> cột B:")
print(df.loc['G1'].loc['a', 'B'])


# ============================================================
# 7. GROUPBY VỚI NHIỀU CỘT
# ============================================================

print("\n==================== 7. GROUPBY VỚI NHIỀU CỘT ====================")

df2 = pd.DataFrame({
    'gender': ['F', 'F', 'M', 'M'],
    'bloodtype': ['A', 'B', 'A', 'A'],
    'height': [160, 165, 170, 180]
})

print("DataFrame:")
print(df2)

result = df2.groupby(
    ['gender', 'bloodtype']
)['height'].mean()

print("\nChiều cao trung bình theo gender + bloodtype:")
print(result)


# ============================================================
# 8. PIVOT TABLE
# ============================================================

print("\n==================== 8. PIVOT TABLE ====================")

data = {
    'Size': ['L', 'L', 'M', 'M', 'M', 'S', 'S', 'S', 'S'],
    'Type': ['A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B'],
    'Location': ['L1', 'L1', 'L1', 'L2', 'L2',
                 'L1', 'L2', 'L2', 'L1'],
    'A': [1, 2, 2, 3, 3, 4, 5, 6, 7],
    'B': [2, 4, 5, 5, 6, 6, 8, 9, 9]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nPIVOT TABLE - values='B':")
print(
    pd.pivot_table(
        df,
        index=['Size', 'Type'],
        columns='Location',
        values='B'
    )
)

print("\nPIVOT TABLE - fill_value=0 + mean:")
print(
    pd.pivot_table(
        df,
        index=['Size', 'Type'],
        columns='Location',
        values='B',
        fill_value=0,
        aggfunc='mean'
    )
)


# ============================================================
# NHỚ NHANH
# ============================================================

print("\n============================================================")
print("                       NHỚ NHANH")
print("============================================================")

print("merge()")
print("  -> Gộp DataFrame theo KHÓA / CỘT")

print("\nconcat()")
print("  -> Nối DataFrame")

print("\nconcat(axis=0)")
print("  -> Nối theo DÒNG")

print("\nconcat(axis=1)")
print("  -> Nối theo CỘT")

print("\ngroupby()")
print("  -> Nhóm dữ liệu + tính toán")

print("\napply()")
print("  -> Áp dụng hàm cho từng phần tử")

print("\nunique()")
print("  -> Lấy các giá trị khác nhau")

print("\nnunique()")
print("  -> Đếm số giá trị khác nhau")

print("\nvalue_counts()")
print("  -> Đếm số lần xuất hiện")

print("\nMultiIndex")
print("  -> Index nhiều cấp")

print("\npivot_table()")
print("  -> Tạo bảng tổng hợp")

print("\n============================================================")
print("       KẾT THÚC ÔN TẬP PANDAS DATAFRAME NÂNG CAO")
print("============================================================")