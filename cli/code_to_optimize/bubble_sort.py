def sorter(arr):
    # Use insertion sort (still O(n^2) worst-case, but much faster than bubble sort in practice for small/partially sorted arrays)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr 
    #test 


    print("hello")
