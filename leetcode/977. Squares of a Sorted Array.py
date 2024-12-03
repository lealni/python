import unittest

def sortedSquares_1(nums: list[int]) -> list[int]:
    """
    https://leetcode.com/problems/squares-of-a-sorted-array/
    O(nlogn)
    """
    num_square = [x**2 for x in nums]
    num_square.sort()
    return num_square

def sortedSquares(nums: list[int]) -> list[int]:
    """
    https://leetcode.com/problems/squares-of-a-sorted-array/
    O(n)
    """
    left_u = 0
    right_u = len(nums) -1
    res = []
    if nums[0] < 0:
        while left_u <= right_u:
            if nums[left_u]**2 > nums[right_u]**2:
               res.append(nums[left_u]**2)
               left_u += 1
            else:
                res.append(nums[right_u]**2)
                right_u -= 1
    else:
        return [x**2 for x in nums]
    return res[::-1]


                






    #         if num_square[right_u] < nums[u1]**2:
    #             num_square.append(nums[u1]**2)
    #             num_square.pop(u1)
    #             u1 +=1
    #         else:
    #             u2 -= 1

    # else:
    #     return num_square

    
 
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