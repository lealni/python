#!/usr/bin/env python3
c = 1
a= 0
sum = []
qrt = 0
while c != 0:
  ls = [ int(i) for i in input().split('\n')]
  sum.append(ls)
  for i in ls:
    a += i
    if a == 0:
      c = 0
      for i in sum:
        for j in i:
          qrt += j ** 2
print(qrt)

