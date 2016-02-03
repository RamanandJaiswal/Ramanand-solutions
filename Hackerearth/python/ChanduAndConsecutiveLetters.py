'''
Created on Feb 3, 2016

@author: Ramanand.Jaiswal
Chandu is very fond of strings. (Or so he thinks!) But, he does not like strings which have same consecutive letters. No one has any idea why it is so. He calls these strings as Bad strings. So, Good strings are the strings which do not have same consecutive letters. Now, the problem is quite simple. Given a string S, you need to convert it into a Good String.

You simply need to perform one operation - if there are two same consecutive letters, delete one of them.
aab--ab
abab--abab
aadd--ad
'''

from collections import OrderedDict
from itertools import groupby

def remove_dupes(arg):
    # create generator of distinct characters, ignore grouper objects
    unique = (i[0] for i in groupby(arg))
    return ''.join(unique)

T=int(raw_input())
for t in range(T):
    p=raw_input()
    #print "".join(set(p)) this will be unordered
    #print "".join(OrderedDict.fromkeys(p))
    print remove_dupes(p)
            
