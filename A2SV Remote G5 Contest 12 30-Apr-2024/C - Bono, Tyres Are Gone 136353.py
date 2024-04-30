# Problem: C - Bono, Tyres Are Gone - https://codeforces.com/gym/520098/problem/C

n = int(input())

stack = []
reorder = 0
cnt_rmv = 1
for i in range(2 * n):
    cmd = input().split()

    if cmd[0] == "add":
        stack.append(int(cmd[1]))

    elif cmd[0] == "remove" and stack:
        
        if stack[-1] != cnt_rmv:
            reorder += 1
            stack.clear()
        else:
            stack.pop()
        cnt_rmv += 1
    else:
        cnt_rmv += 1
print(reorder)