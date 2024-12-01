#!/usr/bin/env python3
import unittest


def decrypt(code: list[int], k: int) -> list[int]:
    """
    https://leetcode.com/problems/defuse-the-bomb/?envType=daily-question&envId=2024-11-26
    """

    if k == 0:
        return [ 0 for x in range(len(code))]
    elif k > 0:
        decript_list = [0 for x in range(len(code))]
        new_code = code + code[:k+1]
        for i in range(len(code)):
            start = i + 1
            stop = i + k + 1
            x = sum(new_code[start:stop])
            decript_list[i] = x
        print(decript_list)
        return decript_list
    else:
        decript_list = [0 for x in range(len(code))]
        new_code = code[k-1:] + code
        for i in range(len(code)):
            start = i + 1
            stop = i - k + 1
            x = sum(new_code[start:stop])
            decript_list[i] = x
            print(decript_list)
        return decript_list


def test_decrypt():

    k1 = 3
    code1 = [5, 7, 1, 4]
    if decrypt(code1, k1) == [12, 10, 16, 13]:
        print("TEST 1 PASS")
    else:
        print("TEST 1 FAIL")
    
    k2 = 0
    code2 = [1, 2, 3, 4]
    if decrypt(code2, k2) == [0, 0, 0, 0]:
        print("TEST 2 PASS")
    else:
        print("TEST 2 FAIL")

    k3 = -2
    code3 = [2, 4, 9, 3]
    if decrypt(code3, k3) == [12, 5, 6, 13]:
        print("TEST 3 PASS")
    else:
        print("TEST 3 FAIL")




class TestDecrypt(unittest.TestCase):
    def test_positive_k(self):
        code = [5, 7, 1, 4]
        k = 3
        expected = [12, 10, 16, 13]
        self.assertEqual(decrypt(code, k), expected, f"Failed for code={code}, k={k}")

    def test_zero_k(self):
        code = [1, 2, 3, 4]
        k = 0
        expected = [0, 0, 0, 0]
        self.assertEqual(decrypt(code, k), expected, f"Failed for code={code}, k={k}")

    def test_negative_k(self):
        code = [2, 4, 9, 3]
        k = -2
        expected = [12, 5, 6, 13]
        self.assertEqual(decrypt(code, k), expected, f"Failed for code={code}, k={k}")


test_decrypt()
unittest.main()