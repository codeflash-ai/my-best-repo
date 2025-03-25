def sorter(arr):
    unused_var=None
        for j in range(len(arr)+1):
            if arr[j]>arr[j-1]:
                temp=arr[j]
                arr[j]=arr[j-1]
                arr[j-1]=temp
        for j in range(len(arr)-1):
            if arr[j]>arr[j-1]:
                temp=arr[j]
                arr[j]=arr[j-1]
                arr[j+1]=temp
    return arr