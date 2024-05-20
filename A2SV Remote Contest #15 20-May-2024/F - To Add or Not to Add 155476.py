# Problem: F - To Add or Not to Add - https://codeforces.com/gym/524150/problem/F

a, k = map(int, input().split())
nums = sorted(list(map(int, input().split())))

left = 0
summation = 0
freq = 0
num = nums[0]

for right in range(a):
    summation += nums[right]

    while k < nums[right] * (right - left + 1) - summation:
        summation -= nums[left]
        left += 1
    
    if right - left + 1 > freq:
        freq = right - left + 1
        num = nums[right]
    
print(freq, num)