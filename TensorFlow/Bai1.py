# Bài 1: Làm quen với TensorFlow Tensor và các phép xử lý cơ bản.
# Tensor là mảng nhiều chiều mà TensorFlow dùng để lưu và tính toán dữ liệu.
# Chạy file này sẽ in kết quả của từng ví dụ ra màn hình.
import tensorflow as tf
import numpy as np

print('---------------')
print(tf.__version__)

print('---------------')
np.set_printoptions(precision=2)

arr = np.array([1.234567, 6.78665])
print(arr)

print('---------------')

# So sánh mảng NumPy với danh sách Python; dtype chọn kiểu số nguyên 32-bit.
a = np.array([1,2,3], dtype=np.int32)  ## Mang NumPy
b = [4,5,6]                            ## Danh sach Python

# Chuyển cả hai dạng dữ liệu thành Tensor. a vẫn là mảng NumPy nên is_tensor(a)
# bên dưới trả về False; t_a mới là Tensor.
t_a = tf.convert_to_tensor(a)
t_b = tf.convert_to_tensor(b)

print(t_a)
print(t_b)
print(tf.is_tensor(a))

# Tạo Tensor 2 hàng, 3 cột gồm toàn số 1.
print('---------------')
t_ones = tf.ones((2,3))
print(t_ones)

##tf.Tensor(
# [[1. 1. 1.]
#  [1. 1. 1.]], shape=(2, 3), dtype=float32)

# t_ones.numpy() -> Array 

# Tạo Tensor 3 chiều kích thước 3 x 4 x 5, mọi phần tử bằng 9. one_hot mã hóa
# các chỉ số 0..3 thành các hàng có 5 cột, mỗi hàng có một vị trí bằng 1.
print('---------------')
print(tf.fill((3,4,5),9))  ## 3 chiều, 4 hàng, 5 cột

print(tf.one_hot([0,1,2,3,3],5)) ## [] số hàng, 5 số cột, giá trị trong [] lần lượt đc đánh số

# cast chuyển kiểu các số nguyên trong t_a thành số thực float32.
t_a_new = tf.cast(t_a, tf.float32)
print(t_a_new)

print('---------------')
# uniform tạo ma trận số ngẫu nhiên trong [2, 4); transpose đổi hàng và cột.
t = tf.random.uniform(shape=(3,5), minval=2, maxval=4)
print(t)
t_tr = tf.transpose(t)
print(t_tr)

print('---------------')

# zeros tạo Tensor 5 chiều. squeeze bỏ các chiều có kích thước 1 (trục 0, 2, 4),
# nên kết quả còn kích thước 2 x 4.
t = tf.zeros((1,2,1,4,1))
print(t)

t_sqz = tf.squeeze(t, axis=(0, 2, 4))
print(t_sqz)

print('---------------')

# Seed giúp có thể lặp lại chuỗi giá trị ngẫu nhiên. uniform lấy mẫu đều,
# normal lấy mẫu theo phân phối chuẩn với trung bình 0 và độ lệch chuẩn 1.
tf.random.set_seed(1)
t1 = tf.random.uniform(shape=(5,2), minval=-1.0, maxval=1.0)
t2 = tf.random.normal(shape=(5,2), mean=0.0, stddev=1.0)

print(t1)
print(t2)

print('---------------')
# Nhân từng cặp phần tử ở cùng vị trí trong hai Tensor.
t3 = tf.multiply(t1,t2)
print(t3)

# Tính trung bình từng hàng (axis=1 là chiều cột), rồi hiển thị bằng NumPy.
t4 = tf.math.reduce_mean(t1, axis=1)
print(t4.numpy())
