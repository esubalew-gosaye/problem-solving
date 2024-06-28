# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graphs = defaultdict(list)
        ans = [-1] * n
        
        for a, b in redEdges:
            graphs[a].append((b, 0))

        for u, v in blueEdges:
            graphs[u].append((v, 1))

        queue = deque([(0, 0, 0), (0, 0, 1)])
        visited = set([(0, 0), (0, 1)])

        while queue:
            node, distance, color = queue.popleft()

            if ans[node] == -1:
                ans[node] = distance

            for neighbor in graphs[node]:
                if not neighbor in visited and color != neighbor[-1]:
                    queue.append((neighbor[0], distance + 1, neighbor[-1]))
                    visited.add(neighbor)
        return ans



        