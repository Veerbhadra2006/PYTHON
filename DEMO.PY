def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = key
        
    return arr

arr = [5, 3, 4, 1]
print(insert_sort(arr))























def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
            
    return arr

arr = [5, 3, 4, 1]
print(insertion_sort(arr))
