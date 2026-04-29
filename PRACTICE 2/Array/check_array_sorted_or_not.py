# write a program to check if array sorted or not

arr = [80, 20, 30, 50, 10, 70, 60, 40, 30]
# arr = [10, 20, 30, 40, 50]
is_sorted = True;
for i in range(len(arr) -1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break
    
if is_sorted:
    print("The  array is sorted")
else:
    print("The array was not sorted")
    
    
