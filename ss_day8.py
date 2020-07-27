# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 20:32:15 2020

@author: Pooja
"""

#TUPLES

#LIST, NESTED LIST, LIST COMPREHENSION
"""
Sequence """
#Tuples are initialized with () brackets 
t = tuple([2,3])
print(type(t))
print(t)
t1= tuple(['c','a','t',2,3])
for i in t1:
    print(type(i))

print(t1[3])
t=('c','a','t')
t=(4,)
t1=(1,2,3,4,'a')
t2=('b','c','d')

t1[0]
t1[0] = 90
t3 = t1+t2
print(len(t1))
t1[5]=90
list_1=['a','b','c','d']
list_1.append(90)

t_l = tuple(list_1)

import timeit
timeit.timeit('x=[1,2,3,4,5,6,7,8,9]', number=100000)

t= (2,2,[3,4])

id(t[0])
id(t[1])
id(t[2])

t[2].append(45)
t.count(2)
t.index(2)


t*2
t+t
20 in t
t==t1
t=(2,3,4,15)
tt=(2,3,4,5)
for i in range(len(t)):
    if (t[i]==tt[i]):
        print('same')
    else:
        print('different')

t=(2,3)

a,b=t
swapping two number

a=9
b=90
t=(9,90)
b, a = a, b

(a,b)=('A', 'B')
















