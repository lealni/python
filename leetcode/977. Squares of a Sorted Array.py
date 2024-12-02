import unittest

def sortedSquares(nums: list[int]) -> list[int]:
    """
    https://leetcode.com/problems/squares-of-a-sorted-array/
    """
    num_square = [x**2 for x in nums]
    num_square.sort()
    return num_square

 
class TestDecrypt(unittest.TestCase):
    def test_array1(self):
        arr1 = [-4,-1,0,3,10]
        expected2 = [0,1,9,16,100]
        self.assertEqual(sortedSquares(arr1), expected2, f"Failed for arr1={arr1}")

    def test_array2(self):
        arr2 = [-7,-3,2,3,11]
        expected2 = [4,9,9,49,121]
        self.assertEqual(sortedSquares(arr2), expected2, f"Failed for arr2={arr2}")


unittest.main()