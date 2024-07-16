# Problem: B - Guess the Maximum - https://codeforces.com/gym/535309/problem/B

for _ in range(int(input())):
    n = int(input())
    v = list(map(int, input().split()))

    count = float('inf')
    for i in range(n - 1):
        ans = max(v[i], v[i + 1])
        count = min(count, ans)
    
    print(count - 1)