
n = int(input()) #number of stops 

capacity = 0; # tarce the capacity of the trams
store_value = 0; # store the maximum trams value

while n:
    exit, enter  = map(int, input().split()) # number people exits and enter at stop
    capacity += enter
    capacity -= exit
    
    if capacity > store_value:
        store_value = capacity
    
    n -= 1 
print(store_value)
    

    
    
    
