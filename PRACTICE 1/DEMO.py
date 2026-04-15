# write a program to find the heighest value in array or list

arr = [80, 3, 24, 56, 76, 85, 2, 4]

arr.append(2)

maxVal = arr[0]

for i in arr:
    if i > maxVal:
        minVal = i

print("The mximum value in array is : ", minVal)
