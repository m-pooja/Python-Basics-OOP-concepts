# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:44:09 2020

@author: Pooja
"""

#LIST
"""
sequence
items are indexed : negative positive
slicing
mutable
different data types as items
"""
#creating list
list([1,2,3,4])
list((1,2,3,4))
l=[1,2,'a',2.3,5]
l1=[[1,2,3],23,'red',4.5]
for i in l1:
    print(type(i))
list_1 = [['a','b','c', ['d','e']], 23,34,8.9]

list_1[0][3][1]

list_1[-1]

list_1[0]=['A','B']
l1=list_1[:2]
"""
shallow copy
deep copy
"""

l=[1,2,3,4,5,6,7]
l1=l

l1
l

l[0]=11
l
l1
l1=l.copy()
l=list(range(1001))
l_even = list(range(0,21,2))

l=['a','b','c']
len(l)
l.append('d')

l=[]
for i in range(6):
    x=int(input("enter the marks"))
    l.append(x)

l.clear()  
l=['a','b','c','d','d','e','b','b'] 
l.count('b')
l.index('b')

l1=[1,2,3,4]

l1.extend(['we','are','united'])
l.extend(l1)

l=['p','o','o']
l1=['j','a']

l.extend(l1)
l.insert(1,'am')
l.insert(1,['a','b'])

l.pop(1)
l.remove('p')
l.reverse()
l=[1,2,3,4]
l=[23,12,67,45,90]

l.sort(reverse = True)
l=[23,['a',['b','c']],67,45,90]

l[1][1][1]

l1= [1,2,3]
l2=[4,5,6]
l=[23,12,67,45,90]
for i in range(len(l)):
    print(l[i])

#List Comprehension: 
l=[]    
for i in range(10):
    l.append(i**2)  
print(l)
    
l1=[i**2 for i in range(100)]
len(l1)

l=[]    
for i in range(10):
    if(i%2==0):
        l.append(i**2)  
print(l)
l1=[j for i in range(100) for j in range(i)]
l=[]
for i in range(10):
    for j in range(i):
        print(j, end = " ")
    print(" ")
len(l1)

l=[]
l1=[]
for i in range(5):
    l1.append(i)
    l1.append(1**2)
    l.append(l1)
    
l[0][3]

l=['a','b','c']

l1=l

print(l)
print(l1)

l.append('g')

print(l)
print(l1)

l1 = l.copy()
print(l)
print(l1)
l.append('G')

l=[23,12,56,78,90,34]

l.sort()
l2=[89,56,7,23,45]

sort_l2 = sorted(l2)

even=[]
for i in range(21):
    if(i%2==0):
        even.append(i)

even_lc = [i for i in range(21) if(i%2==0)]

from math import sqrt 

even_lc = [sqrt(i) for i in range(21) if(i%2==0)]

import math as m

sin_lc = [m.sin(i) for i in range(21)]

DAY 8
#pangram is string which contains all possible alphabet

"""
the quick brown fox jumps over the lazy dog"""





l="the quick brown fox jumps over the lazy dog"
s=set(l)

strng = set(input("enter the sentence to be checked for pangram").lower())
if (s-strng ==set([])):
    print("it is a pangram")
else:
    print("it is NOT a pangram")

S1=set([2,3,4,4,5])

S2=set([2,3,4,4,5,6,6,7,8,9])

l="the quick brown fox jumps over the lazy dog"
l1=list(set(l))
l1.index(' ')
l1.pop(21)