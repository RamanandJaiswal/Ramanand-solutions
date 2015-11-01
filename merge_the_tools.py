'''
Created on Nov 2, 2015

@author: Ramanand.Jaiswal
'''
from collections import OrderedDict
#set will change order(sort the order)
s=raw_input()
N=int(raw_input())

l=len(s)
i=0
k=l/N
p=N
print k
while(k>=1):
    temp=s[i:p]
    #print temp
    print "".join(OrderedDict.fromkeys(s[i:p]))
    i=p
    p=N+p
    k=k-1
