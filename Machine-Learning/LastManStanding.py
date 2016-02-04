
# coding: utf-8

# In[80]:

filepath="E:\\DataScience\\last Man Standing\\"
train=filepath+"Train_Fyxd0t8.csv"
test=filepath+"Test_C1XBIYq.csv"
import pandas as pd
import numpy as np

#################################
train=pd.read_csv(train)
test=pd.read_csv(test)
train.head(20)


# In[81]:

train['Number_Weeks_Used']=train['Number_Weeks_Used'].fillna(-1)
test['Number_Weeks_Used']=test['Number_Weeks_Used'].fillna(-1)
train.isnull().sum()


# In[120]:

test["new_variable"]=test[['Number_Weeks_Used','Number_Weeks_Quit']].mean(axis=1)
train["new_variable"]=train[['Number_Weeks_Used','Number_Weeks_Quit']].mean(axis=1)
train[['new_variable','Crop_Damage']]


# In[113]:

Features=['Estimated_Insects_Count','Crop_Type', 'Soil_Type','Pesticide_Use_Category','Number_Doses_Week','Number_Weeks_Used',
       'Number_Weeks_Quit','new_variable','Season']
target=['Crop_Damage']


# In[114]:


train.describe()


# In[121]:

from sklearn.cross_validation import cross_val_score,KFold
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.grid_search import GridSearchCV

label=train[target]
x_train,x_test,y_train,y_test=train_test_split(train,label,test_size=0.2,random_state=12242)
clf=GradientBoostingClassifier(learning_rate=0.1, n_estimators=600,max_depth =3)
param_grid2 = {'max_depth': [10, 15, 20],
              'min_samples_leaf': [3, 5, 10, 20]
              }
#cv = KFold(n=x_train.shape[0],n_folds=5,random_state=12345,shuffle=True)
#clf = GridSearchCV(clf, param_grid2,cv=cv).fit(x_train[Features].values,y_train.values)
#cv = KFold(n=x_train.shape[0],n_folds=5,random_state=12345,shuffle=True)
print 'Training..'
clf=clf.fit(x_train[Features].values,y_train.values)
print 'predicting..'
cfm=confusion_matrix(y_test,clf.predict(x_test[Features]))
predict=clf.predict(test[Features].values)
test["Crop_Damage"]=predict
test.to_csv(filepath+"submission.csv",columns=['ID','Crop_Damage'],index=False)


# In[57]:

#cv = KFold(n=x_train.shape[0],n_folds=5,random_state=12345,shuffle=True)
#scores1 = cross_val_score(clf, x_train[Features] ,y_train,cv=None, scoring='accuracy')
#print scores1.mean()


# In[122]:

from sklearn.metrics import classification_report
classification_report(y_test,clf.predict(x_test[Features]))


# In[123]:

clf.feature_importances_


# In[124]:

score=clf.score(x_test[Features],y_test)
score


# In[125]:

print "Accuracy = %.13f" % ((cfm[0][0]+cfm[1][1]+cfm[2][2])*1.0/sum(sum(cfm)))


# In[ ]:



