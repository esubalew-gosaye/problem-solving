# Problem: C - Potions (Hard Version) - https://codeforces.com/gym/536373/problem/C

from heapq import heappop, heappush

n = int(input())
array = list(map(int, input().split()))

heap = []
health = 0

for num in array:
    health += num 
    heappush(heap, num)
    
    if health < 0:
        health -= heappop(heap)
print(len(heap))