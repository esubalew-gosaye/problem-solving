# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

tests = int(input())

for _ in range(tests):
    x = int(input())
    y = x & -x

    while True:
        if x ^ y > 0 and x & y > 0:
            break
        y += 1
    print(y)