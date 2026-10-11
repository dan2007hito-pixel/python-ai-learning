import tensorflow as tf
import numpy as np

# Bài này minh họa cách tạo và xử lý dữ liệu bằng tf.data.Dataset.
# Dataset là một luồng các mẫu; có thể duyệt từng mẫu hoặc gom nhiều mẫu
# thành một batch để đưa vào mô hình học máy.

# Tạo Dataset từ danh sách 6 số. from_tensor_slices tách danh sách thành
# 6 phần tử riêng, mỗi lần duyệt sẽ lấy ra một phần tử.
a= [1.2, 3.4, 7.5, 4.1, 5.0, 1.0]
ds = tf.data.Dataset.from_tensor_slices(a)
print(ds)  # In mô tả Dataset: kiểu dữ liệu và hình dạng của mỗi phần tử.

# Đọc lần lượt từng phần tử. item là Tensor; TensorFlow thường hiển thị
# trực tiếp giá trị Tensor khi print.
for item in ds:
    print(item)
    
# batch(3) gom 3 phần tử liên tiếp thành một nhóm (batch).
# enumerate(..., 100) đánh số các batch bắt đầu từ 100 để tiện theo dõi.
ds_batch = ds.batch(3)
for i, elemen in enumerate(ds_batch, 100):
    print('batch {}: '.format(i), elemen.numpy())
    
# Tạo dữ liệu mẫu cho bài toán có đầu vào x và nhãn y.
# t_x có hình dạng (4, 3): 4 mẫu, mỗi mẫu có 3 đặc trưng.
# t_y có 4 nhãn; nhãn ở vị trí nào đi cùng mẫu x ở vị trí đó.
# Đặt seed để có thể tái tạo chuỗi số ngẫu nhiên khi chạy lại.
tf.random.set_seed(42)
t_x = tf.random.uniform([4,3], dtype=tf.float32)
t_y = tf.range(4)

print(t_y)  # Các nhãn lần lượt là 0, 1, 2, 3.

# Tách t_x thành Dataset gồm 4 mẫu đầu vào; mỗi mẫu là một vector 3 số.
ds_x = tf.data.Dataset.from_tensor_slices(t_x)
print(ds_x)

# Tách t_y thành Dataset gồm 4 nhãn tương ứng.
ds_y = tf.data.Dataset.from_tensor_slices(t_y)
print(ds_y)

# zip ghép phần tử cùng vị trí trong ds_x và ds_y thành cặp (đầu vào, nhãn).
# Nhờ vậy mỗi mẫu luôn đi cùng đáp án đúng của nó.
ds_joint = tf.data.Dataset.zip(ds_x, ds_y)
# Mỗi example gồm hai phần: example[0] là x, example[1] là y.
# numpy() chuyển Tensor thành giá trị/mảng NumPy để in dễ đọc.
for example in ds_joint:
    print('x: ', example[0].numpy(),
          'y: ', example[1].numpy())
print('------------------------------')

# map áp dụng phép biến đổi lên từng cặp dữ liệu.
# x*2-1 đổi giá trị x từ khoảng [0, 1) sang [-1, 1); y được giữ nguyên.
ds_trans = ds_joint.map(lambda x,y: (x*2-1.0, y))
for example in ds_trans:
    print('x: ', example[0].numpy(),
          'y: ', example[1].numpy())
print('------------------------------')

# shuffle xáo trộn thứ tự các cặp, đồng thời vẫn giữ đầu vào và nhãn đi chung.
# buffer_size=4 vì tập này có 4 mẫu; đây là kích thước vùng dùng để xáo trộn.
ds_shuff = ds_joint.shuffle(buffer_size=len(t_x))

for example in ds_shuff:
    print('x: ', example[0].numpy(),
          'y: ', example[1].numpy())
print('------------------------------')     

# Chia 4 cặp thành batch có tối đa 3 mẫu: batch đầu có 3 mẫu, batch sau có 1.
# drop_remainder=False giữ lại batch cuối dù nó chưa đủ 3 mẫu.
ds = ds_joint.batch(batch_size=3, drop_remainder=False)

# iter(ds) tạo bộ lặp và next(...) lấy batch đầu tiên trong Dataset.
# batch_x chứa đầu vào, batch_y chứa các nhãn ứng với những đầu vào đó.
batch_x, batch_y = next(iter(ds))
print('batch x: \n', batch_x.numpy())
print('batch y: ', batch_y)
print('------------------------------')

# repeat(count=2) đọc toàn bộ 4 mẫu hai lần, tạo thành 8 mẫu liên tiếp.
# batch(3) gom 8 mẫu thành các batch kích thước 3: 3 + 3 + 2.
# Batch cuối có 2 mẫu vì mặc định batch vẫn giữ phần dư.
ds = ds_joint.repeat(count=2).batch(3)
for i, (batch_x, batch_y) in enumerate(ds):
    print('batch {}', format(i))
    print('batch x: \n', batch_x.numpy())
    print('batch y: ', batch_y)
    
print('------------------------------')

# Vẫn có 8 mẫu sau khi lặp hai lần. Gom 2 mẫu mỗi batch nên có 4 batch đủ.
ds = ds_joint.repeat(count=2).batch(2)
for i, (batch_x, batch_y) in enumerate(ds):
    print('batch {}', format(i))
    print('batch x: \n', batch_x.numpy())
    print('batch y: ', batch_y)
    
print('------------------------------')

# Pipeline kết hợp nhiều bước. Các bước được thực hiện từ trái sang phải:
# xáo trộn 4 mẫu, gom 2 mẫu thành batch, rồi lặp lại pipeline 3 lần.
# Mỗi lượt có 2 batch; tổng cộng vòng lặp bên dưới in 6 batch.
ds = ds_joint.shuffle(4).batch(2).repeat(3)
for i, (batch_x, batch_y) in enumerate(ds):
    print('batch {}', format(i))
    print('batch x: \n', batch_x.numpy())
    print('batch y: ', batch_y)


