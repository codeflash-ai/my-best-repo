def sorter(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


def unsorter(arr):
    temp = []
    while True:
        if len(arr) == 0:
            break
        temp.append(arr.pop(0))
    return temp
