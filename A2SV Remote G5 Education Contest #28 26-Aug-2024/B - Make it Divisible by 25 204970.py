# Problem: B - Make it Divisible by 25 - https://codeforces.com/gym/543262/problem/B

for _ in range(int(input())):
    n = input()

    min_steps = float('inf')
    length = len(n)
    targets = ["00", "25", "50", "75"]

    for target in targets:
        pos2 = -1
        pos1 = -1
        
        for index in range(length - 1, -1, -1):
            if n[index] == target[1]:
                pos2 = index
                break
        
        if pos2 != -1:
            for index in range(pos2 - 1, -1, -1):
                if n[index] == target[0]:
                    pos1 = index
                    break
        
        if pos1 != -1 and pos2 != -1:
            steps = (length - pos2 - 1) + (pos2 - pos1 - 1)
            min_steps = min(min_steps, steps)
    
    print(min_steps)