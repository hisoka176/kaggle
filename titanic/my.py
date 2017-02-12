# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import os
import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import csv

# <codecell>

import IPython.nbformat.current as nbf
nova = nbf.read(open('my.ipynb','r'),'ipynb')
nbf.write(nova,open('my.py','w'),'py')

# <headingcell level=2>

# test_df.Pclass.value_counts()
# np.unique(test_df.Age)
# np.unique(test_df.SibSp)
# np.unique(test_df.Parch)
# test_df.loc[test_df.Fare.isnull(),['Fare']]
# test_new_em = pd.get_dummies(test_df.Embarked,prefix='Embarked')
# test_df.drop(['Embarked'])
# test_df.join(test_new_em)
# test_df.head(3)

# <codecell>

# train the model
from sklearn.linear_model import LogisticRegression

train_df = pd.read_csv('data/train.csv',header=0)
test_df = pd.read_csv('data/test.csv',header=0)

new_test_dm = pd.get_dummies(test_df.Embarked,prefix='Embarked')
test_df.drop(['Embarked'],axis=1,inplace=True)
test_df = test_df.join(new_test_dm)

new_em = pd.get_dummies(train_df.Embarked,prefix='Embarked')
train_df.drop(['Embarked'],axis=1,inplace=True)
train_df = train_df.join(new_em)




clf = LogisticRegression()
train_data = train_df.loc[:,['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked_C','Embarked_Q','Embarked_S']]
train_label = train_df.loc[:,['Survived']]

test_data = test_df.loc[:,['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked_C','Embarked_Q','Embarked_S']]
test_label = test_df.loc[:,['Survived']]



total_data = train_data.append(test_data)

new_sex = pd.get_dummies(total_data['Sex'],prefix='Sex')
total_data.drop(['Sex'],axis=1,inplace=True)
total_data = total_data.join(new_sex)

total_data.Age = total_data.Age.fillna(total_data.Age.mode().tolist()[0])
total_data.Fare = total_data.Fare.fillna(total_data.Fare.mode().tolist()[0])

from sklearn.preprocessing import MinMaxScaler

train_lengh = len(train_data)
test_length = len(test_data)

total_array_data = total_data.values
train_array_data= total_array_data[:train_lengh,:]
test_array_data = total_array_data[train_lengh:,:]

train_array_label = train_label.values
test_array_label = test_label.values

# <codecell>

total_data.head(3)

# <codecell>

total_data.head(3)

# <markdowncell>


