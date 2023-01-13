m, n = map(int, input().split())
count = 0
if m==2:
    count+=n
elif m > 2:
    count += (m//2)*n 
    if m%2==1:
        count += n//2
elif m==1:
    count += n//2
print(count)
