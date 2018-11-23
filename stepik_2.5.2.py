#!/usr/bin/env python3

a = [ int(i) for i in input().split() ]
print(a)
b = []
if len(a) == 1:
    sh = [str(i) for i in a]
    print(' '.join(sh))
else:
    for i in range(len(a)):
        print("afte for " + str(i))
        print( b)
        if i == len(a)-1:
            b += [ a[i-1] + a[0] ]
            print(b)
        else:
            b += [ a[i-1] + a[i+1]  ]
            print(b)
    sh = [str(i) for i in b]
    print(' '.join(sh))
