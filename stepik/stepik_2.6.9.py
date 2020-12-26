#!/usr/bin/env python3
'''

'''



#a=int(input())
l = []
hm = [i for i in input().split()]
find = input()
i=0
while i < len(hm):
    if hm[i:].count(find):
        a = hm.index(find, i)
        l.append(a)
        i = 0 + a + 1
    else:
        i = len(hm)
if len(l) == 0:
    print("Отсутствует")
else:
    print(' '.join(str(i) for i in l))