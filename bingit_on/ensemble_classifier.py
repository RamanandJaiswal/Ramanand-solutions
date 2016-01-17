import pandas as pd
from sklearn.cross_validation import cross_val_score, KFold
from sklearn.cross_validation import train_test_split
import numpy as np
from nltk import re
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn import metrics
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from compiler.ast import flatten
import nltk as nl
from sklearn.decomposition import PCA
from sklearn.svm import LinearSVC
from sklearn.lda import LDA
#from openpyxl import Workbook, load_workbook
from scipy.stats.stats import pearsonr   
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier,GradientBoostingClassifier
import csv as csv
def remove(line):
    line = re.sub(';', ' ', line)
    line =line.split("\\s+")
    return line
def remove2(t):
    t=str(t)
    t=re.sub('\\s+', ',', t)
    t=t.split(',')
    return t
train = pd.read_csv("/home/mohan/microsoft_hackthon/BingHackathonTrainingData.txt" ,sep='\t',header=None)
test = pd.read_csv("/home/mohan/microsoft_hackthon/BingHackathonTestData.txt",sep='\t',header=None)
#X = train.iloc[1:5,5]
train.iloc[:,3]=train.iloc[:,3].apply(remove)
test.iloc[:,3] = test.iloc[:,3].apply(remove)
#train.iloc[:,4]=train.iloc[:,4].apply(remove)
#train.iloc[:,5]=train.iloc[:,5].apply(remove)
data = train.iloc[:,[3,4,5]]
record_id = test.iloc[:,0]
test_data1 = test.iloc[:,[3,4,5]]

test_data = np.asarray(test_data1)
train1 = [] 
test = []
#data = data.apply(remove2)
label = train.iloc[:,1]
data = np.asarray(data)#converting the data to array format
label = np.asarray(label)
#print data.iloc[4]
#X_train, X_test, y_train, y_test = train_test_split(data ,label, test_size=0.0, random_state=42)#splitting the train_test data as per cross-validation

for i in range(len(data)): #processing of the train data
    string = str(data[i])
    string = string.split(',')
    train1.append(' '.join(string))

for i in range(len(test_data)): #processing of the test data  
    string = str(test_data[i])
    string = string.split(',')
    test.append(' '.join(string))  
vctr = TfidfVectorizer(lowercase =False, ngram_range=(1, 1))
train_input = vctr.fit_transform(train1).toarray()
clf1 = LinearSVC(C = 0.15)
clf2 = LinearSVC(C = 0.25)
clf3 = LinearSVC(C = 0.35)
clf4 = LinearSVC(C = 0.45)
#clf4 = SVC(kernel = C = 0.45)
clf5 = LinearSVC(C = 0.55)
#output = open('/home/mohan/clf_SVC.pkl', 'wb')
#pickle.dump(clf, output)
#output.close()
print "trainingdata shape"
#print np.shape(train_input)
X_test1 = vctr.transform(test).toarray()
#X_test1 = pca.transform(X_test1)
#y_pred1 = clf1.predict(X_test1)
#y_pred2 = clf2.predict(X_test1)
#y_pred3 = clf3.predict(X_test1)
#print "scores5"
#print scores4
#print "scores5"
#print scores5
eclf1 = VotingClassifier(estimators=[('LSVC', clf1), ('LSVC', clf2), ('LSVC', clf3),('LSVC',clf4),('LSVC',clf5)], voting='hard')
eclf1 = eclf1.fit(train_input, label)
y_pred = eclf1.predict(X_test1)
print y_pred
predicted = y_pred
submission="/home/mohan/submission_ensemble.tsv"

#test["topic_id"]= predicted
#test["record_id"]= record_id
#test.to_csv(submission,
#columns=['record_Id','topic_id'],index=False,sep='\t')

predictions_file = open(submission, "wb")
open_file_object = csv.writer(predictions_file,delimiter='\t')
open_file_object.writerow(["record_id","topic id"])
open_file_object.writerows(zip(record_id,predicted))
predictions_file.close()

