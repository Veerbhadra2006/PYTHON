# write a program to check if array is sorted or not

arr = [10, 20, 30, 40, 50, 60, 70, 80];
issorted = True

for i in range(len(arr) -1):
    if arr[i] > arr[i + 1]:
        issorted = False
        break

if issorted:
    print("The array is sorted")

else:
    print("The array is not sorted")
    
    
    