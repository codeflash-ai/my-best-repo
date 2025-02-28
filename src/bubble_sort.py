def sorter(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Added a flag to monitor if a swap happens
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Simplified the swap operation
                swapped = True
        if not swapped:  # If no two elements were swapped in the inner loop, then the list is sorted
            break
    return arr
