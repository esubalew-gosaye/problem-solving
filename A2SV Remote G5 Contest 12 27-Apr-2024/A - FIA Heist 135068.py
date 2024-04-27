# Problem: A - FIA Heist - https://codeforces.com/gym/520098/problem/A

s = input()

stack = []

is_back = False

for i in s:

    if i == '<':
        is_back = True
        if stack:
            stack.pop()
    elif is_back and i == "-":
        is_back = False
        continue
    else:
        stack.append(i)

print("".join(stack))