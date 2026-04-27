# write a program to find the maximum elements in the arrau and list

arr = [2, 40, 35, 300, 45, 12, 1, 90, 120]

maxVal = arr[0]

for x in arr:
    if x > maxVal:
        maxVal = x
        
print("The highest number is : ",maxVal)
