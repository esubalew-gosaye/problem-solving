# Problem: Problemsolving Log - https://codeforces.com/gym/522997/problem/A

from collections import Counter

# Input number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Input duration of the contest and Monocarp's contest log
    n = int(input())
    logs = input().strip()

    counter = Counter(logs)
    solved = 0
    for log in counter:
        if counter[log] >= (ord(log) - 64):
            solved += 1
    print(solved)