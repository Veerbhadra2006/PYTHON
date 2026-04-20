# Find the maximum element in the array and list

arr = [2, 40, 35, 60, 45, 12, 2, 90, 120]

maxVal = arr[0]

for i in arr:
    if i > maxVal:
        maxVal = i

print("The Highest number is : ", maxVal)
