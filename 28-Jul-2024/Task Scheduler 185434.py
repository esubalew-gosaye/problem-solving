# Problem: Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = []
        ans = 0
        
        for i, j in count.items():
            heapq.heappush(heap, (-j, i))

        while heap:
            i = 0
            temp = []
            while i <= n:
                ans += 1
                if heap:
                    a, b = heapq.heappop(heap)
                    a += 1
                    if a < 0:
                        temp.append((a, b))
                if not temp:
                    break
                i += 1
            for a, b in temp:
                heapq.heappush(heap, (a, b))
    
        return ans