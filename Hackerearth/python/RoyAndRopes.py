'''
Created on Feb 3, 2016

@author: Ramanand.Jaiswal
Roy has a rope of length L meters. This rope has several other ropes attached to it at the end of every meter (except for the end of the rope). 
At each meter there are two ropes attached to this main rope, let's call them upper and lower ropes.
Roy lit the rope on fire from the left end. This fire burns down the rope by 1 meter/minute. 
Your task is to find how much time (in minutes) will the fire take to burn down the entire rope.
input t=1
int l=3
5 4
7 4
output:8
'''
t=int(raw_input())
for i in range(t):
    n=int(raw_input())
    upper=raw_input()
    lower=raw_input()
    a=map(int, upper.split(" "))
    b=map(int, lower.split(" "))
    count=0;maxUL=0;maxVal = 0;
    
    for i in range(n-1):
        if a[i] > b[i]:
            maxUL = a[i] 
        else:
             maxUL= b[i];
        count = i+1 + maxUL;
        if(maxVal<count) :
                maxVal=count;
    print maxVal
