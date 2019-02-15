#!/usr/bin/env python3
'''
Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.

﻿
Sample Input:
abc a bCd bC AbC BC BCD bcd ABC
Sample Output:
abc 3
'''
from itertools import chain

with open('dataset_3363_3-2.txt', 'r') as code:
    code0 = code.read()
    code1 = code0.lower().split()
    code3 = set(code0.split())

Kmax=1
Imax = code1[0]

for i in code3:
    im = i.lower()
    k = code1.count(im)
    if k >= Kmax and i <= Imax:
        res={i: k}
        Kmax=k
print(res)