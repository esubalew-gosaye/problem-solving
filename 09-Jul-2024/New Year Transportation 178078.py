# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A

n, t = list(map(int, input().split()))
transportation = list(map(int, input().split()))

flag = False 
cell = 1

while t >= cell:
    if t == cell:
        flag = True 
        break

    cell = cell + transportation[cell - 1]
print("YES" if flag else "NO")
    