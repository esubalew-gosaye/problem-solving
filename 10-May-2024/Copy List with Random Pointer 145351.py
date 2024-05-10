# Problem: Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        nodeDict = {None: None}

        current = head

        if not current:
            return

        while current:
            temp = Node(current.val)
            nodeDict[current] = temp
            current = current.next

        current = head
        while current:
            ncurrent = nodeDict[current]
            ncurrent.next = nodeDict[current.next]

            if current.random:
                ncurrent.random = nodeDict[current.random]
            
            current = current.next

        return nodeDict[head]