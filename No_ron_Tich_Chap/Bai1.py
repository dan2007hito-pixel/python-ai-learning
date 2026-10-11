"""Bai 1: Tich chap 1D va CNN phan loai chu so MNIST."""

import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt


def conv1d(x, w, p=0, s=1):
    """Tinh tich chap 1D voi padding p va stride s."""
    if p < 0 or s <= 0:
        raise ValueError("p phai >= 0 va s phai > 0")

    w_rot = np.asarray(w[::-1])
    x_padded = np.asarray(x)
    if p > 0:
        zero_pad = np.zeros(p, dtype=x_padded.dtype)
        x_padded = np.concatenate((zero_pad, x_padded, zero_pad))

    if len(w_rot) > len(x_padded):
        return np.array([])

    result = []
    for i in range(0, len(x_padded) - len(w_rot) + 1, s):
        result.append(np.sum(x_padded[i:i + len(w_rot)] * w_rot))
    return np.asarray(result)


def main():
    # Vi du tich chap 1D
    x = [1, 3, 2, 4, 5, 6, 1, 3]
    w = [1, 0, 3, 1, 2]
    print("Ket qua conv1d:", conv1d(x, w, p=2, s=1))

    # Tai va tien xu ly MNIST
    mnist_builder = tfds.builder("mnist")
    mnist_builder.download_and_prepare()
    datasets = mnist_builder.as_dataset(shuffle_files=False)
    mnist_train_origin = datasets["train"]
    mnist_test_origin = datasets["test"]

    buffer_size = 1000
    batch_size = 64
    num_epochs = 20

    def preprocess(item):
        image = tf.cast(item["image"], tf.float32) / 255.0
        label = tf.cast(item["label"], tf.int32)
        return image, label

    mnist_train = mnist_train_origin.map(preprocess)
    mnist_test = mnist_test_origin.map(preprocess)

    tf.random.set_seed(1)
    mnist_train = mnist_train.shuffle(
        buffer_size, reshuffle_each_iteration=False
    )
    mnist_valid = mnist_train.take(10000).batch(batch_size)
    mnist_train = mnist_train.skip(10000).batch(batch_size)

    # Xay dung CNN
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(
            filters=32, kernel_size=(5, 5), strides=(1, 1),
            padding="same", data_format="channels_last",
            name="conv_1", activation="relu",
        ),
        tf.keras.layers.MaxPool2D(pool_size=(2, 2), name="pool_1"),
        tf.keras.layers.Conv2D(
            filters=64, kernel_size=(5, 5), strides=(1, 1),
            padding="same", data_format="channels_last",
            name="conv_2", activation="relu",
        ),
        tf.keras.layers.MaxPool2D(pool_size=(2, 2), name="pool_2"),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(units=1024, name="fc_1", activation="relu"),
        tf.keras.layers.Dropout(rate=0.5),
        tf.keras.layers.Dense(units=10, name="fc_2", activation="softmax"),
    ])

    print("Kich thuoc dau ra:", model.compute_output_shape((None, 28, 28, 1)))
    tf.random.set_seed(1)
    model.build(input_shape=(None, 28, 28, 1))
    model.compile(
        optimizer=tf.keras.optimizers.Adam(),
        loss=tf.keras.losses.SparseCategoricalCrossentropy(),
        metrics=["accuracy"],
    )

    history = model.fit(
        mnist_train,
        epochs=num_epochs,
        validation_data=mnist_valid,
        shuffle=True,
    )

    # Ve loss va accuracy trong qua trinh huan luyen
    hist = history.history
    epochs = np.arange(1, len(hist["loss"]) + 1)
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    axes[0].plot(epochs, hist["loss"], "-o", label="Train loss")
    axes[0].plot(epochs, hist["val_loss"], "--<", label="Validation loss")
    axes[0].set(xlabel="Epoch", ylabel="Loss")
    axes[0].legend()
    axes[1].plot(epochs, hist["accuracy"], "-o", label="Train accuracy")
    axes[1].plot(epochs, hist["val_accuracy"], "--<", label="Validation accuracy")
    axes[1].set(xlabel="Epoch", ylabel="Accuracy")
    axes[1].legend()
    plt.tight_layout()
    plt.show()

    # Danh gia tren tap test
    test_loss, test_accuracy = model.evaluate(mnist_test.batch(20))
    print("Test accuracy: {:.2f}%".format(test_accuracy * 100))

    # Du doan va hien thi 12 anh dau tien trong tap test
    batch_test = next(iter(mnist_test.batch(12)))
    predictions = model.predict(batch_test[0], verbose=0)
    predicted_labels = tf.argmax(predictions, axis=1)
    print("Nhan du doan:", predicted_labels.numpy())

    fig = plt.figure(figsize=(12, 4))
    for i in range(12):
        ax = fig.add_subplot(2, 6, i + 1)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.imshow(batch_test[0][i, :, :, 0], cmap="gray_r")
        ax.set_title("Du doan: {}\nNhan: {}".format(
            predicted_labels[i].numpy(), batch_test[1][i].numpy()
        ))
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
