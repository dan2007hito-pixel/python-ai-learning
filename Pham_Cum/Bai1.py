# Phân cụm: Kỹ thuật phân chia dữ liệu chưa được gắn nhãn và chưa được
# phân loại thành các nhóm tương tự dựa trên các giá trị được quan sát đã cho

# 1. Phân cụm theo phân cấp
# a. Phân cụm tích tụ
# Từ dưới lên
# Bắt đầu với n cụm để dần dần kết tụ các cụm tương tự cho đến khi
# không còn lại một cụm cuối cùng
#
# b. Phân cụm chia
# Từ trên xuống
# Bắt đầu từ 1 cụm duy nhất bao gồm tất cả các bản ghi
# và chia dần thành n cụm


from sklearn.datasets import make_blobs, make_moons
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2,2)
# ============================================================
# 1. DATASET MAKE_BLOBS - DỮ LIỆU GỐC
# ============================================================

x1, label1 = make_blobs(
    n_samples=200,
    n_features=2,
    centers=2,
    cluster_std=5,
    random_state=123
)

ax[0,0].scatter(x1[:, 0], x1[:, 1], c=label1, alpha=0.7)
ax[0,0].set_title('Dataset #1: Original')


# ============================================================
# 2. DATASET MAKE_MOONS - DỮ LIỆU GỐC
# ============================================================

x2, label2 = make_moons(
    n_samples=200,
    noise=0.08,
    random_state=123
)

ax[0,1].scatter(x2[:, 0], x2[:, 1], c=label2, alpha=0.7)
ax[0,1].set_title('Dataset #2: Original')

# ============================================================
# 3. AGGLOMERATIVE CLUSTERING - MAKE_BLOBS
# ============================================================

from sklearn.cluster import AgglomerativeClustering
import pandas as pd


aggle = AgglomerativeClustering(n_clusters=4)
aggle.fit(x1)

myColor = {
    0: 'red',
    1: 'blue',
    2: 'green',
    3: 'yellow'
}

ax[1,0].scatter(
    x1[:, 0],
    x1[:, 1],
    c=pd.Series(aggle.labels_).apply(lambda x: myColor[x]),
    alpha=0.7
)

ax[1,0].set_title('Dataset make_blobs: AgglomerativeClustering')

# ============================================================
# 4. AGGLOMERATIVE CLUSTERING - MAKE_MOONS
# ============================================================

aggle_moons = AgglomerativeClustering(n_clusters=2, linkage='single')
aggle_moons.fit(x2)

myColor_moons = {
    0: 'red',
    1: 'blue'
}

ax[1,1].scatter(
    x2[:, 0],
    x2[:, 1],
    c=pd.Series(aggle_moons.labels_).apply(
        lambda x: myColor_moons[x]
    ),
    alpha=0.7
)

ax[1,1].set_title('Dataset make_moons: AgglomerativeClustering')
plt.show()

from scipy.cluster.hierarchy import fcluster, dendrogram, linkage
myLinkage = linkage(x1,method='complete')
plt.figure(figsize=(20,5))
dendrogram(myLinkage)
plt.title('Dataset make_blobs: Dendrogram')
plt.show()

lables = fcluster(myLinkage, 5, criterion='maxclust')
print(pd.Series(lables).value_counts())



myLinkage_moons = linkage(x2,method='single')
plt.figure(figsize=(20,5))
dendrogram(myLinkage_moons)
plt.title('Dataset make_moons: Dendrogram')
plt.show()

lables_moons = fcluster(myLinkage_moons, 2, criterion='maxclust')
print(pd.Series(lables_moons).value_counts())