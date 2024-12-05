from typing import Optional
import unittest


def isPalindrome(head: Optional[ListNode]) -> bool:
    """
    https://leetcode.com/problems/palindrome-linked-list/
    """
    head_list = []
    ind = head
    while ind:
        head_list.append(ind.val)
        ind = ind.next

    return head_list == head_list[::-1]
