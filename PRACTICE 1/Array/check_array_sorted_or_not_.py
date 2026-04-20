# check if array is sorted or not

# arr = [80, 20, 60, 30, 40, 10, 50, 70]

arr = [10, 20, 30, 40, 50, 60, 70, 80];

issorted = True;

for i in range(len(arr) -1):
    if arr[i] > arr[i + 1]:
        issorted = False
        break

if issorted:
    print("The array is sorted");
else:
    print("the array is not sorted")