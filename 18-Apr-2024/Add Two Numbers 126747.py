# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []

        while l1:
            num1.append(str(l1.val))
            l1 = l1.next
        while l2:
            num2.append(str(l2.val))
            l2 = l2.next
        
        added = str(int("".join(num1)[::-1]) + int("".join(num2)[::-1]))


        dummy = ListNode()
        curr = dummy
        for i in added[::-1]:
            node = ListNode(int(i))
            curr.next = node
            curr = curr.next

        return dummy.next