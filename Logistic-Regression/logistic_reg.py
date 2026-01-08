import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

df = pd.read_csv("logis_reg.csv");

df

df.isna().sum() ## Verifying any null data

df[df['Has_Disease']==0]

encoder = LabelEncoder();

df['Smoker'] = encoder.fit_transform(df['Smoker']);

X = df[['Age', 'BMI', 'BloodPressure', 'Smoker']];
y = df[['Has_Disease']];

model = LogisticRegression();

X_train , X_test, y_train, y_test = train_test_split(X,y,test_size=0.20 ,random_state=42);

model.fit(X_train,y_train);
result = model.predict([[32,60,145,0]])[0];
# print(result);
if(result == 0):
  print("User is fit and fine");
else:
  print("User has desease");

y_pred = model.predict(X_test);
print(f"Accuracy : {accuracy_score(y_test, y_pred)}");

print(f"Precision: {precision_score(y_test, y_pred)}");
print(f"Recall: {recall_score(y_test, y_pred)}");
print(f"F1-Score: {f1_score(y_test, y_pred)}");

print(f"Precision: {confusion_matrix(y_test, y_pred)}");

