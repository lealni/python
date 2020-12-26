#!/usr/bin/env python3
'''
Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d
 и два числа: key
 и value
.

Если ключ key
 есть в словаре d
, то добавьте значение value
 в список, который хранится по этому ключу. 
Если ключа key
 нет в словаре, то нужно добавить значение в список по ключу 2⋅key
. Если и ключа 2⋅key
 нет, то нужно добавить ключ 2⋅key
 в словарь и сопоставить ему список из переданного элемента [value]
.

Требуется реализовать только эту функцию, кода вне неё не должно быть.
Функция не должна вызывать внутри себя функции input и print.
'''

d = {}

def update_dictionary(d, key, value):
    if key in d.keys():
        v = d.get(key)
        v.append(value)
        print(v)
        d[key] = v
        print(d)
    elif 2*key in d.keys():
        v = d.get(2*key)
        v.append(value)
        d[2*key] = v
    else:
        d[2*key] = [value]

    print(d)

update_dictionary(d, 1, -1)
update_dictionary(d, 2, -2)
update_dictionary(d, 1, -3)
update_dictionary(d, 3, -4)
update_dictionary(d, 0, -5)