import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# reading csv file and exttracting class column to y.
data = pd.read_csv("UNSW_NB15_training-set.csv")

print(data.shape)
print(data.head())

# Preprocessing the data
data_enc = data.apply(LabelEncoder().fit_transform)
print(data_enc)

x = data_enc.drop('label', axis=1)
y = data_enc['label']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)
svc_cl = SVC(kernel='linear')
svc_cl.fit(x_train, y_train)

y_pred = svc_cl.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
