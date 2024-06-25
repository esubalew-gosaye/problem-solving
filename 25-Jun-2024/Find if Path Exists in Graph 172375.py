# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int):
        graph = defaultdict(list)

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        visited = [False for i in range(n)]

        def dfs(start):
            visited[start] = True
            if start == destination:
                return True 
            
            for adj in graph[start]:
                if not visited[adj]:
                    if dfs(adj):
                        return True
                
            return False
        
        return dfs(source)

