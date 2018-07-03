import pandas as pd 
import sys
import numpy as np
import findCorrelation as cat
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics 
from sklearn.metrics import classification_report

targetCol=""
targetColFile=open("targetVariable.txt","r")
for line in targetColFile:
	targetCol=line.split(" ")[0]

corrdatframe=cat.correlateddatframe()
#print('Total count of rows',len(corrdatframe.axes[0]))
columns=len(corrdatframe.axes[1])
#print(columns)
dmy=corrdatframe.drop([targetCol],axis=1)
X = dmy.ix[:].values
y = corrdatframe.ix[:,targetCol].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .3, random_state=25)
#deploying and evaluating the model
LogReg = LogisticRegression()
LogReg.fit(X_train, y_train)
y_pred = LogReg.predict(X_test)

confusion_matrix = confusion_matrix(y_test, y_pred)

classification_report = classification_report(y_test, y_pred)

mat = np.matrix(confusion_matrix)

with open("finalReport.txt", "w") as text_file:
	text_file.write("------Confusion Matrix-----\n\n")
	for line in mat:
		text_file.write(np.str(line))
	text_file.write("\n\n")
		#np.savetxt(text_file, line, fmt='%d %d')
	text_file.write("------Classification Report------\n\n")
	text_file.write(classification_report)
	#text_file.write(classification_report)
# calculate the fpr and tpr for all thresholds of the classification
probs = LogReg.predict_proba(X_test)
preds = probs[:,1]
fpr, tpr, threshold = metrics.roc_curve(y_test, preds)
roc_auc = metrics.auc(fpr, tpr)

# method I: plt
import matplotlib.pyplot as plt
fig=plt.figure()
plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()
fig.savefig("ROC_curve.png")