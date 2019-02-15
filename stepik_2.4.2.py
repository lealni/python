#!/usr/bin/env python3

'''
Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.

Sample Input 1:
aaaabbcaa
Sample Output 1:
a4b2c1a2
Sample Input 2:
abc
Sample Output 2:
a1b1c1
'''

src = input()
dst = ''
s = 1
if len(src) == 1:
    dst += src + str(s)
else:
    for i in range(len(src)):
        a = src[i]
        if (i+1) ==  len(src):
            dst += a + str(s)
            break
        if src[i] == src[i+1]:
            s += 1
        elif (src[i] != src[i+1]) and s != 1:
            dst += a + str(s)
            s = 1
        else:
            s = 1
            dst += a + str(s)
print(dst)

# abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# c=1
# d = ''
# s = input()
# d += s[0]
# i = 1
# while d == s[i]:
#   c += 1
#   i +=1
#   if i > len(s)-1:
#     break
# d += str(c)
# print(d+str(c))
# print(i)
# print(c)
# d += s[i]
# print(d)


# #for i in range(len(s)):
#  # j = i
#  # if j >= len(s)-1:
#   #  break
#   #while s[j] == s[j+1]:
#    # c += 1
#    # j += 1
#    # if j >= len(s):
#     #  break
#     #d += s[i] + str(c)
# #print(d)  
# #  for j in len(s):
#  #   if s[i] == s[j]:
#   #    c += s[i] 
