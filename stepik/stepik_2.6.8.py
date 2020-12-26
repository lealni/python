#!/usr/bin/env python3

a=int(input())
l = []
hm = [[str(i)]*i for i in range(1,a+1)]
for i in hm:
    for j in range(len(i)):
        l.append(i[j])

print(' '.join(l[i] for i in range(a)))
