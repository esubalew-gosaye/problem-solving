class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=0
        return [i[1] for i in sorted([(v, k) for k, v in d.items()], reverse=True)[:k]]
