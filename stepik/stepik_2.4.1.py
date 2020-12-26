#!/usr/bin/env python3
'''
Задание 2.4
'''
a = input()
c = a.upper().count('g'.upper())
s = a.upper().count('c'.upper())
print(((c+s)/len(a))*100)
