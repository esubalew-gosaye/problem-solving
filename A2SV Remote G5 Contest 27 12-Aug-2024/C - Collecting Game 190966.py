# Problem: C - Collecting Game - https://codeforces.com/gym/541399/problem/C

n = int(input())
m = list(map(int, input().split())) 

max_mass = max(m)
freq = [0] * (max_mass+1)
for pl_mass in m:
    freq[pl_mass] += 1

dp = [0] * (max_mass+1)
dp[1] = freq[1]

for i in range(2, max_mass+1):
    dp[i] = max(dp[i-1], dp[i-2] + i * freq[i]) 

print(dp[max_mass])