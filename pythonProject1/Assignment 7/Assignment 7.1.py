import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report


df = pd.read_csv('data_banknote_authentication.csv')

# Selecting feature and target variables as X and y
X = df.drop(columns=['class'])
y = df['class']

# split dataset into 80/20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)


# Train SVM Model Linear
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)
y_pred = svm_model.predict(X_test)

# compute confusion matrix and classification report
conf_matrix = confusion_matrix(y_test, y_pred)
print(f'Confusion Matrix (Kernel=Linear): {conf_matrix}')

class_report = classification_report(y_test, y_pred)
print(f'Classification Report (Kernel=Linear): {class_report}')


# Train SVM model RBF
svm_model_rbf = SVC(kernel='rbf')
svm_model_rbf.fit(X_train, y_train)
y_pred_rbf = svm_model_rbf.predict(X_test)

# compute confusion matrix and classification report for rbf kernel
conf_matrix_rbf = confusion_matrix(y_test, y_pred_rbf)
print(f'Confusion Matrix (Kernel=RBF): {conf_matrix_rbf}')

class_report_rbf = classification_report(y_test, y_pred_rbf)
print(f'Classification Report (Kernel=RBF): {class_report_rbf}')



'''
Comparing two SVM Model:


'''