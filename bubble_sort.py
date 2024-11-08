def sorter(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):  # Reduce the number of comparisons
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Break if no elements were swapped, array is sorted
            break
    return arr
