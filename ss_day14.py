# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 14:23:11 2020

@author: Pooja
"""

"""
Anonymous Functions
lambda 
"""

def fun(a,b):
    return a+b
#single line function
#lambda aurguments : expression
x = lambda a,b : a+b
print(x(2,3))
add=x(6,8)
x1 = lambda a,b : a-b
x1(5,3)
sq=lambda x:x**2
sq_2 = sq(2)
l_sq=[]
for i in range(11):
    l_sq.append(sq(i))

"""
filter(), map() and reduce(), zip()
"""

l=[]
for i in range(0,20):
    l.append(i)

l_ev = list(filter(lambda x:x%2==0, l ))

tuple(filter(lambda x:x%2==0, l ))

def even(x):
    return x%2==0
lambda x:x%2==0
        
even(3)
list(filter(even,l))

#lambda x : True if (x > 10 and x < 20) elif (x==21) x+1 else False

print(l)

l_ev = list(map(lambda x:x*2, l ))

l1=['a','b','c']
l2=[1,2,3]

l=[1,2,3,4,5]
def mul_3(x):
    return x*3
for i in l:
    print(mul_3(i))
    
list(map(lambda x:x*3, l ))

l=[]
x=input()
for i in range(len(x)):
    l.append(int(i))














