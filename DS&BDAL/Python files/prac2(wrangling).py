# -*- coding: utf-8 -*-
"""Prac2(wrangling).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FC0ZogjrkeubODO75i5U_3iWdSE_zuTJ

<a href="https://colab.research.google.com/github/PankajAgarwalS/TE-COMP-SEM-6/blob/main/Prac2.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
"""

import pandas as pd
import numpy as np
import seaborn as sns
url = "https://raw.githubusercontent.com/Sahil-Naik/TE-Programming/main/DSBDAL/Assignment-2/Academic%20Performance.csv"

df = pd.read_csv(url)

df.head()

df.info()

df.sample(5)

df.shape

df.describe()

df.isnull().sum()

df['Physics'] = df['Physics'].fillna(value=df['Physics'].mean())
df['Mathematics'] = df['Mathematics'].fillna(value=df['Mathematics'].mean())
df['AI'] = df['AI'].fillna(value=df['AI'].mean())

df.isnull().sum()

sns.boxplot(df['Physics'])

sns.boxplot(df['Mathematics'])

sns.boxplot(df['Chemistry'])

sns.boxplot(df['AI'])

Q1 = np.percentile(df['Physics'], 25, interpolation = 'midpoint')
Q3 = np.percentile(df['Physics'], 75, interpolation = 'midpoint')
IQR = Q3 - Q1

print("Old Shape of Dataset: {}".format(df.shape))

# Upper bound
upper = np.where(df['Physics'] >= (Q3+1.5*IQR))

# Lower bound
lower = np.where(df['Physics'] <= (Q1-1.5*IQR))

df.drop(upper[0], inplace = True)
df.drop(lower[0], inplace = True)

print("New Shape of Dataset: {}".format(df.shape))

Q1 = np.percentile(df['Chemistry'], 25, interpolation = 'midpoint')
Q3 = np.percentile(df['Chemistry'], 75, interpolation = 'midpoint')
IQR = Q3 - Q1

print("Old Shape of Dataset: {}".format(df.shape))

# Upper bound
upper = np.where(df['Chemistry'] >= (Q3+1.5*IQR))

# Lower bound
lower = np.where(df['Chemistry'] <= (Q1-1.5*IQR))

df.drop(upper[0], inplace = True)
df.drop(lower[0], inplace = True)

print("New Shape of Dataset: {}".format(df.shape))

sns.boxplot(df['Chemistry'])

df['DOB'] =  pd.to_datetime(df['DOB'])

df.info()

df['Birth_Year'] = pd.DatetimeIndex(df['DOB']).year   # Used to extract year from datetime65[ns] entity
df['Birth_Month'] = df['DOB'].dt.month_name(locale='English')

df