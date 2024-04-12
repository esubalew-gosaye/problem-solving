# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

ans = arr[k - 1]

if k == 0:
    ans = arr[0] - 1
    

if n > k:
    if arr[k] > ans and ans >= 1 and ans <= 1000 * 1000 * 1000:
        print(ans)
    else:
        print(-1)
else:
    if ans >= 1 and ans <= 1000 * 1000 * 1000:
        print(ans)
    else:
        print(-1)
