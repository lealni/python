from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: Optional[TreeNode]) -> bool:
    """
    https://leetcode.com/problems/symmetric-tree/description/
    """
    res_left = []
    res_right = []
    def left_node(tree):
        if tree:
            left_node(tree.left)
            res_left.append(tree.val)
            left_node(tree.right)

    def right_node(tree):
        if tree:
            right_node(tree.left)
            res_right.append(tree.val)
            right_node(tree.right)

    left_node(root.left)
    right_node(root.right)
    print(f"left {res_left}")
    print(f"right {res_right}")
    return True if res_left == res_right[::-1] else False
    


class TestDecrypt(unittest.TestCase):
    def test_tree01(self):
        expected1 = True
        self.assertEqual(isSymmetric(root1), expected1, f"Failed for root1={root1}")

    def test_tree02(self):
        expected2 = False
        self.assertEqual(isSymmetric(root2), expected2, f"Failed for root2={root2}")
    
    def test_tree03(self):
        expected3 = False
        self.assertEqual(isSymmetric(root3), expected3, f"Failed for root4={root3}")


root1 = TreeNode(val=1)
root1.left = TreeNode(val=2)
root1.right = TreeNode(val=2)
root1.left.left = TreeNode(val=3)
root1.left.right = TreeNode(val=4)
root1.right.right = TreeNode(val=3)
root1.right.left = TreeNode(val=4)

root2 = TreeNode(val=1)
root2.left = TreeNode(val=2)
root2.right = TreeNode(val=2)
root2.left.right = TreeNode(val=3)
root2.right.right = TreeNode(val=3)

root3 = TreeNode(val=1)
root3.left = TreeNode(val=2)
root3.right = TreeNode(val=2)
root3.left.left = TreeNode(val=2)
root3.right.left = TreeNode(val=2)

unittest.main()
