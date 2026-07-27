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
print(books["title"])