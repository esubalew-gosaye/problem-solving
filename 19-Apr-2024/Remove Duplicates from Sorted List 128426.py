# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-500, head)
        prev = dummy
        curr = head

        while curr:
            prev = prev.next
            curr = curr.next

            while curr and prev.val == curr.val:
                prev.next = curr.next
                curr = curr.next
        return head
            

        