# Problem: Insertion Sort List - https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5001)
        current = head

        while current:
            target = dummy
           
            while target.next and target.next.val < current.val:
                
                target = target.next
            
            target_val = current.val
            new = ListNode(target_val)
            new.next = target.next
            target.next = new
            
            current = current.next
           
        
        return dummy.next