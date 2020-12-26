#!/usr/bin/env python3
'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число 𝑛 — количество завершенных игр.
После этого идет 𝑛n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.
Sample Input:
3
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2
Sample Output:
Зенит:2 2 0 0 6
ЦСКА:2 0 1 1 1
Спартак:2 0 1 1 1
'''
# Games_total = int(input())
# Matches = []
# while Games_total:
#     Matches.append(input().split(';'))
#     Games_total -= 1

def include_data(kolvo):
    Matches = []
    #Games_total = int(input())
    # Games_total = int(kolvo)
    # it = range(Games_total)
    # for i in raz, dva, tri:
    #     Matches.append(i.split(';'))
    while kolvo:
        Matches.append(input().split(';'))
        kolvo -= 1
    return Matches

# def include_data(kolvo, raz, dva, tri):
#     Matches = []
#     #Games_total = int(input())
#     # Games_total = int(kolvo)
#     # it = range(Games_total)
#     for i in raz, dva, tri:
#         Matches.append(i.split(';'))
#     # while it:
#     #     Matches.append(input().split(';'))
#     #     it -= 1
#     return Matches

def igry(Matches):
    #schitaem = []
    schitaem_dic = {}
    for i in range(len(Matches)):
        for j in range(0, len(Matches[i]), 2):
            # print(Matches[i][j])
            games = Matches[i].count(Matches[i][j])
            #print(games)
            if Matches[i][j] in schitaem_dic.keys():
                key = schitaem_dic.get(Matches[i][j])
                key[0] += games
            else:
                schitaem_dic.update({Matches[i][j]: [games, 0, 0, 0, 0]})
                #schitaem.insert(0, games)
    return schitaem_dic


def data_processing(Matches, schitaem_dic):
    result = schitaem_dic
    for i, j, y, z in Matches:
        # print(i, j, y, z)
        if int(j) > int(z):
            pobeda_comand = result.get(i)
            pobeda_comand[1] += 1
            pobeda_comand[4] += 3

            porazhen_comand01 = result.get(y)
            porazhen_comand01[3] += 1
            result.update({y: porazhen_comand01})

        elif int(j) < int(z):
            porazhen_comand01 = result.get(i)
            porazhen_comand01[3] += 1
            result.update({i: porazhen_comand01})

            pobeda_comand = result.get(y)
            pobeda_comand[1] += 1
            pobeda_comand[4] += 3
            result.update({y: pobeda_comand})

        else:
            nich_comand01 = result.get(i)
            nich_comand01[2] += 1
            nich_comand01[4] += 1
            result.update({i: nich_comand01})

            nich_comand02 = result.get(y)
            nich_comand02[2] += 1
            nich_comand02[4] += 1
            result.update({y: nich_comand02})

    #print(result)
    # return result.items()
    return print_result(result)

def print_result(result):
    for key in result.keys():
        # values = result.get(key)
        game, vin, nich, porazh, ochki = result.get(key)
        # tot = ' '.join(game, vin, nich, porazh, ochki)
        print(key + ':',game, vin, nich, porazh, ochki)

def data_main():
    kolvo = int(input())
    a=include_data(kolvo)
    # b = data_processing(a)
    c = igry(a)
    d = data_processing(a, c)
    #print(b)
    # print(d)
    # return b

    



# def test_main():
#     print("test_main...")
#     assert (sorted(data_main("3 Зенит;3;Спартак;1 Спартак;1;ЦСКА;1 ЦСКА;0;Зенит;2".split()) == ['Зенит:2 2 0 0 6', 'ЦСКА:2 0 1 1 1', 'Спартак:2 0 1 1 1']))
#     print('OK')

if __name__ == '__main__':
    # a = main('3', 'Зенит;3;Спартак;1', 'Спартак;1;ЦСКА;1', 'ЦСКА;0;Зенит;2')
    # assert (a == 'Зенит:2 2 0 0 6', 'ЦСКА:2 0 1 1 1', 'Спартак:2 0 1 1 1')
    # test_main()
    # kolvo = int(input())
    # data_main("3", "Зенит;3;Спартак;1", "Спартак;1;ЦСКА;1", "ЦСКА;0;Зенит;2")
    data_main()