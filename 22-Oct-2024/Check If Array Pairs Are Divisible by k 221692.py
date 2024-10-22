# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count = 0
        store = defaultdict(int)

        for i in arr:
            if store.get(i % k):
                store[i % k] = store.get(i % k) - 1
                count += 1
            else:
                store[-i % k] += 1
        
        return True if count == len(arr) // 2 else False

