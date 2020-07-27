# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:36:45 2020

@author: Pooja


LOOPS

when you want some instructions to followed again n again.
iteration

want program to print some value grades/cost.

list of grades

"""
name = input("enter your name")
age = int(input("enter your age"))

s1 = "My name is {0}. I am {1} years old. My friend's name is also {0}".format(name,age)

for num in range(101):
    if(num%2==0):
        print( "{} is an even number".format(num))
    else:
        print( "{} is an odd number".format(num))

for num in range(1,11,2):
    if(num==5):
        continue
    print( "{} is an odd number".format(num))
print("I came out of for loop")
    
for num in range(0,101,5):
    print( "{} is a multiple of 5".format(num))   

i=0
while(i<10):
    print(i)
    i=i+1


for i in range(20):
    pass
print("I am out of for")

   
    