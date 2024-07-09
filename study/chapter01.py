#!/usr/bin/env python3

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    iteration = 0

    while low <= high:
        midle = (low + high) // 2
        guess = list[midle]
        iteration += 1
        print(iteration)
        if guess == item:
            return midle
        if guess > item:
            high = midle - 1
        else:
            low = midle + 1
    return None

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_search(my_list, 7))
# print binary_search(my_list, -1)