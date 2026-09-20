# ============================================================
# OS - QUẢN LÝ THƯ MỤC / FILE
# ============================================================
import os

# 1. THƯ MỤC HIỆN TẠI
print(os.getcwd())

# 2. ĐỔI THƯ MỤC LÀM VIỆC
# os.chdir(r'D:\Python\data')
# print(os.getcwd())

# 3. XEM FILE / THƯ MỤC
print(os.listdir('.'))

# 4. KIỂM TRA TỒN TẠI
print(os.path.exists('data_studentlist.csv'))

# Kiểm tra là file hay thư mục
print(os.path.isfile('data_studentlist.csv'))
print(os.path.isdir('.'))

# 5. TẠO THƯ MỤC
# os.mkdir('data')       # Tạo 1 thư mục
# os.makedirs('data/a/b') # Tạo nhiều cấp

# 6. XÓA
# os.remove('test.txt')  # Xóa file
# os.rmdir('data')       # Xóa thư mục rỗng

# 7. LÀM VIỆC VỚI ĐƯỜNG DẪN
path = os.path.join('data', 'student.csv')
print(path)

print(os.path.basename(path))  # student.csv
print(os.path.dirname(path))   # data

# 8. KÍCH THƯỚC FILE
if os.path.exists(path):
    print(os.path.getsize(path))

# 9. KẾT HỢP VỚI PANDAS
# Đổi đến thư mục chứa dữ liệu:
# os.chdir(r'D:\Python\data')

# Đọc CSV:
# import pandas as pd
# df = pd.read_csv('data_studentlist.csv')

# Ghi CSV:
# df.to_csv('data_mine.csv', index=False)

# Đọc Excel:
# df = pd.read_excel('data_studentlist.xlsx', sheet_name='Sheet1')

# Ghi Excel:
# df.to_excel('data_studentlist2.xlsx',
#             sheet_name='NewSheet',
#             index=False)

# NHỚ NHANH:
# os.getcwd()       -> thư mục hiện tại
# os.chdir(path)    -> đổi thư mục
# os.listdir(path)  -> xem file/thư mục
# os.path.exists()  -> kiểm tra tồn tại
# os.path.isfile()  -> có phải file?
# os.path.isdir()   -> có phải thư mục?
# os.path.join()    -> nối đường dẫn
# os.remove()       -> xóa file
# os.mkdir()        -> tạo thư mục