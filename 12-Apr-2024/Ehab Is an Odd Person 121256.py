# Problem: Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n = int(input())
arr = list(map(int, input().split()))

if all(arr[i - 1] % 2 == arr[i] % 2 for i in range(1, n)):
    print(*arr)
else:
    print(*sorted(arr))