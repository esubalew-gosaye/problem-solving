# Problem: Reorganize String - https://leetcode.com/problems/reorganize-string/description/

class Solution:
    def reorganizeString(self, s: str) -> str:
        occurrence = Counter(s)
        heap = []
        for char, count in occurrence.items():
            if count > ceil(len(s) / 2):
                return ""
            heap.append((-count, char))
        heapq.heapify(heap)

        res = []
        last = None
        while heap or last:
            f1, ch1 = heapq.heappop(heap)
            res.append(ch1)
            f1 += 1 

            if last:
                heapq.heappush(heap, last)
            
            last = (f1, ch1) if f1 < 0 else None

        return "".join(res)        

        