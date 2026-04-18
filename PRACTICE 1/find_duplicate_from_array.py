# write a program to find the duplicates from an array

arr = [10, 20, 30, 40, 50 , 20, 30]

unique = set()
duplicates = set()

for num in arr:
    if num in unique:
        duplicates.add(num)
    
    else:
        unique.add(num)
        

print("\n The array with the unique element : ", unique)
print("The duplicates elements in the array is : ", duplicates)