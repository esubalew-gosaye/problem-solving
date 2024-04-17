# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        fast = slow
        slow = head
        first_half = []
        second_half = []

        while fast:
            first_half.append(slow.val)
            second_half.append(fast.val)
            fast = fast.next
            slow = slow.next
        second_half.reverse()
        return first_half == second_half