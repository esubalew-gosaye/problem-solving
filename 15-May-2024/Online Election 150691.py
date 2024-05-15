# Problem: Online Election - https://leetcode.com/problems/online-election/

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.vote = persons
        self.times = times
        
        count = {}
        winner = {}
        leader = persons[0]

        for i in range(len(times)):
            count[persons[i]] = count.get(persons[i], 0) + 1

            if count[persons[i]] >= count[leader]:
                leader = persons[i]
            
            winner[times[i]] = leader

        self.winner = winner    
        print(winner)
    def q(self, t: int) -> int:
        n = len(self.times) - 1
        low = -1
        high = n + 1

        while low + 1 < high:
            mid = (low + high) // 2

            if self.times[mid] <= t:
                low = mid 
            else:
                high = mid 

        return self.winner[self.times[low]]
