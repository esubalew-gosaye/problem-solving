# Problem: Remove Duplicates from Sorted List II - https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-500, head)
        tail = dummy
        prev = head

        if not head:
            return head

        curr = head.next

        while curr:

            has_duplicate = False
            while curr and prev.val == curr.val:
                has_duplicate = True
                prev.next = curr.next
                curr = curr.next

            if curr:
                prev = prev.next
                curr = curr.next
            else:
                prev = None
                
            if has_duplicate:
                tail.next = prev
            else:
                tail = tail.next

        return dummy.next