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
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from compiler.ast import flatten
import nltk as nl
import pickle
from sklearn.ensemble import VotingClassifier
#from openpyxl import Workbook, load_workbook
from scipy.stats.stats import pearsonr   
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier,GradientBoostingClassifier
from sklearn.decomposition import TruncatedSVD
from sklearn.lda import LDA
def remove(line):
    line = re.sub(';', ' ', line)
    line =line.split("\\s+")
    return line
def remove2(t):
    t=str(t)
    t=re.sub('\\s+', ',', t)
    t=t.split(',')
    return t
test = []
train = pd.read_csv("/home/mohan/microsoft_hackthon/BingHackathonTrainingData.txt" ,sep='\t',header=None)

#X = train.iloc[1:5,5]
train.iloc[:,3]=train.iloc[:,3].apply(remove)
#train.iloc[:,4]=train.iloc[:,4].apply(remove)
#train.iloc[:,5]=train.iloc[:,5].apply(remove)
data = train.iloc[:,[3,4,5]]

train1 = [] 
#data = data.apply(remove2)
label = train.iloc[:,1]
data = (data)#converting the data to array format
label = (label)
#print data.iloc[4]
X_train, X_test, y_train, y_test = train_test_split(data ,label, test_size=0.2, random_state=42)#splitting the train_test data as per cross-validation
cv = KFold(n=X_train.shape[0],  # total number of samples
           n_folds=5,           # number of folds the dataset is divided into
           random_state=12345,shuffle=True)
for i in range(len(X_train)): #processing of the train data
    string = str(X_train.iloc[i])
    string = string.split(',')
    train1.append(' '.join(string))

for i in range(len(X_test)): #processing of the test data  
    string = str(X_test.iloc[i])
    string = string.split(',')
    test.append(' '.join(string))

###########################################################################################################################################
#pca = TruncatedSVD(n_components = 8000) 
vctr = TfidfVectorizer(lowercase =False, ngram_range=(1, 1))
train_input = vctr.fit_transform(train1).toarray()
#train_input = pca.fit_transform(train_input)
#input_data_matrix = open('/home/mohan/input_data.pkl', 'wb')
#pickle.dump(train_input, input_data_matrix)
#input_data_matrix.close()
clf1 = SVC(kernel = 'linear', C = 0.15)
clf2 = SVC(kernel = 'linear', C = 0.25)
clf3 = SVC(kernel = 'linear', C = 0.35)
#clf4 = SVC(kernel = C = 0.45)
#clf5 = SVC(C = 0.55)
#output = open('/home/mohan/clf_SVC.pkl', 'wb')
#pickle.dump(clf, output)
#output.close()
print "trainingdata shape"
print np.shape(train_input)


scores1 = cross_val_score(clf1, train_input , y_train, cv=cv, scoring='accuracy')
scores2 = cross_val_score(clf2, train_input , y_train, cv=cv, scoring='accuracy')
scores3 = cross_val_score(clf3, train_input , y_train, cv=cv, scoring='accuracy')
#scores4 = cross_val_score(clf4, train_input , y_train, cv=cv, scoring='accuracy')
#scores5 = cross_val_score(clf5, train_input , y_train, cv=cv, scoring='accuracy')
X_test1 = vctr.transform(test).toarray()
#X_test1 = pca.transform(X_test1)
#y_pred1 = clf1.predict(X_test1)
#y_pred2 = clf2.predict(X_test1)
#y_pred3 = clf3.predict(X_test1)
print "scores1"
print scores1
print "scores2"
print scores2
print "scores3"
print scores3
#print "scores5"
#print scores4
#print "scores5"
#print scores5
eclf1 = VotingClassifier(estimators=[('LSVC', clf1), ('LSVC', clf2), ('LSVC', clf3)], voting='hard')
eclf1 = eclf1.fit(train_input, y_train)
y_pred = eclf1.predict(X_test1)
print np.mean(y_pred == y_test)
    
    







