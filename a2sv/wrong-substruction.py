n, k = input().split()
k = int(k)

while k:
    
    if n[-1] != '0':
        n = str(int(n) - 1)
    else:
        n = n[:-1]
    
    k -= 1 
    
print(n)
