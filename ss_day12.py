# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 20:29:01 2020

@author: Pooja
"""

#funtions: block of code : build in | user defined 

# input()
#print()
#list()

#1. define / declare /write functionality
#2. call a function : its name ()
def Fun(  ):
    return 
v=Fun()

print("Out of fun")



"""
#1. function : no aurguments not return anything
#2. function may have aurgument, return nothing
#3. function no aurgument return something
#4. function aurugemnt returns

parameters/aurguments, when called, 
same parameterss/aurguments need to passed to the function
"""
def fun_1():
    x=int(input("Enter a number"))
    print(x**2)

fun_1()

def fun_2(x):
    print(x*2)

fun_2("hello")


def fun_21(x,z,y=12):
    print(x)
    print(y**2)
    print(z**3)

fun_21(2)


def fun_3():
    x=9
    return x**2, x**3 #tuple

sq_of_x, cu_of_x =fun_3()
l_x=fun_3()


def fun_4(x):
    return x**2, x**3 #tuple

sq_of_x, cu_of_x =fun_4(3)

def ex_1(x):
    x=x.lower()
    count=0
    for i in range(len(x)):
        if i=='a':
            count=count+1
    if count >3:
        print("inaccurate string")
    else:
        print("accurate string")
    

string1=input("enter a string")

c_str = ex_1(string1)


def f1():
    global a,b
    a=900
    b=90
    return a,b
def finf1():
    return a,b

a_value, b_value = f1()
a_value_f1, b_value_f1 = finf1()








