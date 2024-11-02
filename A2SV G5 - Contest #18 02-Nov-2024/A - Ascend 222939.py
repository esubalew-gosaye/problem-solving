# Problem: A - Ascend - https://codeforces.com/gym/526229/problem/A

def subarray_length(n, array):
    if n == 1:
        return 1

    max_length = 1
    current_length = 1

    for i in range(1, n):
        if array[i] > array[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    max_length = max(max_length, current_length)

    return max_length

n = int(input())
array = list(map(int, input().split()))
print(subarray_length(n, array))
