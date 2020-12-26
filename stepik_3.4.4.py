#!/usr/bin/env python3
'''
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.

Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому языку по всем абитуриентам:

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом: 

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
Sample Input:
Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85
'''
file = './stepik_3.4.4.txt'

def ReadJournal(Journal):
    with open(Journal, 'r') as journal:
        for string in journal:
            yield string.strip().split(';')

math = 0
physics = 0
rus = 0
total = 0

for i in ReadJournal(file):
    # print(i)
    A = (int(i[1]) + int(i[2]) + int(i[3]))/3
    # ocen = 
    math += int(i[1])
    physics += int(i[2])
    rus += int(i[3])
    total += 1
    with open("./stepik_3.4.4.out", 'a') as out:
        print(A, file=out)
print("Средние оценки по Математике, Физике и Русскому:")
with open("./stepik_3.4.4.out", 'a') as out:
    print(math/total, physics/total, rus/total, sep=' ', file=out)

# {math:[0, 0], physics: [0, 0], rus: [0, 0]}