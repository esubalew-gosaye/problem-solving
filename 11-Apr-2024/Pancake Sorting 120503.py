# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flip = []
        n = len(arr)
        for i in range(n - 1, 0, -1):
            max_index = arr.index(max(arr[: i + 1]))

            if max_index != i:
                arr[:max_index + 1] = reversed(arr[:max_index + 1])
                flip.append(max_index + 1)

                arr[:i + 1] = reversed(arr[:i + 1])
                flip.append(i + 1)
        return flip
    