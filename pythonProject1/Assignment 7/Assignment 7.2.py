import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report

df = pd.read_csv('suv.csv')

# feature variable X ['Age','EstimatedSalary']
X = df[['Age','EstimatedSalary']]

# target variable y ['Purchased']
y = df['Purchased']

# split dataset into 80-20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Scale feature using StandardScaler
scaler  = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# train model using DecisionTreeClassifier with entropy
dt_entropy = DecisionTreeClassifier(criterion='entropy')
dt_entropy.fit(X_train, y_train)
y_pred_entropy = dt_entropy.predict(X_test)


# Confusion matrix and classification report
dt_entropy_conf = confusion_matrix(y_test, y_pred_entropy)
print(f'Confusion Matrix Entropy: {dt_entropy_conf}')

dt_entropy_class = classification_report(y_test, y_pred_entropy)
print(f'Classification Report Entropy: {dt_entropy_class}')



# Again train model using DecisionTreeClassifier with gini
dt_gini = DecisionTreeClassifier(criterion='gini')
dt_gini.fit(X_train, y_train)
y_pred_gini = dt_gini.predict(X_test)

# Confusion matrix and classification report gini
dt_gini_conf = confusion_matrix(y_test, y_pred_gini)
print(f'Confusion Matrix Gini: {dt_gini_conf}')

dt_gini_class = classification_report(y_test, y_pred_gini)
print(f'Classification Report Gini: {dt_gini_class}')

'''
The entropy model made 6 mistakes in both directions—wrongly labeling positives and missing actual positives. 
The gini model also made 6 false positives but only 4 false negatives, meaning it was a bit better at spotting class 1.

For class 0, both models made the same number of mistakes (6 false positives).

Overall, the gini model did a better job, with 88% accuracy, compared to 85% for entropy.

Gini was a little more accurate when identifying negatives (class 0) and slightly better at recognizing class 1.



'''