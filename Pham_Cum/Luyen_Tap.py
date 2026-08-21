import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, fcluster, linkage
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import load_iris


print('---------------- Dữ liệu Iris ----------------')
iris = load_iris()
iris_data = pd.DataFrame(iris.data, columns=iris.feature_names)
features = iris_data.iloc[:, 2:4]

print('Hai thuộc tính dùng để phân cụm: petal length và petal width')
print(features.head())

linkage_methods = ['complete', 'average', 'single']

for method in linkage_methods:
    print(f'------- Agglomerative Clustering: {method} linkage -------')
    model = AgglomerativeClustering(
        n_clusters=3,
        linkage=method,
        metric='euclidean',
    )
    cluster_labels = model.fit_predict(features)

    plt.figure(figsize=(7, 5))
    plt.scatter(features.iloc[:, 0], features.iloc[:, 1], c=cluster_labels)
    plt.title(f'Iris: {method} linkage')
    plt.xlabel('petal length (cm)')
    plt.ylabel('petal width (cm)')
    plt.show()

    print(pd.Series(cluster_labels).value_counts().sort_index())

print('---------------- Dendrogram ----------------')
linkage_iris = linkage(features, method='complete')
plt.figure(figsize=(20, 10))
dendrogram(linkage_iris)
plt.title('Iris: Dendrogram (complete linkage)')
plt.show()

labels_tree = fcluster(linkage_iris, 3, criterion='maxclust')
print('Số phần tử trong từng cụm:')
print(pd.Series(labels_tree).value_counts().sort_index())
