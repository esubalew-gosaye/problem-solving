# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n = int(input())

count = 0
for num in range(n + 1):
    ls = set()
    d = 2
    while d * d <= num:
        while num % d == 0:
            ls.add(d)
            num = num // d 
        d += 1
    if num > 1:
        ls.add(num)
    if len(ls) == 2:
        count += 1
print(count)
