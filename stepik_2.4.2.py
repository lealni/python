#!/usr/bin/env python3
abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
c=1
d = ''
s = input()
d += s[0]
i = 1
while d == s[i]:
  c += 1
  i +=1
  if i > len(s)-1:
    break
d += str(c)
print(d+str(c))
print(i)
print(c)
d += s[i]
print(d)


#for i in range(len(s)):
 # j = i
 # if j >= len(s)-1:
  #  break
  #while s[j] == s[j+1]:
   # c += 1
   # j += 1
   # if j >= len(s):
    #  break
    #d += s[i] + str(c)
#print(d)  
#  for j in len(s):
 #   if s[i] == s[j]:
  #    c += s[i] 
