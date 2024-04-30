# Problem: B - Mattia Binotto - https://codeforces.com/gym/520098/problem/B


def max_satisfied_drivers(n, pit_stop_times):
    pit_stop_times.sort() 
    max_satisfied = 0
    cumulative_time = 0

    for pit_stop_time in pit_stop_times:
        wait_time = cumulative_time
        if wait_time <= pit_stop_time:
            max_satisfied += 1
            cumulative_time += pit_stop_time

    return max_satisfied


n = int(input())
pit_stop_times = list(map(int, input().split()))


print(max_satisfied_drivers(n, pit_stop_times))