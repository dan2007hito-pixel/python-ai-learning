import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, fcluster, linkage
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs, make_moons


# Phân cụm là kỹ thuật chia dữ liệu chưa gắn nhãn thành các nhóm có đặc điểm
# tương tự nhau.
#
# Phân cụm phân cấp:
# - Tích tụ (bottom-up): bắt đầu từ từng điểm dữ liệu rồi gộp dần thành cụm.
# - Chia (top-down): bắt đầu từ một cụm lớn rồi tách dần thành các cụm nhỏ.


print('---------------- Dữ liệu mẫu ----------------')

# Dữ liệu gồm các cụm tách biệt rõ ràng.
x_blobs, labels_blobs = make_blobs(
    n_samples=200,
    n_features=2,
    centers=4,
    cluster_std=1.5,
    random_state=123,
)

# Dữ liệu có dạng hai nửa vòng tròn.
x_moons, labels_moons = make_moons(
    n_samples=200,
    noise=0.08,
    random_state=123,
)

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

axes[0, 0].scatter(x_blobs[:, 0], x_blobs[:, 1], c=labels_blobs, alpha=0.7)
axes[0, 0].set_title('make_blobs: nhãn gốc')

axes[0, 1].scatter(x_moons[:, 0], x_moons[:, 1], c=labels_moons, alpha=0.7)
axes[0, 1].set_title('make_moons: nhãn gốc')

print('------- Agglomerative Clustering: make_blobs -------')
model_blobs = AgglomerativeClustering(n_clusters=4)
labels_blobs_pred = model_blobs.fit_predict(x_blobs)

axes[1, 0].scatter(x_blobs[:, 0], x_blobs[:, 1], c=labels_blobs_pred, alpha=0.7)
axes[1, 0].set_title('make_blobs: phân cụm tích tụ')
print(pd.Series(labels_blobs_pred).value_counts().sort_index())

print('------- Agglomerative Clustering: make_moons -------')
model_moons = AgglomerativeClustering(n_clusters=2, linkage='single')
labels_moons_pred = model_moons.fit_predict(x_moons)

axes[1, 1].scatter(x_moons[:, 0], x_moons[:, 1], c=labels_moons_pred, alpha=0.7)
axes[1, 1].set_title('make_moons: phân cụm tích tụ')
print(pd.Series(labels_moons_pred).value_counts().sort_index())

plt.tight_layout()
plt.show()

print('---------------- Dendrogram ----------------')

linkage_blobs = linkage(x_blobs, method='complete')
plt.figure(figsize=(20, 5))
dendrogram(linkage_blobs)
plt.title('make_blobs: Dendrogram (complete linkage)')
plt.show()

labels_blobs_tree = fcluster(linkage_blobs, 4, criterion='maxclust')
print('Số phần tử trong từng cụm của make_blobs:')
print(pd.Series(labels_blobs_tree).value_counts().sort_index())

linkage_moons = linkage(x_moons, method='single')
plt.figure(figsize=(20, 5))
dendrogram(linkage_moons)
plt.title('make_moons: Dendrogram (single linkage)')
plt.show()

labels_moons_tree = fcluster(linkage_moons, 2, criterion='maxclust')
print('Số phần tử trong từng cụm của make_moons:')
print(pd.Series(labels_moons_tree).value_counts().sort_index())
