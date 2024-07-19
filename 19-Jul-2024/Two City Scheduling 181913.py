# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost_determine_list = [(cost[0] - cost[1], cost) for cost in costs]
        cost_determine_list.sort()

        total_cost = 0
        length = len(costs)
        for i in range(length):
            if i < length // 2:
                total_cost += cost_determine_list[i][1][0]
            else:
                total_cost += cost_determine_list[i][1][1]

        return total_cost