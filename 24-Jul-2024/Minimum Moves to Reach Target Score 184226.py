# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        step = 0
        while target != 1 and maxDoubles > 0:
            step += 1
            if target % 2:
                target -= 1
            else:
                target //= 2
                maxDoubles -= 1

        return step + target - 1