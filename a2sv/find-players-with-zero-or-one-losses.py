class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        store = dict()
        not_lost = []
        one_lost = []

        for winner, looser in matches:
            get_winner = store.get(winner, [0, 0])
            get_looser = store.get(looser, [0, 0])
            store[winner] = [get_winner[0] + 1, get_winner[1]]
            store[looser] = [get_looser[0], get_looser[1] + 1]
        
        for key in store:
            if store[key][1] == 0:
                not_lost += [key]
            elif store[key][1] == 1:
                one_lost += [key]
                
        return [sorted(not_lost), sorted(one_lost)]
