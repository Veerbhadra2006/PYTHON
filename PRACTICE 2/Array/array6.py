# write a program to find the minimum number(lowest value) in the array

arr = [9, 15, 18, 20, 22, 60, 70, 3, 4]

arr.append(45)
print("The raw data is : ", arr)

minVal = arr[0]

for i in arr:
    if i < minVal:
        minVal = i
        
print("The lowest value is : ", minVal)
