# -*- coding: utf-8 -*-
"""Loan approval predictor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K8nTDCw9Lo2sPMVkxpk4zdWxLnMrtvUd
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)

# Importing the dataset
dataset = pd.read_csv('/content/gdrive/MyDrive/Loan predict.csv')
dataset.head()

# Understanding dataset informations
dataset.info()

# Visualizing the dataset
sns.countplot(x='Loan_Status', data=dataset, palette = 'Set2')

sns.countplot(x='Married', data=dataset, palette = 'Set1')

sns.countplot(x='Gender', data=dataset, palette = 'Set3')

gender = dataset.groupby(['Gender', 'Loan_Status']).Loan_Status.count().unstack()
gender.plot(kind='bar')

gender = dataset.groupby(['Gender', 'Loan_Status']).Loan_Status.count().unstack()
gender.plot(kind='bar')

married = dataset.groupby(['Married', 'Loan_Status']).Loan_Status.count().unstack()
married.plot(kind='bar')

education = dataset.groupby(['Education', 'Loan_Status']).Loan_Status.count().unstack()
education.plot(kind='bar')

credit = dataset.groupby([ 'Credit_History', 'Loan_Status'  ]).Loan_Status.count().unstack()
credit.plot(kind='bar')

area = dataset.groupby(['Property_Area', 'Loan_Status']).Loan_Status.count().unstack()
area.plot(kind='bar')

dependents = dataset.groupby(['Dependents', 'Loan_Status']).Loan_Status.count().unstack()
dependents.plot(kind='bar')

# let's plot pair plot to visualise the attributes all at once
sns.pairplot(data=dataset, hue = 'Loan_Status')

# Check the number of missing values in each column using Integer
dataset.isnull().sum()

dataset.nunique()

df= dataset.copy()

# Replacing missing values with most frequent value of the particular column
df['Gender'].fillna(df['Gender'].value_counts().idxmax(), inplace=True)
df['Married'].fillna(df['Married'].value_counts().idxmax(), inplace=True)
df['Dependents'].fillna(df['Dependents'].value_counts().idxmax(), inplace=True)
df['Self_Employed'].fillna(df['Self_Employed'].value_counts().idxmax(), inplace=True)
df["LoanAmount"].fillna(df["LoanAmount"].mean(skipna=True), inplace=True)
df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].value_counts().idxmax(), inplace=True)
df['Credit_History'].fillna(df['Credit_History'].value_counts().idxmax(), inplace=True)

df.isnull().sum()

# Replacing '3+' with '3'
dependents_stat = {'0':0,'1':1,'2':2,'3+':3}
df['Dependents'] = df['Dependents'].replace(dependents_stat)
df.head()

cols = ['Gender', 'Married', 'Education', 'Self_Employed' , 'Loan_Status']

# Encode labels of multiple columns at once
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df[cols] = df[cols].apply(LabelEncoder().fit_transform)
df.head()

# Understanding the distribution of Loan status approval where 1 means approved
df['Loan_Status'].value_counts()

sns.heatmap(df.corr())

X = df.iloc[:,1:12].values
Y = df.iloc[: ,12].values
print (Y)

print(X)

#One-hot encoding categorical attribute 'Property_Area' 
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [10])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
X = X[:, 1:]
print(X)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, stratify=Y, random_state = 0)
print(X.shape, X_train.shape, X_test.shape)

# Random Forest Classifier
# Fitting Random Forest Classification to the Training set 
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 55, criterion =  'entropy', random_state = 0)
classifier.fit(X_train, Y_train)

# Predicting the Random Forest Classifier for both train and test data
Y_pred = classifier.predict(X_test)
Y_train_pred = classifier.predict(X_train)

#Making the confusion matrix for test data
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)
print(cm)

# Visualizing the confusion matrix
import seaborn as sns
sns.heatmap(cm, annot=True)

#Performance metrics for both the training and testing data

# Accuracy 
from sklearn.metrics import accuracy_score
training_data_accuracy = accuracy_score(Y_train_pred, Y_train)
print('Accuracy on Training data is %f' % training_data_accuracy)
accuracy = accuracy_score(Y_test, Y_pred)
print('Accuracy on Test data is %f' % accuracy)

#Precision
from sklearn.metrics import precision_score
training_data_precision = precision_score(Y_train_pred, Y_train)
print('Precision on Training data is %f' % training_data_precision)
precision = precision_score(Y_test, Y_pred)
print('Precision on Test data is %f' % precision)
 
# Recall
from sklearn.metrics import recall_score
training_data_recall = recall_score(Y_train_pred, Y_train)
print('Recall on Training data is %f' % training_data_recall)
recall = recall_score(Y_test, Y_pred)
print('Recall on Test data is %f' % recall)

