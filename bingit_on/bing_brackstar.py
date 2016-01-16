'''
Created on Jan 16, 2016

@author: Ramanand.Jaiswal
'''
import pandas as pd
import numpy as np
train="C:\\Users\\Ramanand.Jaiswal\\Desktop\\bing\\BingHackathonTrainingData.txt\\BingHackathonTrainingData.txt"
test="C:\\Users\\Ramanand.Jaiswal\\Desktop\\bing\\"

if __name__=='__main__':
    
    train=pd.read_table(train,sep='\t',header=None)
    print train.iloc[:,0:6].head(2)
    traindata= train.iloc[:,0:6]
    
    print traindata.head(5)
