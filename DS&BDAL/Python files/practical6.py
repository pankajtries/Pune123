# -*- coding: utf-8 -*-
"""Practical6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1o58_sWCSKpG9x_jXsOjpFhvdoyu-33H8
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv")

X = data.drop(['class'], axis=1)
y = data.drop(['sepal length',  'sepal width',  'petal length',  'petal width'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)

model = GaussianNB()
model.fit(X_train, y_train.values.ravel())

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()

def get_confusion_matrix_values(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    return(cm[0][0], cm[0][1], cm[1][0], cm[1][1])

# Get confusion matrix values
TP, FP, FN, TN = get_confusion_matrix_values(y_test, y_pred)
print("TP:", TP)
print("FP:", FP)
print("FN:", FN)
print("TN:", TN)

print("The precision is ", TP/(TP+FP))
print("The recall is ", TP/(TP+FN))