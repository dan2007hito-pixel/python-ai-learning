import numpy as np
print('----------B1----------')
arr_b1 = np.array([1,2,3,4,5])
print(arr_b1)

print('----------B2----------')
arr_b2 = np.arange(6).reshape(2,3)
print(arr_b2.shape)
print(arr_b2)

print('----------B3----------')
arr_b3 = np.array([1,2,3], dtype=complex)
print(arr_b3)
print(arr_b3.dtype)

print('----------B4----------')
arr_b4 = np.array([10, 20, 30], ndmin=2)
print(arr_b4.ndim)

print('----------B5----------')
arr_b5 = np.arange(24).reshape(2,4,3)
print(arr_b5.ndim)

print('----------B6----------')
arr_int_b6 = np.array([1,2,3,4], dtype=np.int8)
arr_float_b6 = np.array([5,6,7,8], dtype=float)
print(arr_int_b6.itemsize)
print(arr_float_b6.itemsize)

print('----------B7----------')
arr_b7 = np.array([10, 20, 30])
arr_b7 = arr_b7.astype(np.int8)
print(arr_b7.dtype)

print('----------B8----------')
arr_float_b8 = np.array([1.5, 2.5, 3.5], dtype='f4')

print(arr_float_b8)
print(arr_float_b8.dtype)

arr_string_b8 = np.array(["Apple", "Banana", "Orange"], dtype='S20')

print(arr_string_b8)
print(arr_string_b8.dtype)

print('----------B9----------')
inventory = np.dtype([("item_code", np.int32)])
arr_b9 = np.array([
    (1001,),
    (1002,),
    (1003,)
], dtype=inventory)
print(arr_b9)

print('----------B10----------')
book = np.dtype([
    ("title", "S30"),
    ("pages", "i2"),
    ("price", "f4")
])

books = np.array([
    (b"Python", 350, 99.5),
    (b"NumPy", 220, 79.9)
], dtype=book)

print(books)

print('----------B11----------')
print(books["title"])

print('----------B12----------')
arr_b12 = np.arange(12)
print(arr_b12)
arr_b12 = arr_b12.reshape(4,3)
print(arr_b12)

print('----------B13----------')
# Tạo mảng
arr_b13 = np.arange(6)

# In thông tin flags
print(arr_b13.flags)

print('----------B14----------')
a_b14 = np.zeros(5)
b_b14 = np.zeros(5, int)
print(a_b14)
print(b_b14)

print('----------B15----------')
arr_b15 = np.ones((2,2), dtype=int)
print(arr_b15)

print('----------B16----------')
arr_b16 = np.empty((2,3), dtype=int)
print(arr_b16)

print('----------B17----------')
arr_b17 = np.zeros((3,3), order='C')
print(arr_b17.flags)

print('----------B18----------')
dt = np.dtype([
    ('x','i4'),
    ('y','i4')
])

arr_b18 = np.zeros((2,2), dtype=dt)

print(arr_b18)

print('----------B19----------')
a_b19 = np.asarray([1.5,2.5,3.5])

b_b19 = np.asarray((10,20,30))

print(a_b19)
print(a_b19.dtype)

print(b_b19)

print('----------B20----------')
arr_b20 = np.asarray([
    (1,2),
    (3,4)
])

print(arr_b20)

print(arr_b20.shape)

# Hàm	        Chức năng 	                          Ví dụ
# arr.flags	    Xem trạng thái bộ nhớ của mảng	      print(arr.flags)
# np.zeros()	Tạo mảng toàn số 0	                  np.zeros((2,3))
# np.ones()	    Tạo mảng toàn số 1	                  np.ones((2,2))
# np.empty()	Tạo mảng chưa khởi tạo giá trị	      np.empty((3,2))
# order='C'	    Lưu dữ liệu theo hàng (Row-major)	  np.zeros((3,3), order='C')
# order='F'	    Lưu dữ liệu theo cột (Column-major)	  np.zeros((3,3), order='F')
# np.dtype()	Tạo kiểu dữ liệu có cấu trúc	      np.dtype([('x','i4'),('y','i4')])
# np.asarray()	Chuyển list, tuple... thành ndarray	  np.asarray([1,2,3])