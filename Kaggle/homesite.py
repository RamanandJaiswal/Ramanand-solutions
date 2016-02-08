"""
Train,test set data  you can get on kaggle 
https://www.kaggle.com/c/homesite-quote-conversion
"""

import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split


unix_path="//mnt//datacopy//test//homesite//"
filepath=unix_path
train="train.csv"
test="test.csv"
submission="submission.csv"

if __name__=='__main__':

    train=pd.read_csv(train)
    test=pd.read_csv(test)
    print train.head(6)
    print train.isnull().sum()
    seed = 260681
    train,validation=train_test_split(train_df, train_size = 0.6)
    train_y = train.QuoteConversion_Flag.values
    train = train.drop(['QuoteNumber', 'QuoteConversion_Flag'], axis=1)
    test = test.drop('QuoteNumber', axis=1)

    #date conversion
    train['Date'] = pd.to_datetime(pd.Series(train['Original_Quote_Date']))
    train = train.drop('Original_Quote_Date', axis=1)

    test['Date'] = pd.to_datetime(pd.Series(test['Original_Quote_Date']))
    test = test.drop('Original_Quote_Date', axis=1)

    test['Year'] = test['Date'].apply(lambda x: int(str(x)[:4]))
    test['Month'] = test['Date'].apply(lambda x: int(str(x)[5:7]))
    test['weekday'] = test['Date'].dt.dayofweek
    
    #drop date
    train = train.drop('Date', axis=1)
    test = test.drop('Date', axis=1)

    #null values treatment
    train = train.fillna(-1)
    test = test.fillna(-1)

    #label encoding
    for f in train.columns:
        if train[f].dtype=='object':
            print(f)
            lbl = preprocessing.LabelEncoder()
            lbl.fit(list(train[f].values) + list(test[f].values))
            train[f] = lbl.transform(list(train[f].values))
            test[f] = lbl.transform(list(test[f].values))
    #XGB Model 
    clf = xgb.XGBClassifier(n_estimators=25,
                        nthread=-1,
                        max_depth=10,
                        learning_rate=0.025,
                        silent=True,
                        subsample=0.8,
                        colsample_bytree=0.8)
    #cv check
    param = {'max_depth':2, 'eta':1, 'silent':1, 'objective':'binary:logistic'}
    num_round = 2
    print ('running cross validation')
    # do cross validation, this will print result out as
    # [iteration]  metric_name:mean_value+std_value
    # std_value is standard deviation of the metric
    xgb.cv(param, dtrain, num_round, nfold=5,
       metrics={'error'}, seed = 0)
    #Training
    print 'Training .....'
    xgtrain = xgb.DMatrix(train, label=train_y,missing = -1)
    xgtest = xgb.DMatrix(test,missing = -1)
    clf = clf.train(xgtrain)

    print 'Predicting......'
    preds = clf.predict_proba(test)[:,1]

    #writing to file
    print 'writing to file'
    test["QuoteConversion_Flag"]=preds
    test.to_csv(submission,
    columns=['QuoteNumber','QuoteConversion_Flag'],index=False)
    print 'Now it\'s completed'
    
                        
