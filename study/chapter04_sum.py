def sum(arr):
    total = 0
    if len(arr) == 0:
        return 0
    else:
        total = arr[0] + sum(arr[1:])
        return total


print(sum([2, 4, 6, 8, 10, 12]))



def max(arr):
    
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    else:
        sub_max = max(arr[1:]) 
        return arr[0] if arr[0] > sub_max else sub_max

print(max([1, 2, 5, 4, 9, 0, 3, 10, 50, 11, 22, 60]))
print(max([]))
print(max([3]))


def binary_recurs(arr, target):

    if len(arr) == 0:
        return None
    mid_arr_index = len(arr) // 2
    if arr[mid_arr_index] == target:
        return mid_arr_index
    if arr[mid_arr_index] > target:
        return binary_recurs(arr[:mid_arr_index], target)
    else:
        return binary_recurs(arr[mid_arr_index:], target)
    
print(binary_recurs([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 15))