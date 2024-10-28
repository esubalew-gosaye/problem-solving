# Problem: B - Discounts - https://codeforces.com/gym/559568/problem/B

_ = input()
a = list(map(int, input().split()))
c = input()
m = list(map(int, input().split()))
a.sort(reverse=True)
t_sum = sum(a)
for q in range(int(c)):
    print(t_sum - a[m[q] - 1])