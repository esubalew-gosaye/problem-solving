# Problem: C - Hello World - https://codeforces.com/gym/543262/problem/C

test = int(input())
for _ in range(test):
    size = int(input())
    array = sorted(list(map(int, input().split())))
    currSum = 1 
    valid = True if array[0] == 1 else False
    for num in array[1:]:
        if num > currSum:
            valid = False
        currSum += num
    print('YES' if valid else 'NO')