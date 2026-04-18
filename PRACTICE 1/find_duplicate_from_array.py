# write a program to find the duplicates elements from an array

arr = [10, 20, 30, 40, 50,  20, 10]

unique = set()
duplicate = set()

for num in arr:
    if num in unique:
        duplicate.add(num)
    else:
        unique.add(num)
        
print("\n The array fill with the unique elements : " , unique)
print("\n The duplicates elemens in the array is : ", duplicate)