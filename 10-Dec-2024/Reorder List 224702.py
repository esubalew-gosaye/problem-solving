# Problem: Reorder List - https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # split the linked list into half
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the last half

        curr = slow.next
        slow.next = prev = None
        while curr:
            temp = curr.next

            curr.next = prev
            prev = curr 
            curr = temp

        # merging the two halfs

        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1

            first, second = temp1, temp2

        



        