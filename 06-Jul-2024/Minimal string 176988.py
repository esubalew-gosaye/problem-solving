# Problem: Minimal string - https://codeforces.com/contest/797/problem/C

from collections import Counter

def minimal_string_game(s):
    t = []
    u = []
    counter = Counter(s)
    
    for ch in s:
        t.append(ch)
        counter[ch] -= 1
        
        while t and (not any(counter[ch] for ch in counter if ch < t[-1])):
            u.append(t.pop())
    
    return ''.join(u)


s = input().strip()

result = minimal_string_game(s)

print(result)