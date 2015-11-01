'''
Created on Oct 24, 2015

@author: Ramanand.Jaiswal
'''
import pandas as pd
import numpy as np
import csv as csv
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
from sklearn import svm

train=" train_FBFog7d.csv"
test="Test_L4P23N3.csv"
output_file=" Sample_Submission_i9bgj6r.csv"
new_variable_alcohol="NewVariable_Alcohol.csv"
 
def clean_data(train_df):
    #Data Clean up
    #filling missing values
    train_df['income'] = train_df['income'].map( {'$25000 or more': 7, '$20000 - 24999':6,'$15000 - 19999':5,'lt $1000':0,'$1000 to 2999' :1,'$3000 to 3999':2,'$4000 to 4999':2,'$5000 to 5999':2 ,'$6000 to 6999':3,'$7000 to 7999':3,'$8000 to 9999':3,'$10000 - 14999':4,} )
    train_df.income=train_df['income'].fillna(-9999)

    train_df['Engagement_Religion'] = train_df['Engagement_Religion'].map({'2-3x a month':6, 'every week':8, 'lt once a year':2, 'more thn once wk':9,'never':1, 'nrly every week':7, 'once a month':5, 'once a year':3, 'sevrl times ayr':4})
    train_df.Engagement_Religion=train_df['Engagement_Religion'].fillna(-9999)

    train_df.Unemployed10=train_df['Unemployed10'].fillna(-9999)

    train_df.Divorce=train_df['Divorce'].map({'yes':1,'no':0})
    train_df.Divorce=train_df['Divorce'].fillna(-9999)

    train_df.Widowed=train_df['Widowed'].map({'yes':1,'no':0})
    train_df.Widowed=train_df['Widowed'].fillna(-9999)

    train_df.Gender=train_df['Gender'].fillna(-9999)
    
    train_df.babies=train_df['babies'].fillna(-9999)
    train_df.preteen=train_df['preteen'].fillna(-9999)
    train_df.teens=train_df['teens'].fillna(-9999)
    
    train_df['Alcohol_Consumption'] = train_df['Alcohol_Consumption'].map({'Once a week':9,'Rarely':5,'Once a month':7,'Multiple times in a week' :10,'Occassional':6,'2 - 3 times a month':8,'Never':0})
    train_df.Alcohol_Consumption=train_df['Alcohol_Consumption'].fillna(-9999)
    
    #train_df.Education=train_df['Education'].fillna(-9999)
    

    #drop other columns
    train_df=train_df.drop([ 'Var1','Score','WorkStatus','Var2','TVhours','Education','Residence_Region','Gender','Widowed','Divorce','Engagement_Religion','babies','preteen','teens','Unemployed10'],axis=1)

    #print train_df.head(100)
    return train_df 

if __name__ == '__main__':
    alcohol = pd.read_csv(new_variable_alcohol)
    
    train_df=pd.read_csv(train,header=0)
    train_df = pd.merge(train_df, alcohol, how='inner')
    train_df=clean_data(train_df)
    train_df.Happy=train_df['Happy'].map({'Very Happy':15,'Pretty Happy':10,'Not Happy':5})
     
    test_df=pd.read_csv(test,header=0)
    test_df = pd.merge(test_df, alcohol, how='inner')
    test_df=clean_data(test_df) 
    
    #print train_df.head(10)
    #print test_df.head(10)
    
    # Collect the test data's PassengerIds before dropping it
    ids = test_df['ID'].values
    test_df=test_df.drop(['ID'],axis=1)
  
     
    # The data is now ready to go. So lets fit to the train, then predict to the test!
    # Convert back to a numpy array
    #train_data = train_df.values
    test_data = test_df.values
    
    
    
    train_data_result=train_df['Happy'].values
    train_df=train_df.drop(['Happy','ID'],axis=1)
    
    train_data = train_df.values
    train_data_feature=train_data[:,0:2]
    
    #print train_data.shape,train_data_feature.shape,test_data.shape
    print 'Training...'
    forest = RandomForestClassifier(n_estimators=100,max_features=2,max_depth=200,oob_score=True,random_state=None)
     
    ##Simple K-Fold cross validation. 10 folds.
    cv = cross_validation.KFold(len(train_data), n_folds=10, indices=False)
    #forest = forest.fit(train_data_feature,train_data_result)
    
    print 'Predicting...'
    for train_datacv, test_datacv in cv:
        probas = forest.fit(train_data_feature[train_datacv],train_data_result[train_datacv])
         
    predicted=probas.predict(test_data).astype(int)
    
    
    #writing to file
    predictions_file = open(output_file, "wb")
    open_file_object = csv.writer(predictions_file)
    open_file_object.writerow(["ID","Happy"])
    open_file_object.writerows(zip(ids,predicted))
    predictions_file.close()
    
    output_df=pd.read_csv(output_file,header=0)
    output_df.Happy=output_df['Happy'].map({15:'Very Happy',10:'Pretty Happy',5:'Not Happy'})
   
    predictions_file = open(output_file, "wb")
    open_file_object = csv.writer(predictions_file)
    open_file_object.writerow(["ID","Happy"])
    open_file_object.writerows(zip(ids,output_df.Happy))
    predictions_file.close()
    
    print 'Done.'
