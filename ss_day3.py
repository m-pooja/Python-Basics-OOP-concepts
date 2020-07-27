# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 14:24:44 2020

@author: Pooja
"""
"""
1. Create a simple calculator using different operators. Take numbers from users.
2. Create a calculator using an if-elif statement. 
Ask the user to enter the numbers 
and options (what he/she wants to calculate), 
accordingly your program should provide a result.
3. take the age and name from your friends as input
 and display who is oldest as :-  "Umar is oldest. His age is 23
 """
 #2nd

print("This is a calculator.")
print("Choose an option from below: \n A for Addition\n B for Subtraction \n C for Multiplication \n D for division")
option = input().upper()
num_1 = int(input("Enter first number"))
num_2 = int(input("Enter second number"))

if(option=='A'):
    print("Sum : ", (num_1+num_2))
elif(option=='B'):
    print("Difference", (num_1-num_2))
elif(option=='C'):
    print("Multiplication", (num_1*num_2))
elif(option=='D'):
    print("Division", (num_1/num_2))
else:
    print("wrong option")



name1 = input("Enter your name")
age1 = int(input("Enter your age"))
name2 = input("Enter your name")
age2 = int(input("Enter your age"))
name3 = input("Enter your name")
age3 = int(input("Enter your age"))

if((age3>age2) and (age3>age1)):
    print("{} is oldest with age as {} years".format(name3,age3))
    
"""
print the cost of item purchased by user.
discount of 10% if the quantity purchased if more than 200
unit price of item is 30
"""
q = int(input("How much quantity do you want?"))

if (q>200):
    tc=((q*30)-(.1*q*30))
    print("You need to pay {}".format(tc))
else:
    print("you need to pay ", (q*30))

sal = float(input("Enter your salary"))
yos = float(input("Enter years of service"))

if(yos>5):
    b=.1*sal
    print("You will recieve bonus of {} amount. So your total salary for the month is  {}".format(b, b+sal))
else:
    print("You will recieve NO bonus. So your total salary for the month is  {}".format(sal))

num = int(input("Enter a number"))
if ((num%2)!=0):
    print("{} is an odd number".format(num))
else:
    print("{} is not an odd number".format(num))



x = 0
a = 0
b = -5
if a >= 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)













































