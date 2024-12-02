import unittest
def arrayRankTransform_02(arr: list[int]) -> list[int]:
    """
    chatgpt Solution
    """
    rank_dict = {num: rank for rank, num in enumerate(sorted(set(arr)), start=1)}
    
    # Заменяем элементы их рангами
    return [rank_dict[num] for num in arr]

def arrayRankTransform_02(arr: list[int]) -> list[int]:
    """
    Second attempt to solve the task, this is too slow with big array
    """
    grab_rank_arr = []
    equil = set(arr)
    # sort_arr = list(equil)
    # sort_arr.sort()
    sort_arr = sorted(equil)
    for el in arr:
        grab_rank_arr.append(sort_arr.index(el)+1)

    return grab_rank_arr

def arrayRankTransform_01(arr: list[int]) -> list[int]:
    """
    First attempt to solve the task 
    https://leetcode.com/problems/rank-transform-of-an-array/?envType=daily-question&envId=2024-11-26
    """
    rank_arr = [1 for x in range(len(arr))]
    delitel = 0
    equs = set()
    for i in range(len(arr)):
        for y in range(len(arr)):
            if arr[i] == arr[y] and i != y:
                equs.add(arr[i])
                delitel += 1
            elif arr[i] > arr[y]:
                rank_arr[i] += 1
    print(f"equs = {equs}")
    print(f"rank = {rank_arr}")
    print(f"delitel = {delitel}")
    if delitel >= 1:
        for equ in equs:
            for i in range(len(arr)):
                if arr[i] > equ:
                    rank_arr[i] -= 1

    return rank_arr


class TestDecrypt(unittest.TestCase):
    def test_array1(self):
        array1 = [40,10,20,30]
        expected1 = [4,1,2,3]
        self.assertEqual(arrayRankTransform(array1), expected1, f"Failed for array1={array1}")

    def test_equal_rank(self):
        array2 = [100,100,100]
        expected2 = [1,1,1]
        self.assertEqual(arrayRankTransform(array2), expected2, f"Failed for array2={array2}")

    def test_array3(self):
        array3 = [37,12,28,9,100,56,80,5,12]
        expected3 = [5,3,4,2,8,6,7,1,3]
        self.assertEqual(arrayRankTransform(array3), expected3, f"Failed for array3={array3}")
    
    def test_array4(self):
        array4 = [37,12,28,9,100,56,80,5,12,37]
        expected4 = [5,3,4,2,8,6,7,1,3,5]
        self.assertEqual(arrayRankTransform(array4), expected4, f"Failed for array4={array4}")

    def test_array5(self):
        array5 = [37,12,28,9,100,56,80,5,12,37,9]
        expected5 = [5,3,4,2,8,6,7,1,3,5,2]
        self.assertEqual(arrayRankTransform(array5), expected5, f"Failed for array5={array5}")

    def test_array6(self):
        array6 = [37,12,28,9,12,100,56,80,5,12]
        expected6 = [5,3,4,2,3,8,6,7,1,3]
        self.assertEqual(arrayRankTransform(array6), expected6, f"Failed for array6={array6}")

    def test_array7(self):
        array7 = [-1,-1,-1,-1,1,2,3]
        expected7 = [1,1,1,1,2,3,4]
        self.assertEqual(arrayRankTransform(array7), expected7, f"Failed for array7={array7}")


unittest.main()