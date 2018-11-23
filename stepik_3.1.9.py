#!/usr/bin/env python3

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def modify_list(l):
    print(len(l))
    # for i in range(-1, -len(l), -1):
    #     print(i)
    #     if l[i] % 2 != 0:
    #         l.pop(i)
    #         print(l)
    #         i +=1
    #     print(l)
    i = 0
    while i <= len(l)-1:
        print(i)
        if l[i] % 2 !=0:
            l.pop(i)
            print(l)
            i -= 1
        i += 1
    
    for j in range(len(l)):
        l[j] = l[j] // 2

    print(l)
        

c = modify_list(l)