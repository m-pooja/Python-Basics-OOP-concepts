# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 20:35:44 2020

@author: Pooja
"""

#Dictionaries

#composite data type
"""
items/elements 
index - keys:value
dynamic
mutables
"""

d = {}
print(type(d))
d={1:'Apple', 2: "Bed",'c':'cat'}
nested_d={1:'Apple', 2: "Bed",'c':'cat', 4:{41:'a',42:'b'}, '4':'hi'}
nested_d[4][42]='B'

l=[(1,'ONE'),(2,'TWO')]
dict(l)

l1=[34,45,67,56]
l=['thiry four', 'forty five', 'sixty seven']

zip_dict2 = dict(zip(l1,l))

d={1:'Apple', 2: "Bed",'c':'cat'}
d['e']='elly'

d.get('d')
d.pop('c')
d.popitem()
d.clear()
del(d)

d.keys()
d.values()
d.items()
for i in d.keys():
    print(d[i])

l=['a','b','c','d']
d={}
d.fromkeys(l,23)

d = {1: "one", 2: "three"}
d1 = {3: "two"}
d.update(d1)

d = {'a': 21}

d.update(y = 3, z = 0)

d={'name':'Hitesh'}

age =d.setdefault('age')


l=[12,23,34]

print()
