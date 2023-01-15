def countingValleys(steps, path):
    count = 0
    traversed = 0
    for i in range(len(path)):
        if path[i] == 'U':
            count += 1
        else:
            count -= 1
        if count == 0 and path[i] == 'U':
            traversed += 1
    return traversed
