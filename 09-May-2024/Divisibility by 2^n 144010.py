# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

# Input number of test cases
t = int(input())

def countwos(n):
    number_of_two = 0
    while n % 2 == 0:
        n //= 2
        number_of_two += 1
    return number_of_two


# Process each test case
for _ in range(t):
    # Input duration of the contest and Monocarp's contest log
    n = int(input())
    logs = list(map(int, input().split()))

    twos = 0
    for log in logs:
        twos += countwos(log)

    twos_index = [countwos(i) for i in range(1, n + 1)]
    twos_index.sort(reverse=True)
    i = 0
    op = 0
    while twos < n and i < n:
        twos += twos_index[i]
        op += 1
        i += 1

    print(op if n <= twos else -1)