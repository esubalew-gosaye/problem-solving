# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int):
        graph = defaultdict(list)

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        visited = [False for i in range(n)]
        visited[source] = True
        stack = [source]

        while stack:
            node = stack.pop()
            
            if node == destination:
                return True
            
            for adj in graph[node]:
                if not visited[adj]:
                    stack.append(adj)
                    visited[adj] = True
                    if adj == destination:
                        return True
                        
        return False

