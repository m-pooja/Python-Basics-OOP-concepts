# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 13:53:35 2020

@author: Pooja
"""

dic1 = {'fname': 'Pooja', 'lname':'singh'}
dic1['age']
dic1.setdefault('age', 12)
person = {'name': 'Phill', 'age': 22}

age = person.setdefault('age')
print('person = ',person)
print('Age = ',age)

person = {'name': 'Phill'}

#age = person.setdefault('age')
print('person = ',person)
print('Age = ',age)
person1 = {'name': 'Phill'}

lname = person1.setdefault('lname','Bob')
print('name = ',person1)
print('lname = ',lname)
name =  {'name': 'Phill'}
lname =  2

l=dict([(i,k) for i in range(90)])

l=dict([(1,'one'), (92,'two')])



d = {i : chr(i) for i in range(65,92)}



