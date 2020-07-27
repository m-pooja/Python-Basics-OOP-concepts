# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 20:34:24 2020

@author: Pooja
"""

#functions
#create a function to add some values

def Add(num_1,num_2):
    return num_1+num_2

def Add_3(num_1,num_2,num_3):
    return num_1+num_2+num_3
    
add3=Add_3(5,6,7)
#variable_length aurguments
"""
args | non- keyword type
"""
def Add_multiple_aru(*args):
    for i in args:
        print(type(i))
    for i in args:
        print(i)
Add_multiple_aru('2','3',5,6,8,9,7)

Add_multiple_aru(2,3,5,6)
"""
kwargs | non- keyword type length of aurguments to be
passed by user is not defined.
"""
def print_kw(**kwargs):
    for k,v in kwargs.item():
     print("{}:{}".format(k,v))

print(kwargs)

print_kw(kwargs_1='a',kwargs_2='b')

d={1:'ONE',2:'two' }

for i,j in d.items():
    print(j)

for i in d.values():
    print(i)

def pos_Aur(x,y=0):
    return x*2,y*3

pos_Aur()



