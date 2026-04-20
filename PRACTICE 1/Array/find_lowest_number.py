#   Find the lowest value in array / list

arr = [9, 15, 18, 20, 22, 60, 70, 3, 4]

arr.append(45)
print("the raw data is : ", arr)


minVal = arr[0]

for i in arr:
    if i < minVal:
        minVal = i

print("The Lowest value is : ", minVal)

