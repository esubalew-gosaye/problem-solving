# Problem: C - Pairs - https://codeforces.com/gym/504384/problem/C

from collections import Counter
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(3)]

first = Counter(matrix[0])

cnt = 0
for i in range(n):
    cnt += first.get(matrix[1][matrix[2][i] - 1], 0)
print(cnt)