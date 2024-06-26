# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

from collections import defaultdict, deque

vertices, edges = list(map(int, input().split()))
start, destination = list(map(int, input().split()))

graph = defaultdict(list)
parent = {start: -1}
queu = deque([start])
for _ in range(edges):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

while queu:
    node = queu.popleft()

    if node == destination:
        break 
    
    for neighbor in graph[node]:
        if not neighbor in parent:
            queu.append(neighbor)
            parent[neighbor] = node 

if not destination in parent:
    print(-1)
    quit()

ans = []

par = destination
while parent[par] != -1:
    ans.append(par)
    par = parent[par]
ans.append(par)

print(len(ans) - 1)
print(*ans[::-1])

    

