def countingSort(arr):
    list_of_numbers = [0 for i in range(100)]
    for i in arr:
        list_of_numbers[i] += 1
    return (list_of_numbers)
