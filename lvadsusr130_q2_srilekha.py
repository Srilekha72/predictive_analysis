# -*- coding: utf-8 -*-
"""LVDASUSR130_Q2_srilekha.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10uCJO-VzGki7yAEnNyIu5XNGj0N6qEYq
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
from sklearn.linear_model import LinearRegression
d=pd.read_csv('auto-mpg.csv')
d.shape
d.isnull().sum()

d=d.dropna()
d.isnull().sum()
d.duplicated().sum()
d.info()
d.head()

d['horsepower'] = d['horsepower'].str.replace(r'\D', '')
d['horsepower'] = pd.to_numeric(d['horsepower'])
d=d.dropna()
d.info()

sns.boxplot(d)

Q1 = d.quantile(0.25)
Q3 = d.quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

cleaned= d[~((d < lower_bound) | (d > upper_bound)).any(axis=1)]

print(cleaned)
d=cleaned

plt.figure(figsize=(7, 5))
sns.distplot(d['mpg'])
plt.title('mpgs distribution')
plt.xlabel('Miles per Gallon(mpg)')
plt.ylabel('mass/volume')
plt.show()

d.drop('car name',axis=1,inplace=True)
d.head()
d['cylinders'].value_counts()

d['origin'].value_counts()

corr_matrix = d.corr()

corr_mpg = corr_matrix['mpg'].drop('mpg')

print("Correlation according to 'mpg':")
print(corr_mpg)
sns.heatmap(d.corr(),annot=True)

sns.pairplot(d[['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration']])
plt.show()
m=d.iloc[:,1:]
n=d.iloc[:,0]

from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
m_train, m_test, n_train, n_test = train_test_split(m, n, test_size=0.5, random_state=49)
l= LinearRegression()
l.fit(m_train, n_train)
n_pred = l.predict(m_test)
mse = mean_squared_error(n_test, n_pred)
r2 = r2_score(n_test, n_pred)
mae=mean_absolute_error(n_test, n_pred)
print( mse)
print( r2)
print( mae)
plt.scatter(n_test, n_pred, color='green', label='original vs expected')
plt.plot([n_test.min(), n_test.max()], [n_test.min(), n_test.max()], color='blue', linestyle='-', label='Regression-Line')
plt.xlabel('real mpg')
plt.ylabel('expected mpg')
plt.title('expected vs. original mpg')
plt.legend()
plt.show()