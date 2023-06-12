import pandas as pd
from matplotlib import pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from joblib import dump

df = pd.read_csv("data.csv") 

# X represent the first to the before the last column of the csv. It means all the caracteristics
X_train = df.iloc[:, 0:-1].values

# y represent the column class: 0 false 1 true
y_train = df.iloc[:, -1].values

#here we build the model
model = linear_model.LogisticRegression()
model.fit(X_train,y_train)
dump(model,'model_saved.joblib')

# #la prediction
# #la partie test
# df_test = pd.read_csv("false.csv")
# X_test = df_test.iloc[:,0:-1].values
# y_test = df_test.iloc[:,-1].values

# prediction = model.predict(X_test)
# print(prediction)

# # confusion matrix
# cm = confusion_matrix(y_test, prediction)
# print(cm)

# # accuracy score
# score = accuracy_score(y_test, prediction)
# print("score: ", score)
