# -*- coding: utf-8 -*-
"""Prac9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XABcN8WfR2fKBejxK14KZnuO1Y1wLd44

### **Titanic Vizualization**
"""

import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('titanic')

df.head()

df.info()

"""## **Box Plot**"""

sns.boxplot( y='age', data=df)

sns.boxplot( x='sex',y='age', data=df)

sns.boxplot( x='survived',y='age', data=df)

sns.boxplot( x='sex',y='age',hue='survived', data=df)