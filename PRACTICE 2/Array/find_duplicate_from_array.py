# write a program to find the duplicates elements from an array

arr = [10, 20, 30, 40, 50, 20, 10]

seen = set()
added = set()
duplicates = []

for x in arr:
    if x in seen and x not in added:
        duplicates.append(x)
        added.add(x)
    else:
        seen.add(x)
        
print(duplicates)



# ========================================================================
# METHOD -2 

unique = set()
duplicate = []

for x in arr:
    if x in unique:
        duplicate.append(x)
    else:
        unique.add(x)
        
print("The duplicates element in the array is : ", duplicate)