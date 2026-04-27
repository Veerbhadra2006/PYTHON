# write a progra t find the duplicates elements form an array:

arr = [10, 20, 30 , 40, 40 , 50, 60, 70, 80, 80]

unique = []

duplicates = []

for x in arr:
    if x not in unique:
        unique.append(x)
    else:
        duplicates.append(x)
        
print("THE UNIQUE ELEMENTS IS : ", unique)

print("THE DUPLICATES ELEMENTS IS  : ", duplicates)