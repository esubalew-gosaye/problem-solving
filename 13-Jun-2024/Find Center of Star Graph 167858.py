# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        store = defaultdict(int)

        for u, v in edges:
            store[v] += 1
            store[u] += 1
            
        for key in store:
            if store[key] == len(edges):
                return key