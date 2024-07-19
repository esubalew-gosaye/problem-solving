# Problem: Odd Sum - https://codeforces.com/problemset/problem/797/B

n = int(input())
seq = list(map(int, input().split()))

odd_count = 0
odd_sum = 0
min_pos_odd = float("inf")
max_neg_odd = float("-inf")


for i in range(n):
    if seq[i] > 0:
        if seq[i] % 2 == 0:
            odd_sum += seq[i]
        else:
            odd_sum += seq[i]
            min_pos_odd = min(min_pos_odd, seq[i])
            odd_count += 1
    else:
        if seq[i] % 2:
            max_neg_odd = max(max_neg_odd, seq[i])

if odd_count == 0:
    print(odd_sum + max_neg_odd)
elif odd_count % 2:
    print(odd_sum )
else:
    print(odd_sum - min(min_pos_odd, -max_neg_odd))        



