import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("marks.csv");

df

## Detecting NaN - missing data
df.isna().sum()
print(df['hours_studied'].mean());
print(df['marks_obtained'].mean());

## Replacing NaN - missing data

df['hours_studied'] = df['hours_studied'].fillna(df['hours_studied'].mean());
df['marks_obtained'] = df['marks_obtained'].fillna(df['marks_obtained'].mean());
df

X = df[['hours_studied']];
y = df[['marks_obtained']]

model = LinearRegression();

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42);

model.fit(X_train, y_train);

marks_predicted = model.predict([[6]]);

print(float(marks_predicted));

