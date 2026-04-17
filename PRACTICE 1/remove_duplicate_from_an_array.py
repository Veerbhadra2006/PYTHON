arr1 = [10, 20, 30, 30, 40, 50, 60, 70, 80, 80, 90]
# duplicates = 30, 80

unique_value = list(set(arr1))

print(unique_value)



# Method 2 - creating a loop 
arr2 = [10, 20, 30, 30, 40, 50, 60, 70, 80, 80, 90]
unique_value = []

for i in arr2:
    if i not in unique_value:
        unique_value.append(i)
print(unique_value)