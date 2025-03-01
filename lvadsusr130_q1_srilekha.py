# -*- coding: utf-8 -*-
"""LVDASUSR130_Q1_srilekha.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/148as-RkfQjxBRW5oZ3rkgJaIPrVCb-WG
"""

import pandas as pd
d = pd.read_csv('loan_approval.csv')
d.info()
d.isnull().sum()
d.head(2)

from matplotlib import pyplot as plt
d[' loan_amount'].plot(kind='hist', bins=20, title=' amount')
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
d.plot(kind='scatter', x=' income_annum', y=' loan_amount', s=30, alpha=.7)
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
import seaborn as sns
d.groupby(' loan_status').size().plot(kind='bar', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
import seaborn as sns
d.groupby(' education').size().plot(kind='bar', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

dup= d.duplicated(keep=False)
d['dup_bool'] = dup
print(d[d['dup_bool'] == True].count())
d.drop('dup_bool',axis=1)
d.head(1)

from sklearn.preprocessing import LabelEncoder

lb = LabelEncoder()
d[' education'] = lb.fit_transform(d[' education'])
d[' self_employed'] = lb.fit_transform(d[' self_employed'])
d[' loan_status'] = lb.fit_transform(d[' loan_status'])

from sklearn.model_selection import train_test_split


m = d.drop(['loan_id',' loan_status'],axis=1)
n = d[' loan_status']

m_train, m_test, n_train, n_test = train_test_split(m,n,test_size=0.44, random_state=49)

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
import xgboost as xgb
from sklearn.metrics import accuracy_score, classification_report

algorithms = ['Decision tree','Logistic','RandomForest', 'XGB']
a=[]

de = DecisionTreeClassifier()
de.fit(m_train,n_train)
n_pred = de.predict(m_test)
accu= accuracy_score(n_test, n_pred)
print("Accuracy of decision tree:", accu)
print(classification_report(n_test, n_pred))
a.append(round(accu*100,2))


lo = LogisticRegression()
lo.fit(m_train,n_train)
n_pred = lo.predict(m_test)
accu = accuracy_score(n_test, n_pred)
print("Accuracy of logistic tree:", accu)
print(classification_report(n_test, n_pred))
a.append(round(accu*100,2))


Ra = RandomForestClassifier()
Ra.fit(m_train,n_train)
n_pred = Ra.predict(m_test)
accu = accuracy_score(n_test, n_pred)
print("Accuracy of randomforest:", accu)
print(classification_report(n_test, n_pred))
a.append(round(accu*100,2))


xg= xgb.XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=44)
xg.fit(m_train, n_train)
n_pred = xg.predict(m_test)
accu= accuracy_score(n_test, n_pred)
print("Accuracy of XGB:", accu)
print(classification_report(n_test, n_pred))
a.append(round(accu*100,2))

a