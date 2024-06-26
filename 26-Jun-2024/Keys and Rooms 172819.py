# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queu = deque([0])
        visited.add(0)
        while queu:
            node = queu.popleft()
            
            for room in rooms[node]:
                if not room in visited:
                    queu.append(room)
                    visited.add(room)
        
        return len(visited) == len(rooms)
        

        

    # [[1,3],[1,4],[2,3,4,1],[],[4,3,2]]
    #    0     1       2     3     4

    '''
        visited = [
        queu = [1, 3
    
    '''