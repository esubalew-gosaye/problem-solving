# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: set() for i in range(n)}
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        cmps, used = [], set()
        for eg in graph:
            if eg in used:
                continue
            q, counter = deque([eg]), 0
            used.add(eg)
            while q:
                pp = q.popleft()
                counter += 1
                for nn in graph[pp]:
                    if nn not in used:
                        q.append(nn)
                        used.add(nn)
            cmps.append(counter)
        prefix = [cmps[0]] + [0]*(len(cmps) - 1)
        for i in range(1, len(cmps)):
            prefix[i] = prefix[i - 1] + cmps[i]
        ans = 0
        for i in range(len(cmps)):
            ans += (n - prefix[i])*cmps[i]
        return ans


            