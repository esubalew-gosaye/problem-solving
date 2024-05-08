# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        list1 = []
        list2 = []
        itr1 = l1
        while itr1:
            list1.append(itr1.val)
            itr1 = itr1.next
        itr2 = l2
        while itr2:
            list2.append(itr2.val)
            itr2 = itr2.next
        total = str(int("".join(map(str, list1))) + int("".join(map(str, list2))))
        head = ListNode(total[0])
        itr = head
        for val in range(1, len(total)):
            current = ListNode(total[val])
            itr.next = current
            itr = current
        return head

        