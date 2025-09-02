def heapify(arr, n, i):
    small = i  
    l = 2 * i + 1  
    r = 2 * i + 2  

    if l < n and arr[l] < arr[small]:
        small = l

    if r < n and arr[r] < arr[small]:
        small = r

    if small != i:
        (arr[i], arr[small]) = (arr[small], arr[i])
        heapify(arr, n, small)
        
def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  
        heapify(arr, i, 0)
    arr.reverse() # making it min Heap comment it to make it max heap 


arr = [12, 11, 13, 5, 6, 7, ]
heap_sort(arr)
print('Sorted array is')
print(arr)
