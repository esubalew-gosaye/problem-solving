# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, fh: Optional[ListNode], sh: Optional[ListNode]):
        dummy = ListNode()
        tail = dummy

        while fh and sh:
            if fh.val <= sh.val:
                tail.next = fh
                fh = fh.next
            else:
                tail.next = sh
                sh = sh.next
            tail = tail.next

        if fh:
            tail.next = fh
        elif sh:
            tail.next = sh

        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        if not head or not head.next:
            return head 
    
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        first_half = head
        second_half = slow

        if prev:
            prev.next = None
        
        left = self.sortList(first_half)
        right = self.sortList(second_half)

         

        return self.merge(left, right)

# 