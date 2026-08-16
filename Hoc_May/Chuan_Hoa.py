from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

data = load_breast_cancer()
x_train, x_test, y_train, y_test = train_test_split(data['data'], data['target'], random_state=42) 

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = DecisionTreeClassifier(criterion='entropy')
model.fit(x_train, y_train)
print(model.score(x_test, y_test))

# Tương tự bên kia (Sửa dụng để xem nó có tốt hơn không)

