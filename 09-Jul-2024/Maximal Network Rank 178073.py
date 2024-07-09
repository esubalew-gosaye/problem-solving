# Problem: Maximal Network Rank - https://leetcode.com/problems/maximal-network-rank/description/

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adjList = defaultdict(list)
        # {0: [1, 3], 1: [0, 2, 3], 3: [0, 1], 2: [1], 9:[6, 7, 8]}
        # {0: [1, 3], 1: [0, 2, 3], 3: [0, 1, 2], 2: [1, 3, 4], 4: [2]}
        # {0: [1], 1: [0, 2], 2: [1, 3, 4], 3: [2], 4: [2], 5: [6, 7], 6: [5], 7: [5]}
        
        maxNetwork = 0
        for u, v in roads:
            adjList[u].append(v)
            adjList[v].append(u)
        

        for node in adjList:
            for con in adjList:
                if con == node:
                    continue
                    
                if con in adjList[node]:
                    maxNetwork = max(len(adjList[node]) + len(adjList[con]) - 1, maxNetwork)
                else:
                    maxNetwork = max(len(adjList[node]) + len(adjList[con]), maxNetwork)
                

        return maxNetwork