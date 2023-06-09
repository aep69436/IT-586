# -*- coding: utf-8 -*-
"""APollock Final Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DRvuOwcqg5W9IpC9AO04Po_L3DyzkxtQ
"""

import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
df=pd.read_csv("Alzheimer_s_Disease_and_Healthy_Aging_Data.csv")
df=df.dropna(axis='columns', how='all')
df = df.drop(df.index[df['High_Confidence_Limit'] == 100])
df = df.drop(df.index[df['Data_Value'] == '.'])
df=df.dropna()

from sklearn.model_selection import train_test_split
X=df[['High_Confidence_Limit']]
y=df['Data_Value']
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline
plt.scatter(X_train, y_train, s=5)
plt.xlabel('X')
plt.ylabel('y')

model = LinearRegression()
df=df.dropna()
model.fit(X_train,y_train)
model.score(X_train, y_train)

pred=model.predict(X_train)

plt.scatter(X_train, y_train, s=5)
plt.plot(X_train, pred, color='red')
plt.xlabel('X Train')
plt.ylabel('y Train')
plt.show()

pred=model.predict(X_test)

plt.scatter(X_test, y_test, s=5)
plt.plot(X_test, pred, color='red')
plt.xlabel('X Test')
plt.ylabel('y Predictions')
plt.show()

from sklearn.metrics  import mean_squared_error 
mean_squared_error(y_test, pred)

