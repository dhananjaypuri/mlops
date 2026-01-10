import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error
import numpy as np

## Load CSV
df = pd.read_csv("student_marks_project1.csv");

df.head()
## check if there is any null data

df.isnull().sum()

## Create a new column Pass and Fain depending upon marks

df['Result'] = df['Final_Marks'].apply(lambda x: 'Pass' if x>=33 else 'Fail');
# print(df[df['Final_Marks']<33]);
df['Result'] = df['Result'].replace({'Pass': 1, 'Fail': 0});
## Create Model 1 to predict marks

XReg = df[['Study_Hours_Per_Day', 'Previous_Exam_Marks']];
yReg = df['Final_Marks'];

reg_model = LinearRegression();

XReg_train, XReg_test, yReg_train, yReg_test = train_test_split(XReg,yReg,test_size=0.2,random_state=42);

reg_model.fit(XReg_train, yReg_train);

# df[(df['Study_Hours_Per_Day'] < 3) & (df['Final_Marks'] < 45)][['Final_Marks', 'Study_Hours_Per_Day']]

## Create Model 2 to predict Result
X_clf = XReg;
yclf = df['Result'];

clf_model = LogisticRegression();

Xclf_train, Xclf_test, yclf_train, yclf_test = train_test_split(X_clf,yclf,test_size=0.2,random_state=42);

clf_model.fit(Xclf_train, yclf_train);

new_input = [[1,50]];
print(reg_model.predict(new_input));

print(clf_model.predict(new_input));
