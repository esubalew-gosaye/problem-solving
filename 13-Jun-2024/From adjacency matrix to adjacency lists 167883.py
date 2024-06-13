# Problem: From adjacency matrix to adjacency lists - https://basecamp.eolymp.com/en/problems/3981

from collections import defaultdict
store = defaultdict(list)

n = int(input())
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j]:
            store[i].append(j + 1)
for key in store:
    print(len(store[key]), *store[key])



