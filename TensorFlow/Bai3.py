from pathlib import Path
import matplotlib.pyplot as plt
import os
import tensorflow as tf

# Đường dẫn đến thư mục chứa ảnh; đổi lại nếu ảnh nằm ở nơi khác.
path = r"C:\Users\dan20\Downloads\cat_dog_6"
cat_dog_image_dir = Path(path)

# Tìm các ảnh JPG trong thư mục và các thư mục con, sau đó sắp xếp danh sách.
cat_dog_file_paths = sorted(
    str(image_path) for image_path in cat_dog_image_dir.rglob('*.jpg'))

if not cat_dog_file_paths:
    raise FileNotFoundError(f'Không tìm thấy ảnh JPG trong thư mục: {cat_dog_image_dir}')

# In danh sách để kiểm tra các ảnh đã được tìm thấy.
print(cat_dog_file_paths)

# Tạo biểu đồ xem trước ảnh.
fig = plt.figure(figsize=(10,5))

for i, cat_dog_file_path in enumerate(cat_dog_file_paths):
    # Đọc dữ liệu ảnh từ tệp rồi giải mã thành tensor ảnh.
    cat_dog_image_bytes = tf.io.read_file(cat_dog_file_path)
    cat_dog_preview_image = tf.image.decode_image(cat_dog_image_bytes)
    print('Image size: ', cat_dog_preview_image.shape)

    # Đặt ảnh vào ô tương ứng trong lưới 2 hàng, 3 cột.
    ax = fig.add_subplot(2,3,i+1)
    ax.imshow(cat_dog_preview_image)
    ax.set_title(os.path.basename(cat_dog_file_path), size = 15)
    
plt.tight_layout()
# Bỏ dấu # nếu muốn hiển thị phần xem trước này ngay tại đây.
# plt.show()

# Gán nhãn: 0 = mèo, 1 = chó (tên tệp có chứa "dog").
cat_dog_labels = [1 if 'dog' in os.path.basename(file_path) else 0
                  for file_path in cat_dog_file_paths]
print(cat_dog_labels)

print('---------------------------')
# Tạo Dataset gồm các cặp (đường dẫn ảnh, nhãn).
cat_dog_path_label_ds = tf.data.Dataset.from_tensor_slices(
    (cat_dog_file_paths, cat_dog_labels))

# In thử các cặp dữ liệu đầu vào.
for item in cat_dog_path_label_ds:
    print(item[0], item[1].numpy())
    
cat_dog_resize_width, cat_dog_resize_height = 120, 80

def load_and_preprocess_cat_dog_image(image_path, image_label):
    # Đọc tệp và giải mã ảnh thành ảnh RGB có 3 kênh màu.
    image_bytes = tf.io.read_file(image_path)
    decoded_image = tf.image.decode_jpeg(image_bytes, channels=3)

    # Đổi kích thước ảnh về cùng chiều cao và chiều rộng.
    resized_image = tf.image.resize(
        decoded_image, [cat_dog_resize_height, cat_dog_resize_width])

    # Chuẩn hóa giá trị pixel từ khoảng 0–255 về khoảng 0–1.
    normalized_image = resized_image / 255.0

    # Trả về ảnh đã xử lý cùng nhãn tương ứng.
    return normalized_image, image_label

# Áp dụng hàm tiền xử lý cho từng phần tử trong Dataset.
cat_dog_image_label_ds = cat_dog_path_label_ds.map(load_and_preprocess_cat_dog_image)

# Hiển thị ảnh đã xử lý và nhãn để kiểm tra kết quả.
fig = plt.figure(figsize=(10,5))
for i, cat_dog_example in enumerate(cat_dog_image_label_ds):
    print(cat_dog_example[0].shape, cat_dog_example[1].numpy())
    ax = fig.add_subplot(2,3,i+1)
    ax.set_xticks([]);ax.set_yticks([])
    ax.imshow(cat_dog_example[0])
    ax.set_title('{}'.format(cat_dog_example[1].numpy()), size = 15)
    
plt.tight_layout()
plt.show()

# Bài mới: tải và xem dữ liệu CIFAR-100, sau đó tải và xem dữ liệu MNIST.
import tensorflow_datasets as tfds

print(len(tfds.list_builders()))
print(tfds.list_builders()[:10])

cifar100_builder = tfds.builder('cifar100')
cifar100_builder.download_and_prepare()  # Tải dữ liệu nếu máy chưa có.

print(cifar100_builder.info.features)
print(cifar100_builder.info.features.keys())
print(cifar100_builder.info.features['image'])
print(cifar100_builder.info.features['label'])
print(cifar100_builder.info.citation)

cifar100_splits = cifar100_builder.as_dataset(shuffle_files=False)
cifar100_train_ds = cifar100_splits['train']
assert isinstance(cifar100_train_ds, tf.data.Dataset)

cifar100_example = next(iter(cifar100_train_ds))
print(type(cifar100_example))
print(cifar100_example.keys())

cifar100_train_ds = cifar100_train_ds.map(
    lambda sample: (sample['image'], tf.cast(sample['label'], tf.int32)))
print(cifar100_train_ds)

cifar100_batch_ds = cifar100_train_ds.shuffle(18).batch(18)
cifar100_image_batch, cifar100_label_batch = next(iter(cifar100_batch_ds))
print(cifar100_image_batch.shape, cifar100_label_batch.shape)

fig = plt.figure(figsize=(12, 8))
for index, (cifar100_image, cifar100_label) in enumerate(
        zip(cifar100_image_batch, cifar100_label_batch)):
    ax = fig.add_subplot(3, 6, index + 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.imshow(cifar100_image)
    ax.set_title(str(cifar100_label.numpy()), size=15)
plt.tight_layout()
plt.show()

mnist_splits, mnist_info = tfds.load(
    name='mnist', with_info=True, shuffle_files=False)
print(mnist_info)
print(mnist_splits.keys())

mnist_train_ds = mnist_splits['train']
assert isinstance(mnist_train_ds, tf.data.Dataset)
mnist_train_ds = mnist_train_ds.map(
    lambda sample: (sample['image'], sample['label']))

mnist_batch_ds = mnist_train_ds.shuffle(buffer_size=1000).batch(10)
mnist_image_batch, mnist_label_batch = next(iter(mnist_batch_ds))
print(mnist_image_batch.shape, mnist_label_batch)

fig = plt.figure(figsize=(15, 6))
for index, (mnist_image, mnist_label) in enumerate(
        zip(mnist_image_batch, mnist_label_batch)):
    ax = fig.add_subplot(2, 5, index + 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.imshow(mnist_image[:, :, 0], cmap='gray_r')
    ax.set_title(str(mnist_label.numpy()), size=15)
plt.tight_layout()
plt.show()
