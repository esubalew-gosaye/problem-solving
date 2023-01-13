def insertionSort1(n, arr):
    stored = arr[-1]
    for i in range(-1, -len(arr), -1):
        if(stored < arr[i-1]):
            arr[i] = arr[i-1]
            print(*arr)
        else:
            arr[i] = stored
            print(*arr)
            break
        if i==-len(arr)+1:
            arr[0] = stored
            print(*arr)
