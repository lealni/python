#!/usr/bin/env python3
def f(x):
    if x <= -2:
        a = 1 - (x+2)**2
    if -2 < x <= 2: 
        a = - ( x / 2 )
    if x > 2:
        a = (x - 2)**2 + 1
    print(a)
    return a

f(4.5)
f(-4.5)
f(1)
