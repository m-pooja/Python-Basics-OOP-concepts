# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 14:21:48 2020

@author: Pooja
"""

s="It is second day we are working on stringß. On todays day, last year we did something different"
s1="It is second day we are working on stringss"

s1.swapcase()
s.encode("utf8")
tmap = {97:"AB",119:"VV" }
s.translate(tmap)

s.lower()
s.upper()
s.capitalize()
s.title()
s.center(50, "*")
s.casefold()
if (s.casefold() == s1.casefold()):
    print("same")

s.count('we',10, 25)
s.endswith('differ')
s.startswith('second', 6, 45)
s_t= "this\tis\ta\tbeautiful\tday"
s_t.expandtabs(15)
s.encode(encoding='UTF-8',errors='strict')
s_f='pythön!. python. python. python'
s_f.encode("ascii", "replace")

s_f.find('o', 14, 35)

s="poooja"
ss= "123.6789"
ss.isdigit()
s='_12python'
s.isidentifier()
s = chr(97)

if s.isprintable() == True:
  print('Printable')
else:
  print('Not Printable')

S= "    I code in python"
S.partition("in")

S.rstrip().lower()

S.strip('on')






