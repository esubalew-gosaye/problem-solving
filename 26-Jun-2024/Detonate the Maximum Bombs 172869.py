# Problem: Detonate the Maximum Bombs - https://leetcode.com/problems/detonate-the-maximum-bombs/description/

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(bombs)):
            x, y, d = bombs[i]
            for j in range(i + 1, len(bombs)):
                X, Y, D = bombs[j]
                distance = ((X - x)**2 + (Y - y)**2)

                if distance <= d ** 2:
                    graph[i].append(j)

                if distance <= D ** 2:
                    graph[j].append(i)

        maxDetonate = 0

        def dfs(start, visited):
            visited.add(start)

            for neigh in graph[start]:
                if not neigh in visited:
                    dfs(neigh, visited)

            return len(visited)
        
        for k in range(len(bombs)):
            maxDetonate = max(maxDetonate, dfs(k, set()))

        return maxDetonate
        # {1: [0]}
        # {0: [1, 2], 2: [1, 3], 3: [1, 2, 4], 4: [2, 3]}
        

