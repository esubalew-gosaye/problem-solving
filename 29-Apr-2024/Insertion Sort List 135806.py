# Problem: Insertion Sort List - https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(-5000, head)
        dummy = head

        while dummy:
            
            loop = head
            while loop != dummy:
                
                if dummy.val < loop.val:
                    temp = dummy.val
                    dummy.val = loop.val
                    loop.val = temp

                loop = loop.next

            dummy = dummy.next
        
        return head