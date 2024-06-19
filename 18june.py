# -*- coding: utf-8 -*-
"""18june.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WeIz_Xln-GDXJuv1YKAZUayhoDdy7ddx
"""

import pandas as pd
import numpy as np

df=pd.read_csv("tips.csv")
df

df.head(2)

df.isnull().sum()

x=df.drop(columns=['size'],axis=1)
y=df['size']

print("dataframe shape = " , df.shape)
print("Independent data shape = " , x.shape)
print("Dependent data shape = " , y.shape)

from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size = 0.2 , random_state = 42)

print("X_train  data shape = " , x_train.shape)
print("X_test  data shape = " , x_test.shape)
print("Y_train data shape = " , y_train.shape)
print("Y_test data shape = " , y_test.shape)

np.round(x_train.describe(),2)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

# Normalization
from sklearn.preprocessing import MinMaxScaler

mn = MinMaxScaler()

# Encoding ===> Convert categorical data into numerical data .

# Gender ===> Male(0) , Female(1)

# Grade ===> A(0) , B(1) , C(2)

# (1). LabelEncoding ==> Single data ..

df

df=df.dropna()

from sklearn.preprocessing import LabelEncoder

lb=LabelEncoder()

df['sex'] = lb.fit_transform(df['sex'])
df['smoker'] = lb.fit_transform(df['smoker'])
df['day'] = lb.fit_transform(df['day'])
df['time'] = lb.fit_transform(df['time'])

df.head(4)

x=df.drop(columns=['size'])

y=df['size']

from sklearn.model_selection import train_test_split

x_train , x_test , y_train, y_test = train_test_split(x,y,test_size = 0.2 , random_state = 42)

from sklearn.preprocessing import MinMaxScaler

mn=MinMaxScaler()

x_train_mn = mn.fit_transform(x_train)

x_train_new = pd.DataFrame(x_train_mn , columns = x_train.columns)

x_train_new

np.round(x_train_new.describe() , 1)

