# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest(object):

    def __init__(self, k, nums):
        self.store = nums
        self.k = k
        heapq.heapify(self.store)
        while len(self.store) > k:
            heapq.heappop(self.store)

            
    def add(self, val):
        if len(self.store) < self.k:
            heapq.heappush(self.store, val)
        elif val > self.store[0]:
            heapq.heapreplace(self.store, val)
        return self.store[0]
    
