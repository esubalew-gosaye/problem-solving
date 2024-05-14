# Problem: Team Composition: Programmers and Mathematicians - https://codeforces.com/problemset/problem/1611/B

for _ in range(int(input())):
    a, b = map(int, input().split())

    low = 0
    high = min(a, b)
    ans = 0
    while low <= high:

        mid = (low + high) // 2

        if a >= mid and b >= mid and a + b >= mid * 4:
            ans = max(ans, mid)
            low = mid + 1
        else:
            high = mid - 1
    print(ans)