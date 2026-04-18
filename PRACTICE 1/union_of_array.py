# Write a program  union of the array

arr =  [1, 2, 3, 4, 5]
arr2 =  [1, 2, 3, 5, 6]

union = []

for x in arr:
    if x not in union:
        union.append(x)
        
for y in arr2:
    if y not in union:
        union.append(y)
        
print("Union of array is : ", union)