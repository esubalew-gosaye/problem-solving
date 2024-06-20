# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        def dfs(node):
            for neigh in graph[node]:
                if neigh in colors:
                    if colors[neigh] == colors[node]:
                        return False
                else:
                    colors[neigh] = 1 - colors[node]
                    if not dfs(neigh):
                        return False
            return True

        for node in range(len(graph)):
            if node not in colors:
                colors[node] = 0
                if not dfs(node):
                    return False
        
        return True

            