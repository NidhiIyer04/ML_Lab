# -*- coding: utf-8 -*-
"""Play_Tennis_Decision_Tree.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q3ouQNAROgXf8AFoIn24CvzMI35JKC-h

#  Load libraries
"""

# Load libraries
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

"""# Importing the Dataset"""

df=pd.read_csv("/content/Play Tennis.csv")
df

"""# Data Analysis"""

len(df)           #Dataset Lenght

df.shape  #To see the number of rows and columns in our dataset:

df.head()         #To inspect the first five records of the dataset:

df.tail()         #To inspect the last five records of the dataset:

df.info()

df.describe()     #To see statistical details of the dataset:

"""# Preparing the Data (Data Slicing)"""

#machine learning algorithms can only learn from numbers (int, float, doubles .. )
#so let us encode it to int
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for col in df.columns:
    df[col] = le.fit_transform(df[col])
df

#To divide our data into attribute set and Label:
X = df.drop(['Play_Tennis', 'Day'], axis=1)
y = df['Play_Tennis']

X

#To divide our data into training and test sets:
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10)

X_train.shape

"""# Training and Making Predictions"""

# perform training
from sklearn.tree import DecisionTreeClassifier                             # import the classifier
classifier =DecisionTreeClassifier(criterion="entropy", random_state=100)     # create a classifier object
classifier.fit(X_train, y_train)                                              # fit the classifier with X and Y data or

# Plot the decision tree
import matplotlib.pyplot as plt
from sklearn import tree
plt.figure(figsize=(12,8))
tree.plot_tree(classifier, feature_names=X.columns, class_names=['No', 'Yes'], filled=True)
plt.show()

#Predict the response for test dataset
y_pred= classifier.predict(X_test)
results=X_test.copy()
results['Actual']=y_test
results['Predicted']=y_pred
value=X.columns
results

sample = [[2, 1, 0, 0]]
prediction = classifier.predict(sample)
print(prediction)

# Model Accuracy, how often is the classifier correct?
from sklearn.metrics import accuracy_score
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

"""- Now let's compare some of our predicted values with the actual values and see how accurate we were:

# Evaluating the Algorithm
"""

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))

print(classification_report(y_test, y_pred))