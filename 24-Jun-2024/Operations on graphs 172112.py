# Problem: Operations on graphs - https://basecamp.eolymp.com/en/problems/2472

from collections import defaultdict

graphs = defaultdict(list)
vertices = int(input())
for _ in range(int(input())):
    inp = list(map(int, input().split()))
    if len(inp) == 3:
        a, b, c = inp 
        graphs[b].append(c)
        graphs[c].append(b)
    else:
        b, c = inp 
        print(*graphs[c])