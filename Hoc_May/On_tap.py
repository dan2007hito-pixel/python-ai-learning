from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

digits = load_digits()
x = digits.data
y = digits.target
print(pd.DataFrame(x))


x_train, x_test, y_train, y_test = train_test_split(digits['data'], digits['target'], random_state=42)

model = DecisionTreeClassifier(criterion='entropy')

model.fit(x_train, y_train)

value = model.score(x_test, y_test)
print('Độ chính xác: ', value * 100, '%')




# Dự đáo và đáp án thật
print('--------------Dự đoán và đáp án---------------')

y_pred = model.predict(x_test)
y_pred_2d = y_pred.reshape(len(y_pred),1)
y_test_2d = y_pred.reshape(len(y_test),1)

df1 = pd.DataFrame(y_pred_2d, columns=['pred'])
df2 = pd.DataFrame(y_test_2d, columns=['real'])

df_concat = pd.concat([df1, df2], axis=1)
print(df_concat)

# Thử in ảnh ra

# Xem 1 ảnh
# plt.imshow(digits['images'][0], cmap='gray')
# plt.show()

# Xem nhiều ảnh
fig, axes = plt.subplots(2, 5)

for i, ax in enumerate(axes.ravel()):
    ax.imshow(digits['images'][i], cmap='gray')
    ax.set_title(f"Real: {digits['target'][i]}")
    ax.axis('off')

plt.show()