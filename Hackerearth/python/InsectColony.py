'''
Created on Feb 2, 2016
Yesterday Oz heard a story about insect colony. The specialty of insects is that they splits sometimes i.e an insect of size A can split into two insects of positive integral sizes B and C such that A = B + C. 
Also sometimes they attack each other i.e. two insects of sizes P and Q will become R = P XOR Q .
You are given the sizes of the insects of insect colony, you have to determine whether it is possible for insect colony to disappear after several splits and/or attacks?
input       output
2           Yes
2 9 17      No
1 1
@author: Ramanand.Jaiswal
'''
T=int(raw_input())
for t in range(T):
    #N=int(raw_input())
    #for i in range(N):
    p=raw_input()
    user_lst = map(int, p.split(" "))
    length=len(user_lst)
    if length>2:
        n= user_lst[0]
        a=user_lst[1]
    else:
        print 'No'
        break;
         
    for idx, val in enumerate(user_lst,start=2):
        a=a^val
            
    result=a%2
    if result:
        print 'Yes'
    else:
        print 'No'
                      
