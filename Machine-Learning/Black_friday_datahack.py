'''
Created on Nov 20, 2015

@author: Ramanand.Jaiswal
'''
import pandas as pd
import xgboost as xgb
from sklearn.ensemble import GradientBoostingRegressor,RandomForestRegressor,AdaBoostRegressor
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.grid_search import GridSearchCV

file_path="//mnt//test//"
train=file_path+"train.csv"
test=file_path+"test.csv"
submission=file_path+"submission_xgb.csv"

 
if __name__=='__main__':
    
    train=pd.read_csv(train)
    test=pd.read_csv(test) 
    test1=test
    print test1.head(5)
    train['Type']='Train'
    test['Type']='Test'
    fullData = pd.concat([train,test],axis=0)
    
    #check Null Values :count null values
    print fullData.isnull().sum()
    cat=['Product_Category_2','Product_Category_3']
    fullData[cat]=fullData[cat].fillna(value='-99999')
   
    #convert non numericto numeric
    transform=['Product_ID','Gender','Age','Occupation','City_Category','Stay_In_Current_City_Years','Marital_Status']
    #encoding categorical variable
    for var in transform:
	#fullData=fullData.astype('str')
        le = LabelEncoder()
        #le.fit(fullData)
        fullData[var] = le.fit_transform(fullData[var])
     
     
    print fullData.head(5)
    
    #segregate train,test set:
    train=fullData[fullData['Type']=='Train']
    test=fullData[fullData['Type']=='Test']
    #Drop feature Type
    train = train.drop(['Type'], 1)
    test = test.drop(['Type','Purchase'], 1)
    
    features=['Product_ID','Gender','Age','Occupation','City_Category','Stay_In_Current_City_Years','Marital_Status','Product_Category_1','Product_Category_2','Product_Category_3']
    target=['Purchase']
    
    #preparing data for Model
    train_x=train[features].values
    train_y=train[target].values
    test_x=test[features].values
    
    print 'check Null values'
    print test.isnull().sum()
    print train.isnull().sum()
    
   
    print "Building XGB1"
    params = {}
    params["objective"] = "reg:linear"
    params["eta"] = 0.1
    params["min_child_weight"] = 10
    params["subsample"] = 0.7
    params["colsample_bytree"] = 0.7
    params["scale_pos_weight"] = 0.8
    params["silent"] = 1
    params["max_depth"] = 8
    #params["max_delta_step"]=2
    params["seed"] = 0
    params["thread"]=8
    plst = list(params.items())
    xgtrain = xgb.DMatrix(train_x, label=train_y)
    xgtest = xgb.DMatrix(test_x)
    num_rounds = 1500
    #cv
    print ('running cross validation')
    #bst.cv = xgb.cv(params=params, dtrain=xgtrain, num_boost_round = num_rounds, nfold= 5,metrics={'error'})
    
    print 'Training Model ...'
    model = xgb.train(plst, xgtrain, num_rounds)
    
    print 'Predicting.....'
    result = model.predict(xgtest)
    #result= bst.cv.predict(xgtest)
     
    print 'Writing to File'
    test1["Purchase"]=result
    test1.to_csv(submission,
    columns=['User_ID','Product_ID','Purchase'],index=False)
    
    print 'now its completed...'
    
    
