# Problem: Cities and road - https://basecamp.eolymp.com/en/problems/992

from collections import defaultdict
n = int(input())
store = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j]:
            if not sorted((i, j)) in store:
                store.append(sorted((i, j)))
print(len(store))