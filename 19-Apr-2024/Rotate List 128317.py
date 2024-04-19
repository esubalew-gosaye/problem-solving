# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        ptr = head
        while ptr:
            count += 1
            ptr = ptr.next

        if not head or k == 0 or count == 1 or k % count == 0:
            return head

        k = k % count

        dummy = ListNode(-1, head)
        curr = dummy
        prev = dummy

        for _ in range(k):
            curr = curr.next
        
        for _ in range(count - k):
            curr = curr.next
            prev = prev.next
        
        
        new_head = prev.next
        prev.next = None
        curr.next = head
        

        return  new_head