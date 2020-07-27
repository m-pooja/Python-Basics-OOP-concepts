# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 20:03:08 2020

@author: Pooja
"""
"""
Conditional Statements: If, If- else, Nested if-else.
"""
age = input("Enter your age: ") #string
if ((int(age))>50):#false for age =48
    print("Old one")
else:
    print("Adult person")  

#build a gradebook if else if
"""
if marks of student in a subject is between 10-20, 
grade is F:
    between 21-30, grade is D
"""
marks = int(input("Enter your marks "))
if (20>marks>=10):#True
    if(marks==10):#False
        print("You FAILED")
    else:
        print("Your grade is F")
        print("You got promoted")
elif (30>marks>=21):
    if(marks == 21):
        print("you are at the lowest of grade D")
    else:
        print("Your grade is D")
elif(40>marks>31):#TRUE
     print("Your grade is C")
else:
    print("No record found")

and
or
"""
 == equality x==12
 > greater than
 < less than
 >= greater than or equal to
 <=
 != not equal to
 
if((x==True)or(y==False)):

"""
x=9
print(x*3)
print(x*=3)
x=9
x+=9
x-=9

x+=1
x-=1















    

