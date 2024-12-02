import unittest
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional['TreeNode']) -> list[int]:
    """
    https://leetcode.com/problems/binary-tree-inorder-traversal/
    """
    result = []
    if not root:
        return result
    
    def sorter(tree):
        
        if tree:
            sorter(tree.left)        # Рекурсивно обходим левое поддерево
            result.append(tree.val) # Добавляем значение текущего узла
            sorter(tree.right) # Рекурсивно обходим правое поддерево
 
    sorter(root)
    return result

  
class TestDecrypt(unittest.TestCase):
    def test_tree2(self):
        expected2 = [4,2,6,5,7,1,3,9,8]
        self.assertEqual(inorderTraversal(root2), expected2, f"Failed for root2={root2}")

    def test_empty(self):
        expected3 = []
        self.assertEqual(inorderTraversal(root3), expected3, f"Failed for root3={root3}")
    
    def test_array4(self):
        expected4 = [1]
        self.assertEqual(inorderTraversal(root4), expected4, f"Failed for root4={root4}")


root2 = TreeNode(val=1)
root2.left = TreeNode(val=2)
root2.right = TreeNode(val=3)
root2.left.left = TreeNode(val=4)
root2.left.right = TreeNode(val=5)
root2.left.right.left = TreeNode(val=6)
root2.left.right.right = TreeNode(val=7)
root2.right.right = TreeNode(val=8)
root2.right.right.left = TreeNode(val=9)

root3 = []
root4 = TreeNode(val=1)

unittest.main()
