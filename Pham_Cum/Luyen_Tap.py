from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

iris = load_iris()
iris_data = iris.data
iris_data_pd = pd.DataFrame(iris_data, columns=iris.feature_names)
print(iris.target)

linkage=["complete", "average", "single"]

for idx, i in enumerate(linkage):
    plt.figure(idx)
    hier = AgglomerativeClustering(n_clusters=3, linkage=i, metric="euclidean")
    hier.fit(iris_data_pd.iloc[:, 2:4])
    plt.scatter(iris_data_pd.iloc[:, 2], iris_data_pd.iloc[:, 3], c=hier.labels_)
    plt.title("Clustering" + i)
    plt.xlabel('petal length')
    plt.ylabel('petal width')
    plt.show()
    
from scipy.cluster import hierarchy

hierar = hierarchy.linkage(iris_data_pd.iloc[:, 2:4], 'complete')
plt.figure(figsize=(20,10))
dh = dendrogram(hierar)
plt.show()


labels = fcluster(hierar, 3, criterion='maxclust')
pd.Series(labels).value_counts()

hierar.data