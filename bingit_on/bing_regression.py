'''
Created on Jan 16, 2016

@author: Ramanand.Jaiswal
'''
import pandas as pd
import numpy as np
from scipy import stats
import re
import sklearn.linear_model as lm
import xgboost as xgb
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import cross_val_score,KFold
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics.regression import mean_squared_error
from math import sqrt

train="//mnt//resource//data//bing//train.tsv//BingHackathonTrainingData.txt"
test="//mnt//resource//data//bing//test.tsv//BingHackathonTestData.txt"
submission="//mnt//resource//data//bing//submission_svr.tsv"
from sklearn.cross_validation import   train_test_split

def remove(line):
     
    line = re.sub(';', ' ', line)
    line = re.sub('\\s+', ',', line)
    
    return line

def remove2(t):
    t=str(t)
    t=re.sub('\\s+', ',', t)
    t=t.split(',')
    t=','.join(t)
    return t
    


def remove_whitespace(line):
    line = re.sub('\\s+', ',', line)
    return line
    

if __name__=='__main__':
    
    train=pd.read_table(train,sep='\t',header=None)
    #print train.iloc[:,0:6].head(2)
    traindata= train.iloc[:,[1,3,4,5]]
    #print traindata.isnull().sum()
    label=train.iloc[:,2]
    print label.head(10)
    #print traindata.head(5)
    #reading test data set
    test=pd.read_table(test,sep='\t',header=None)
    record_id=test.iloc[:,0]
    test= test.iloc[:,[1,3,4,5]]
    test.iloc[:,1]=test.iloc[:,1].apply(remove)
    test=test.applymap(remove2)
    print 'test datat set'
    print test.head(10)
    
    print traindata.shape
    x_train,x_test,y_train,y_test=train_test_split(traindata,label,test_size=0.2,random_state=42)
    
    print y_train.head(10)
    x_train.iloc[:,1]=x_train.iloc[:,1].apply(remove)
    #x_train=x_train.iloc[:,[0,1,3,4,5]]
    x_train=x_train.applymap(remove2)
    
    #validation set
    x_test.iloc[:,1]=x_test.iloc[:,1].apply(remove)
    #x_test=x_test.iloc[:,[0,1,3,4,5]]
    x_test=x_test.applymap(remove2)
    
    #print train_x.head(5)
    cv = KFold(n=x_train.shape[0],n_folds=5,random_state=12345,shuffle=True)

    
    #print  list(train_x)
    tfv = TfidfVectorizer(tokenizer=lambda doc: doc,lowercase=False)
    #tfv = TfidfVectorizer()
    print "fitting pipeline"
    
    tfv=tfv.fit(list(np.asarray(x_train)))
    
    print 'Transforming data..'
    data=tfv.fit_transform(list(np.asarray(x_train)))
    print data.shape
    #tfv=tfv.fit_transform(list(np.asarray(x_train)))
    n_features=10640                                                         
    #rd = lm.LogisticRegression(penalty='l2', dual=True, tol=0.0001, 
    #                        C=1, fit_intercept=True, intercept_scaling=1.0, 
    #                       class_weight=None, random_state=None)
    rd=SVR(kernel='linear', degree=3, gamma='auto', coef0=0.0, tol=0.001, C=1.0, epsilon=0.1, shrinking=True, cache_size=200, verbose=False, max_iter=-1)
    
    
    
     
    print "Training data"
     
    rd.fit(data.toarray(),y_train.values)
    scores1 = cross_val_score(rd, data , y_train, cv=cv, scoring='mean_squared_error')
    print scores1
    pred = rd.predict(tfv.transform(list(np.asarray(x_test))).toarray())
    print pred
    print sqrt(mean_squared_error(pred,y_test))
    
    pred=np.round(pred)
    pred=pred.astype(int)
    print 'predicting actual test set...'
    predicted=rd.predict(tfv.transform(list(np.asarray(test))).toarray())
    
    #for p in predicted:
        #print p
    predicted=np.round(predicted)
    predicted=predicted.astype(int)
    test["publication year"]=predicted
    test["record Id"]=record_id
    test.to_csv(submission,
    columns=['record Id','publication year'],index=False,sep='\t')
    
    
    
    
     
    
    
