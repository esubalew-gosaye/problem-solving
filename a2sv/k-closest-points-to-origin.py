class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in points:
            i.append(i[0]**2+i[1]**2)
        points.sort(key=lambda x:x[-1])
        return [points[i][:-1] for i in range(k)]
