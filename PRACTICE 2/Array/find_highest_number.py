# write a prorgram to find the highest number from an array

arr = [2, 40, 35, 60, 45, 12, 2, 90, 120]

maxVal = arr[0]

for x in arr:
    if x > maxVal:
        maxVal = x

print("The Highest number is : ", maxVal)